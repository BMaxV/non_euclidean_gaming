from vector import vector
import math


def test():
    v1=vector.Vector(1,1,0)
    v2=vector.Vector(1,0.8,0)
    v3=vector.Vector(1,0,0)
    
    v1=v1.normalize()
    v2=v2.normalize()
    v3=v3.normalize()
    
    ang1=vector.angle_v1v2(v1,v2)
    ang2=vector.angle_v1v2(v2,v1)
    print(ang1,ang2)
    
    ang1=vector.get_radians_from_vector(v1.x,v1.y)
    ang2=vector.get_radians_from_vector(v2.x,v2.y)
    ang3=vector.get_radians_from_vector(v3.x,v3.y)
    print(ang1,ang2,ang3)
    
    xs=[]
    ys1=[]
    ys2=[]
    ys3=[]
    
    c=0
    while c < 8:
        x=math.cos(c*math.pi)
        y=math.sin(c*math.pi)
        x2=math.cos(c/2*math.pi)
        y2=math.sin(c/2*math.pi)
        my_v=vector.Vector(x,y,0)
        my_v2=vector.Vector(x2,y2,0)
        angx=vector.get_radians_from_vector(my_v.x,my_v.y)
        angx2=vector.get_radians_from_vector(my_v2.x,my_v2.y)
        #print(round(c,3),round(angx/math.pi,3),round(angx2/math.pi,3))
        xs.append(c)
        ys1.append(math.cos(c*math.pi))
        
        my_val=math.sin(c/4*math.pi)# < --- magic
        my_val=abs(my_val) # <--- comment...
        ys2.append(my_val) 
        
        # dividing the counter by 4 makes the period longer
        # doing sin instead of cos, means it will start at 0
        # given that you need a full rotation to see anything happen
        # that means your initial position doesn't matter
        
        # ... so, the peaks of the regular grey wave are "normal straight"
        # if we want something to happen on every second rotation,
        # we must take the aboslute value. If we didn't, we would 
        # only create the effect on the first rotation and then the 4th
        # from that, we don't want. we want to phase in and out every
        
        # second rotation. alternatively, we can add something 
        # and shift the curve up a bit.
        
        
        
        my_val=math.sin((c/2)*math.pi-math.pi*0.5)
        my_val=my_val/2 +0.5 # make amplitude smaller and shift everything up.
        ys3.append(my_val) 
        
        # but as can be seen form the peaks, the difference is very small.
        # you want things to trigger on the grey peaks
        # but that's it.
        
        # you want to make sure things are out of sight anway.
        # either completely behind the back, or ideally obscured 
        # by other means.
        
        c+=0.1
    
    return xs, ys1,ys2,ys3
def render_demo(xs, ys1,ys2,ys3):
    from geom import geom
    
    l=[]
    c=0
    m=len(xs)
    while c < m-1:
        xs_1,xs_2=xs[c],xs[c+1]
        ys1_1,ys1_2=ys1[c],ys1[c+1]
        ys2_1,ys2_2=ys2[c],ys2[c+1]
        ys3_1,ys3_2=ys3[c],ys3[c+1]
        
        p1,p2=(xs_1,ys1_1,0),(xs_2,ys1_2,0)
        p11,p22=(xs_1,ys2_1,0),(xs_2,ys2_2,0)
        p31,p32=(xs_1,ys3_1,0),(xs_2,ys3_2,0)
        l.append(geom.Line.from_two_points(p1,p2))
        l[-1].style="stroke:rgb(150,150,150);"
        l.append(geom.Line.from_two_points(p11,p22))
        l.append(geom.Line.from_two_points(p31,p32))
        l[-1].style="stroke:rgb(0,100,0);"
        c+=1
    l.append(geom.Line.from_two_points((0,0,0),(xs[-1],0,0)))
    l.append(geom.Line.from_two_points((0,0.8,0),(xs[-1],0.8,0)))
    l[-1].style="stroke:red;"
    view_box_d=geom.make_view_box_d(l,scale=1.1)
    
    fl=[]
    for x in l:
        fl.append(x.as_svg())
    geom.main_svg(fl,"demo.svg",view_box_d=view_box_d)
    
    

if __name__=="__main__":
    l=test()
    if False:
        render_demo(*l)
