from graphics import *
# The window
win = GraphWin("My Calculator", 320, 500)
win.setCoords(0, 0, 320, 500)
win.setBackground(color_rgb(32, 32, 32))
# Drawing buttons
for i in range(6):
    line = Line(Point(0, i*70), Point(320, i*70))
    line.setFill(color_rgb(64, 64, 64))
    line.setWidth(2)
    line.draw(win)


for i in range(4):
    line = Line(Point(i*80, 0), Point(i*80, 350))
    line.setFill(color_rgb(64, 64, 64))
    line.setWidth(2)
    line.draw(win)
line = Line(Point(160, 350), Point(160, 443))
line.setFill(color_rgb(64, 64, 64))
line.setWidth(2)
line.draw(win)
# Filling buttons
button = Text(Point(40, 35), "±")
button.setFill("white")
button.draw(win)

button = Text(Point(120, 35), "0")
button.setFill("white")
button.draw(win)

button = Text(Point(200, 35), ",")
button.setFill("white")
button.draw(win)

button = Text(Point(280, 35), "=")
button.setFill("white")
button.draw(win)

button = Text(Point(40, 105), "1")
button.setFill("white")
button.draw(win)

button = Text(Point(120, 105), "2")
button.setFill("white")
button.draw(win)

button = Text(Point(200, 105), "3")
button.setFill("white")
button.draw(win)

button = Text(Point(280, 105), "+")
button.setFill("white")
button.draw(win)

button = Text(Point(40, 175), "4")
button.setFill("white")
button.draw(win)

button = Text(Point(120, 175), "5")
button.setFill("white")
button.draw(win)

button = Text(Point(200, 175), "6")
button.setFill("white")
button.draw(win)

button = Text(Point(280, 175), "-")
button.setFill("white")
button.draw(win)

button = Text(Point(40, 245), "7")
button.setFill("white")
button.draw(win)

button = Text(Point(120, 245), "8")
button.setFill("white")
button.draw(win)

button = Text(Point(200, 245), "9")
button.setFill("white")
button.draw(win)

button = Text(Point(280, 245), "×")
button.setFill("white")
button.draw(win)

button = Text(Point(40, 315), "**")
button.setFill("white")
button.draw(win)

button = Text(Point(120, 315), "%")
button.setFill("white")
button.draw(win)

button = Text(Point(200, 315), "//")
button.setFill("white")
button.draw(win)

button = Text(Point(280, 315), "÷")
button.setFill("white")
button.draw(win)

button = Text(Point(80, 395), "C")
button.setFill("white")
button.draw(win)

button = Text(Point(240, 395), "Delete")
button.setFill("white")
button.draw(win)

screen = Entry(Point(160, 472), 12)
screen.setFill(color_rgb(95, 95, 95))
screen.setSize(36)
screen.setTextColor("white")
screen.text.set("0")
screen.setStyle("italic")
screen.draw(win)


def operation(st):
    # To maintain operations
    global total
    if st != "" and sign is None:
        if "." in st:
            total = float(st)
        else:
            total = int(st)
    if st != "" and sign == 1:
        if "." in st:
            total += float(st)
        else:
            total += int(st)
    if st != "" and sign == 2:
        if "." in st:
            total -= float(st)
        else:
            total -= int(st)
    if st != "" and sign == 3:
        if "." in st:
            total *= float(st)
        else:
            total *= int(st)
    if st != "" and sign == 4:
        if "." in st:
            total /= float(st)
        else:
            total /= int(st)


def click(p1, st):
    global sign
    global total
    # Getting button clicks
    # ------ Operation signs area ------
    if (240 <= p1.x <= 320) and (0 <= p1.y <= 70):
        # equal sign
        operation(st)
        sign = None
        screen.setText(str(total))
        st = "0"
    if (240 <= p1.x <= 320) and (70 <= p1.y <= 140):
        # 1 is stored for plus sign
        if sign is None:
            if "." in st:
                total = float(st)
            else:
                total = int(st)
        else:
            operation(st)
        st = ""
        sign = 1
        screen.setText(str(total))

    if (240 <= p1.x <= 320) and (140 <= p1.y <= 210):
        # 2 is stored for minus sign
        if sign is None:
            if "." in st:
                total = float(st)
            else:
                total = int(st)
        else:
            operation(st)
        st = ""
        sign = 2
        screen.setText(str(total))

    if (240 <= p1.x <= 320) and (210 <= p1.y <= 280):
        # 3 is stored for multi sign
        if sign is None:
            if "." in st:
                total = float(st)
            else:
                total = int(st)
        else:
            operation(st)
        st = ""
        sign = 3
        screen.setText(str(total))

    if (240 <= p1.x <= 320) and (280 <= p1.y <= 350):
        # 4 is stored for division sign
        if sign is None:
            if "." in st:
                total = float(st)
            else:
                total = int(st)
        else:
            operation(st)
        st = ""
        sign = 4
        screen.setText(str(total))

    # ------- Getting number clicks ------
    else:
        if (80 <= p1.x <= 160) and (0 <= p1.y <= 70):
            if st == "0":
                st = "0"
                screen.setText(st)

            else:
                st += "0"
                screen.setText(st)

        if (160 <= p1.x <= 240) and (0 <= p1.y <= 70):
            if st == "0":
                st = "0."
                screen.setText(st)

            else:
                st += "."
                screen.setText(st)

        if (0 <= p1.x <= 80) and (70 <= p1.y <= 140):
            if st == "0":
                st = "1"
                screen.setText(st)

            else:
                st += "1"
                screen.setText(st)

        if (80 <= p1.x <= 160) and (70 <= p1.y <= 140):
            if st == "0":
                st = "2"
                screen.setText(st)

            else:
                st += "2"
                screen.setText(st)

        if (160 <= p1.x <= 240) and (70 <= p1.y <= 140):
            if st == "0":
                st = "3"
                screen.setText(st)

            else:
                st += "3"
                screen.setText(st)

        if (0 <= p1.x <= 80) and (140 <= p1.y <= 210):
            if st == "0":
                st = "4"
                screen.setText(st)

            else:
                st += "4"
                screen.setText(st)

        if (80 <= p1.x <= 160) and (140 <= p1.y <= 210):
            if st == "0":
                st = "5"
                screen.setText(st)

            else:
                st += "5"
                screen.setText(st)

        if (160 <= p1.x <= 240) and (140 <= p1.y <= 210):
            if st == "0":
                st = "6"
                screen.setText(st)

            else:
                st += "6"
                screen.setText(st)

        if (0 <= p1.x <= 80) and (210 <= p1.y <= 280):
            if st == "0":
                st = "7"
                screen.setText(st)

            else:
                st += "7"
                screen.setText(st)

        if (80 <= p1.x <= 160) and (210 <= p1.y <= 280):
            if st == "0":
                st = "8"
                screen.setText(st)

            else:
                st += "8"
                screen.setText(st)

        if (160 <= p1.x <= 240) and (210 <= p1.y <= 280):
            if st == "0":
                st = "9"
                screen.setText(st)

            else:
                st += "9"
                screen.setText(st)

        if (160 <= p1.x <= 320) and (350 <= p1.y <= 443):
            st = st[:-1]
            screen.setText(st)

        if (0 <= p1.x <= 160) and (350 <= p1.y <= 443):
            st = "0"
            screen.setText(st)
    return st


total = 0
sign = None
string = ""
while win.isOpen():
    point = Point(0, 0)
    try:
        point = win.getMouse()
    except GraphicsError:
        win.close()
    string = click(point, string)
