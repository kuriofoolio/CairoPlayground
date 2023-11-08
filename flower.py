# make necessary imports
import cairo, functions

surface=cairo.ImageSurface(cairo.FORMAT_RGB24,600, 600)
ctx=cairo.Context(surface)
functions.set_shape_color(ctx, {'r':.1, 'g':.1, 'b':.1})
ctx.paint() 

#global radius value for arcs
r=100 

                            # FLOWER
#draw square                             
rect_points={'x':200,'y':200,'w':200,'h':200}
functions.draw_rectangle(ctx, rect_points)
functions.set_shape_color(ctx, {'r':.0, 'g':.0, 'b':.0})
ctx.set_line_width(10)
ctx.stroke()

#center petal
functions.draw_circle(ctx, 300,200,r, 0,1)
ctx.stroke()

#left petal
functions.draw_circle(ctx, 200,300,r, 3/2,0)
ctx.stroke()

#right petal
functions.draw_circle(ctx, 400,300,r, 1,3/2)
ctx.stroke()

#right inner petal
functions.draw_circle(ctx, 300,250,50, 3/2,1/2)
ctx.stroke()

#left inner petal
functions.draw_circle(ctx, 300,250,50, 1/2,3/2)
ctx.stroke()

# stalk
ctx.move_to(300,300)
ctx.line_to(300,400)
ctx.set_line_width(10)
functions.set_shape_color(ctx, {'r':.0, 'g':.0, 'b':.0})
ctx.stroke()

surface.write_to_png('img/flower.png')



















