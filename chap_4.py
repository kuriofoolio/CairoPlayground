# make necessary imports
import cairo, functions,math

surface=cairo.ImageSurface(cairo.FORMAT_RGB24,1000, 1000)
ctx=cairo.Context(surface)
ctx.set_source_rgb(.33, .33, .33)
ctx.stroke() 

#draw a pattern
functions.draw_pattern(ctx,5,0,350,150,150)
ctx.set_line_width(10)
ctx.set_source_rgb(.33,.67,0)
ctx.stroke()


surface.write_to_png(f'{functions.IMAGE_PATH}/pattern.png')


surface=cairo.ImageSurface(cairo.FORMAT_RGB24,600, 400)
ctx=cairo.Context(surface)
ctx.set_source_rgb(.33, .33, .33)
ctx.stroke() 




# points=[]
# for x in range(-100,101):
#     y=x**2
#     points.append((x,y))

# ctx.move_to(points[0][0], points[0][1])
# for x,y in points:
#     ctx.line_to(x,y)


# draw an arc
# functions.draw_circle(ctx, 200,200,150,.5,)
# functions.draw_circle(ctx, 250,250,50,.5)
ctx.arc(200,200,150,3*math.pi/4,5*math.pi/4)
ctx.set_source_rgb(.33,.67,0)
ctx.stroke()

# Draw an arc bending to the right, touching the ends of the previous arc
ctx.arc(200, 200, 150, 5 * math.pi / 4, 3 * math.pi / 4)
ctx.set_source_rgb(0, 0.33, 0.67)
ctx.stroke()


surface.write_to_png(f'{functions.IMAGE_PATH}/2arcs.png')

#draw a sphere
surface=cairo.ImageSurface(cairo.FORMAT_RGB24,600, 400)
ctx=cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint() 

functions.draw_sphere(ctx, 300, 200, 150, (.67, 0.98, 0.5), (0,0,0))
surface.write_to_png(f'{functions.IMAGE_PATH}/sphere.png')


