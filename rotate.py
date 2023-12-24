import cairo , functions, math


surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,800,800)
ctx=cairo.Context(surface)
# ctx.set_source_rgba(1,1,1,0)
# ctx.paint()


# # Translate to the center of semicircle B right
ctx.translate(0, 0)

# Rotate the context by 90 degrees (in radians)
ctx.rotate(1 * math.pi)


# semicircle A left
ctx.arc(400,400,200,0*math.pi, 1*math.pi)
ctx.set_source_rgb(1,0,0)
ctx.stroke()

surface.write_to_png(f"{functions.IMAGE_PATH}graphix2.png")

