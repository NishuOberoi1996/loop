# num=int(input("enter the number:-"))
# i=0
# while i<10:
#     i+=1
#     if num%2==0:
#         print(num,"*",i,"=",num*i)
#     elif num%2==1:
#         print("odd")
#         break



# i=0
# sum=0
# while i<=42:
#     sum+=1
#     i+=1
#     if sum%2==0:
#         print(sum,"even")
#     elif sum%2==1:
#         print(sum,"odd")

num=int(input("enter the number:-"))
sum1=0
sum2=0
i=1
while i<=num:
    if i%2==0:
        print(i,"even number")
        sum1+=i
        print(sum1)
    elif i%2==1:
        print(i,"odd")
        sum2+=i
    i+=1
print(sum2)
