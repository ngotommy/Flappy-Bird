# import arcade
# SW = 640
# SH = 480
# SPEED = 3
#
# class Ball:
#     def __init__(self, pos_x, pos_y, dx, dy, rad, col):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.dx = dx
#         self.dy = dy
#         self.rad = rad
#         self.col = col
#         self.laser_sound = arcade.load_sound("sounds/laser.wav")
#
#     def draw_ball(self):
#         arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)
#
#     def update_ball(self):
#         self.pos_y += self.dy
#         self.pos_x += self.dx
#
#         #screen border collision
#         if self.pos_x < self.rad:
#             self.pos_x = self.rad
#             arcade.play_sound(self.laser_sound)
#         if self.pos_x > SW - self.rad:
#             self.pos_x = SW - self.rad
#             arcade.play_sound(self.laser_sound)
#
#         if self.pos_y < self.rad:
#             self.pos_y = self.rad
#             arcade.play_sound(self.laser_sound)
#         if self.pos_y > SH - self.rad:
#             self.pos_y = SH - self.rad
#             arcade.play_sound(self.laser_sound)
#
#         # if self.pos_x < self.rad or self.pos_x > SW - self.rad:
#         #     self.dx *= 0
#         # if self.pos_y < self.rad or self.pos_y > SH - self.rad:
#         #     self.dy *= 0
#
# class MyGame(arcade.Window):
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         arcade.set_background_color(arcade.color.ASH_GREY)
#         self.set_mouse_visible(False)
#         self.ball = Ball(320, 240, 0, 0, 15, arcade.color.AUBURN)
#
#     def on_draw(self):
#         arcade.start_render()
#         self.ball.draw_ball()
#
#     # def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
#     #     self.ball.pos_x = x
#     #     self.ball.pos_y = y
#     #
#     # def on_mouse_press(self, x, y, button, modifiers):
#     #     if button == arcade.MOUSE_BUTTON_LEFT:
#     #         print("left mouse button pressed at ", x, y)
#     #     elif button == arcade.MOUSE_BUTTON_RIGHT:
#     #         print("right mouse button pressed at ", x ,y)
#
#     def on_update(self, dt):
#         self.ball.update_ball()
#
#     def on_key_press(self, key, modifiers):
#         if key == arcade.key.LEFT:
#             self.ball.dx = -SPEED
#         elif key == arcade.key.RIGHT:
#             self.ball.dx = SPEED
#         elif key == arcade.key.UP:
#             self.ball.dy = SPEED
#         elif key == arcade.key.DOWN:
#             self.ball.dy = -SPEED
#
#     def on_key_release(self, key, modifiers):
#         if key == arcade.key.LEFT or key == arcade.key.RIGHT:
#             self.ball.dx = 0
#         elif key == arcade.key.UP or key == arcade.key.DOWN:
#             self.ball.dy = 0
#
#
# def main():
#     window = MyGame(SW, SH, "User Control Practice")
#     arcade.run()
#
# if __name__=="__main__":
#     main()


import arcade
SW = 500
SH = 500
BLUE_SPEED = 4
RED_SPEED = 3

class Box:
    def __init__(self, pos_x, pos_y, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = 0
        self.dy = 0
        self.col = col
        self.laser_sound = arcade.load_sound("sounds/laser.wav")
        self.explosion_sound = arcade.load_sound("sounds/explosion.wav")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, 30, 30, self.col)

    def update_red_box(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        # screen border collision
        if self.pos_x < 15:
            self.pos_x = 15
            arcade.play_sound(self.laser_sound)
        if self.pos_x > SW - 15:
            self.pos_x = SW - 15
            arcade.play_sound(self.laser_sound)
        if self.pos_y < 15:
            self.pos_y = 15
            arcade.play_sound(self.laser_sound)
        if self.pos_y > SH - 15:
            self.pos_y = 15
            arcade.play_sound(self.laser_sound)

    def update_blue_box(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        #screen border collision
        if self.pos_x < 15:
            self.pos_x = 15
            arcade.play_sound(self.explosion_sound)
        if self.pos_x > SW - 15:
            self.pos_x = SW - 15
            arcade.play_sound(self.explosion_sound)
        if self.pos_y < 15:
            self.pos_y = 15
            arcade.play_sound(self.explosion_sound)
        if self.pos_y > SH - 15:
            self.pos_y = 15
            arcade.play_sound(self.explosion_sound)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.set_mouse_visible(False)
        self.red = Box(100, 100, arcade.color.RED)
        self.blue = Box(400, 400, arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        self.red.draw_box()
        self.blue.draw_box()

    def on_update(self, dt):
        self.red.update_red_box()
        self.blue.update_blue_box()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.red.dx = -RED_SPEED
        elif key == arcade.key.D:
            self.red.dx = RED_SPEED
        elif key == arcade.key.W:
            self.red.dy = RED_SPEED
        elif key == arcade.key.S:
            self.red.dy = -RED_SPEED

        if key == arcade.key.LEFT:
            self.blue.dx = -BLUE_SPEED
        elif key == arcade.key.RIGHT:
            self.blue.dx = BLUE_SPEED
        elif key == arcade.key.UP:
            self.blue.dy = BLUE_SPEED
        elif key == arcade.key.DOWN:
            self.blue.dy = -BLUE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.red.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.red.dy = 0

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.blue.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.blue.dy = 0

def main():
    window = MyGame(SW, SH, "User Control Practice")
    arcade.run()

if __name__=="__main__":
    main()
