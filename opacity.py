import cairo, functions, math

# Set up surface
surface = cairo.ImageSurface (cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, .8,.8)
ctx.paint_with_alpha(1)

# 0-opaque 1-transparent
alpha=.5
pi=functions.PI

# #green rect
redA, greenA, blueA=0,1,0
green_rect = {'x': 195, 'y': 205, 'w': 100, 'h': 100}
functions.draw_rectangle(ctx, green_rect)
ctx.set_source_rgba(redA, greenA, blueA, 1/1e1)
# ctx.set_source_rgba(redA, greenA, blueA,alpha)
ctx.set_line_width(10)
ctx.stroke()

#red rect
redB, greenB, blueB=1,0,0
red_rect = {'x': 275, 'y': 125, 'w': 100, 'h': 100}
functions.draw_rectangle(ctx, red_rect)
# ctx.set_source_rgba(redB, greenB, blueB, alpha)
ctx.set_source_rgba(redB, greenB, blueB,  1/1e1)
ctx.stroke()

#overlap area
red = redA * alpha + redB * (1 - alpha)
green = greenA * alpha + greenB * (1 - alpha)
blue = blueA * alpha + blueB * (1 - alpha)

ctx.rectangle(270,200,30,30)
ctx.set_source_rgb(red, green, blue)
ctx.fill()

surface.write_to_png(f'{functions.IMAGE_PATH}opacity.png')


# transparent background
with cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 400) as surface:
    ctx = cairo.Context(surface)

    ctx.rectangle(270,200,30,30)
    ctx.set_source_rgb(red, green, blue)
    ctx.fill()

    surface.write_to_png(f'{functions.IMAGE_PATH}transparency.png')


# grayscale
r,g,b=1,1,1
with cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 400) as surface:
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(.8,.8,.8)
    ctx.paint_with_alpha(.0004)


    # ctx.scale(5,5)
    # ctx.translate(150,0)
    # ctx.rotate(1/9*pi)
    ctx.rectangle(0,0,150,150)
    functions.return_grayscale(ctx,r,g,b)
    ctx.fill()

    # flip to the right 
    ctx.scale(1,1)
    ctx.translate(0,0)
    # ctx.rotate(1/9*pi)
    ctx.rectangle(150,0,150,150)
    functions.return_grayscale(ctx,r,g,b)
    ctx.fill()

    # flip down

    ctx.scale(1,1)
    ctx.translate(0,0)
    # ctx.rotate(1/9*pi)
    ctx.rectangle(0,150,150,150)
    functions.return_grayscale(ctx,r,g,b)
    ctx.fill()

    
    # ellipse
    # ctx.save()
    # ctx.translate(150,200)
    # ctx.scale(2,1)
    # ctx.translate(-150,-200)
    # functions.draw_circle(ctx,150,200, 100,0,2 )
    # # ctx.translate(-300, -350)
    # # ctx.arc(300, 350, 100, 0, math.pi*2)
    # ctx.restore()
    # ctx.set_source_rgb(0.8, 0, 0)
    # ctx.fill_preserve()
    
    # ctx.set_source_rgb(1, 1, 1)
    # ctx.set_line_width(10)
    # ctx.stroke()

    

    surface.write_to_png(f'{functions.IMAGE_PATH}grayscale.png')

