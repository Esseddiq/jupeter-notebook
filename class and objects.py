# class Profile:
#     def __init__(self,name,email,language):
#         self.name=name
#         self.email=email
#         self.language=language
# first_person=Profile("Esseddiq El harrar","elharraresseddiq@gmail.com","Python")
# second_person=Profile("Ahmed Razi","raziahmed@gmail.com","C++")
# third_person=Profile("Dreams","dreams@gmail.com","unknown")
# print(first_person.name)
# print(second_person.email)
# print(third_person.language)

# class Message:
#     def __init__(self,name_of_sender,name_of_reciever,content,date):
#         self.name_of_sender=name_of_sender
#         self.name_of_reciever=name_of_reciever
#         self.content=content
#         self.date=date
        
# messege1=Message("Esseddiq","Morad","hi Morad how are you doing?","22:04:2025")
# messege2=Message("Esseddiq","his brohter","family is everything","22:04:2025")
# messege3=Message("Esseddiq","a friend","hi I need you","22:04:2025")
# print(messege1.name_of_sender)
# print(messege2.name_of_reciever)
# print(messege3.content)
# print(messege1.date)

# class Product:
#     def __init__(self,name,price,description,rating):
#         self.name=name
#         self.price=price
#         self.description=description
#         self.rating=rating
# product1=Product("Labtop","200$","HP the 8th generation","4/5")
# product2=Product("bag","10$","a lether bag for ladies","5/5")
# product3=Product("book","8$","best for those whom serching for propuse","4/5")
# print(product1.name)
# print(product2.price)
# print(product3.description)
# print(product1.rating)

# class Film:
#     def __init__(self,title,director,release,genre):
#         self.title=title
#         self.director=director
#         self.release=release
#         self.genre=genre
#     def print_elements(self):
#         print(f"Title:{self.title}")
#         print(f"Director:{self.director}")
#         print(f"Release:{self.release}")
#         print(f"Genre:{self.genre}")
#     def change_director(self,newdr):
#         self.director=newdr
# film1=Film("Dirilis Artugul","Mohamed Bozedagh",2014,"Adventure")
# film2=Film("Class 8","Omar Esari",2010,"Drama")
# film3=Film("Peaky Blinders","Unknown",2012,"Action")
# print("")
# film1.print_elements()
# print("")
# film2.print_elements()
# print("")
# film3.print_elements()
# print("")
# print("changing movies derectors...")
# print("")
# film1.change_director("Tom Cros")
# film1.print_elements()
# print("")
# film2.change_director("Jacki Chan")
# film2.print_elements()
# print("")
# film3.change_director("Nolan")
# film3.print_elements()
# print("")
# class user:
#     def __init__(self,firstname,lastname,email,password,status="inactive"):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.email=email
#         self.password=password
#         self.status=status
#     def printuserinfo(self):
#         print(f"First name is {self.firstname}")
#         print(f"Last name is {self.lastname}")
#         print(f"Email is {self.email}")
#         print(f"Password is {'*' * len(self.password)}")
#         print(f"Email satatus is { self.status}")
#     def status_update(self):
#         self.status="active"
# def userinputs():
#     firstname=input("please enter your first name? ")
#     lastname=input("please enter your last name? ")
#     email=input("please enter your email? ")
#     password=input("please enter your password? ")

#     return user(firstname,lastname,email,password)
# user1=userinputs()
# print("\nThese are user1 informations:")
# user1.printuserinfo()
# print("")
# print("\nThese are user1 informations with email status update:")
# user1.status_update()
# user1.printuserinfo()
class Recipie:
    def __init__(self,name,ingrediants,time,instructions):
        self.name=name
        self.ingrediants=ingrediants
        self.time=time
        self.instructions=instructions
    def printrecepie(self):
        print("Displaying recepie...")
        print(f"The recepie name is: {self.name}")
        print(f"The recepie ingrediants are: {self.ingrediants}")
        print(f"The recepie cooking time is: {self.time}")
        print(f"The recepie instructions are: {self.instructions}")
def recepieinputs():
    name=input("please enter the recepie name?")
    ingrediants=input("please enter the recepie ingrediants?")
    time=input("please enter how much time it could take?")
    instructions=input("please enter the instructions to follow?")
    print ("recepie added succssfuly")
    return Recipie(name,ingrediants,time,instructions)
recepie1=recepieinputs()
print("")
recepie1.printrecepie()


        




