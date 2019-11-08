# a121_catch_a_turtle.py
#-----import statements-----# 
import turtle as trtl
import random 
import leaderboard as lb

#-----game configuration----
turtleshape="arrow"
turtlesize= 3
turtlecolor="gold"

score= 0


timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False



#scorebord varibles 
leaderboard_file_name= "a122_leaderboard.txt"
leader_names_list =[]
leader_scores_list=[]
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


def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Game over!", font=font_setup)
        timer_up = True
        manage_leaderboard()
        
      
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)
        
def manage_leaderboard():
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

#-----events----------------

wn = trtl.Screen()
wn.bgcolor("silver")
wn.ontimer(countdown, counter_interval)
deal.onclick(deal_clicked) 
wn.mainloop()