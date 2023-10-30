import cairo
# explicitly mention the surface being used
surface=cairo.ImageSurface(cairo.FORMAT_RGB24,600,600)
ctx=cairo.Context(surface)
ctx.set_source_rgb(.33,.33,.33)
# ctx.stroke()  #black output
ctx.paint() #white output

#draw triangle
ctx.move_to(20,300)
ctx.line_to(20,570)
ctx.line_to(500,570)
ctx.set_line_width(15)
ctx.set_source_rgb(1,0,0)
ctx.close_path()
ctx.stroke()

#draw another triangle that is diametrically opposite to the first one

ctx.move_to(500,200)
ctx.line_to(500, 450)
ctx.line_to(20, 200)
ctx.set_line_width(15)
ctx.set_source_rgb(0,0,0)
ctx.close_path()
ctx.stroke()


surface.write_to_png('img/triangle.png')

