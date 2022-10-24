
import random

 # between 0 and 1

for i in range (10):
    ball = random.random()
    print(ball)
    if ball <= 0.5 and ball >= 0:
        print("Bucket 1")

    elif ball > 0.5 and ball <=1:
        print("Bucket 2")

    else :
        print("Out of Range")

