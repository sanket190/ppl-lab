
while True:

    print("1.value error exception ")
    print("2.invalid lateral exception")
    print("3.zero division exception")
    print("4.file not open exception")
    print("enter the choice")
    i = int(input())
    if(i == 1):

        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    elif(i==2):

        try:
            print(int('sk'))
        except Exception as err:

            print("Error {}".format(err))
    elif(i==3):
        try:
            a = int(input("Enter a:"))
            b = int(input("Enter b:"))
            c = a / b
            print("a/b = %d" % c)
        # Using Exception with except statement. If we print(Exception) it will return exception class
        except Exception:
            print("can't divide by zero")
            print(Exception)
        else:
            print("Hi I am else block")

    elif(i==4):
        try:
            with open("not_existing_file.txt", 'r') as text:
                pass
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))
    else:
        print('Something went wrong.')
