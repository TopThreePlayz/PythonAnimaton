import simplegui

y = 0
x = 300


    

def draw_handler(canvas):
    global x
    global y
    y = y + .5
    canvas.draw_text("Hello", (y - 50, 250), 50, "White")
    canvas.draw_circle((y, 300), 10, 10, "White")
    canvas.draw_circle((300, 300), 10, 10, "Blue")
    if (y > 80):
        canvas.draw_line((0, 230), (600, 230), 50, "Black")
        canvas.draw_text("I am a circle", (y - 80, 250), 50, "White")
    if (y > 150):
        canvas.draw_line((0, 230), (600, 230), 50, "Black")
        canvas.draw_text("This is my friend", (y - 150, 250), 50, "White")
    if (y > 200):
        y = y - .5
        x = x - 2
        canvas.draw_line((0, 230), (600, 230), 70, "Black")
        canvas.draw_text("I am bob", (250, 250), 50, "Blue")
        canvas.draw_circle((x , 300), 10, 10, "Blue")
    if (x < 201):
        y = y - .5
        canvas.draw_circle((x , 300), 10, 10, "Blue")
        canvas.draw_line((0, 230), (600, 230), 70, "Black")
        canvas.draw_text("Tasty", (190, 250), 50, "Blue")

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()




