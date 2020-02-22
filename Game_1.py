import turtle
import winsound #windows only

wn=turtle.Screen()
wn.title("Pong by @AMOSA")
wn.bgcolor("black") #background color
wn.setup(width=800,height=600) #Screen resolution
wn.tracer(0)
#Score
score_a=0
score_b=0
#Paddle A

paddle_a= turtle.Turtle() # Turtle object
paddle_a.speed(0) # speed animation  set to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)#wid=5*20  len=20*1 pix
paddle_a.penup()
paddle_a.goto(-350,0) #start at position (x,y)

#Paddle B

paddle_b= turtle.Turtle() # Turtle object
paddle_b.speed(0) # speed animation  set to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)#wid=5*20  len=20*1 pix
paddle_b.penup()
paddle_b.goto(350,0) #start at position (x,y)

#Ball
ball= turtle.Turtle() # Turtle object
ball.speed(0) # speed animation  set to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0) #start at position (x,y)
#mouvment speed  
ball.dx=0.6  
ball.dy=0.6
#Pen Score
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260) #text position
pen.write("Player A:0 Player B: 0", align="center",font=("courier",24,"normal"))
#Function
def paddle_a_up():
    y=paddle_a.ycor() #current y coordinate of paddle a
    y+=20
    paddle_a.sety(y) # uppdate y  coordinate  of the paddle_a

def paddle_a_down():
    y=paddle_a.ycor() #current y coordinate of paddle a
    y-=20
    paddle_a.sety(y) # uppdate y  coordinate  of the paddle_a



def paddle_b_up():
    y=paddle_b.ycor() #current y coordinate of paddle a
    y+=20
    paddle_b.sety(y) # uppdate y  coordinate  of the paddle_a

def paddle_b_down():
    y=paddle_b.ycor() #current y coordinate of paddle a
    y-=20
    paddle_b.sety(y) # uppdate y  coordinate  of the paddle_a
    
#Kkeyboard binding
wn.listen() #listen to keyboard input
wn.onkeypress(paddle_a_up,"z")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"5")  # Up
wn.onkeypress(paddle_b_down,"2")  #Down 
#Main  game loop
while True:
    
     wn.update() #update Screen

     
     ball.setx(ball.xcor()+ball.dx)
     ball.sety(ball.ycor()+ball.dy)

     # Border checking
     if ball.ycor()>290 : #top
         ball.sety(290)
         ball.dy*=-1
         winsound.PlaySound("jumping.wav",winsound.SND_ASYNC) #for windows system only
     if ball.ycor()<-290 : #down
         ball.sety(-290)
         ball.dy*=-1
         winsound.PlaySound("jumping.wav",winsound.SND_ASYNC) #for windows system only
     if ball.xcor()>390 : #left
         ball.goto(0,0)
         ball.dx*=-1
         score_a+=1
         pen.clear()
         pen.write("Player A:{} Player B:{}".format(score_a,score_b), align="center",font=("courier",24,"normal"))
     if ball.xcor()<-390 : #right 
         ball.goto(0,0)
         ball.dx*=-1
         score_b+=1
         pen.clear() #clear text from screen
         #uppdate score 
         pen.write("Player A:{} Player B:{}".format(score_a,score_b), align="center",font=("courier",24,"normal"))
        
    #Paddle and ball collision
     if(((ball.xcor() > 330 )and( ball.xcor() < 350))==True)and((( ball.ycor() < (paddle_b.ycor()+40))and ( ball.ycor() > (paddle_b.ycor()-40)))== True):
              #ball.setx(340)
              ball.dx*=-1
              winsound.PlaySound("jumping.wav",winsound.SND_ASYNC) #for windows system only
     
     if (((ball.xcor() <- 330 )and( ball.xcor() > -350))==True)and((( ball.ycor() < (paddle_a.ycor()+40))and ( ball.ycor() > (paddle_a.ycor()-40)))== True):
             #ball.setx(-340)
               ball.dx*=-1
               winsound.PlaySound("jumping.wav",winsound.SND_ASYNC) #for windows system only
     #print("test exit")























     
