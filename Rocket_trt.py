import turtle

window = turtle.Screen()

r = turtle.Turtle()
X = 0
Y = -200
r.speed(100)
r.up()
r.setposition(X, Y)
r.down()
r.speed(1)

h_con = 100
w_con = 50
h3 = 100
h2 = 110
h1 = 120
h_side = 150
w_side = 40

r.goto(X+w_con*0.7, Y)  # 1 ступень
r.goto(X+w_con*0.7, Y+h1*0.9)
r.goto(X+w_con*0.6, Y+h1)
r.goto(X-w_con*0.6, Y+h1)
r.goto(X-w_con*0.7, Y+h1*0.9)
r.goto(X-w_con*0.7, Y)
r.goto(X, Y)

r.up()  # 2 ступень
r.setposition(X, Y+h1)
r.down()
r.goto(X+w_con*0.6, Y+h1)
r.goto(X+w_con*0.6, Y+h1+h2*0.9)
r.goto(X+w_con*0.5, Y+h1+h2)
r.goto(X-w_con*0.5, Y+h1+h2)
r.goto(X-w_con*0.6, Y+h1+h2*0.9)
r.goto(X-w_con*0.6, Y+h1)
r.goto(X, Y+h1)

r.up()  # 3 ступень
r.setposition(X, Y+h1+h2)
r.down()
r.goto(X+w_con*0.5, Y+h1+h2)
r.goto(X+w_con*0.5, Y+h1+h2+h3)
r.goto(X-w_con*0.5, Y+h1+h2+h3)
r.goto(X-w_con*0.5, Y+h1+h2)
r.goto(X, Y+h1+h2)

r.up()  # обтекатель
r.setposition(X, Y+h1+h2+h3)
r.down()
r.goto(X+w_con*0.5, Y+h1+h2+h3)
r.goto(X+w_con*0.6, Y+h1+h2+h3+h_con*0.1)
r.goto(X+w_con*0.6, Y+h1+h2+h3+h_con*0.5)
r.goto(X, Y+h1+h2+h3+h_con)
r.goto(X-w_con*0.6, Y+h1+h2+h3+h_con*0.5)
r.goto(X-w_con*0.6, Y+h1+h2+h3+h_con*0.1)
r.goto(X-w_con*0.5, Y+h1+h2+h3)

r.up()  # бок.ускор.лев.
r.setposition(X-w_con*0.7, Y)
r.down()
r.goto(X-w_con*0.7-w_side, Y)
r.goto(X-w_con*0.7-w_side, Y+h_side*0.8)
r.goto(X-w_con*0.7-w_side*0.5, Y+h_side)
r.goto(X-w_con*0.7, Y+h_side*0.8)
r.goto(X-w_con*0.7, Y)

r.up()  # бок.ускор.прав.
r.setposition(X+w_con*0.7, Y)
r.down()
r.goto(X+w_con*0.7+w_side, Y)
r.goto(X+w_con*0.7+w_side, Y+h_side*0.8)
r.goto(X+w_con*0.7+w_side*0.5, Y+h_side)
r.goto(X+w_con*0.7, Y+h_side*0.8)
r.goto(X+w_con*0.7, Y)

r.up()  # сопло бок.ускор.лев.
r.setposition(X-w_con*0.7-w_side*0.5, Y)
r.down()
r.goto(X-w_con*0.7-w_side*0.3, Y-h1*0.2)
r.goto(X-w_con*0.7-w_side*0.7, Y-h1*0.2)
r.goto(X-w_con*0.7-w_side*0.5, Y)

r.up()  # сопло бок.ускор.прав.
r.setposition(X+w_con*0.7+w_side*0.5, Y)
r.down()
r.goto(X+w_con*0.7+w_side*0.3, Y-h1*0.2)
r.goto(X+w_con*0.7+w_side*0.7, Y-h1*0.2)
r.goto(X+w_con*0.7+w_side*0.5, Y)

r.up()  # сопло сред.лев.
r.setposition(X-w_con*0.3, Y)
r.down()
r.goto(X-w_con*0.5, Y-h1*0.2)
r.goto(X-w_con*0.1, Y-h1*0.2)
r.goto(X-w_con*0.3, Y)

r.up()  # сопло сред.прав.
r.setposition(X+w_con*0.3, Y)
r.down()
r.goto(X+w_con*0.5, Y-h1*0.2)
r.goto(X+w_con*0.1, Y-h1*0.2)
r.goto(X+w_con*0.3, Y)

r.up()  # крыло лев.
r.setposition(X-w_con*0.5, Y+h1+h2+h3*0.3)
r.down()
r.goto(X-w_con*0.7, Y+h1+h2+h3*0.3)
r.goto(X-w_con*0.5, Y+h1+h2+h3*0.6)

r.up()  # крыло прав.
r.setposition(X+w_con*0.5, Y+h1+h2+h3*0.3)
r.down()
r.goto(X+w_con*0.7, Y+h1+h2+h3*0.3)
r.goto(X+w_con*0.5, Y+h1+h2+h3*0.6)

r.up()  # иллюминатор
r.setposition(X, Y+h1+h2+h3+h_con*0.3)
r.down()
r.circle(w_con*0.2)

r.up()  #  надпись
r.setposition(X, Y+h1+h2+h3*0.05)
r.down()
r.write('S\nI\nR\nI\nU\nS')

r.hideturtle()

window.mainloop()