#top level function
def gwcGame():
  position = "home"
  while position != "sleep":
    printOptions(position)  
    newposition = input("Where to? : ")    
    position = move(position,newposition)
  
#print options for each location
def printOptions(place):
  if place == "home":
    print("It's a Saturday and you're at home; what to do?")
    print("You could go to [school] to help out with a club project, stay at [home], or go to [sleep].")
  elif place == "school":
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
