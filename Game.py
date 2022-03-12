import turtle # importing turtle module for graphics 

#creating the window of the game

wind=turtle.Screen()
wind.title("Ping Bong Game ") # title of the screen 
wind.bgcolor("black")   # screen background color 
wind.setup(width=800,height=600)    # screen dimensions 
wind.tracer(0) # preventing screen from updating automatically so we can control updating the screen 



# create madraeb


# madrab 1

madrab1=turtle.Turtle() # turtle object 
madrab1.speed(0)     # speed of drawing animation of it  , 0 __> fastest 
madrab1.shape("square")     # shape 
madrab1.color("blue") # color 
madrab1.penup() # to prevent the object from drawing lines while moving
madrab1.goto(-350,0)  # co-ordinates 
madrab1.shapesize(stretch_wid=5,stretch_len=1) # without defining the shape size it automatically takes the size of 20*20 pixels 
                                               # so by using shapesize function it multiples the arguments given in stretch by 20 
                                               # 20*5 = 400 width and 20 *1 = 20 length 





# madrab 2

madrab2=turtle.Turtle() 
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup() # to prevent the object from drawing lines while moving
madrab2.goto(350,0) 
madrab2.shapesize(stretch_wid=5,stretch_len=1)



# ball

ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.goto(0,0)
ball.penup()
ball.speed(0)
ball.dx = 0.3 # d is for delta
ball.dy = 0.3


# score

score1 = 0
score2 =  0 
score=turtle.Turtle()
score.color("white")
score.penup()
score.speed(0)
score.goto(0,260)
score.hideturtle()  
score.write("Player2 :0   Player2 : 0  ",align="center",font=("Courier",24,"normal"))




# functions

def madrab1_up():
    y=madrab1.ycor()  # for key bindings we need to get the co ordinates of y axis and change it when the key is pressed
    y+=20           # change the co ordiantes of y by 20 
    madrab1.sety(y)     #set the co - ordiantes of y to the new one  



def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)




def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)



def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)






# Key bindings
wind.listen() # makes the screen listen for any key to be pressed 
wind.onkey(madrab1_up,"w") # when the key w is pressed it calls the function which increaments the co-ordinates of y by 20 
wind.onkey(madrab1_down,"s") # when key s is pressed it calls the function which decreaments the co-ordinates by 20 
wind.onkey(madrab2_up,"Up")
wind.onkey(madrab2_down,"Down")





while True:
    wind.update() # updating the screen with max speed


    # move the ball
    ball.setx(ball.xcor() +   ball.dx)
    ball.sety(ball.ycor() +   ball.dy)
   
# border check

    if ball.ycor() >290: # checking if the ball toches the top right of the screen so it bounces back

        ball.sety(290)   # set the co-ordinates to 290

        ball.dy *= -1   # start decreamnting the deltay by -1 



    if ball.ycor() <-290: # cheks if the ball toches the bottom of the screen so it bounces back

        ball.sety(-290)  # sets the co-ordinates to -290

        ball.dy *= -1   #start decreamiting the ball by -1 

    
    if ball.xcor() >390:

        ball.goto(0, 0)

        ball.dx *= -1
        score1 +=1 # increasing the score by one when the basl
        score.clear()   # clearing the screen previous text for printing out the new txt 
        score.write("Player2 : {}   Player2 : {}  ".format(score1,score2),align="center",font=("Courier",24,"normal"))
        
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1 
        score2 +=1
        score.clear()
        score.write("Player2 : {}   Player2 : {}  ".format(score1,score2),align="center",font=("Courier",24,"normal"))
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):

        ball.setx(340)

        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):

        ball.setx(-340)

        ball.dx *= -1     


