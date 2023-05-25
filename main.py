import pygame, sys, random, math
from pygame.locals import *
pygame.init()


# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

maxsize = 0
while maxsize < 1 or maxsize > WINDOW_WIDTH*WINDOW_HEIGHT:
  maxsize = input('Maximum entity size: ')
  try:
    maxsize = int(maxsize)
  except:
    maxsize = 0

minsize = 0
while minsize < 1 or minsize > maxsize:
  minsize = input('Minimum entity size: ')
  try:
    minsize = int(minsize)
  except:
    minsize = 0

entmax = WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)
characters = -1
def characterinput():
  global characters
  characters = input('Character amount (maximum of %i): ' % entmax)
  try:
    while int(characters) > entmax or int(characters) < 0:
      characters = input('Character amount (maximum of %i): ' % entmax)
  except:
    characterinput()
characterinput()
characters = int(characters)

locs = list()
o = WINDOW_WIDTH + maxsize
u = WINDOW_HEIGHT - maxsize
#p = WINDOW_WIDTH*WINDOW_HEIGHT/(WINDOW_WIDTH*WINDOW_HEIGHT/WINDOW_WIDTH)
for i in range(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)):
  o -= maxsize
  if o == 0:
    o = WINDOW_WIDTH - maxsize
    if u != 0:
      u -= maxsize
    #p = WINDOW_WIDTH*WINDOW_HEIGHT/(WINDOW_WIDTH*WINDOW_HEIGHT/(WINDOW_WIDTH/(((i + 1)*50)/4)))
  locs.append([o,u])
  origlocs = locs
entities = list()
for i in range(characters):
  u = random.randint(0,len(locs) - 1)
  o = locs[u]
  size = random.randint(minsize,maxsize)
  entities.append([o,size,size,(6,36,216),u,u,u,u])
  del(locs[u])

# The main function that controls the game

def main () :
  t = 0
  looping = True
  
  # The main game loop
  while looping :
    t += 1
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
      pressed = pygame.key.get_pressed()
      
      if event.type == pygame.KEYDOWN and event.key == K_d:
        #print(origlocs[entities[0][4] - 1][0])
        entities[0][0][0] = origlocs[entities[0][4] - 1][0]
        entities[0][4] -= 1
      
      if event.type == pygame.KEYDOWN and event.key == K_a:
        entities[0][0][0] = origlocs[entities[0][4] + 1][0]
        entities[0][4] += 1
      
      if event.type == pygame.KEYDOWN and event.key == K_w:
        #print(origlocs[entities[0][4]][0])
        if entities[0][5] >= (WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)): - WINDOW_WIDTH//maxsize:
          entities[0][5] = -(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) + WINDOW_WIDTH//maxsize
        entities[0][0][1] = origlocs[entities[0][5] + WINDOW_WIDTH//maxsize][1]
        entities[0][5] += WINDOW_WIDTH//maxsize
      
      if event.type == pygame.KEYDOWN and event.key == K_s:
        #print(-(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)))
        if entities[0][5] <= -(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) + WINDOW_WIDTH//maxsize:
          entities[0][5] = 0
        entities[0][0][1] = origlocs[entities[0][5] - WINDOW_WIDTH//maxsize][1]
        entities[0][5] -= WINDOW_WIDTH//maxsize
    
    # Processing
    # This section will be built out later
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    for i in entities:
      #print(i[0][1],i[0][0])
      ent = pygame.Rect(i[0][0],i[0][1],i[1],i[2])
      pygame.draw.rect(WINDOW,i[3],ent)
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()














