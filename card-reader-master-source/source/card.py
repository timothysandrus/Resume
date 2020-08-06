import mysql.connector
from time import time,ctime
'''Made by Timothy Andrus
   this code interacts with the database directly using mysql connector and mysql code
   in every query(mysql code) you will see that at the end there is a starting value of dbn that is the database name.
   if you have any questions you can contact me at timothy.s.andrus@gmail.com 
   Please make the subject (card database).
'''
mydb = mysql.connector.connect(      # this gives you the host name your user name the password and what database
        host = "localhost",
        user="admin",
        passwd="12345",
        database="cards"
)
dbn = 'cards'
t = time()

def taSigninlog(num): # this will create a log of when TAs sign in only appending to the txt
    mycursor = mydb.cursor()
    mycursor.execute("SELECT first_name, last_name "
                     "FROM %s.card_numbers "
                     "WHERE usernumber = %i;" %(dbn,num))
    r = mycursor.fetchall()
    for name in r:
        file = open("cardreaderlogs.txt", "a")
        file.write("card %i "
                   "belonging to %s %s "
                   "sign in at %s\n" % (num,name[0],name[1],ctime(t)))
    file.close()
def taSignoutlog(num): # this will create a log of when TAs sign out only appending to the txt
    mycursor = mydb.cursor()
    mycursor.execute("SELECT first_name, last_name "
                     "FROM %s.card_numbers "
                     "WHERE usernumber = %i;" %(dbn,num))
    r = mycursor.fetchall()
    for name in r:
        file = open("cardreaderlogs.txt", "a")
        file.write("card %i "
                   "belonging to %s %s "
                   "sign out at %s\n" % (num,name[0],name[1],ctime(t)))
    file.close()
def studentSignInLog(num,cclass): #this will log when a student signs in with all the info gathered
    file = open("cardreaderlogs.txt", "a")
    file.write("card %i signed in "
                "for the class %s  "
                "and signed in at %s\n" % (num,cclass, ctime(t)))
    file.close()
def studentSignOutLog(num,tanum,experience): #this will log when a student signs in with all the info gathered
    mycursor = mydb.cursor()
    mycursor.execute("SELECT first_name, last_name "
                     "FROM %s.card_numbers "
                     "WHERE usernumber = %i;" %(dbn,tanum))# this will get the TA's name
    r = mycursor.fetchall()
    for name in r:
        file = open("cardreaderlogs.txt", "a")
        file.write(
            "card %i signed out after "
            "getting help from %s,%s "
            "which was a %s experiance and signed out at "
            "%s\n"% (num, name[0], name[1], experience, ctime(t)))
    file.close()
def addTA(num,firnam,lasnam):# adds a TA to the system
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE %s.`card_numbers` "
                     "SET `first_name` = '%s', `last_name` = '%s', `special` = '2' "
                     "WHERE (`usernumber` = '%i');" % (dbn,firnam,lasnam, num))
    #INSERT INTO `card_login`.`TAs` (`idTAs`) VALUES ('12');
    mycursor.execute("SELECT idTAs "
                     "FROM %s.TAs  "
                     "WHERE TAs.idTAs = '%i';" % (dbn,num))
    r = mycursor.fetchall()
    if r:
        mydb.commit()
    else:
        mycursor.execute("INSERT INTO %s.`TAs` (`idTAs`, `here`) "
                         "VALUES ('%i', '0');" % (dbn,num));
        mydb.commit()
    return 0
def addAdmin(num,firnam,lasnam): #adds an admin to the system
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE %s.`card_numbers` "
                     "SET `first_name` = '%s', `last_name` = '%s', `special` = '4' "
                     "WHERE (`usernumber` = '%i');" % (dbn,firnam, lasnam, num));
    mydb.commit()
    return 0
def createNewUser(num): #creates a new card login
    mycursor = mydb.cursor()
    print("Welcome new User")
    mycursor.execute("INSERT INTO %s.`card_numbers` (`cardnum`) "
                     "VALUES (%i);" % (dbn,num))
    mydb.commit()
    result = getcardnum(num)
    signin(result)
    return 0
def getteachers(): #gets the teachers number and names
    #SELECT * FROM card_login.Teachers; this returns the number,firstname,lastname of all teachers
    mycursor = mydb.cursor()  # SELECT idsigned_in FROM card_login.signed_in;
    mycursor.execute("SELECT * FROM %s.Teachers;" %(dbn))
    r = mycursor.fetchall()
    return r
def getClasses(): #gets the classes numbers and names
    # SELECT * FROM card_login.Classes; gives class number for database, name, and hour
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM %s.Classes;"%(dbn))
    r = mycursor.fetchall()
    return r
def adminLogin():
    t =""
    while t != "Q":
        if t =="Q":
            break
        else:
            t = input("what do you want to do \n 1 addTA \n 2 addadmin \n Q go back to scan\n")
            if t == "1":
                print(1)
                h = input("scan new TA's ID\n")
                d = input("what is there first,last name\n")
                d = d.split(',')
                hd = getcardnum(int(h))
                for gb in hd:
                    addTA(int(gb[0]), str(d[0]), str(d[1]))
            if t == "2":
                print(2)
                h = input("scan new Admin's ID\n")
                d = input("what is there first,last name\n")
                d = d.split(',')
                hd = getcardnum(int(h))
                for gb in hd:
                    addAdmin(int(gb[0]), str(d[0]), str(d[1]))
            else:
                continue
def getsignedin(): # gets every card that is signed in
    mycursor = mydb.cursor()#SELECT idsigned_in FROM card_login.signed_in;
    mycursor.execute("SELECT idsigned_in FROM %s.signed_in;"%(dbn))
    r = mycursor.fetchall()
    return r
def getcardnum(num):        #looks up the card number an returns it
    mycursor = mydb.cursor()
    mycursor.execute("SELECT usernumber "
                     "FROM %s.card_numbers "
                     "WHERE card_numbers.cardnum = '%i';" % (dbn,num))
    r =mycursor.fetchall()
    return r
def signinTA(result):      #sign in a TA by changing here from 0 to 1
    mycursor = mydb.cursor()
    for db in result:
        mycursor.execute("UPDATE %s.`TAs` "
                         "SET `here` = '1' "
                         "WHERE (`idTAs` = '%i');" % (dbn, db))
        mydb.commit()
        taSigninlog(db)
        return 0
def signoutTA(result):      #sign out a TA by changing here from 1 to 0
    mycursor = mydb.cursor()
    for db in result:
        mycursor.execute("UPDATE %s.`TAs` "
                         "SET `here` = '0' "
                         "WHERE (`idTAs` = '%i');" % (dbn,db));
        mydb.commit()
        taSignoutlog(db)
    if (len(getTAs()) == 0):
        r = getsignedin()
        for db in r:
            #print("you are signed out")
            mycursor.execute("DELETE FROM %s.`signed_in` "
                             "WHERE (`idsigned_in` = '%i');" % (dbn,int(db[0])))
            mydb.commit()
    return 0
def checkspecial(num):         #check if they have a variable other than just 1 for student
    mycursor = mydb.cursor()
    mycursor.execute("SELECT special "
                     "FROM %s.card_numbers "
                     "WHERE card_numbers.usernumber = '%i';" % (dbn, num[0]))
    r = mycursor.fetchall()
    for db in r:
        if db[0] == 2:
            return 2
        elif db[0] == 4:
            return 4
        elif db[0] == 1:
            return 1
    return 1
def getTAs():                #get if there is a TA login
    mycursor = mydb.cursor()
    mycursor.execute("SELECT idTAs,first_name,last_name "
                     "FROM %s.TAs, %s.card_numbers "
                     "WHERE TAs.here = 1 and idTAs = usernumber;"
                     ""%(dbn,dbn))
    r = mycursor.fetchall()
    #print(r)
    return r
def signin(result):                # signin a number that is put into it
    print("you are signed in")
    mycursor = mydb.cursor()
    for db in result:
        # print(db)
        mycursor.execute("INSERT INTO %s.`signed_in`(`idsigned_in`) "
                         "VALUES('%i');" % (dbn, int(db[0])))
        mydb.commit()
    # for db in mycursor:
    # print(db)
    return 0
def signout(result):        # signout a number that is put into it
    mycursor = mydb.cursor()
    for db in result:
        print("you are signed out")
        mycursor.execute("DELETE FROM %s.`signed_in` "
                         "WHERE (`idsigned_in` = '%i');" % (dbn, int(db[0])))
        mydb.commit()
    return 0
def scan(num):   #takes in a number and sign in or signs out based on the results
    mycursor = mydb.cursor()
    result = getcardnum(num)
    #print(result)
    if result:
        for db in result:
            mycursor.execute("SELECT idsigned_in "
                             "FROM %s.signed_in "
                             "WHERE signed_in.idsigned_in = '%i';" % (dbn, int(db[0])))
        test = mycursor.fetchall()
        if test:
            for db in result:
                if checkspecial(db) == 2:
                    signoutTA(db)
            signout(result)
            if (checkspecial(db) == 2):

                return "TA Sign Out"        # TA signing out

            else:

                return "Student Sign Out"        # Non-TA signing out

        else:
            for db in result:
                if checkspecial(db) == 2:
                    signinTA(db)
                if checkspecial(db) == 4:
                    adminLogin()
                    return "Admin Sign In"
            #print(len(getTAs()))
            if(len(getTAs()) == 0):
                print("Please have a TA sign in first")
                return "Get TA"                 # Need TA to sign in
            else:
                signin(result)
                if (checkspecial(db) == 2):

                    return "TA Sign In"            # TA signing in
                else:

                    return "Student Sign In"            # Non-TA signing in
    else:
        if (len(getTAs()) == 0):
            print("Please have a TA sign in first")
            return "Get TA"            # Need TA to sign in
        else:
            createNewUser(num)
            return "Student Sign In"
if __name__ == "__main__":
    y = ""
    while(y != "Q"):
        y = input("scan you id or type Q to end\n")
        if(y == "Q"):
            break
        else:
            try:
                #print(getcardnum(1111))
                scan(int(y))

            except ValueError:
                y =input("you entered a wrong value \n")
