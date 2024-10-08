# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from pygame.locals import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  # Groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  
  # Asteroids
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()
  
  # Shots
  Shot.containers = (shots, updatable, drawable)
  
  # Players
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

    # Check asteroid collision
    for asteroid in asteroids:
      if asteroid.check_collision(player):
        print("Game Over!")
        sys.exit()
      
      for shot in shots:
        if asteroid.check_collision(shot):
          shot.kill()
          asteroid.split()

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