
class User:
    def __init__(self,firstname,lastname,email,status="inactive"):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.status=status
    def printuserinfo(self):
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"email: {self.email}")
        print(f"email status: {self.status}")
        print("_"*8)
def userinputs():
            firstname=input("please enter your first name?")
            lastname=input("please enter your last name?")
            email=input("please enter your email?")
            return User(firstname,lastname,email,status="inactive")
users=[]
while True:
    print ("Welcome to user management system\n")
    print("please chose an action\n")
    print("1. add new user")
    print("2. display user info")
    print("3. exit the system\n")
    try:
        choice=int(input("enter your choice ?"))
    except ValueError:
         print("WRONG VALUE!!\nplease enter a whole number(1,2,3)")
    if choice == 1:
        users.append(userinputs())
        print("")
    elif choice==2:
        if not users:
            print("NO USERS FOUND!! PLEASE ENTER USERS FIRST")
        else:
            print("")
            for i, user in enumerate(users,start=1):
               print("")
               print(f"Displaying the user{i} informations...\n")
               user.printuserinfo()
            print("")
    if choice==3:
         print("Exiting the system...")
