import cairo 
with cairo.SVGSurface("img/example.svg", 400, 200) as surface:

    context = cairo.Context(surface)

    x, y, x1, y1 = 0.5, 0.5, 0.4, 0.9

    x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5

#     the curves
    context.scale(400, 200)

    context.set_line_width(.09)

    context.move_to(x,y)

    context.curve_to(x1, y1, x2, y2, x3, y3)

    context.stroke()
    
#     the lines 
    context.set_source_rgba(1.0, 0.0, 0.0, 1.0)

    context.set_line_width(0.09)

    context.move_to(x, y)

    context.line_to(x1, y1)

    context.move_to(x2, y2)

    context.line_to(x3, y3)

    context.stroke()
    
  
