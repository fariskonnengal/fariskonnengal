choice=input("enter the choice")
addressbook=[]
def add_contact():

    name=input("enter name")
    print(name)
    ph=input("enter phone number")
    print(ph)
    f=open("contacts.txt","w")
    f.write((name))
    f.write(f"{ph}")
    f.close()
    print("contact saved")
    addressbook.append([name,ph])

add_contact()


def view_list():
    print(addressbook)
view_list()

def viewcontact():
    f=open("contacts.txt","r")
viewcontact()





