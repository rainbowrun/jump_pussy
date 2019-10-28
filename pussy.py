# TODO: Add more swords.
# TODO: When one sword goes out of window, make new sword.

# TODO: Refactor the code to put pussy data in a class.
# TODO: Build a binary which can be downloaded and run.
# TODO: Make the sword looks better.
# TODO: Add Bird
# TODO: Add duck for Character.
# TODO: Add the your current time cycle.
# TODO: Corp Pussy to remove unnecessary background.
# TODO: When you die, make it visible on the screen.
# TODO: Add 3 lifes.

import random
import pygame

class Sword:
  def __init__(self, x, y, width, height, velocity, move_total_period):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.velocity = velocity
    self.move_total_period = move_total_period
    self.current_cycle = 0

  def Rectangle(self):
    return pygame.Rect(self.x, self.y, self.width, self.height)

  def Move(self):
    self.current_cycle += 1
    if (self.current_cycle == self.move_total_period):
      self.current_cycle = 0
      self.x = self.x - self.velocity
    

# Size of game window.
max_width = 1200
max_height = 500

    
# Return a list of sword.
def InitializeSword(sword_count, start_x, end_x):
  sword_list = []
  for _ in range(sword_count):
    x = random.randint(start_x, end_x)
    sword_list.append(Sword(x, 400, 20, 100, 4, 10))

  return sword_list


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

velocity = 20


# Refresh time in millisecond
refresh_time = 10

# Whether you are dead.
is_dead = False

# Whether in jump mode and jump cycle.
is_jump = False
jump_count = 10

def Initialize():
  global x, y, is_jump, jump_count
  x = 100
  y = 400
  is_jump = False
  jump_count = 10

Initialize()
sword_list = InitializeSword(2, max_width/2, max_width);

run = True
while run:
    pygame.time.delay(refresh_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    # Detect if Pussy is dead.
    for sword in sword_list:
      if pygame.Rect(x, y, width, height).colliderect(sword.Rectangle()):
        is_dead = True
        break

    if is_dead == True:
      if keys[pygame.K_RETURN]:
        is_dead = False
        Initialize();
        sword_list = InitializeSword(2, max_width/2, max_width);

      else:
        continue
    
    # Move the swords.
    for sword in sword_list:
      sword.Move()
    
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
    for sword in sword_list:
      pygame.draw.rect(win, (100, 100, 100), sword.Rectangle())
      
   
    # Draw pussy
    win.blit(pussy, (x,y))

    pygame.display.update()
    
pygame.quit()
