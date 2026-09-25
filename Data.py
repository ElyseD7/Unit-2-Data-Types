# x=3 
# y=float(3)
# print(x,y)

# values = [1,2,3,4,.25,30,51]
# print(values)

# for i in values:
#     print(i)

# print(values[-1])
# print(values[1])

# x= "This is a good string"
# y= x.split()
# z= y[0]
# print(y)
# print(x)

# sentence = input("Ask me a question")

# y  = sentence.split()
# print(len(y))

# day_of_the_week = input("What day is it today")
# if day_of_the_week == "Thursday":
#     print("That's true")
# else:
#     print("Wrong")

# x = "test"
# print (f"hello {x}")

# temp = 75
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')

# number = int(input("Give me number"))
# if number % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

# print("Welcome to the tip calculator ")
# bill = int(input("How much did your bill cost? "))
# service = input("How was you service : bad, okay, good, great ")
# if service == "bad":
#     print(f"your total bill is {bill} ")
# if service == "okay":
#     bill = 1.15 * bill
#     print(f"your total bill is {bill} ")
# if service == "good":
#     bill = 1.20 * bill
#     print(f"your total bill is {bill} ")
# if service == "great":
#     bill = 1.25 * bill
#     print(f"your total bill is {bill} ")

# num = int(input("tell me a positive integer"))

factor(19)
def factor(num):
    factor = []
    for i in range(2, num + 1):
        if num % i == 0:
            factor.append(i)
        print(factor)

