import arcade
import random
SW = 640
SH = 480
SHIP_SPEED = 10


class Ship:
    def __init__(self):
        self.pos_x = SW/2
        self.pos_y = 30
        self.dx = 0
        self.rad = 50
        self.laser_sound = arcade.load_sound("sounds/laser.wav")

    def draw_ship(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, 10, 40, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, 30, 30, arcade.color.ORANGE)
        arcade.draw_arc_filled(self.pos_x, self.pos_y, 50, 50, arcade.color.GREEN, 0, 180, 180)

    def update_ship(self):
        self.pos_x += self.dx

        if self.pos_x < 0-self.rad:
            self.pos_x = SW+self.rad
        if self.pos_x > SW+self.rad:
            self.pos_x = 0 - self.rad

class Star():
    def __init__(self):
        self.x = random.randint(0, SW)
        self.y = random.randint(0, SH+50)
        self.dy = -1
        self.radius = random.randint(1, 3)
        self.color = arcade.color.WHITE

    def draw_star(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def update_star(self):
        self.y += self.dy
        if self.y < 0:
            self.y = random.randint(SH+10, SH+300)
            self.x = random.randint(0, SW)

class Bullet:
    def __init__(self, x):
        self.x = x
        self.y = 30
        self.dy = 0
        self.rad = 2
        self.color = arcade.color.RED

    def draw_bullet(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color)

    def update_bullet(self):
        self.y += self.dy

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(False)
        self.bullet_sound = arcade.load_sound("sounds/laser.wav")
        self.bullet_list = []
        self.star_list = []
        for i in range(300):
            self.star = Star()
            self.star_list.append(self.star)

        self.ship = Ship()

    def on_draw(self):
        arcade.start_render()
        for bullet in self.bullet_list:
            bullet.draw_bullet()
        for star in self.star_list:
            star.draw_star()
        self.ship.draw_ship()


    def on_update(self, dt):
        for bullet in self.bullet_list:
            bullet.update_bullet()
        for star in self.star_list:
            star.update_star()
        self.ship.update_ship()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ship.dx = -SHIP_SPEED
        elif key == arcade.key.RIGHT:
            self.ship.dx = SHIP_SPEED

        if key == arcade.key.SPACE:
            self.bullet = Bullet(self.ship.pos_x)
            self.bullet_list.append(self.bullet)
            for bullet in self.bullet_list:
                bullet.dy = SHIP_SPEED
            arcade.play_sound(self.bullet_sound)


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ship.dx = 0


def main():
    window = MyGame(SW, SH, "CSP INVADERS!")
    arcade.run()

if __name__=="__main__":
    main()