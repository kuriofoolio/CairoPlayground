import math ,cairo

# global image path
IMAGE_PATH='img'

#draw canvas 
# explicitly mention the surface being used
# def draw_surface(ctx,width, height,red=.33, green=.33, blue=.33):
#     surface=cairo.ImageSurface(cairo.FORMAT_RGB24,width, height)
#     ctx=cairo.Context(surface)
#     ctx.set_source_rgb(red,green,blue)

# this function takes custom rectangle params 

def draw_rectangle(ctx, coordinates:dict)->None :
    if 'x' in coordinates and 'y' in coordinates and 'w' in coordinates and 'h' in coordinates:
        ctx.rectangle(coordinates['x'], coordinates['y'], coordinates['w'], coordinates['h'])

def set_shape_color(ctx, values:dict):
    if 'r' in values and 'g' in values and 'b' in values :
        ctx.set_source_rgb(values['r'], values['g'], values['b'])


# def draw_rectangle(ctx, x_start, y_start ,red, green, blue, rect_width=100, rect_height=100):
#     ctx.rectangle(x_start, y_start, rect_width, rect_height)
#     ctx.set_source_rgb(red, green, blue)
    

# this function takes custom circle params
#the context is passed because this function is called from outside this function
def draw_circle(ctx, x, y, r,start_angle:int,end_angle:int)->None :
    # ,red=.33, green=.67, blue=0
     # Set the circle's center coordinates (x, y) and radius (r)
     #start angle is where your arc starts 
     #end angle is where your arc ends 
    ctx.arc(x, y, r, (start_angle)* math.pi, (end_angle)* math.pi)
    # ctx.set_source_rgb(red, green, blue)

def dict_draw_circle(ctx, coordinates):
    if 'x' in coordinates and 'y' in coordinates and 'radius' in coordinates:
        ctx.arc(coordinates['x'], coordinates['y'], coordinates['radius'], 0, 2 * 3.14159)


# this function draws a sphere
def draw_sphere(ctx, x, y, radius, gradient_color1:set, gradient_color2:set)->None :
    # Create a radial gradient
    radial = cairo.RadialGradient(x, y, radius / 890898, x, y, radius)

    # Add color stops
    radial.add_color_stop_rgb(0, *gradient_color1)
    radial.add_color_stop_rgb(1, *gradient_color2)

    # Set the gradient as the source
    ctx.set_source(radial)

    # Draw the circle
    draw_circle(ctx, x, y, radius, 0, 2 )
    ctx.fill()
    

# this function draws an arrowhead
def draw_arrowhead (ctx, x,y, width, height, a,b,red=.33, blue=.67,green=0 ):
    ctx.move_to(x,y+b) #1
    ctx.line_to(a,b) #2
    ctx.line_to(a,x) #3
    ctx.line_to(width,height/2) #4
    ctx.line_to(a,height) #5
    ctx.line_to(a,height-b) #6
    ctx.line_to(x,height-b) #7
    ctx.close_path()
    ctx.set_source_rgb(red,green,blue)


# this function draws rounded arcs at the edges of a 2D shape
def roundrect(ctx, x, y, width, height, r):
    ctx.arc(x+r, y+r, r, math.pi, 3*math.pi/2)
    ctx.arc(x+width-r, y+r, r, 3*math.pi/2, 0)

    # ctx.paint()

    ctx.arc(x+width-r, y+height-r, r, 0, math.pi/2)
    ctx.arc(x+r, y+height-r, r, math.pi/2, math.pi)
    ctx.close_path()


def draw_pattern(ctx,n:int , x,y, 
                 width, height, offset=150
        
                 ):
    offset=0
    while n>0:
            #draw pattern2
            # width=200, height =200
        ctx.move_to(x,y) #0, 350
        ctx.line_to(x,y-height) #0, 150

        #1st bezier
        ctx.move_to(x+offset,y)
        ctx.curve_to(x+offset,y,width+offset,y,(width*.5)+offset,250)
        #2nd bezier
        ctx.move_to(width+offset,y)
        ctx.curve_to(width+offset,y,x+offset,y,(width*.5)+offset,250)

        n-=1
        offset+=150

    while n>0:
        ctx.line_to(x,y-height) #0, 150
        n-=1
        offset+=150


# #draw pattern1
# ctx.move_to(0,350)
# ctx.line_to(0,150)
# ctx.line_to(150,150)
# ctx.line_to(150,350)

# #1st bezier
# ctx.move_to(0,350)
# ctx.curve_to(0,350,150,350,75,250)
# #2nd bezier
# ctx.move_to(150,350)
# ctx.curve_to(150,350,0,350,75,250)

# ctx.set_source_rgb(.33,.67,0)
# ctx.stroke()

# #draw pattern2
# offset=150
# ctx.move_to(0+offset,350)
# ctx.line_to(0+offset,150)
# ctx.line_to(150+offset,150)
# ctx.line_to(150+offset,350)

# #1st bezier
# ctx.curve_to(150+offset,350,0+offset,350,75+offset,250)
# #2nd bezier
# ctx.move_to(0+offset,350)
# ctx.curve_to(0+offset,350,150+offset,350,75+offset,250)

# ctx.set_source_rgb(.33,.67,0)
# ctx.stroke()

# #draw pattern3
# ctx.move_to(0+(offset*2),350)
# ctx.line_to(0+(offset*2),150)
# ctx.line_to(150+(offset*2),150)
# ctx.line_to(150+(offset*2),350)

# #1st bezier
# ctx.curve_to(150+(offset*2),350,0+(offset*2),350,75+(offset*2),250)
# #2nd bezier
# ctx.move_to(0+(offset*2),350)
# ctx.curve_to(0+(offset*2),350,150+(offset*2),350,75+(offset*2),250)
