def while_loop(n, step):
    numbers = []
    for i in xrange(0, n, step):
        print ("At the top i is %d" % i).center(30, '-')
        numbers.append(i)
        print "Numbers now: ", numbers
        print ("At the bottom i is %d" % i).center(30, '-')

    print "The numbers: "

    for num in numbers:
        print num

while_loop(1, 1)
while_loop(2, 1)
while_loop(3, 1)
while_loop(4, 1)
while_loop(5, 1)
while_loop(6, 1)
while_loop(7, 2)
while_loop(7, 4)



