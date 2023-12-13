import functions, cairo, math


#set the surface
surface=functions.draw_surface(800,800)
ctx=cairo.Context(surface)
ctx.set_source_rgb(1,1,1)
ctx.paint()

# rectangle
ctx.rectangle(200,200,400,400)
ctx.set_source_rgb(0,0,0)
ctx.stroke()

#semicircle B bottom
ctx.arc(400,600,200,math.pi,2*math.pi)
ctx.set_source_rgb(0,0,1)
ctx.stroke()

# semicircle A left
ctx.arc(200,400,200,1.5*math.pi, .5*math.pi)
ctx.set_source_rgb(1,0,0)
ctx.stroke()

ctx.save()
# Translate to the center of semicircle B right
ctx.translate(600, 400)

#semicircle B right
ctx.arc(0,0,200,0.5*math.pi,1.5*math.pi)
ctx.set_source_rgb(0,0,1)
ctx.stroke()

ctx.restore()

ctx.translate(400,200)
# #semicircle A top
ctx.arc(00,0,200,0,1*math.pi)
ctx.set_source_rgb(1,0,0)
ctx.stroke()

surface.write_to_png(f"{functions.IMAGE_PATH}spiral_in_square.png")

