import  math 

#draw canvas 
# explicitly mention the surface being used
# def draw_surface(ctx,width, height,red=.33, green=.33, blue=.33):
#     surface=cairo.ImageSurface(cairo.FORMAT_RGB24,width, height)
#     ctx=cairo.Context(surface)
#     ctx.set_source_rgb(red,green,blue)

# this function takes custom rectangle params 
def draw_rectangle(ctx, x_start, y_start ,red, green, blue, rect_width=100, rect_height=100):
    ctx.rectangle(x_start, y_start, rect_width, rect_height)
    ctx.set_source_rgb(red, green, blue)
    

# this function takes custom circle params
#the context is passed because this function is called from outside this function
def draw_circle(ctx, x, y, r,scalar=2,red=.33, green=.67, blue=0):
     # Set the circle's center coordinates (x, y) and radius (r)
    ctx.arc(x, y, r, 0, (scalar)* math.pi)  # Full circle (0 to 2*pi radians) 

    ctx.set_source_rgb(red, green, blue)
    
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
        ctx.move_to(x+offset,y) #0, 350
        ctx.line_to(0+offset,y-height) #0, 150
        ctx.line_to(width+offset,y-width) #150+ofse, 150
        ctx.line_to(height+offset,y) #150+ofse, 350

        #1st bezier
        ctx.move_to(x+offset,y)
        ctx.curve_to(x+offset,y,width+offset,y,(width*.5)+offset,250)
        #2nd bezier
        ctx.move_to(width+offset,y)
        ctx.curve_to(width+offset,y,x+offset,y,(width*.5)+offset,250)

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
