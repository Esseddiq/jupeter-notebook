import os 
import time
members=[]
class Member:
    def __init__(self,firstname,lastname,age,ID,status="inactive"):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.ID=ID
        self.status=status
    def printmembersinfo(self):
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"Member Age: {self.age}")
        print(f"Member ID: {self.ID}")
        print(f"Member Status: {self.status}")
def memberinputs():
    firstname=input("enter the member first name?")
    lastname=input("enter the member last name?")
    while True:
        try:
           age=int(input("enter the member age?"))
           break
        except ValueError:
           print("invalid input age must be a whole number\n")
    ID=input("enter the member ID?")
    status=input("enter the member status or press enter for default?")
    if status.strip()=="":
         status="inactive"
    print("Member added succssfuly!\n")
    return Member(firstname,lastname,age,ID,status)
def clear_screen():
      # Windows uses 'cls', Linux/Mac uses 'clear'
       os.system("cls")
def membersearch():
            print("Search by:\n")
            print("1. Member ID")
            print("2. First name")
            print("3. Age")
            print("4. Status\n")
            try:
                 search_choice=int(input("enter your search choice?"))
            except ValueError:
                 print("Invalid input!! please enter a whole number(1,2 or 3)\n")
                 return
            if search_choice==1:
                 search_ID=input("enter the member ID?")
                 found=False
                 for mbr in members:
                      if mbr.ID.lower()==search_ID.lower():
                           print("Member found:\n")
                           mbr.printmembersinfo()
                           found=True
                 if not found:
                      print("no member yet with such ID\n")
            elif search_choice==2:
                 search_firstname=input("enter the member first name?")
                 found=False
                 for mbr in members:
                      if mbr.firstname.lower()==search_firstname.lower():
                           print("Member found:\n")
                           mbr.printmembersinfo()
                           found=True
                 if not found:
                      print("no member yet with such First name\n")
            elif search_choice==3:
                 try:
                     search_age=int(input("enter the member age"))
                 except ValueError:
                      print("Invalid input!! age must be a whole number\n")
                      return
                 found=False
                 for mbr in members:
                      if mbr.age==search_age:
                           print("Member found:\n")
                           mbr.printmembersinfo()
                           found=True
                 if not found:
                      print("no member yet with such Age\n")
            elif search_choice==4:
                 search_status=input("enter the member status?")
                 found=False
                 for mbr in members:
                      if mbr.status.lower()==search_status.lower():
                           print("")
                           print("Member found\n")
                           mbr.printmembersinfo()
                           found=True
                      continue
                 if not found:
                      print("no members yet with such status\n")
            else:
                 print("OUT OF RANGE!! please chose(1,2 or 3)\n")
            time.sleep(5)
            #clear_screen()
def mainpage():
     while True:  
        print("Welcom to the Gym memberships system\n")
        print("Choose an action\n")
        print("1. Add new member")
        print("2. Display all members")
        print("3. Search for a member")
        print("4. Exit the program\n")
        try:
             choice=int(input("please enter your choice?"))
        except ValueError:
             print("Invalid input!! please chose a whole number(1,2,3 or 4)\n")
             continue
        if choice==1:
             members.append(memberinputs())
             time.sleep(5)
             clear_screen()
        elif choice==2:
            if not members:
                print("NO MEMBERS FOUND!! PLEASE ENTER MEMBERS FIRST\n")
            else:
               for i, member in enumerate(members,start=1):
                   print(F"Dispalying member{i} informations\n")
                   member.printmembersinfo()
                   print("")
            time.sleep(5)
            clear_screen()
        elif choice==3:
             membersearch()
        elif choice==4:
             print("Exiting the system...\n")
             break
        else:
             print("Input out of range(1,2,3,4)!!\n")
mainpage()             