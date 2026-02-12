n1,n2= map(float, input().split())
choice = input()
if(choice=='+'):
    print(n1+n2)
elif(choice=='-'):
    print(n1-n2)
elif(choice=='*'):
    print(n1*n2)
else:
    print(n1/n2)