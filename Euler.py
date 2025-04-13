def define_func(y,t):
    return -y*t + (4*t)/y

def define_node(a,i,h):
    return a + i*h

def developement_Taylor(t,y,h):
    return y + h*define_func(y,t)

a = int(input("a : "))
b = int(input("b : "))
N = int(input("intersection : "))
alpha = int(input("alpha : "))

h = (b-a)/N
W = alpha

print("i_|__t___|__W____")
for i in range(N+1):
    node = define_node(a,i,h)
    # y_diff = define_func(W,node)
    print(i,"|",format(node,".2f"),"|",format(W,".6f"))
    W = developement_Taylor(node,W,h)














