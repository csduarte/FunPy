def while_loop(n, step):
    i = 0
    numbers = []
    while i < n:
        print ("At the top i is %d" % i).center(30, '-')
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print ("At the bottom i is %d" % i).center(30, '-')

    print "The numbers: "

    for num in numbers:
        print num

while_loop(1, 1)
while_loop(2, 2)
while_loop(3, 3)
while_loop(4, 4)
while_loop(5, 5)
while_loop(6, 6)



