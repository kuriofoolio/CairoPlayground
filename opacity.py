import cairo, functions

# Set up surface
surface = cairo.ImageSurface (cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgba(0.8, .8,.8)
ctx.paint_with_alpha(1)

# 0-opaque 1-transparent
alpha=.5

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
r,g,b=0,0,1
with cairo.ImageSurface(cairo.FORMAT_RGBA128F, 600, 400) as surface:
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(.8,.876544321234,0)
    ctx.paint()

    ctx.rectangle(270,200,30,30)
    functions.return_grayscale(ctx,r,g,b)
    ctx.fill()

    surface.write_to_png(f'{functions.IMAGE_PATH}grayscale.png')



