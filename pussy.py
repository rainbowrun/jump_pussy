# TODO: Add more swords.

# TODO: Build a binary which can be downloaded and run.
# TODO: Make the sword looks better.
# TODO: Add Bird
# TODO: Add duck for Character.
# TODO: Add the your current time cycle.
# TODO: Corp Pussy to remove unnecessary background.
# TODO: When you die, make it visible on the screen.
# TODO: Add 3 lifes.

import pygame

# The start position of a sword.
sword_x = 400
sword_y = 350
sword_width = 20
sword_height = 100
sword_velocity = 4

# Sword move total period
sword_move_total_period = 10
current_cycle = 0


velocity = 20

# Size of game window.
max_width = 1200
max_height = 500

pygame.init()
win = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption("Pussy Jumping Game")

# Load character.
pussy = pygame.image.load('IMG-0102-new.JPG')
print('Image is loaded successfully: %s' % pussy)
print('Image size:', pussy.get_size())

# Start position of the character.
x = 100
y = 400
width, height = pussy.get_size()


# Refresh time in millisecond
refresh_time = 10

# Whether you are dead.
is_dead = False

# Whether in jump mode and jump cycle.
is_jump = False
jump_count = 10

def Initialize():
  global sword_x, sword_y, x, y, is_jump, jump_count
  sword_x = 400
  sword_y = 350
  x = 100
  y = 400
  is_jump = False
  jump_count = 10

Initialize()

run = True
while run:
    pygame.time.delay(refresh_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    if is_dead == True:
      if keys[pygame.K_RETURN]:
        is_dead = False
        Initialize();
      else:
        continue
    
    # Pussy is dead.
    if pygame.Rect(x, y, width, height).colliderect(pygame.Rect(sword_x, sword_y, sword_width, sword_height)):
      is_dead = True
      continue

    # Move the sword.
    current_cycle += 1
    if (current_cycle == sword_move_total_period):
      current_cycle = 0
      sword_x = sword_x - sword_velocity
    
    if keys[pygame.K_LEFT]:
        x = x - velocity
        if x <= 0:
            x = 0
    if keys[pygame.K_RIGHT]:
        x = x + velocity
        if x+width >= max_width:
            x = max_width-width
    
    if not is_jump:
      if keys[pygame.K_SPACE]:
          is_jump = True

    else:
      if jump_count >= -10:
         if jump_count > 0:
           y = y - (jump_count ** 2) * 0.5
         else:
           y = y + (jump_count ** 2) * 0.5
         jump_count -= 1
      else:
         is_jump = False
         jump_count = 10
        
    # Clear screen.
    win.fill((255, 255, 255))

    # Draw sword.
    pygame.draw.rect(win, (100, 100, 100),
      (sword_x, sword_y, sword_width, sword_height))
   
    # Draw pussy.
    win.blit(pussy, (x,y))

    pygame.display.update()
    
pygame.quit()
