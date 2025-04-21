def f(t,y):
    return -y + t + 1

def define_node(a,i,h):
    return a + i*h


def pt_milieu(func,h,ti,Wi):
    k1 = ti + (h/2)
    k2 = Wi + (h/2)*func(ti,Wi)
    k3 = func(k1,k2)

    return k3

