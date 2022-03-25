import turtle
tao = turtle.Pen()
tao.shape('turtle')

def go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def pent():
    '''for drawing pentagon'''
    for i in range(6):
        tao.forward(100)
        tao.right(60)

a = 1
while a <=100:
    go(a,a)
    a=a+10
    pent()
