import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(10)
t.pensize(2)
h =0.5
t.goto(50,0)

for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.6
    t.fillcolor(c)
    t.begin_fill()
    t.fd(i*2)
    t.rt(190)
    t.circle(i+20,144)
    t.end_fill()
t.done

