seatno=[]
def booking():
    n= print("Your booking seats are ",end="")
    for i in seatno:
        print(i,end=" ")
    l=len(seatno)
    print("your Price is: ",l*190)

def MarkAntony():
    print("One Ticket of  Movie Cost Rps:190\n\n")
    n=int(input("Enter the number of Seats to Book: "))
    print("""              A1 A2 A3 A4 A5 A6 A7 A8 A9 \n
              B1 B2 B3 B4 B5 B6 B7 B8 B9 \n
              C1 C2 C3 C4 C5 C6 C7 C8 C9 \n
              """)
    for i in range(1,n+1):
        getseat=input(f"Enter the {i}seat number:")
        seatno.append(getseat)
    booking()
    
    
def Demon():
    print("One Ticket of  Movie Cost Rps:190\n\n")

    n=int(input("Enter the number of Seats to Book: "))
    
    print("""              A1 A2 A3 A4 A5 A6 A7 A8 A9 \n
              B1 B2 B3 B4 B5 B6 B7 B8 B9 \n
              C1 C2 C3 C4 C5 C6 C7 C8 C9 \n
              """)
    for i in range(1,n+1):
        getseat=input(f"Enter the {i}seat number:")
        seatno.append(getseat)
    booking()

def Jawan():
    print("One Ticket of  Movie Cost Rps:190\n\n")

    n=int(input("Enter the number of Seats to Book: "))
    
    print("""              A1 A2 A3 A4 A5 A6 A7 A8 A9 \n
              B1 B2 B3 B4 B5 B6 B7 B8 B9 \n
              C1 C2 C3 C4 C5 C6 C7 C8 C9 \n
              """)
    for i in range(1,n+1):
        getseat=input(f"Enter the {i}seat number:")
        seatno.append(getseat)
    booking()

def AreYouOkBaby():
    print("One Ticket of  Movie Cost Rps:190\n\n")

    n=int(input("Enter the number of Seats to Book: "))
    
    print("""              A1 A2 A3 A4 A5 A6 A7 A8 A9 \n
              B1 B2 B3 B4 B5 B6 B7 B8 B9 \n
              C1 C2 C3 C4 C5 C6 C7 C8 C9 \n
              """)
    for i in range(1,n+1):
        getseat=input(f"Enter the {i}seat number:")
        seatno.append(getseat)
    booking()


print("🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇 Welcome to Movie Ticket Booking🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇\n")


name=input("\nEnter Your Full name:")
print(f"\nWelcome {name}!!!\n")

Movie_name=int(input("1-Mark Antony\n2-Jawan\n3-Demon\n4-Are You ok Baby?\n\nEnter the Movie to Book:"))

if Movie_name==1:
    MarkAntony()
elif Movie_name == 2:
    Jawan()
elif Movie_name == 2:
    Demon()
elif Movie_name == 2:
    AreYouOkBaby()
else:
    print("Enter Valid number")