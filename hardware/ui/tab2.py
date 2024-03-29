from ui.views import Button, Label
from ui.utils import colors, to_float
import uasyncio as asyncio

class Tab2:
    """Second tab, consists of 4 Labels of temperature and pressuare"""

    is_draw = False

    def __init__(self, lcd, control):
        self.control = control
        self.l1 = Label(lcd, 45, 26, "000.0", fg=colors["orange"])
        self.l2 = Label(lcd, 45, 51, "000.0", fg=colors["red"])
        self.l3 = Label(lcd, 45, 76, "000.0", fg=colors["light_green"])
        self.l4 = Label(lcd, 45, 101, "000.0", fg=colors["green"])
        self.strings = [self.l1, self.l2, self.l3, self.l4] 
        loop = asyncio.get_event_loop()
        loop.create_task(self.on_tick())

    async def on_tick(self):
        while True:
            if self.is_draw:
                self.update_data()
            await asyncio.sleep_ms(1000)

    def update_data(self):
        if self.control.owen_is_broken:
            self.strings[0].text = "ERROR"
            self.strings[1].text = "ERROR"
            self.strings[2].text = "ERROR"
            self.strings[3].text = "ERROR"
        else:
            self.strings[0].text = to_float(self.control.t1)
            self.strings[1].text = to_float(self.control.t2)
            self.strings[2].text = to_float(self.control.p1)
            self.strings[3].text = to_float(self.control.p2)
        for string in self.strings:
            string.draw()

    def draw(self):
        self.is_draw = True
        self.update_data()
    
    def handle_touch(self, x, y):
        return 0

    def clear(self):
        self.is_draw = False
        for string in self.strings:
            string.clear()
