# Specify the capacity of two water jugs and the target volume
Jug_5_gallon = 5
Jug_3_gallon = 3
target = 4

# Make a function represetning water pouring process 
def big2small(maxSmall, Water_in_SmallJug,Water_in_BigJug):
    pour = min(maxSmall - Water_in_SmallJug, Water_in_BigJug) 
    Water_in_BigJug -= pour
    Water_in_SmallJug += pour
    return Water_in_BigJug, Water_in_SmallJug
    
# Complete the whole solution to the problem    
def  solution(maxBig, maxSmall, target):
    Water_in_BigJug = 0
    Water_in_SmallJug = 0
    print("%d                       \t%d" % (Water_in_BigJug, Water_in_SmallJug))
    while True:
        if Water_in_BigJug > 0:
            Water_in_SmallJug = 0       # Empty the smaller jug
            print("%d                       \t%d" % (Water_in_BigJug, Water_in_SmallJug))
            Water_in_BigJug, Water_in_SmallJug = big2small(maxSmall, Water_in_SmallJug,Water_in_BigJug)
            print("%d                       \t%d" % (Water_in_BigJug, Water_in_SmallJug))            
        else:
            Water_in_BigJug =  maxBig  # Refill the bigger jug to full
            print("%d                       \t%d" % (Water_in_BigJug, Water_in_SmallJug))
            Water_in_BigJug, Water_in_SmallJug = big2small(maxSmall, Water_in_SmallJug,Water_in_BigJug)
            print("%d                       \t%d" % (Water_in_BigJug, Water_in_SmallJug))        
        if Water_in_BigJug == target:
            break

print("Water in BigJug\tWater in SmallJug")
solution(Jug_5_gallon, Jug_3_gallon, target)
