import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
VELOCITE = 3

COLORS = [arcade.color.WHITE, arcade.color.WHEAT, arcade.color.LIGHT_YELLOW, arcade.color.YELLOW,
          arcade.color.ORANGE, arcade.color.RED, arcade.color.GREEN,
          arcade.color.PURPLE, arcade.color.BROWN, arcade.color.CYAN, arcade.color.PINK,
          arcade.color.LIGHT_GREEN, arcade.color.ASH_GREY]

class Balle:
   def __init__(self, xx, yy, change_xx, change_yy, rayon_b, color_b):
       self.x = xx
       self.y = yy

       self.change_x = change_xx
       self.change_y = change_yy

       self.rayon = rayon_b
       self.color = color_b

   def update(self):
       self.x = self.x + self.change_x
       self.y = self.y + self.change_y
       # Verifier la bordure droite
       if self.x > SCREEN_WIDTH - self.rayon:
           self.change_x *= -1.0
       # Verifier la bordure superieur
       if self.y > SCREEN_HEIGHT - self.rayon:
           self.change_y *= -1.0
       # Verifier la bordure gauche
       if self.x < self.rayon:
           self.change_x *= -1.0
       # Verifier la bordure inferieur
       if self.y < self.rayon:
           self.change_y *= -1.0

   def draw(self):
       # dessiner la balle
       arcade.draw_circle_filled(self.x,
                                 self.y,
                                 self.rayon,
                                 self.color)

class Rectangle:
   def __init__(self, xx, yy, change_xx, change_yy, r_width, r_height, r_color):
       self.x = xx
       self.y = yy

       self.change_x = change_xx
       self.change_y = change_yy
       ##self.change_angle = 0

       self.width = r_width
       self.height = r_height
       self.color = r_color

   def update(self):
       self.x = self.x + self.change_x
       self.y = self.y + self.change_y
       # Verifier la bordure droite
       if self.x > SCREEN_WIDTH - self.width / 2:
           self.change_x *= -1.0
       # Verifier la bordure superieur
       if self.y > SCREEN_HEIGHT - self.height / 2:
           self.change_y *= -1.0
       # Verifier la bordure inferieur
       if self.x < self.width / 2:
           self.change_x *= -1.0
       # Verifier la bordure inferieur
       if self.y < self.height / 2:
           self.change_y *= -1.0

   def draw(self):
       # dessiner le rectangle
       arcade.draw_rectangle_filled(self.x,
                                 self.y,
                                 self.width,
                                 self.height,
                                 self.color)

class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TP 4 - Martin Cinkler")
       self.liste_balles = []
       self.liste_rectangles = []

   def setup(self):
       pass


   def ajouter_balle(self):
       rayon = random.randint(10, 30)
       center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
       center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
       change_x = 1 + VELOCITE * random.random()
       change_y = 1 + VELOCITE * random.random()
       color = random.choice(COLORS)
       b = Balle(center_x, center_y, change_x, change_y, rayon, color)
       self.liste_balles.append(b)

   def ajouter_rectangle(self):
       width = random.randint(10, 40)
       height = random.randint(10, 30)
       center_x = random.randint(0 + width, SCREEN_WIDTH - width)
       center_y = random.randint(0 + height, SCREEN_HEIGHT - height)
       color = random.choice(COLORS)
       change_xx = 1 + VELOCITE * random.random()
       change_yy = 1 + VELOCITE * random.random()

       rectangle = Rectangle(center_x, center_y, change_xx, change_yy, width, height, color)
       self.liste_rectangles.append(rectangle)

   def on_update(self, delta_time: float):
       for balle in self.liste_balles:
           balle.update()
       for rectangle in self.liste_rectangles:
           rectangle.update()

   def on_draw(self):
       arcade.start_render()
       for balle in self.liste_balles:
           balle.draw()

       for rectangle in self.liste_rectangles:
           rectangle.draw()


   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       if (button == 1):
           self.ajouter_balle()
       elif (button == 4):
           self.ajouter_rectangle()

def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()

