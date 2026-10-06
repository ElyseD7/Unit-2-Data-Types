# def virus(P, N, R):
#     x = 1
#     days = 1
#     while x < P:
#         x = x + R^days 
#         days +=1
#         print(days,x)
#     else:
#         print(days)

# virus(750, 1, 5)
# # p is how many cant have disease
# # N is number on day 1
# #R they infect exactly other people but only on the very next day.

def mega(N, months, used):
    total_used = 0
    for i in range(len(used)):
        total_used = total_used + used[i]
    bites = (months +1) * N - total_used
    print(bites)
              
mega(10, 3, [4, 6, 2])