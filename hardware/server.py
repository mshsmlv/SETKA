from uModBus.serial import Serial
from mainconfig import uart_ctrl_pin

from math import ceil
import uasyncio as asyncio
from pc import Computer
from makhina.makhina import Owen
from ui.utils import chunkstring, islice_first, file_iter


max_tries = 10


class ModbusMaster:

    buffer_start = 100
    buffer_len = 122
    sending_offset = -1
    sending_data = None
    sending_block = False

    def __init__(self, control, screen):
        self.connection = Serial(6, baudrate=115200, ctrl_pin=uart_ctrl_pin)
        self.pc = Computer(self, control, screen)
        self.owen = Owen(self, control)
        loop = asyncio.get_event_loop()
        loop.create_task(self.serve())

    async def proceed_sending(self):
        print('SENDING OFFSET', self.sending_offset)
        chunk = islice_first(self.sending_data, self.buffer_len)
        print('Sending chunk:', chunk)
        if not chunk: return 0
        success = False
        tries = 0
        while:
            try:
                await self.connection.write_multiple_registers(5, self.buffer_start, chunk)
            except Exception as e:
                print(e)
                if tries > max_tries:
                    return 2
                tries += 1
        return 1

    async def send_data(self, slave_addr, data):
        self.sending_data = iter(data)
        self.sending_block = False
        self.sending_offset = 0

    async def send_file(self, slave_addr, filename):
        print("FILE NAME", filename)
        return await self.send_data(slave_addr, file_iter('/sd/logs/' + filename))

    async def send_string(self, slave_addr, starting_address, text):
        try:
            return await self.connection.write_multiple_registers(slave_addr, starting_address, list(map(ord, text)))
        except Exception as e:
            print(e)

    async def get_string(self, slave_addr, starting_address, size):
        try:
            result = await self.connection.read_holding_registers(slave_addr, starting_address, size)
            print('result', result)
            return ''.join([chr(x) for x in result])
        except Exception as e:
            print(e)

    async def handle_sending(self):
        recieve_flag = await self.connection.read_holding_registers(5, 99, 1, False)
        recieve_flag = recieve_flag[0]
        if not recieve_flag:
            self.sending_block = True
            try:
                proceed_result = await self.proceed_sending()
            except Exception as e:
                proceed_result = 2
                print('Exception while transfering data, ', e)
            self.sending_block = False
            if not proceed_result:
                self.sending_offset = -1
                self.sending_data = None
                recieve_flag = 2
            elif proceed_result == 1:
                self.sending_offset += 1
                recieve_flag = 1
            elif proceed_result == 2:
                recieve_flag = 3
            await self.connection.write_single_register(5, 99, recieve_flag)

    async def serve(self):
        while True:
            # Handle pc
            if self.pc.connected:
                if self.sending_offset > -1 and not self.sending_block:
                    await self.handle_sending()
                else:
                    await self.pc.get_and_process_command()
            else:
                await self.pc.try_connect()

            await asyncio.sleep_ms(10)
            # Handle owen
            await self.owen.read_owen_data()           
            await asyncio.sleep_ms(10)
