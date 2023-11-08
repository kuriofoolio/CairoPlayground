# make necessary imports
import cairo, functions

surface=cairo.ImageSurface(cairo.FORMAT_RGB24,1000, 1000)
ctx=cairo.Context(surface)
functions.set_shape_color(ctx, {'r':.67, 'g':.59, 'b':.11})
ctx.paint() 

r=100
colors={'r':1,'g':0,'b':0}
                            # SQUARE WITH SPIRALS
#draw square                             
rect_points={'x':400,'y':200,'w':200,'h':200}
functions.draw_rectangle(ctx, rect_points)
functions.set_shape_color(ctx, {'r':.0, 'g':.0, 'b':.0})
ctx.stroke()

# draw spirals 
functions.draw_circle(ctx, 400,200,r, 3/2,1/2)
functions.set_shape_color(ctx, colors)
ctx.stroke()

functions.draw_circle(ctx, 600,400,r, 1/2,3/2)
functions.set_shape_color(ctx, colors)
ctx.stroke()

functions.draw_circle(ctx, 400,400,r, 1,0)
functions.set_shape_color(ctx, colors)
ctx.stroke()

functions.draw_circle(ctx, 600,200,r, 0,1)
functions.set_shape_color(ctx, colors)
ctx.stroke()

surface.write_to_png('img/spiral.png')



















#draw a segment 
# ctx.new_sub_path()
# functions.set_shape_color(ctx, {'r':.5, 'g':.67, 'b':.22})
# functions.draw_circle(ctx, 350,200,150,.75, 5/4)
# # ctx.arc(350,200,150,.75, 5/4)
# ctx.close_path()

# ctx.move_to(x+offset,y) #0, 350
#         ctx.line_to(0+offset,y-height) #0, 150
#         ctx.line_to(width+offset,y-width) #150+ofse, 150
#         ctx.line_to(height+offset,y) #150+ofse, 350



