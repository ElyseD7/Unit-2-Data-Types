
# def mega(N, months, used):
#     total_used = 0
#     for i in range(len(used)):
#         total_used = total_used + used[i]
#     bites = (months +1) * N - total_used
#     print(bites)
              
# mega(10, 3, [4, 6, 2])


# def v(most, number, infect):
#     x = number
#     y = 1
#     while x < most:
#         x = x + infect * y
#         y += 1
#     print(y)

# v(10,2,1) 

char = 0
list = ["Cats","dogs"]
for i in list:
    char += len(i)
print(char)