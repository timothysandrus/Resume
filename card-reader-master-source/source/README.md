CardReader.py contains the GUI, and uses functions from card.py to communicate with the database. This program is the one you run to start the software. <br>
card.py contains functions that allow for the communcation between the GUI and the database. <br>
Database2.sql is the database that the other programs depend on and manipulate. <br>

The first step to start the program working is to download mysql server
and an optional but highly recommended second step is to download mysql workbench to double check on the database

Next after downloading the files you need to download the libraries that they use.
which will include: 
    mysql-connector (or mysql-connector-python depending how you are downloading it) for the connection to the database
    tkinter for the gui 

Next make sure that the mysql server is runing 

after that you should import the database into mysql workbench if you downloaded it<br>
    https://www.linode.com/docs/databases/mysql/deploy-mysql-workbench-for-database-administration/<br>
    ^^^^^^^^THIS IS A GOOD RESOURCE^^^^^^^^
    
after all of that the code should connect to the database given if it doesn't and you imported it through mysql workbench
    find this part in card.py
    
    mydb = mysql.connector.connect(      # this gives you the host name your user name the password and what database
        host = "localhost",  <- this is the host which should just be localhost because it should be running off your computer
        user="admin", <- this is a user that you have to create the default is "root"
        passwd="12345", <- this is the user's password the default is the password to get into the server 
        database="cards" <- name of the database schema
    )
    dbn = 'cards' <- name of the database schema (should be the same as the one above)
Having problems with this step these are good sources:<br>
https://www.datacamp.com/community/tutorials/mysql-python<br>
https://www.youtube.com/watch?v=x7SwgcpACng
    