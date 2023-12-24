import cairo, functions

# explicitly mention the surface being used
surface=cairo.ImageSurface(cairo.FORMAT_RGB24,500,500)
ctx=cairo.Context(surface)
ctx.set_source_rgb(.9,.8,.4)
# ctx.stroke()  #black output
ctx.paint() #white output

# draw rectangle
# place a rectangle at the (150, 100) position, with a width of 100 pixels and a height of 240 pixels
# ctx.rectangle(0,0,100,240)
# ctx.set_source_rgb(1,0,0)

#outer boxes
functions.draw_rectangle(ctx, 0,0,1,0,0) #top left
ctx.fill()

functions.draw_rectangle(ctx,0,400,1,0,0) #bottom left
ctx.fill()

functions.draw_rectangle(ctx,400,0,1,0,0) #top right
ctx.fill()

functions.draw_rectangle(ctx,400,400,1,0,0) #bottom right
ctx.fill()

functions.draw_rectangle(ctx,200,200,.33,.33,.33) #center
ctx.stroke()

# Draw the circle in the center using the arc method
functions.draw_circle(ctx,250, 250, 50)
ctx.fill()


#inward boxes
functions.draw_rectangle(ctx,100,100,.5,.5,.5) 
ctx.fill()

functions.draw_rectangle(ctx,300,100,.5,.5,.5)
ctx.fill()

functions.draw_rectangle(ctx,100,300,.5,.5,.5)
ctx.fill()

functions.draw_rectangle(ctx,200,400,.5,.5,.5)
ctx.fill()

functions.draw_rectangle(ctx,400,200,.5,.5,.5)
ctx.fill()

functions.draw_rectangle(ctx,200,0,.5,.5,.5)
ctx.fill()

functions.draw_rectangle(ctx,0,200,.5,.5,.5)
ctx.fill()

functions.draw_rectangle(ctx,300,300,.5,.5,.5) 
ctx.fill()


surface.write_to_png('img/etymos_board.png')

