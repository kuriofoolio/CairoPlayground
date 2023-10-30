# make necessary imports
import cairo, functions

# explicitly mention the surface being used
surface=cairo.ImageSurface(cairo.FORMAT_RGB24,500,500)
ctx=cairo.Context(surface)
ctx.set_source_rgb(.33,.33,.33)
# ctx.stroke()  #black output
ctx.paint() #white output

# Draw the circle in the center using the arc method
functions.draw_circle(ctx,250, 250, 150, 2,0,0,0)
ctx.fill()

#Draw lines in circles
ctx.move_to(250,100)
ctx.line_to(250,400)
ctx.move_to(400,250)
ctx.line_to(100,250)
ctx.close_path()
ctx.set_source_rgb(.33, .67, 0)
ctx.set_line_width(10)
ctx.stroke()

#Draw arc 
functions.draw_circle(ctx,250, 250, 145,.5)
ctx.stroke()

surface.write_to_png('img/circle.png')