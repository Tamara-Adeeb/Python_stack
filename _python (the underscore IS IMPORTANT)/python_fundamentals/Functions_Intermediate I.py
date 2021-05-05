import random
def randInt(min=0   , max=100  ):
    if(min!=0):
        max-=min
    num = random.random()* max + min
    return int(num)
print(randInt(max=25,min=10))
