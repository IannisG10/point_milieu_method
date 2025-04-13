from sympy import diff,symbols
from sympy import integrate

t = symbols('t')
y = symbols('y')
h = symbols('h')

def f(t,y):
    return (1/t) * (y**2 + y)

def term_of_h(hi,d = 1):
    if d > degre:
        return []
    h_term = hi
    return [h_term] + term_of_h(integrate(h_term,h),d+1)

def derive_taylor(f,ti,yi,d=1):
    if (d>degre):
        return []
    
    dy_dt = f
    derive_total = diff(f,t)*diff(ti,t) + diff(f,yi)*f
    return [dy_dt] + derive_taylor(derive_total,ti,yi,d+1)

def developement_Taylor(f,ti,yi,hi):
    list_derive = derive_taylor(f(ti,yi),ti,yi)
    list_term_h = term_of_h(hi)
    Taylor = list(zip(list_term_h,list_derive))
    return Taylor

def define_node(a,i,h):
    return a + i*h

a,b = int(input("a : ")),int(input("b : "))
N = int(input("intersection : "))
alpha = int(input("alpha : "))
degre = int(input("degré : "))

step = (b-a)/N
W = alpha
Wi = [W]

Taylor = developement_Taylor(f,t,y,h)

print("i_|__t___|__W_____")
for i in range(N):
    node = define_node(a,i,step)
    euler = 0
    for hi,yi in Taylor:
        euler += hi.subs(h,step)*yi.subs({t:node,y:W})
    
    W = W + euler
    Wi.append(W)

for i in range(len(Wi)):
    node = define_node(a,i,step)
    print(i,"|",format(node,".2f"),"|",format(Wi[i],".4f"))