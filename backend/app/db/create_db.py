# import mysql.connector
#
#
# conection = mysql.connector.connect(
#     user='root',
#     password='sifra',
#     host='localhost'
#     )
# conection.autocommit = True
# my_cursor = conection.cursor()

#kreiranje baze
#my_cursor.execute("CREATE DATABASE DataBase2")

#Prvo kreiranje klijenta jer je povezan sa creditnom karticom vezom 1...N preko id-a
# my_cursor.execute('INSERT INTO DataBaseDRS.user (user.id,user.name,user.lastname,user.address,user.city,user.country,user.phoneNumber,user.email,user.password) values (1,"Milan","Mastilovic","Sol Dob 45","Gacko","RS",0656662789,"mialn@gmail.com","sifra")')

#Kreiranje kartice pomocu klijentovog id-a
#my_cursor.execute('INSERT INTO DataBaseDRS.credit_card (credit_card.number,credit_card.username,credit_card.expirationDate,credit_card.csc,credit_card.balance,credit_card.user_id) values(12314,"milan",2312,321,10000,1)')




my_cursor.execute("select * from DataBaseDRS.credit_card where user_id=1")
string = my_cursor._fetch_row()

print(string)


conection.close()
