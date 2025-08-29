perform = True
while(perform):
    
    print("Which operation would u like to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    option = int(input("Enter your operation: "))
    match option:
        case 1:
            num1 = float(input("Enter your first Number: "))
            num2 = float(input("Enter your second Number: "))
            print("The answer is: ", num1 + num2)
        case 2:
            num1 = float(input("Enter your first Number: "))
            num2 = float(input("Enter your second Number: "))
            print("The answer is: ", num1 - num2)
        case 3:
            num1 = float(input("Enter your first Number: "))
            num2 = float(input("Enter your second Number: "))
            print("The answer is: ", num1 * num2)
        case 4:
            num1 = float(input("Enter your first Number: "))
            num2 = float(input("Enter your second Number: "))
            print("The answer is: ", num1 / num2)
        case _:
            print("Enter a Valid Option")
    print("Would you like to perform another operation(Y/N) : ")
    choice = input()
    if(choice.lower()  == "y"):
        perform = True
    else:
        perform = False
print("Thank you for using Calculator")
#num2 != 0
#what if num1 or num2 is string
#extra operations ^,%,factorial,square root
#use exit instead of asking everytime
#multiple inputs but one operation(optional)
#print output like 5+10 = 15