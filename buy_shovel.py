price,coin=tuple(map(int,input().split()))

def main_func(price,coin):
    min_shovel=1
    while True:
        if (min_shovel*price)%10==0 or (min_shovel*price)%10==coin:
            return min_shovel
        min_shovel+=1
print(main_func(price,coin))

    
