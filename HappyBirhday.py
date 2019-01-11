import turtle
t = turtle.Turtle()
sizeX = 1024
sizeY = 600

def main():
    turtle.title('Birthday Card')
    turtle.setup(sizeX+10,sizeY+10)
    turtle.screensize(sizeX,sizeY)

    t.penup()
    t.pensize(5)
    t.speed(1)

    t.goto(locateX(50),locateY(sizeY-80))
    t.write("亲",font=('楷体',50))
    t.goto(locateX(120),locateY(sizeY-80))
    t.write("爱",font=('楷体',50))
    t.goto(locateX(190),locateY(sizeY-80))
    t.write("的",font=('楷体',50))
    t.goto(locateX(260),locateY(sizeY-80))
    t.write(":",font=('楷体',50))

    t.speed(2)

    t.goto(locateX(50),locateY(sizeY-120))
    t.setheading(270)
    printHappyBirthday()

    t.goto(locateX(150),locateY(sizeY-430))
    t.setheading(135)
    printHeart(200)

    t.goto(locateX(850),locateY(sizeY-100))
    t.setheading(0)
    printFlower()

    turtle.done()

def printHappyBirthday():
    #生
    t.pendown()
    t.circle(-40, 90)
    t.right(180)
    t.circle(40, 45)
    t.right(45)
    t.fd(100)
    t.penup()
    t.right(160)
    t.fd(90)
    t.left(160)
    t.pendown()
    t.fd(60)
    t.penup()
    t.left(180)
    t.fd(30)
    t.right(90)
    t.fd(80)
    t.right(180)
    t.pendown()
    t.fd(120)
    t.penup()
    t.right(90)
    t.fd(50)
    t.right(180)
    t.pendown()
    t.fd(100)


    #日
    t.penup()
    t.left(60)
    t.fd(130)
    t.right(150)
    t.pendown()
    t.fd(120)
    t.bk(120)
    t.left(90)
    t.fd(90)
    t.right(90)
    t.fd(120)
    t.right(128)
    t.fd(10)
    t.penup()
    t.fd(90)
    t.right(142)
    t.pendown()
    t.fd(70)
    t.penup()
    t.right(142)
    t.fd(95)
    t.left(142)
    t.pendown()
    t.fd(80)

    #快
    t.penup()
    t.left(50)
    t.fd(100)
    t.right(140)
    t.pendown()
    t.fd(50)
    t.penup()
    t.left(165)
    t.fd(90)
    t.right(165)
    t.pendown()
    t.fd(120)
    t.penup()
    t.left(180)
    t.fd(70)
    t.right(135)
    t.fd(10)
    t.pendown()
    t.fd(20)
    t.penup()
    t.left(120)
    t.fd(40)
    t.right(75)
    t.left(90)
    t.fd(10)
    t.right(90)

    t.pendown()
    t.fd(80)
    t.right(90)
    t.fd(55)
    t.penup()
    t.right(90)
    t.fd(80)
    t.right(180)
    t.pendown()
    t.fd(100)
    t.penup()
    t.left(125)
    t.fd(115)
    t.right(215)
    t.pendown()
    t.fd(95)
    t.circle(-60,60)
    t.penup()
    t.right(180)
    t.circle(60,50)
    t.right(130)
    t.pendown()
    t.fd(30)
    t.circle(30,20)
    t.fd(30)

    #乐
    t.penup()
    t.left(30)
    t.left(40)
    t.fd(230)
    t.right(180)
    t.pendown()
    t.circle(-80,30)
    t.fd(60)
    t.left(80)
    t.fd(50)
    t.penup()
    t.right(90)
    t.fd(30)
    t.right(180)
    t.pendown()
    t.fd(160)
    t.penup()
    t.bk(70)
    t.left(90)
    t.fd(40)
    t.right(180)
    t.pendown()
    t.fd(120)
    t.right(130)
    t.fd(20)
    t.penup()
    t.fd(10)
    t.right(50)
    t.fd(40)
    t.left(160)
    t.pendown()
    t.circle(-100,40)
    t.penup()
    t.right(180)
    t.circle(100,40)
    t.right(70)
    t.fd(50)
    t.pendown()
    t.right(60)
    t.fd(50)
    t.circle(30,30)
    t.fd(10)
    t.penup()

def printHeart(size):
    #心
    t.pencolor('red')
    t.fillcolor('red')
    t.pendown()
    t.begin_fill()
    t.circle(-size*0.5,180)
    t.left(90)
    t.circle(-size*0.5,180)
    t.fd(size)
    t.right(90)
    t.fd(size)
    t.end_fill()
    t.penup()
    t.pencolor('black')

def printFlower():
    # 花蕊 
    t.pensize(1)
    t.pencolor('black')
    t.fillcolor("red")
    t.pendown()
    t.begin_fill()
    t.circle(10, 180)
    t.circle(25, 110)
    t.left(50)
    t.circle(60, 45)
    t.circle(20, 170)
    t.right(24)
    t.fd(30)
    t.left(10)
    t.circle(30, 110)
    t.fd(20)
    t.left(40)
    t.circle(90, 70)
    t.circle(30, 150)
    t.right(30)
    t.fd(15)
    t.circle(80, 90)
    t.left(15)
    t.fd(45)
    t.right(165)
    t.fd(20)
    t.left(155)
    t.circle(150, 80)
    t.left(50)
    t.circle(150, 90)
    t.end_fill()
    # 花瓣1 
    t.left(150)
    t.circle(-90, 70)
    t.left(20)
    t.circle(75, 105)
    t.setheading(60)
    t.circle(80, 98)
    t.circle(-90, 40)
    # 花瓣2 
    t.left(180)
    t.circle(90, 40)
    t.circle(-80, 98)
    t.setheading(-83)
    # 叶子1 
    t.fd(30)
    t.left(90)
    t.fd(25)
    t.left(45)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(-80, 90)
    t.right(90)
    t.circle(-80, 90)
    t.end_fill()
    t.right(135)
    t.fd(60)
    t.left(180)
    t.fd(85)
    t.left(90)
    t.fd(80)
    # 叶子2 
    t.right(90)
    t.right(45)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(80, 90)
    t.left(90)
    t.circle(80, 90)
    t.end_fill()
    t.left(135)
    t.fd(60)
    t.left(180)
    t.fd(60)
    t.right(90)
    t.circle(200, 60)
    t.penup()

def locateX(x):
    return x - sizeX*0.5

def locateY(y):
    return y - sizeY*0.5

if __name__ == "__main__":
    main()