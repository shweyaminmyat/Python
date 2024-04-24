Application = input("""Login, Username, Password""")
if  Application == "Login":
    print("Next")
    Next = input("Username")
    Username = input("Next1")
    Next1= input("Password")
if  Application == "Password":
    print('Enter correct username and password combo to continue')
    username = input('Enter username')
    password = input("Enter your password")
if password=='1234' and username=='Sherry':
        print('Access granted')
else:
        print('Access denied. Try again.')
        
