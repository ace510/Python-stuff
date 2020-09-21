from array import array
from dataclasses import dataclass
import arcade
import arcade.gl

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Cambrian Explosion"

@dataclass
class Burst:
    buffer: arcade.gl.buffer
    vao: arcade.gl.geometry

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.burst_list = []

        self.program = self.ctx.load_program(
            vertex_shader="verter_shader_v1.glsl",
            fragment_shader='fragment_shader.glsl'
        )
        self.ctx.enable_only()

    def on_draw(self):
        self.clear()
    
    def on_update(self, dt):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass

if __name__ == "__main__":
    window = MyWindow()
    window.center_window()
    arcade.run()