def f(t,y):
    return -y + t + 1

def define_node(a,i,h):
    return a + i*h

def pt_milieu(func,ti,Wi,h):
    k1 = ti + h/2
    k2 = Wi + h/2*func(ti,Wi)
    k3 = Wi + h*(func(k1,k2))

    return k3

a = int(input("Entrer a : "))
b = int(input("Entrer b : "))
N = int(input("Nombre d'intersection :"))
alpha = int(input("alpha : "))

step = (b-a)/N
W = alpha

approximations = [W]
for i in range(N):
    node = define_node(a,i,step)
    W = pt_milieu(f,node,W,step)
    print(W)
    




