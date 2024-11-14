
import mysql.connector
from datetime import datetime

# start a database 
db = mysql.connector.connect(
    host = "localhost",
    user="rkostova",
    passwd = "ra77fg28",
    auth_plugin='mysql_native_password',
    database = "testdatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdatabase")
# mycursor.execute("CREATE TABLE Customer (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("DESCRIBE Customer")
# for x in mycursor:
#     print(x)

# Add elements to table and retrieve
#mycursor.execute("INSERT INTO Customer (name, age) VALUES (%s, %s)", ("tim", 19))
#db.commit()

# mycursor.execute("SELECT * FROM Customer")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE test2 (name varchar(5), created datetime, gender ENUM('M', 'F', 'O'), id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO test2 (name, created, gender) VALUES (%s,%s,%s)", ("Ralie", datetime.now(), "F"))
# db.commit()

# mycursor.execute("ALTER TABLE test2 ADD COLUMN food VARCHAR(50)")


# remove column
#mycursor.execute("ALTER TABLE test2 DROP food ")

# rename = CHANGE col_1 col_2
#mycursor.execute("ALTER TABLE test2 CHANGE name first_name VARCHAR(50)")


