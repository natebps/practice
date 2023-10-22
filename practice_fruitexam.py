#N(1<= N <= 100)
N = int(input('How many fruits do you have? : '))
for x in range(N) :
    l = float(input('Input the length of the fruit: ')) 
    w = float(input('Input the width of the fruit: ')) 

percent = w/l * 100

print(percent,'%')
def all_cost():
    if percent <= 75:
        cost = 5
    else:
        cost = 3
    return cost
all_cost()



