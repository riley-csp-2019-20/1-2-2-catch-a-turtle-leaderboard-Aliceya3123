# a121_catch_a_turtle.py
#-----import statements-----# 
import turtle as trtl
import random 
import learder as lb

#-----game configuration----
turtleshape="arrow"
turtlesize= 3
turtlecolor="gold"

score= 0


timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#scorebord varibles 
learderbored_file_name= "a1222_learderbored.txt"
learder_manes_list =[]
learder_scores_list=[]
player_name= input("please enter name")

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25



#-----initialize turtle-----
deal= trtl.Turtle(shape=turtleshape)
deal.color(turtlecolor)
deal.shapesize(turtlesize)
deal.speed(230)
#scorewiter 

score_writer=trtl.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-370,270)

font_setup=("Arial", 30, "bold")
score_writer.write(score, font=font_setup) 


counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(300,275)



#-----game functions--------
def deal_clicked(x,y):
    change_position()
    update_score()
   

def change_position():
    print("deal got clicked") 
    deal.penup()
    deal.ht()
    if not timer_up:
        dealx = random.randint(-400,400)
        dealy = random.randint(-300,300)
        deal.goto(dealx,dealy)
        deal.st()
def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup) 
230

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("pulled a sneaky on you ", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        manage_leaderboard()
        counter.getscreen().ontimer(countdown, counter_interval)

def leaderbored():
        # manages the leaderboard for top 5 scorers

  global leader_scores_list
  global leader_names_list
  global score
  global deal

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, deal, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, deal, score)

def load_leaderboard(file_name, leader_names, leader_scores):

  leaderboard_file = open(file_name, "r")  # need to create the file ahead of time in same folder

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  for line in leaderboard_file:
    leader_name = ""
    leader_score = ""    
    index = 0

    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")


    # TODO 2: add the leader name to the list

    
    # TODO 3: read the player score using a similar loop

    
    # TODO 4: add the player score to the list


  leaderboard_file.close()


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):

  leader_index = 0
  # TODO 5: loop through all the scores in the existing leaderboard list
  '''
    while ():
    # TODO 6: check if this is the position to insert new score at
    if ():
      break
    else:
      leader_index = leader_index + 1
  '''
  # TODO 7: insert the new player and score at the appropriate position


  # TODO 8: keep both lists at 5 elements only (top 5 players)

  
  # store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
  leader_index = 0
  # TODO 9: loop through all the leaderboard elements and write them to the file
  '''
    while ():
    leaderboard_file.write(leader_names[leader_index] + "," + str(leader_scores[leader_index]) + "\n")
    leader_index = leader_index + 1
  '''
  leaderboard_file.close()
  

# draw leaderboard and display a message to player
def draw_leaderboard(leader_names, leader_scores, high_scorer, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-200,100)
  turtle_object.hideturtle()
  turtle_object.down()
  leader_index = 0

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while leader_index < len(leader_names):
    turtle_object.write(str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(leader_scores[leader_index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200,int(turtle_object.ycor())-50)
    turtle_object.down()
    leader_index = leader_index + 1

  # Display message about player making/not making leaderboard based on high_scorer
  if (high_scorer):
    turtle_object.write("Congratulations! You made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry, you didn't make the leaderboard. Maybe next time!", font=font_setup)

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # TODO 10: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
  '''
  if ():
    turtle_object.write("You earned a bronze medal!", font=font_setup)
    turtle_object.write("You earned a silver medal!", font=font_setup)
    turtle_object.write("You earned a gold medal!", font=font_setup)
  '''
  

#-----events----------------

wn = trtl.Screen()
wn.bgcolor("red")
wn.ontimer(countdown, counter_interval)
deal.onclick(deal_clicked) 
wn.mainloop()