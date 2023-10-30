import cairo, functions, math

# Set up surface
surface = cairo.ImageSurface (cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)

ctx.paint()

ctx.set_source_rgb(0.8, 0.8, 0.8)

ctx.set_line_width(10)
ctx.set_source_rgb(0, 0, 0.5)
ctx.arc(150, 200, 100, 3*math.pi/4, 5*math.pi/4)

ctx.stroke()

# Arc negative
ctx.arc_negative (400, 200, 100, 3*math.pi/4, 5*math.pi/4)
ctx.stroke()

surface.write_to_png('img/arc_negative.png')


# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw the round rects
functions.roundrect(ctx, 250, 100, 300, 500, 50)
ctx.set_line_width(10)
ctx.set_source_rgb(0, 0, 0.5)
ctx.stroke()

# draw erect diamond
ctx.set_line_width(10)
ctx.set_source_rgb(0.33, 0.67, 0)

# Move to the starting point
ctx.move_to(350, 350)
ctx.line_to(400, 300)
ctx.line_to(450, 350)
ctx.line_to(400, 400)
ctx.close_path()
ctx.stroke()

# Draw the center diamond using Bezier curves
ctx.move_to(350, 350)
# ctx.curve_to(350, 350,450, 350,400, 300)
ctx.arc(375,325,25,0,math.pi)
ctx.set_source_rgb(0.33, 0.67, 0)

ctx.stroke()

#draw letter A in left top corner
ctx.move_to(320,120) #A
ctx.line_to(280,170) #B
ctx.move_to(320,120) #A
ctx.line_to(360,170) #E
ctx.move_to(300,145) #C
ctx.line_to(340,145) #D
ctx.close_path()
ctx.stroke()


surface.write_to_png('img/playing_card.png')



# ctx.move_to()

# ctx.restore()

# offset=150
# ctx.move_to(350, 200+offset)
# ctx.line_to(400, 150+offset)
# ctx.line_to(450, 200+offset)
# ctx.line_to(400, 250+offset)
# ctx.save()



