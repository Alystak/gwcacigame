#INSTALL pygame library as administrator:
#from python\scripts folder> pip install pygame
#from python\scripts folder> pip show pygame

##setup pygame
import sys, pygame
pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

##setup filepaths --- use escape slashes (double up)
from pathlib import Path
#the concatenated string below is specific to my folder structure; adjust to your own:
userbasepath = str(Path.home())+"\\Documents\\GWC\\game\\"

### MEDIA SECTION ##############################################################
#home pic
homepicfilepath = userbasepath + "home.jpg"
homepicBIG = pygame.image.load(homepicfilepath)
homepic = pygame.transform.scale(homepicBIG, (640,480))

#school pic
schoolpicfilepath = userbasepath + "terracycleposterweb.jpg"
schoolpicBIG = pygame.image.load(schoolpicfilepath)
schoolpic = pygame.transform.scale(schoolpicBIG, (640,480))

#music box sound; exit sound so need a time delay
import time
musicboxfilepath = userbasepath + "Music_Box-Big_Daddy-1389738694.wav"
pygame.mixer.music.load(musicboxfilepath)

################################################################################

#top level function
def gwcGame():
  position = "home"
  while position != "sleep":
    pygame.event.get()
    printOptions(position)  
    newposition = input("Where to? : ")    
    position = move(position,newposition)
  time.sleep(3)
  pygame.quit()
  
#print options for each location
def printOptions(place):
  if place == "home":
#    pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
    screen.blit(homepic, (0,0))
    pygame.display.flip()
    print("It's a Saturday and you're at home; what to do?")
    print("You could go to [school] to help out with a club project, stay at [home], or go to [sleep].")
  elif place == "school":
#    pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
    screen.blit(schoolpic, (0,0))
    pygame.display.flip()
    print("You helped make an awesome poster to advertise your club's event next week!")
    print("You can go [home].")
  else:
    print("You've fallen into the ether... perhaps you should go to sleep?")

#ensure movement makes sense
def move(place1,place2):
  newplace = place1                                             # default
  if place2 == "sleep":
    newplace = "sleep"
    print("You feel yourself drift off to sleep as you wonder about the adventures you had today and those to come in the future.")
    pygame.mixer.music.play(1)
  elif place1 == "home":
    if place2 == "home":
      newplace = "home"
    elif place2 == "school":
      newplace = "school"
  elif place1 == "school":
    if place2 == "home":
      newplace = "home"
    elif place2 == "school":
      newplace = "school"
  else:
    print("You've fallen into the ether... perhaps you should go to sleep?")
    newplace = "sleep"
  return newplace

#run automatically upon load/F5
if __name__ == "__main__":
  gwcGame()
