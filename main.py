import pygame, sys, random, math, datetime
from pygame.locals import *
pygame.init()


# Colours
BACKGROUND = (210, 220, 210)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

def definesizes():
  global maxsize, minsize
  maxsize = 5
  while maxsize < 1 or maxsize > WINDOW_WIDTH*WINDOW_HEIGHT:
    maxsize = input('Maximum entity size: ')
    try:
      maxsize = int(maxsize)
    except:
      maxsize = 0
  
  minsize = 0
  while minsize < 1 or minsize > maxsize:
    minsize = input('Minimum entity size (less than or equal to %s): '% maxsize)
    try:
      minsize = int(minsize)
    except:
      minsize = 0

def characterinput():
  global maxsize, minsize, entmax, characters
  entmax = WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)
  characters = -1
  
  characters = input('Character amount (maximum of %i): ' % entmax)
  try:
    while int(characters) > entmax or int(characters) < 0:
      characters = input('Character amount (maximum of %i): ' % entmax)
  except:
    characterinput()
#characterinput()
#characters = int(characters)

def createlocs():
  global locs, origlocs
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

def create_entities():
  global locs, entities
  entities = list()
  for i in range(characters):
    u = random.randint(0,len(locs) - 1)
    o = locs[u]
    size = random.randint(minsize,maxsize)
    if i == 0:
      entities.append([o,5,5,(72,216,6),u,u,u,u])
    else:
      entities.append([o,size,size,random.choice([(200,200,0),(15,15,15),(200,140,0),(240,240,240),(180,180,180)]),u,u,u,u])
    del(locs[u])


# Titlescreen function
def titlescreen():
  global gameongoing, characters, score, startingtime
  score = 0
  definesizes()
  characterinput()
  characters = int(characters)
  createlocs()
  create_entities()
  gameongoing = False
  while gameongoing == False:
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
      
      pressed = pygame.key.get_pressed()
      if event.type == pygame.KEYDOWN and event.key == K_h:
        gameongoing = True
        startingtime = datetime.datetime.now()
        startingtime = str(startingtime)
        #startingtime = startingtime.replace(":","")
        startingtime = startingtime.replace("-","")
        startingtime = startingtime.split(".")
        startingtime = startingtime[0]
        startingtime = startingtime.replace(" ","")
        startingtime = startingtime.split(":")
        for i in range(len(startingtime)):
          startingtime[i] = int(startingtime[i])
        main()
      
      #rendering
      WINDOW.fill((200,160,5))
      title = pygame.font.SysFont('eufm10', 40)
      surfacetitle = title.render('Herding Cats', True, (200,100,10), None)
      WINDOW.blit(surfacetitle,(WINDOW_WIDTH/6,WINDOW_HEIGHT/4))
      subtitle = pygame.font.Font(None, 25)
      surfacesubtitle = subtitle.render('Press H to begin.', True, (200,120,0), None)
      WINDOW.blit(surfacesubtitle,(WINDOW_WIDTH/6,WINDOW_HEIGHT/2.7))
      pygame.display.update()
      fpsClock.tick(FPS)

# Win function
def win():
  pass

# The main function that controls the game

def main () :
  global looping,locs,entities,origlocs, gameongoing, score, startingtime
  looping = True
  paused = False
  scoreshow = False
  timepaused = 0
  pauses = list()
  # The main game loop
  while looping :
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
        if entities[0][5] >= (WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) - WINDOW_WIDTH//maxsize:
          entities[0][5] = -(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) + WINDOW_WIDTH//maxsize
        try:
          entities[0][0][1] = origlocs[entities[0][5] + WINDOW_WIDTH//maxsize][1]
        except:
          #print('debug')
          entities[0][5] = -(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) + WINDOW_WIDTH//maxsize
          entities[0][0][1] = origlocs[entities[0][5] + WINDOW_WIDTH//maxsize][1]
        entities[0][5] += WINDOW_WIDTH//maxsize
      
      if event.type == pygame.KEYDOWN and event.key == K_s:
        #print(-(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)))
        if entities[0][5] <= -(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) + WINDOW_WIDTH//maxsize:
          entities[0][5] = 0
        entities[0][0][1] = origlocs[entities[0][5] - WINDOW_WIDTH//maxsize][1]
        entities[0][5] -= WINDOW_WIDTH//maxsize
      
      if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
        if paused == False:
          paused = True
          startingptime = datetime.datetime.now()
          startingptime = str(startingptime)
          startingptime = startingptime.replace("-","")
          startingptime = startingptime.split(".")
          startingptime = startingptime[0]
          startingptime = startingptime.replace(" ","")
          startingptime = startingptime.split(":")
          for i in range(len(startingptime)):
            startingptime[i] = int(startingptime[i])
          while paused == True:
            newtime = datetime.datetime.now()
            newtime = str(newtime)
            newtime = newtime.replace("-","")
            newtime = newtime.split(".")
            newtime = newtime[0]
            newtime = newtime.replace(" ","")
            newtime = newtime.split(":")
            for i in range(len(newtime)):
              newtime[i] = int(newtime[i])
            
            for event in pygame.event.get() :
              if event.type == QUIT :
                pygame.quit()
                sys.exit()
              if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                pauses.append((newtime[1] - startingptime[1])*60 + (newtime[2] - startingptime[2]))
                timepaused = 0
                for i in range(len(pauses)):
                  timepaused += pauses[i]
                paused = False
            WINDOW.fill((BACKGROUND[0] - 30,BACKGROUND[1] - 30,BACKGROUND[2] - 30))
            for i in entities:
              ent = pygame.Rect(i[0][0],i[0][1],i[1],i[2])
              pygame.draw.rect(WINDOW,i[3],ent)
            pygame.display.update()
            fpsClock.tick(FPS)
      
      if event.type == pygame.KEYDOWN and event.key == K_h:
        looping = False
        titlescreen()
    
    # Processing
    newtime = datetime.datetime.now()
    newtime = str(newtime)
    #newtime = newtime.replace(":","")
    newtime = newtime.replace("-","")
    newtime = newtime.split(".")
    newtime = newtime[0]
    newtime = newtime.replace(" ","")
    newtime = newtime.split(":")
    for i in range(len(newtime)):
      newtime[i] = int(newtime[i])
    #print(newtime)
    #print(int(list(str(newtime))[len(list(str(newtime))) - 5:len(list(str(newtime))) - 3]))
    timetaken = (newtime[1] - startingtime[1])*60 + (newtime[2] - startingtime[2])
    
    if len(entities) == 1:
      looping = False
      scoreshow = True
      #titlescreen()
    for i in range(len(entities) - 1):
      o = i + 1
      try:
        if random.randint(1,5) == 1:
          entities[o][0][0] = origlocs[entities[o][4] - 1][0]
          entities[o][4] -= 1
      
        if random.randint(1,5) == 1:
          entities[o][0][0] = origlocs[entities[o][4] + 1][0]
          entities[o][4] += 1
      
        if random.randint(1,5) == 1:
          if entities[o][5] >= (WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) - WINDOW_WIDTH//maxsize:
            entities[o][5] = -(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) + WINDOW_WIDTH//maxsize
          try:
            entities[o][0][1] = origlocs[entities[o][5] + WINDOW_WIDTH//maxsize][1]
          except:
            entities[o][5] = -(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) + WINDOW_WIDTH//maxsize
            entities[o][0][1] = origlocs[entities[o][5] + WINDOW_WIDTH//maxsize][1]
          entities[o][5] += WINDOW_WIDTH//maxsize
      
        if random.randint(1,5) == 1:
          if entities[o][5] <= -(WINDOW_WIDTH*WINDOW_HEIGHT//(maxsize*maxsize)) + WINDOW_WIDTH//maxsize:
            entities[o][5] = 0
          entities[o][0][1] = origlocs[entities[o][5] - WINDOW_WIDTH//maxsize][1]
          entities[o][5] -= WINDOW_WIDTH//maxsize
      
        if entities[o][0] == entities[0][0]:
          del(entities[o])
          score += 1000
      except:
        pass
    
    # This section will be built out later
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    for i in entities:
      #print(i[0][1],i[0][0])
      ent = pygame.Rect(i[0][0],i[0][1],i[1],i[2])
      pygame.draw.rect(WINDOW,i[3],ent)
    if scoreshow == True:
      title = pygame.font.SysFont('eufm10', 40)
      #print(type(timetaken))
      timetaken -= timepaused
      print(timetaken)
      surfacetitle = title.render('Score: %s' % (score//timetaken), True, (200,100,10), None)
      WINDOW.blit(surfacetitle,(WINDOW_WIDTH/6,WINDOW_HEIGHT/4))
    pygame.display.update()
    fpsClock.tick(FPS)
    if scoreshow == True:
      titlescreen()


titlescreen()













