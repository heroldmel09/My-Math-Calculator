import math
def main():
    x= list(map(int, input("Enter multiple values of X: ").split()))
    y= list(map(int , input("Enter multiple values of Y: ").split()))

    xy= value_xy(x,y)
    x2= value_x2(x)
    y2= value_y2(y)
    sxy=sum(xy)
    sx2=sum(x2)
    sy2=sum(y2)
    sx=sum(x)
    sy=sum(y)
    u=len(x)
    corre=cor_coe(u,sx,sy,sxy,sx2,sy2)
    b=cal_b(u,sx,sy,sxy,sx2,sy2)
    a=cal_a(u,sx,sy,sxy,sx2,sy2,b)
    re=reg_equa(a,b)
    print(f"The value of XY:{xy}")
    print(f"The value of X2:{x2}")
    print(f"The value of y2:{y2}")
    print(f"The sum of XY: {sxy:,}")
    print(f"The sum of X2: {sx2:,}")
    print(f"The sum of Y2: {sy2:,}")
    print(f"The sum of X: {sx:,}")
    print(f"The sum of Y: {sy:,}")
    print(f"The sum of B: {b:,}")
    print(f"The sum of A: {a:,}")
    print (f"The regression equation The x is 5 :{corre}")
    print (f"The correlation coefficient:{re}")



def value_xy(a,b):
    par=len(a)
    val_xy=[]
    for i in range(par) :
        sum=a[i]*b[i]
        val_xy.append(sum)
    return val_xy

def value_x2(a):
    val_x2=[]
    for i in a:
        sum=i**2
        val_x2.append(sum)
    return val_x2

def value_y2(a):
    val_y2=[]
    for i in a:
        sum=i**2
        val_y2.append(sum)
    return val_y2

def cor_coe(n,sx,sy,sxy,sx2,sy2):
    return round (((n*sxy)-(sx*sy))/math.sqrt(((n*sx2)-(sx**2))*((n*sy2)-(sy**2))),3)

def cal_b(n,sx,sy,sxy,sx2,sy2):
    return round(((n*sxy)-(sx*sy))/((n*sx2)-(sx**2)),2)

def cal_a(n,sx,sy,sxy,sx2,sy2,b):
    return round(((sy-(b*sx))/n),2)

def reg_equa(x,y):
    return x+(y*5)  

    


main()