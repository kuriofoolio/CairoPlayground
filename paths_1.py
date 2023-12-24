import cairo, math

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(.33, .67, .45)
# ctx.paint()
ctx.paint_with_alpha(.7)

# Sub-path1 - bigger triangle
ctx.move_to(50, 50)
ctx.line_to(400, 200)
ctx.line_to(50, 350)
ctx.close_path()

# Sub-path2 - smaller triangle
ctx.move_to(100, 100)
ctx.set_source_rgb(1, 0, 0)  # Set the color for the triangles
ctx.line_to(200, 200)
ctx.line_to(100, 300)
ctx.close_path()

ctx.set_line_width(10)
ctx.stroke()  # Draw the triangles

# Sub-path3- number 7
ctx.move_to(450, 100)
ctx.set_source_rgb(0.5, 0.6, 0.8)  # Set the color for number 7
ctx.set_line_width(20)
ctx.line_to(500, 100)
ctx.line_to(450, 300)
ctx.stroke()  # Draw number 7

# Create a transformation matrix for a diametrical opposite
ctx.save()  # Save the current state
ctx.translate(500, 200)  # Translate to the center of the number 7
ctx.rotate(math.pi)  # Rotate 180 degrees (pi radians)
ctx.translate(-500, -200)  # Translate back to the original position

# Draw the diametrical opposite of number 7
ctx.move_to(450, 100)
ctx.set_source_rgb(0.1, 0.9, 0.2)  # Set a different color
ctx.set_line_width(20)
ctx.line_to(500, 100)
ctx.line_to(450, 300)
ctx.stroke()  # Draw the diametrical opposite of number 7

ctx.restore()

surface.write_to_png('img/paths.png')

