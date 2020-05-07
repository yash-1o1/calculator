operation = input("Choose an operation to input (You can choose 'add', 'sub', 'multi' , 'div'): ")
if operation == "add":
    first = input('Choose the first number to be added number: ')
    second = input('Choose the second number: ')
    output  = int(first) + int(second)
    print ('The result of addition was %s \n' % (output))
elif operation == "sub": 
    first = input('Choose first number to be subtracted from: ')
    second = input('Choose the second number to be subtracted: ')
    output  = int(first) - int(second)
    print ('The result of subtraction was %s \n' % (output))
elif operation == "multi":
    first = input('Choose the first number you want to multiply: ')
    second = input('Choose the second number: ')
    output  = int(first) * int(second)
    print ('The result of multiplication was %s \n' % (output))
elif operation == "div":
    first = input('Choose the divident: ')
    second = input('Choose the divisor: ')
    if int(second) == 0:
        output("Error: Can't divide by 0 \n")
    else:
        output = int (first) / int(second)
        print ('The result of division was %s \n' % (output))
else:
    print ('Invalid command entered')

contnue = input("Choose an operation to input (You can choose 'yes' or 'no'): ")

while contnue == "yes":
    operation = input("Choose an operation to input (You can choose 'add', 'sub', 'multi' ,'div'): ")
    if operation == "add":
        first = input('Choose the first number to be added number: ')
        second = input('Choose the second number: ')
        output  = int(first) + int(second)
        print ('The result of addition was %s \n' % (output))
    elif operation == "sub": 
        first = input('Choose first number to be subtracted from: ')
        second = input('Choose the second number to be subtracted: ')
        output  = int(first) - int(second)
        print ('The result of subtraction was %s \n' % (output))
    elif operation == "multi":
        first = input('Choose the first number you want to multiply: ')
        second = input('Choose the second number: ')
        output  = int(first) * int(second)
        print ('The result of multiplication was %s \n' % (output))
    elif operation == "div":
        first = input('Choose the divident: ')
        second = input('Choose the divisor: ')
        if int(second) == 0:
            print("Error: Can't divide by 0 \n")
        else:
            output = int (first) / int(second)
            print ('The result of division was %s \n' % (output))
    else:
        print ('Invalid command entered')
    contnue = input("Choose an operation to input (You can choose 'yes' or 'no'): ")

if contnue != "yes":
    print ('Thank You Professor! Was an amazing overall semester and even though this the third time \nI have taken  a class from you, I just hope to get an opportunity to be taught by you again. \nHave a nice day!')