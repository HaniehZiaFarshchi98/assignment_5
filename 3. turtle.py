import turtle

colors = [' ', 'red' , 'blue', 'yellow','green', 'purple', 'pink' ]
x = int(input("input sides: "))
color = int(input("select color: 1.red, 2.blue, 3.yellow, 4.green, 5.purple, 6.pink :  "))

degree = 180 - ((x-2)*180) / (x)
turtle.dot()

for i in range (x):
    turtle.color(colors[color])
    turtle.right(degree)
    turtle.forward(30)


turtle.done()
