def f(t,y):
    return -y + t + 1

def define_node(a,i,h):
    return a + i*h

def Taylor(f,h,t,y):
    return h*f(t+(h/2),y+(h/2)*f(t,y))

a = int(input("a"))
b = int(input("b"))
N = int(input("Nombre d'intersection"))
alpha = int(input("alpha:"))
step = (b-a)/N