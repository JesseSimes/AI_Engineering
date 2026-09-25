# num = int(input("Enter a number: "))

# if (num%2 == 0):
#     print(f"{num} is even")

# else:
#     print(f"{num} is not even")

# n = int(input())

# for i in range (1, 11, 1):
#     print(f"{i} * {n} = {i * n}")

# n = int(input())
# sum = 0

# # for i in range (1, n+1, 1):
# #     print("Hello World")

# # for i in range (1, n+1, 1):
# #     sum += i

# # print(sum)

# sumOdd = 0
# sumEven = 0

# for i in range (1, n+1, 1):
#     if(i%2==0):
#         sumEven += i
#     else:
#         sumOdd += i

# print(f"Sum of even numbers is {sumEven}")
# print(f"Sum of Odd numbers is {sumOdd}")



# n = int(input())
# rev = 0

# while (n > 0):
#     rev = rev * 10 + n % 10

#     n //= 10

# print(rev)


# l=[1,2,3,-4,-5,-6,9,10]

# for i in range(len(l)):
#     if(l[i] < 0):
#         print(f"{l[i]} is negative")
#     else:
#         print(f"{l[i]} is positive")


# l=[52,79,60,34,22,13,65]

# a=0

# for i in range(len(l)):
#     a += l[i]

# print(f"Average: {a / len(l)}")


# l=[52,79,60,34,22,13,65]
# g =0 

# for i in range(len(l)):
#     if (l[i] > g):
#         g = l[i]

# print(g)

# l=[52,79,60,34,22,13,65]

# largest=0
# second=0
# index=0

# for i in range(len(l)):
#     if(l[i]>largest):
#         largest=l[i]
#     elif(l[i]>second and l[i]<largest):
#         second=l[i]
#         index = i

# print(second)
# print(index)



# l=[1,2,3,4,5]

# for i in range(len(l)-1):
#     if(l[i]<l[i+1]):
#         continue
#     else:
#         print("Not sorted")
#         break
# else:
#     print("Sorted")


# d1={10:100,20:200,30:300}
# d2={40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]


def add (*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3,4,5,6,7,8,9,10)

# d1={10:100,20:200,30:300}
# d2={40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]