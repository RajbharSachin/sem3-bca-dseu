import mysql.connector
prwd = input("Enter the password Please :") 
if prwd == "123":
    db = input("Enter the name of the database :")

    mydb = mysql.connector.connect(host='localhost',user='root',passwd='Sachin@1138..')
    mycursor = mydb.cursor()

    sql = "CREATE DATABASE if not exists %s" % (db,) 
    mycursor.execute(sql)
    print("Database created/opened Successfully...")

    mycursor = mydb.cursor() 
    mycursor.execute("Use "+ db)
    TableName=input("Name of Table to be created/opened:") 
    query="Create table if not exists "+TableName+" (Sno int primary key, firstname varchar(20) not null, lastname varchar(20) not null, Gender char(1) not null, Address varchar(100) not null, contactno varchar(10) not null, relation varchar(15))"
    print("Table "+TableName+" created/opened successfully...") 
    mycursor.execute(query)
 
    while True:
        print('\n\n\n') 
        print("*"*95)
        print('MAIN MENU'.center(95)) 
        print("*"*95)
        print('\t1. Adding a new Contact') 
        print('\t2. For Displaying the Contact List')
        print('\t3. For Displaying the relation wise Contacts') 
        print('\t4. For Displaying Record of Any Particular Contact')
        print('\t5. To Modify the Data of Any Contact')
        print('\t6. For Deleting Any Contact') 
        print('\t7. For Deleting All Contacts') 
        print('\t8. Exit')
        print("*"*95)
        print('THANK YOU'.center(95)) 
        print("*"*95)
        print('Enter Choise...',end='') 

        choise = int(input())

        if choise == 1: 
            try:
                print('Enter Contact information..- ')
                S_no = int(input('Enter Sno.:')) 
                F_name = input('Enter First name:') 
                L_name = input('Enter Last name:') 
                Gen_der = input('Enter Gender(M/F):') 
                Address = input('Enter Address:')
                Contact_no = int(input('Enter Contact no.:')) 
                Relation = input('Enter Relation:')
 
                rec=(S_no,F_name,L_name,Gen_der,Address,Contact_no,Relation)
                query="insert into "+TableName+" values (%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(query,rec)

                mydb.commit()
                print('Record added successfully...!')
                
            except:
                print("Something Went Wrong")
                    
        
        elif choise == 2:
            try:
                query = 'select * from '+TableName 
                mycursor.execute(query)
                data = mycursor.fetchall() 
                print('-'*95)
                print('Sno,First Name, Last Name, Gender, Address, Contact No, Relation')
                print('-'*95)
                print('-'*95) 
                for i in data: 
                    print(i)
                print('-'*95)
 
            except:
                print("Something Went Wrong")
                
        
        elif choise == 3:
            try:
                print('1: Friend') 
                print('2: Cousin') 
                print('3: Teacher') 
                print('4: Uncle')
                print('5: Aunt') 
                print('6: Sister') 
                print('7: Brother') 
                print('8: Mother') 
                print('9: Father') 
                print('10: Self/Me')
                cat = int(input("Select the Category (1 to 10) :")) 
                if cat == 1:
                    query = 'select * from '+TableName+" where relation='Friend'"
                elif cat == 2:
                    query = 'select * from '+TableName+" where relation='Cousin'"
                elif cat == 3:
                    query = 'select * from '+TableName+" where relation='Teacher'"
                elif cat == 4:
                    query = 'select * from '+TableName+" where relation='Uncle'"
                elif cat == 5:
                    query = 'select * from '+TableName+" where relation='Aunt'"
                elif cat == 6: 
                    query = 'select * from '+TableName+" where relation='Sister'"
                elif cat == 7:
                    query = 'select * from '+TableName+" where relation='Brother'"
                elif cat == 8:
                    query = 'select * from '+TableName+" where relation='Mother'"
                elif cat == 9:
                    query = 'select * from '+TableName+" where relation='Father'"
                elif cat == 10:
                    query = 'select * from '+TableName+" where relation='Self'"
                else:
                    print('Something went wrong')
                mycursor.execute(query) 
                data = mycursor.fetchall() 
                print('-'*95)
                print('Sno,First Name, Last Name, Gender, Address, Contact No, Relation')
                print('-'*95)
                print('-'*95) 
                for i in data: 
                    print(i)
                print('-'*95)
            except:
                print('Something went wrong')
                

        elif choise == 4:
            try:
                Num = input('Enter Sno. of the record to be displayed...') 
                query = 'select * from '+TableName+" where Sno="+Num
                mycursor.execute(query) 
                myrecord=mycursor.fetchone() 
                print('\n\nRecord of Sno:- '+Num)  
                print(myrecord)
            except:
                print('Nothing to display')
                
                
        elif choise == 5:
            try:
                Num = input("Enter Sno of the record to be modified...") 
                query = 'select * from '+TableName+" where Sno="+Num 
                mycursor.execute(query)
                myrecord=mycursor.fetchone() 
                c = mycursor.rowcount

                if c>0:
                    ino=myrecord[0] 
                    ifname=myrecord[1] 
                    ilname=myrecord[2] 
                    igen=myrecord[3] 
                    iadd=myrecord[4] 
                    icon=myrecord[5] 
                    irel=myrecord[6]
                    print('Sno. :',myrecord[0])
                    print('First Name :',myrecord[1])
                    print('Last Name :',myrecord[2]) 
                    print('Gender :',myrecord[3]) 
                    print('Address :',myrecord[4]) 
                    print('Contact No. :',myrecord[5]) 
                    print('Relation :',myrecord[6]) 
                    print('	')
                    print('Type Value to modify below or just press Enter for no change')
                    x = input('Enter Sno. :') 
                    if len(x)>0:
                        ino = x
                    x = input('Enter First Name :') 
                    if len(x)>0:
                        ifname = x
                    x = input('Enter Last name :') 
                    if len(x)>0:
                        ilname = x
                    x = input('Enter Gender :') 
                    if len(x)>0:
                        igen = x
                    x = input('Enter Address :') 
                    if len(x)>0:
                        iadd = x
                    x = input('Enter Contact No. :') 
                    if len(x)>0:
                        icon = x
                    x = input('Enter Relation :') 
                    if len(x)>0:
                        irel = x
                query = "Update "+TableName+" set Sno="+str(ino)+','+"firstname="+"'"+ifname+"'"+','+"lastname="+"'"+ilname+"'"+','+"Gender="+"'"+igen+"'"+','+"Address="+"'"+iadd+"'"+','+ "contactno="+str(icon).strip('Decimal')+','+"relation="+"'"+irel+"'"+"where Sno="+Num 
                mycursor.execute(query)
                mydb.commit()
                print("Record modified...")
            except:
                print('Sno. '+Num+' does not exists')
                
                
        elif choise == 6:
            try:
                Num = input("Enter Sno. of the record to be deleted...") 
                query='delete from '+TableName+' where Sno='+Num 
                mycursor.execute(query)
                mydb.commit()
                c = mycursor.rowcount 
                if c > 0:
                    print('Deletion done') 
                else:
                    print('Sno. ',Num,' not found')
            except:
                print('Something went wrong')
                
            
        elif choise == 7:
            try:
                ch = input("Do you want to delete all the contacts(y/n) :") 
                if ch.upper()== 'Y':
                    query = 'delete from '+TableName 
                    mycursor.execute(query) 
                    mydb.commit()
                    print('All the records are deleted...')
            except:
                print('Something went wrong')
                

        elif choise == 8:
            print('Press 0 to Exit')
            print('Press any key to Enter in Main Menu') 
            ch = input('Enter your Choise:')
            if ch == '0':
                print('You have Successfully exited...\nHave A Nice Day') 
                break
            else:
                continue
        else:
            print("Wrong Choise\nPlease Try Again")

    print('-'*95) 
    
else:
    print("Wrong Password!!! \nPlease Try Again")