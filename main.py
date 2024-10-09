# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.locals import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()
  
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2

  Player.containers = (updatable, drawable)
  player = Player(x, y)

  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
  
    screen.fill((0,0,0))
    
    # Update player before rendering
    # player.update(dt)

    # Update using groups
    for update in updatable:
      update.update(dt)

    # Draw the player
    # player.draw(screen)

    # Draw the screen using groups
    for drawing in drawable:
      drawing.draw(screen)
    
    # Refresh the screen
    pygame.display.flip()

    # Set FPS 
    tick = clock.tick(60)
    dt = tick / 1000


if __name__ == "__main__":
    main()