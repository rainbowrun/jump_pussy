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

# Size of game window.
max_width = 1200
max_height = 1000

jump_speed = 0.1
JUMP_COUNT = 30
# Refresh time in millisecond
# TODO: Study how to update the program faster.
refresh_time = 50

# Maximum sword count
max_sword_count = 5

BIRD_IMAGE = pygame.image.load('bird.png')
print('Image is loaded successfully: %s' % BIRD_IMAGE)
print('Image size:', BIRD_IMAGE.get_size())

PUSSY_IMAGE = pygame.image.load('android-new.png')
print('Image is loaded successfully: %s' % PUSSY_IMAGE)
print('Image size:', PUSSY_IMAGE.get_size())


class Bird:
  def __init__(self, x, y):
    self.x = x
    self.y = y

    self.velocity = 5
    self.move_total_period = 1
    self.current_cycle = 0

    self.image = BIRD_IMAGE

    self.width = self.image.get_width()
    self.height = self.image.get_height()

  def Rectangle(self):
    return pygame.Rect(self.x, self.y, self.width, self.height)

  def Move(self):
    self.current_cycle += 1
    if (self.current_cycle == self.move_total_period):
      self.current_cycle = 0
      self.x = self.x + self.velocity
    
def CheckOutOfWindowBirdAndCreateNewIfNecessary():
  for bird in bird_list:
    if bird.x < 0:
      bird.velocity = -1 * bird.velocity
    elif bird.x > max_width - bird.width:
      bird.velocity = -1 * bird.velocity

  return bird_list


class Pussy:
  def __init__(self, x, y, velocity):
    self.x = x
    self.y = y
    self.velocity = velocity

    self.image = PUSSY_IMAGE

    self.width = self.image.get_width()
    self.height = self.image.get_height()

  def Rectangle(self):
    return pygame.Rect(self.x, self.y, self.width, self.height)


class Sword:
  def __init__(self, x, y, height, move_total_period):
    self.x = x
    self.y = y
    self.width = 3
    self.height = height
    self.move_total_period = move_total_period
    self.current_cycle = 0

    # Random speed to make game more interesting.
    self.velocity = random.randint(5, 30)

  def Rectangle(self):
    return pygame.Rect(self.x, self.y, self.width, self.height)

  def Move(self):
    self.current_cycle += 1
    if (self.current_cycle == self.move_total_period):
      self.current_cycle = 0
      self.x = self.x - self.velocity
    

# Return a list of sword.
def InitializeSword(sword_count, start_x, end_x):
  sword_list = []
  for _ in range(sword_count):
    x = random.randint(start_x, end_x)
    sword_list.append(Sword(x, 900, 100, 10))

  return sword_list

def CheckOutOfWindowSwordAndCreateNewIfNecessary():
  new_sword_list = []

  for sword in sword_list:
    if sword.x > 0:
      new_sword_list.append(sword)

  while len(new_sword_list) < max_sword_count:
    x = random.randint(800, max_width)
    new_sword_list.append(Sword(x, 900, 100, 10))

  return new_sword_list



def InitializePussy():
  x = 100
  y = 900
  velocity = 20
  return Pussy(x, y, velocity)


pygame.init()
win = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption("Pussy Jumping Game")

# TODO: Move these into pussy.
# Whether in jump mode and jump cycle.
is_jump = False
jump_count = JUMP_COUNT
# Whether you are dead.
is_dead = False


def Initialize():
  global is_jump, jump_count
  is_jump = False
  jump_count = JUMP_COUNT

  pussy = InitializePussy()
  sword_list = InitializeSword(max_sword_count, max_width/2, max_width)

  bird = Bird(200, 200)
  bird_list = [bird]

  return pussy, sword_list, bird_list

pussy, sword_list, bird_list = Initialize()

run = True
while run:
    pygame.time.delay(refresh_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    # Detect if Pussy is dead.
    for sword in sword_list:
      if pussy.Rectangle().colliderect(sword.Rectangle()):
        is_dead = True
        break

    if is_dead == True:
      if keys[pygame.K_RETURN]:
        is_dead = False
        Initialize();

      else:
        continue
    
    # Move the swords.
    for sword in sword_list:
      sword.Move()
    sword_list = CheckOutOfWindowSwordAndCreateNewIfNecessary()
    
    # Move the birds.
    for bird in bird_list:
      bird.Move()
    bird_list = CheckOutOfWindowBirdAndCreateNewIfNecessary()
    
    if keys[pygame.K_LEFT]:
        pussy.x = pussy.x - pussy.velocity
        if pussy.x <= 0:
            pussy.x = 0
    if keys[pygame.K_RIGHT]:
        pussy.x = pussy.x + pussy.velocity
        if pussy.x+pussy.width >= max_width:
            pussy.x = max_width-pussy.width
    
    if not is_jump:
      if keys[pygame.K_SPACE]:
          is_jump = True

    else:
      if jump_count >= -JUMP_COUNT:
         if jump_count > 0:
           pussy.y = pussy.y - (jump_count ** 2) * jump_speed
         else:
           pussy.y = pussy.y + (jump_count ** 2) * jump_speed
         jump_count -= 1
      else:
         is_jump = False
         jump_count = JUMP_COUNT
        
    # Clear screen.
    win.fill((255, 255, 255))

    # Draw sword.
    for sword in sword_list:
      pygame.draw.rect(win, (100, 100, 100), sword.Rectangle())
      
    # Draw birds.
    for bird in bird_list:
      win.blit(bird.image, (bird.x, bird.y))

    # Draw pussy
    win.blit(pussy.image, (pussy.x, pussy.y))

    pygame.display.update()
    
pygame.quit()