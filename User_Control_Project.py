'''
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.
Hold down the spacebar to move your plane up
Avoid all incoming meteors
Collect gold stars
Don't lose too much altitude!
'''
import arcade
import random
SW = 600
SH = 600
PLANE_SCALE = 0.5
PLANE_SPEED = 3
DEBRIS_SCALE = 0.5
DEBRIS_COUNT = 7
STAR_SCALE = 0.5

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("PNG/Planes/planered1.png", PLANE_SCALE)
        self.dy = int(self.change_y)

    def update(self): 
        self.center_y += self.dy

        if self.center_y >= SH  - self.height:
            self.dy = 0


class Debris(arcade.Sprite):
    def __init__(self):
        super().__init__("PNG/meteor.png", DEBRIS_SCALE)
        self.dx = int(self.change_x)
        self.explosion_sound = arcade.load_sound("sounds/explosion.wav")

    def update(self):
        self.hit = False
        self.center_x += self.dx

        if self.hit:
            arcade.play_sound(self.explosion_sound)

        if self.center_x < -self.width:
            self.center_x = random.randint(SW + 50, SW + 200)
            self.center_y = random.randint(0, SH - self.height)
            self.dx = random.randint(-7, -3)

        if self.center_y <= 0:
            for i in range(1):
                arcade.play_sound(self.explosion_sound)
            self.center_y = 0
            self.dy = 0


class Star(arcade.Sprite):
    def __init__(self):
        super().__init__("PNG/starGold.png", STAR_SCALE)
        self.dx = int(self.change_x)

    def update(self):
        self.center_x += self.dx

        if self.center_x < -self.width:
            self.center_x = random.randint(SW + 200, SW + 300)
            self.center_y = random.randint(0, SH - self.height)
            self.dx = random.randint(-7, -3)

class Score():
    def __init__(self, points):
        self.text = "Score:"
        self.points = points

    def draw(self):
        arcade.draw_text(self.text + " " + str(self.points), 30, 500, arcade.color.WHITE, 15)



class Rain():
    def __init__(self, x, y, dy, droplet_length, color):
        self.x = x
        self.y = y
        self.dy = dy
        self.droplet_length = droplet_length
        self.color = color

    def draw_rain(self):
        arcade.draw_line(self.x, self.y, self.x, self.y + self.droplet_length, self.color)

    def update_rain(self):
        self.y += self.dy
        if self.y < 0:
            self.y = random.randint(600, 700)
            self.x = random.randint(0, 600)


class Clouds():
    def __init__(self, x, y, dx, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.radius = radius
        self.color = color

    def draw_clouds(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def update_clouds(self):
        self.x += self.dx
        if self.x >= SW + self.radius:
            self.x = -70


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
        self.explosion_sound = arcade.load_sound("sounds/explosion.wav")
        self.game_over = False
        self.point_sound = arcade.load_sound("sounds/coin.wav")

        #cloud initalization
        self.clouds_list = []
        x = -640
        for i in range(9):
            self.clouds = Clouds(x, SH, 5, 70, arcade.color.GRAY)
            self.clouds_list.append(self.clouds)
            x += 80

        #rain inititalization
        self.rain_list = []
        for i in range(300):
            dy = random.randint(-4, -1)
            position_x = random.randint(0, 600)
            position_y = random.randint(0, 600)
            droplet_length = random.randint(10, 40)
            color = arcade.color.BLUE
            self.rain = Rain(position_x, position_y, dy, droplet_length, color)
            self.rain_list.append(self.rain)

        self.score = Score(0)

    def on_draw(self):
        arcade.start_render()
        for rain in self.rain_list:
            rain.draw_rain()

        for clouds in self.clouds_list:
            clouds.draw_clouds()

        self.score.draw()

        self.player_list.draw()
        self.debris_list.draw()
        self.star_list.draw()

        if self.game_over:
            arcade.draw_text("Game Over!", 175, SH / 2, arcade.color.BLACK, 30)

    def reset(self):
        #sprite list
        self.player_list = arcade.SpriteList()
        self.debris_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        #set up plane sprites
        self.plane = Player()
        self.plane.center_x = 100
        self.plane.center_y = SH/2
        self.plane.dy = -2
        self.player_list.append(self.plane)

        #set up debris sprites
        for i in range(DEBRIS_COUNT):
            self.debris = Debris()
            self.debris.center_x = random.randint(SW + 50, SW + 200)
            self.debris.center_y = random.randint(0, SH-self.debris.height)
            self.debris.dx = random.randint(-7, -3)
            self.debris_list.append(self.debris)

        #set up star sprites
        self.star = Star()
        self.star.center_x = random.randint(SW + 200, SW + 300)
        self.star.center_y = random.randint(self.star.height, SH - self.star.height)
        self.star.dx = random.randint(-7, -4)
        self.star_list.append(self.star)

    def on_update(self, dt):
        for rain in self.rain_list:
            rain.update_rain()

        for clouds in self.clouds_list:
            clouds.update_clouds()

        self.player_list.update()
        self.debris_list.update()
        self.star_list.update()

        if self.plane.center_y <= 0:
            self.game_over = True

        self.star_touch = arcade.check_for_collision_with_list(self.plane, self.star_list)
        for star in self.star_touch:
            self.star.center_x = random.randint(SW + 200, SW + 300)
            self.star.center_y = random.randint(self.star.height, SH - self.star.height)
            self.score.points += 1
            arcade.play_sound(self.point_sound)
            self.star_touch.pop(0)


        self.debris_touch = arcade.check_for_collision_with_list(self.plane, self.debris_list)
        for debris in self.debris_touch:
             self.game_over = True
             arcade.play_sound(self.debris.explosion_sound)
             debris.kill()
             self.debris_touch.clear()

        if self.game_over:
            self.clock = 0
            self.clock += dt

            self.plane.dy = 0
            self.star.dx = 0
            for rain in self.rain_list:
                for i in range(len(self.rain_list)):
                    self.rain_list[i].dy = 0
            for clouds in self.clouds_list:
                for i in range(len(self.clouds_list)):
                    self.clouds_list[i].dx = 0
            for debris in self.debris_list:
                for i in range(len(self.debris_list)):
                    self.debris_list[i].dx = 0

            if self.clock >= 3:
                self.game_over = False
                self.reset()



    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.plane.dy = PLANE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.plane.dy = -PLANE_SPEED


def main():
    window = MyGame(SW, SH, "Tommy Ngo - Flying Through Bermuda Triangle")
    window.reset()
    arcade.run()

if __name__ == "__main__":
    main()