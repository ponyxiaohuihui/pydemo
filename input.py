import random
my = 0
try:
    my = input("please input : ")
    my = int(my)
    if 0 < my < 4:
        comp = random.randint(0, 3)
        result = my - comp
        print("computer is " + str(comp) + " ")
        if result == 1 or result == -2:
            print("you win")
        else:
            print("you lose")
    print("wrong input " + str(my) + " you lose")
except ValueError:
    print("wrong input " + str(my) + " you lose")


