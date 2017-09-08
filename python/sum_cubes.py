
def sum_cubes_On(n):
    return sum(x * x * x for x in range(n + 1)) 

def sum_cubes_O1(n):
    return (n * (n + 1) // 2)**2

t1 = sum_cubes_On(50)
t2 = sum_cubes_O1(50)

o = "On == {} O1 == {}".format(t1, t2)
print(o)
