# Minesweeper program:
    # first create grid
    # then create a prespecified number of random coordinates
    # then allow the user to enter coordinates
    # if they do not hit a mine, that point is changed to a number denoting the number
    #   of mines in the 8 surrounding points
    # if there are no mines in the surrounding points all those points are uncovered.
    #   and if any of those points are not surrounded their surrounding points will clear.
    # if a mine is hit. GAME OVER.


from math import *
from random import randint

minefield = []
dimension = 10
mines_percent = 25
mines_no = int((mines_percent/100)*dimension**2)
mines_list = []

top_left = [0,0]
top_right = [0,dimension -1]
bottom_left = [dimension - 1, 0]
bottom_right = [dimension - 1, dimension - 1]

top_row = []
bottom_row = []
left_column = []
right_column = []

def top_row_getter(dimension):
  for i in range(1, dimension-1):
    top_row.append([0,i])
  return top_row

def bottom_row_getter(dimension):
  for i in range(1, dimension-1):
    bottom_row.append([dimension-1, i])
  return bottom_row

def left_column_getter(dimension):
  for i in range(1, dimension-1):
    left_column.append([i,0])
  return left_column

def right_column_getter(dimension):
  for i in range(1, dimension-1):
    right_column.append([i, dimension-1])
  return right_column

top_row_getter(dimension)
bottom_row_getter(dimension)
left_column_getter(dimension)
right_column_getter(dimension)




def print_field(minefield):
  for row in minefield:
    print(" ".join(row))
    



def generate_mines(mines_no):
  i=0
  while i < 25:
    new_coord = [randint(0,9), randint(0,9)]
    if new_coord not in mines_list:
      mines_list.append(new_coord)
      i += 1
  return mines_list

##print(generate_points(mines_no))

def minechecker(coord, mines_list):
  if coord in mines_list:
    return True
  else: return False

def hit_mine(coord, mines_list):
  if minechecker(coord, mines_list):
    play_again = input("Surprise Muddafukka! You dead! Are you thirsty for more? (yes/no):")
  else:
    play_again = "yes"
  return play_again

# suround mine will return the mines in the spaces surround the input coord.
# corner points have only 3 and edge points have 5.
# I want a loop that toggles between column and row extremes (dimension - 1) and 0
#


def surround_mine(coord):
  if minechecker(coord):
    play_again = hit_mine(coord)
    return play_again
  else:
    if coord == top_left:
      surround = [[0,1],[1,0],[1,1]]
      return surround
    elif coord == top_right:
      surround = [[0,dimension-2],[1,dimension-2],[1, dimension-1]]
    elif coord == bottom_left:
      surround = [[dimension-1,1],[dimension-2,1],[dimension-2,0]]
    elif coord == bottom_right:
      surround = [[dimension-1, dimension-2],[dimension-2,dimension-2],[dimension-2,dimension-1]]
    elif coord in top_row:
      surround = [[coord[0],coord[1]-1] , [coord[0],coord[1]+1] , [coord[0]+1,coord[1]-1] , [coord[0]+1,coord[1]] , [coord[0]+1,coord[1]+1]]
    elif coord in bottom_row:
      surround = [[coord[0], coord[1]-1],[coord[0], coord[1]+1],[coord[0]-1,coord[1] - 1],[coord[0]-1, coord[1]],[coord[0]-1, coord[1]+1]]
    elif coord in left_column:
      surround = [[coord[0]+1, coord[1]],[coord[0]-1, coord[1]],[coord[0]-1,coord[1] +1],[coord[0], coord[1]+1],[coord[0]-1, coord[1]+1]]
    elif coord in right_column:
      surround = [[coord[0]+1, coord[1]],[coord[0]-1, coord[1]],[coord[0]-1,coord[1] -1],[coord[0], coord[1]-1],[coord[0]-1, coord[1]-1]]
    else:
      surround = [[coord[0], coord[1]-1],[coord[0], coord[1]+1],[coord[0]-1,coord[1] - 1],[coord[0]-1, coord[1]],[coord[0]-1, coord[1]+1],[coord[0]+1,coord[1] - 1],[coord[0]+1, coord[1]],[coord[0]+1, coord[1]+1]]
  return surround
    

def no_mine_count(coord):
  surround_list = surround_mine(coord)
  count = 0
  for i in surround_list:
    if i in mines_list:
      count += 1
  return count

def no_mine_action1(coord):
  first_count = no_mine_count(coord)
  if first_count != 0:
    minefield[coord[0]][coord[1]] = str(first_count)

def no_mine_action2(coord):
  first_count = no_mine_count(coord)
  if first_count == 0:
    count = 0
    surround_list = [surround_mine(coord)]
    while count <= len(surround_list):
      for i in surround_list[count]:
        if no_mine_count(i) != 0:
          no_mine_action1(i)
        else: surround_list.append(i)
      count += 1

def print_start_options():
  print("1 - New Game")
  print("2 - Quit Game")
  print("3 - More Options")

def print_in_game_options():
  print("1 - New Game")
  print("2 - Quit Game")
  print("3 - Go back")
  

########################################################################

print("Welcome to minesweeper")
play_again = "yes"
while play_again == "yes":
  print_start_options()
  option = input("Please select an option: ")
  if option == "3":
    valid = False
    while valid == False:
      dimension = int(input("Enter grid height (5-40): "))
      mines_percent = int(input("Enter percentage of mines (10-90): "))
      valid = True
  elif option == "2":
    print("Goodbye!")
    break
  elif option == "1":
    print("New game")
    for i in range(dimension):
      minefield.append(["O"]*dimension)
    mines_no = int((mines_percent/100)*dimension**2)
    mines_list = generate_mines(mines_no)
    cont = "yes"
    while cont == "yes":
      print_field(minefield)
      coord1 = int(input("Select your latitude (1 - " + str(dimension) + ") or 0 for options: "))
      if coord1 == 0:
        valid2 = False
        while valid2 == False:               
          print_in_game_options()
          option2 = input("Please select an option: ")
          if option2 == "1":
            cont = "no"
            valid2 = True
          elif option2 == "2":
            print("Goodbye!")
            cont = "no" 
            play_again = "no"
            break
          elif option2 == "3":
            break
          else:
            print("Invalid selection")
        else: break
      else:
        coord2 = int(input("Select your longitude (1 - " + str(dimension) + "): "))
        coord = [coord1-1, coord2-1]
        hit_mine(coord, mines_list)
        if play_again == "no":
          cont = "no"
        


        
    else:
      print("Invalid selection")    
    test
    
    
    



