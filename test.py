import cairo, functions, time

# Set up surface
surface = cairo.ImageSurface (cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw the rectangle in the center
rect_coordinates = {'x': 200, 'y': 200, 'width': 100, 'height': 100}
functions.draw_rectangle(ctx, rect_coordinates)
values = {'r': 0, 'g': 1, 'b': 0}
functions.set_shape_color(ctx,  values)
ctx.fill()

surface.write_to_png('img/test_dict.png')



# bouncing sphere
# Create an image surface
width, height = 600, 400
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Initial sphere parameters
radius = 50
x, y = width // 2, height // 2
speed = 2
direction = [1, 1]  # x and y direction

# Gradient colors
color1 = (1, 0, 0)
color2 = (0, 0, 1)

# Number of frames
num_frames = 10

for frame in range(num_frames):
    # Clear the canvas
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    # Update sphere position
    x += speed * direction[0]
    y += speed * direction[1]

    # Bounce off the walls
    if x - radius <= 0 or x + radius >= width:
        direction[0] *= -1
    if y - radius <= 0 or y + radius >= height:
        direction[1] *= -1

    # Draw the sphere
    functions.draw_sphere(ctx, x, y, radius, color1, color2)

    # Save the frame
    surface.write_to_png(f'{functions.IMAGE_PATH}/bounce_frame_{frame}.png')

    # Pause for a short time to control the animation speed
    time.sleep(0.05)



# ctx.move_to()

# ctx.restore()

# offset=150
# ctx.move_to(350, 200+offset)
# ctx.line_to(400, 150+offset)
# ctx.line_to(450, 200+offset)
# ctx.line_to(400, 250+offset)
# ctx.save()




#circumscribe triangle

# Draw the circle in the center using the arc method
# r=150
# # functions.draw_circle(ctx,250, 250, 150, 2,0,0,0)
# # ctx.fill()

# #draw line from center to top of circle
# x1,y1=50,50
# angle_in_radians=5/12 
# x2 = x1 + r * math.cos(angle_in_radians)
# y2 = y1 + r * math.sin(angle_in_radians)

# ctx.move_to(x1,y1)
# ctx.line_to(x2,y2)
# ctx.set_source_rgb(.33,.67,0)
# ctx.stroke()

#draw an arrow
# functions.draw_arrowhead(ctx, 0,0,500,500,300,150,.9,.8,.7)
# ctx.stroke()
