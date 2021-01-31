def get_values():
    global L, LimitN, Limit0, h,constant
    coefficient = str(input("Enter the co-efficient of the integrand F(x): "))
    Limit0 = int(input("Enter the Lower Limit: "))
    LimitN = int(input("Enter the Upper Limit: "))
    h = 1
    L = coefficient.split()
    constant = int(input("Enter Constant: "))

table = {}

def simpson_rule():
    n = LimitN - Limit0 / h
    print("I'm Using Simpson's Rule")
    generate_y(n)
    part1 = 0
    part2 = 0
    for keys in table:
        if keys % 2 and (keys!= n):
            part1+= table[keys]
        elif ((keys % 2) and keys != n and keys!=0):
            part2+=table[keys]
    Integral = h/2 * ((table[0] + table[n]) + 4*part1 + 2*part2)
    print(Integral)
  

def trapezoidal_rule():
    n = LimitN - Limit0 / h
    print("I'm using Trapezoidal Rule")
    generate_y(n)
    part1 = 0
    for keys in table:
        if keys!=0 and keys!=n:
            part1+=table[keys]
    Integral = h/2 * ((table[0] + table[n]) + 2*part1)
    print(Integral)
    

coefficient = []

def equation(coefficient):
    counter=len(coefficient)
    for i in coefficient:
        print("{}x^{}".format(i,counter),end=" ")
        if(int(i)>0 and counter!=1):
            print("+",end=" ")
        counter-=1
    if(not constant<0):
        print("+",end=" ")
    print(constant,end=" ")


def find_degree():
    for i in L:
        int(i)
        coefficient.append(i)
    
    equation(coefficient)
    if len(L) >= 3:
        simpson_rule()
    elif len(L) == 1 or len(L) == 2:
        trapezoidal_rule() 



def generate_y(limit):
    for j in range(int(limit+1)):
        counter=len(coefficient)
        temp = 0
        for i in coefficient:
            temp += int(i) * pow(j,counter)
            counter-=1
        temp += constant
        table[j] = temp
 

if __name__ == "__main__":
    get_values()
    find_degree()
   
