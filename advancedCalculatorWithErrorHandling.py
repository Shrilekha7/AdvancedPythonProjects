#advancedCalculatorWithErrorHandling
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return 'invalid b value'
    else:
        return a/b

def calculator():

    print("i welcome you to perform calculations")
    try:
        a=int(input("enter value for a : "))
        b=int(input("enter value for b : "))
        oper=input("enter operation symbol : ")
        if oper=='+':
            print(add(a,b))
        elif oper=='-':
            print(sub(a,b))
        elif oper=='*':
            print(mul(a,b))
        elif oper=='/':
            print(div(a,b))
        else:
            print("invalid operator entered")
    except Exception as e:
        print(e)
calculator()




    