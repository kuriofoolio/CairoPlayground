import cairo 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600,400)
ctx=cairo.Context(surface)
ctx.set_source_rgb(.8,.8,.8)
ctx.paint()

ctx.rectangle (150,100, 100,400)
ctx.set_source_rgb(1,0,0)
ctx.fill()

surface.write_to_png ('img/rect.png')
