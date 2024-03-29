import time

import lcd160cr
import pyb

from pyb import Pin
from pyb import Timer
from ui.utils import colors

import uasyncio as asyncio


class Label:
    """Text label. Display text on the screen"""

    # font scaler
    font_size = 2
    
    def __init__(self, lcd, x, y, text, limit=5, bg=colors['black'], fg=colors['white']):
        """Create Label object, set class variables"""

        self.lcd = lcd
        self.x = x
        self.y = y
        self.text = text
        # limit for text slicing
        self.limit = limit
        self.fg = fg
        self.bg = bg

    def draw(self, fg=None, bg=None):
        """Display self.text at (x, y) pixel of the screen
           with fg and bg (foreground, backgroung) as colors"""

        if not fg: fg = self.fg
        if not bg: bg = self.bg
        self.lcd.set_text_color(self.lcd.rgb(*fg), self.lcd.rgb(*bg))
        self.lcd.set_pos(self.x, self.y)
        self.lcd.set_font(1, scale=self.font_size, bold=0, trans=0, scroll=0)
        self.lcd.write(self.text[:self.limit])

    def draw_char(self, number, fg=None, bg=None):
        """Draw single character of text in fg, bg colors"""

        if not fg: fg = self.fg
        if not bg: bg = self.bg
        self.lcd.set_text_color(self.lcd.rgb(*fg), self.lcd.rgb(*bg))
        self.lcd.set_pos(self.x + number * ((1 + self.font_size) * 6), self.y)
        self.lcd.set_font(1, scale=self.font_size, bold=0, trans=0, scroll=0)
        self.lcd.write(self.text[number])

    def clear(self):
        """Fill text space with black pixels"""

        self.draw(colors['black'], colors['black'])

        
class Button:

    handler = lambda: 0

    def __init__(self, lcd, x, y, width, height, text):
        self.lcd = lcd
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.text_position_x = self.x + self.width // 2 - len(self.text)//2 - 5
        self.text_position_y = self.y + self.height // 2 - 5

    def draw(self, fg, bg):
        self.lcd.set_text_color(self.lcd.rgb(*fg), self.lcd.rgb(*bg))
        self.lcd.set_pen(self.lcd.rgb(*fg), self.lcd.rgb(*bg))
        self.lcd.rect(self.x, self.y, self.width, self.height)
        self.lcd.set_pos(self.text_position_x, self.text_position_y)
        self.lcd.set_font(1, scale=1, bold=0, trans=0, scroll=0)
        self.lcd.write(self.text)

    def draw_normal(self):
        self.draw(colors["white"], colors["black"])

    def draw_touched(self):
        self.draw(colors["black"], colors["white"])
        
    def clear(self):
        self.draw(colors["black"], colors["black"])

    def handle_touch(self, x, y):
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            self.draw_touched()
            time.sleep(0.3)
            return self.handler()


class EditableButton(Button):
    """Label that can be edited (with blinking)"""    

    font_size = 2
    edit_mode = False
    char_editing = 0
    toggled = False

    def __init__(self, lcd, x, y, width, height, text):
        super().__init__(lcd, x, y, width, height, text)
        self.text_position_x = self.x
        self.text_position_y = self.y
        loop = asyncio.get_event_loop()
        loop.create_task(self.run())

    def draw(self, fg, bg):
        self.lcd.set_text_color(self.lcd.rgb(*fg), self.lcd.rgb(*bg))
        self.lcd.set_pen(self.lcd.rgb(*fg), self.lcd.rgb(*bg))
        self.lcd.set_pos(self.text_position_x, self.text_position_y)
        self.lcd.set_font(1, scale=self.font_size, bold=0, trans=0, scroll=0)
        self.lcd.write(self.text)
    
    def draw_normal(self):
        self.draw(colors["white"], colors["black"])

    async def run(self):
        while True:
            if self.edit_mode:
                self.toggle()
            await asyncio.sleep_ms(500)

    def toggle(self):
        self.toggled = not self.toggled
        bg, fg = colors['black'], colors['white']
        if self.toggled: bg, fg = fg, bg
        self.draw_char(fg, bg, self.char_editing)

    def plus(self):
        new_digit = (int(self.text[self.char_editing]) + 1)%10
        self.text = self.text[:self.char_editing] + str(new_digit)\
                    + self.text[self.char_editing + 1:]
        self.draw_normal()

    def minus(self):
        new_digit = (int(self.text[self.char_editing]) - 1)%10
        self.text = self.text[:self.char_editing] + str(new_digit)\
                    + self.text[self.char_editing + 1:]
        self.draw_normal()

    def right(self):
        next_index = (self.char_editing + 1) % len(self.text)
        self.char_editing += 1 if self.text[next_index] in '0123456789' else 2
        self.char_editing %= len(self.text)
        self.draw_normal()

    def draw_char(self, fg, bg, number):
        """Draw single character of text in fg, bg colors"""

        self.lcd.set_text_color(self.lcd.rgb(*fg), self.lcd.rgb(*bg))
        self.lcd.set_pos(self.text_position_x + number * ((1 + self.font_size) * 6), self.text_position_y)
        self.lcd.set_font(1, scale=self.font_size, bold=0, trans=0, scroll=0)
        self.lcd.write(self.text[number])

    def handle_touch(self, x, y):
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            self.edit_mode = not self.edit_mode
            return 1
