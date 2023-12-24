
import cairo
#polygons

with cairo.SVGSurface("img/trapezium.svg", 1000,1000) as surface:

    ctx = cairo.Context(surface)
    ctx.set_source_rgb(.9,.8,.4)
    # ctx.stroke()  #black output
    ctx.paint() #white output

    #trapezium
    ctx.line_to(100,0)
    ctx.line_to(200,0)
    ctx.line_to(250,50)
    ctx.line_to(50,50)
    ctx.close_path()
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()

    #rhombus
    ctx.line_to(300,50)
    ctx.line_to(440,50)
    ctx.line_to(400,90)
    ctx.line_to(260,90)
    ctx.close_path()
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()
    # surface.write_to_png('polygons.png')
