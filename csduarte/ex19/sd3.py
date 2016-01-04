def squared(input):
    result = input ** 2
    print result
    return result
# 1
squared(1)

# 2
squared(1+1)

# 3
value = 1 + 1 + 1
squared(value)

# 4
updated = value + 1
squared(updated)

# 5, 6, 7, 8
for i in range(1, 5):
    squared(updated + i)

# 9 & 10
squared(squared(9))
