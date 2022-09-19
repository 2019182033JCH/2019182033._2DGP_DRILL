Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
idle
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    idle
NameError: name 'idle' is not defined
>>> import turtle
>>> 
>>> def moveup():
...     turtle.setheading(90)
...     turtle.forward(50)
...     turtle.stamp()
... 
...     
>>> def movedown():
...     turtle.setheading(-90)
...     turtle.forward(50)
...     turtle.stamp()
... 
...     
>>> def moveleft():
...     turtle.setheading(180)
...     turtle.forward(50)
...     turtle.stamp()
... 
...     
>>> def moveright():
...     turtle.setheading(0)
...     turtle.forward(50)
...     turtle.stamp()
... 
...     
>>> turtle.shape('turtle')
>>> 
>>> def restart():
...     turtle.reset()
... 
...     
>>> turtle.onkey(moveup, 'w')
>>> turtle.onkey(movedown, 's')
>>> turtle.onkey(moveleft, 'a')
>>> turtle.onkey(moveright, 'd')
>>> turtle.onkey(restart, 'Escape')
>>> turtle.listen()
>>> 
