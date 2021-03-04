import mariadb
import connection

conn = connection.db_connection()

cursor = conn.cursor()

sql_query = """ CREATE table `beer` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    percentageAlcohol VARCHAR(5) NOT NULL,
    category VARCHAR(100) NOT NULL,
    stock INT NOT NULL)"""

sql_querybis = """ CREATE table `user` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pseudo VARCHAR(100) NOT NULL,
    mail VARCHAR(300) NOT NULL,
    password VARCHAR(100) NOT NULL)"""

sql_beer = """ INSERT INTO beer (name,percentageAlcohol,category) VALUES 
(Heineken,3.2,Blonde), 
(1661,5.5,Blonde),
(Leffe Ruby,4.1,Fruit),
(Chouffe,9.2,Blonde);"""

sql_user = """ INSERT INTO user (pseudo,mail,password) VALUES (test,test@test.com,test) """

cursor.execute(sql_query)
cursor.execute(sql_querybis)