def search():
    search = int(input("How do u want to search \n 1.Name \n 2.pincode  \n 3.phone number \n 4.category\n"))
# helloiamchangehere right here
    if search == 1:
        sname = input("Enter the name to search:\n")
        MySQLCursor.execute("SELECT * from directory WHERE Name = '%s'" % (sname,))
    elif search == 2:
        pincode = int(input("Enter the pincode to search:\n"))
        MySQLCursor.execute("SELECT * from directory WHERE pincode %LIKE '%s'" % (pincode,))
    elif search == 3:
        phonenumber= input("Enter phone number to search:\n")
        MySQLCursor.execute("SELECT * from directory WHERE Phone_Number = '%s'" % (phonenumber,))
    elif search == 4:
        category = input("Enter the category to search:\n")
        MySQLCursor.execute("SELECT * from directory WHERE category = '%s'" % (category,))
    rows = MySQLCursor.fetchall()
    print(rows)
import mysql.connector
mydb = mysql.connector.connect(host = '127.0.0.1',
                       user = 'root',
                       passwd = 'trifig*#549',
                       database = 'girrafe')
if mydb.is_connected == False:
    print("Unable to connect")
MySQLCursor = mydb.cursor()
print('''                     _              _
                    | |------------| |
                 .-'| |            | |`-.
               .'   | |            | |   `.
            .-'      \ \          / /      `-.
          .'        _.| |--------| |._        `.
         /    -.  .'  | |        | |  `.  .-    \
        /       `(    | |________| |    )'       \
       |          \  .i------------i.  /          |
       |        .-')/                \(`-.        |
       \    _.-'.-'/     ________     \`-.`-._    /
        \.-'_.-'  /   .-' ______ `-.   \  `-._`-./\
         `-'     /  .' .-' _   _`-. `.  \     `-' \\
                | .' .' _ (3) (2) _`. `. |        //
               / /  /  (4)  ___  (1)_\  \ \       \\
               | | |  _   ,'   `.==' `| | |       //
               | | | (5)  | B.T.| (O) | | |      //
               | | |   _  `.___.' _   | | |      \\
               | \  \ (6)  _   _ (9) /  / |      //
               /  `. `.   (7) (8)  .' .'  \      \\
              /     `. `-.______.-' .'     \     //
             /        `-.________.-'        \ __//
            |                                |--'
            |================================|hjw
            "--------------------------------"''')
g = int(input("Enter 1. to add details \n Enter 2.to search any number \n Enter 3.To edit any contact\n"))

if g==1:
    times= int(input("How many contacts you want to add?"))
    for i in range(0,times):
        print("Enter Contact Information")
        name = str(input("Enter Name:\n"))
        ph_number = input("Enter phone number:\n")
        email = input("Enter email id:\n")
        pincode = int(input("Enter the pincode of the locality:\n"))
        category = input("enter the category for the contact (Friends/Family/Work):\n")
        command = "Insert into directory(Name,Phone_Number,email_id,pincode,category) VALUES(%s,%s,%s,%s,%s)"
        VALUES = (name, ph_number, email, pincode, category)
        MySQLCursor.execute(command,VALUES)

        mydb.commit()

elif g==2:
    search()

elif g==3:
    # edit()
    MySQLCursor.execute('SELECT*FROM directory')
    data=MySQLCursor.fetchall()
    for i in data:
        print(i)
    edt=int(input("What do you want to edit? \n1.Name \n2.phone number \n3.pincode \n4.Delete "))
    if edt == 1:
        pno = int(input("Contact Number to be edited\n(copy and paste the phone number from"))
        sdata = input('The edited name:')
        print(sdata)
        MySQLCursor.execute('UPDATE directory SET Name = "%s" WHERE Phone_Number = "%s"' % (sdata, pno,))
        mydb.commit()
        MySQLCursor.execute('SELECT*FROM directory')
        data = MySQLCursor.fetchall()
        for i in data:
            print(i)
    elif edt == 2:
        pno = int(input('Contact Number to be edited\n(copy and paste the phone number from above):\n'))
        eno = int(input("The edited number:\n"))
        MySQLCursor.execute('UPDATE directory SET Phone_Number = "%s" WHERE Phone_Number = "%s"' % (eno, pno,))
        mydb.commit()
        MySQLCursor.execute('SELECT*FROM directory')
        data = MySQLCursor.fetchall()
        for i in data:
            print(i)
    elif edt == 3:
        pno = int(input('Contact Number to be edited\n(copy and paste the phone number from above):\n'))
        pin = int(input("The edited pincode:\n"))
        MySQLCursor.execute("UPDATE directory SET pincode = '%s'WHERE Phone_Number = '%s'" % (pin, pno,))
        mydb.commit()
        MySQLCursor.execute('SELECT*FROM directory')
        data = MySQLCursor.fetchall()
        for i in data:
            print(i)
    elif edt == 4:
        pno = int(input('Contact Number to be deleted\n(copy and paste the phone number from above):\n'))
        MySQLCursor.execute('DELETE FROM directory WHERE Phone_Number = "%s"' % (pno,))
        mydb.commit()
        MySQLCursor.execute('SELECT*FROM directory')
        data = MySQLCursor.fetchall()
        for i in data:
            print(i)
elif g==4:
    print("here")
mydb.close()