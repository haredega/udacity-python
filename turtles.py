"""
turtle exercice from udacity's programming foundations course
"""
import turtle

def draw_square(brad):
    for x in range(0,4):
        brad.forward(100)
        brad.left(90)
    

def draw_brad():
    window = turtle.Screen()
    window.bgcolor("red")
    window.screensize(100,100)

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(2)
    brad.turtlesize(1.15)
    brad.showturtle()
    for y in range (0,100):
        draw_square(brad)
        brad.left(20)
    
       
    annie= turtle.Turtle()
    annie.shape("turtle")
    annie.color("blue")
    annie.circle(100)
        
    window.exitonclick()
    
draw_brad()    
