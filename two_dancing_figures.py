""" File: two_dancing_figures.py
    Author: Xin Li
    Purpose: This program draws two dancing figures
"""

from graphics import graphics

def people(x):
    """This function draws the First left person
       Arguments: x is an integer
    """
    # Head
    p.ellipse(x+200,100,100,100)
    # Body
    p.line(x,250,x+400,250)
    p.line(x+200,100,x+200,400)
    p.line(x+200,400,x,600)
    p.line(x+200,400,x+400,600)
    p.line(x,250,x,50)
    p.line(x+400,250,x+400,50)

def people2(x):
    """This function draws the Second left perosn
       Arguments: x is an integer
    """
    p.ellipse(x+200,100,100,100)
    p.line(x,250,x+400,250)
    p.line(x+200,100,x+200,400)
    p.line(x+200,400,x,600)
    p.line(x+200,400,x+400,600)
    p.line(x,250,x,450)
    p.line(x+400,250,x+400,450)

def people3(x,y):
    """This function Moves the person
       Arguments: x and y are integers
    """
    p.ellipse(x+200,y+100,100,100)
    p.line(x,y+250,x+400,y+250)
    p.line(x+200,y+100,x+200,y+400)
    p.line(x+200,y+400,x,y+600)
    p.line(x+200,y+400,x+400,y+600)
    p.line(x,y+250,x,y+450)
    p.line(x+400,y+250,x+400,y+450)
# Main carvent
p=graphics(1500,1000,"short")

def move1():
    """This function is for movement
    """
    people(100)
    people(600)

    p.update_frame(1)
    p.clear()

    people3(100,50)
    people3(600,50)
    p.update_frame(1)
    p.clear()


    people(100)
    people(600)

    p.update_frame(1)
    p.clear()

    people3(100,50)
    people3(600,50)
    p.update_frame(1)
    p.clear()
    people(100)
    people(600)

    p.update_frame(1)
    p.clear()

    people3(100,50)
    people3(600,50)
    p.update_frame(1)
    p.clear()


    people2(100)
    people2(600)

    p.update_frame(1)
    p.clear()

    people3(100,50)
    people3(600,50)
    p.update_frame(1)
    p.clear()


    people2(100)
    people2(600)

    p.update_frame(1)
    p.clear()

    people3(100,50)
    people3(600,50)
    p.update_frame(1)
    p.clear()

def move2():
    """This function is also for movement
    """
    people(200)
    people(800)

    p.update_frame(1)
    p.clear()

    people3(200,50)
    people3(800,50)
    p.update_frame(1)
    p.clear()


    people(200)
    people(800)

    p.update_frame(1)
    p.clear()

    people3(200,50)
    people3(800,50)
    p.update_frame(1)
    p.clear()
    people(200)
    people(800)

    p.update_frame(1)
    p.clear()

    people3(200,50)
    people3(800,50)
    p.update_frame(1)
    p.clear()


    people2(200)
    people2(800)

    p.update_frame(1)
    p.clear()

    people3(200,50)
    people3(800,50)
    p.update_frame(1)
    p.clear()


    people2(200)
    people2(800)

    p.update_frame(1)
    p.clear()

    people3(200,50)
    people3(800,50)
    p.update_frame(1)
    p.clear()

# Main loop
while(1):
    move1()
    move2()




# Hold the carvet
p.mainloop()
