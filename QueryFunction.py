import datetime
import mysql.connector

# This file contains the select statements to view the information and the stored procedures
# to insert, delete and update the information in our database.
config = {
        "user": 'JCSP18LA2235',
        "password": '23442235',
        "host": '127.0.0.1',
        "port": '9999',
        "database": 'JCS18336HandL'
    }

# ssh -L 9999:localhost:9999 huan7224@134.74.126.104
# ssh -L 9999:localhost:3306 huan7224@134.74.146.21

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
#---------------------------------------------------------------begin show functions
# We did not write stored procedures for the these simple select statements because what are they now are clean enough
def showTransaction(cursor):
    query = ("SELECT * FROM Transactions2;")
    cursor.execute(query)
    return cursor

def showEmployee(cursor):
    query = ("SELECT * FROM Employees2;")
    cursor.execute(query)
    return cursor

def showEmployee3E(cursor):
    query = ("SELECT * FROM Employees2 WHERE Warning > 2;")
    cursor.execute(query)
    return cursor

def showExpense(cursor):
    query = ("SELECT * FROM Expenses2;")
    cursor.execute(query)
    return cursor

def showBeverage(cursor):
    query = ("SELECT * FROM Beverages2;")
    cursor.execute(query)
    return cursor

def showFood(cursor):
    query = ("SELECT * FROM Foods2;")
    cursor.execute(query)
    return cursor

def showExtremeFood(cursor):
    query = ("SELECT * FROM Foods2 WHERE Popularity > 3")
    cursor.execute(query)
    return cursor

def showGood(cursor):
    query = ("SELECT * FROM Goods2;")
    cursor.execute(query)
    return cursor

def showGoodRestock(cursor):
    query = ("SELECT * FROM Goods2 WHERE Quantity < 10;")
    cursor.execute(query)
    return cursor

def showLunchSpecial(cursor):
    query = ("SELECT * FROM LunchSpecials2;")
    cursor.execute(query)
    return cursor

def showPastTransaction(cursor, begin, now = datetime.date.today()):
    query = "SELECT * FROM Transactions2 WHERE Date BETWEEN %s AND %s;"
    cursor.execute(query, (begin, now))
    return cursor

#------------------------------------------------------------------finish show functions
#------------------------------------------------------------------begin modify functions
# Start to create the stored procedures that we will use.
def addWorker_procedure():

    query=('''CREATE PROCEDURE add_worker(IN new_name VARCHAR(255),IN new_dob DATE, new_salary INT, new_position VARCHAR(255))
            BEGIN
                INSERT INTO Employees2(Name, DOB, BaseSalary, Position) 
                VALUES (new_name,new_dob,new_salary,new_position);
            END               
               ''')
    cursor.execute(query)
    cnx.commit()

def updateWorker_procedures():

    query=('''CREATE PROCEDURE update_worker(IN new_wage INT(11),IN new_position CHAR(30),IN worker_id INT(11))
            BEGIN
                UPDATE Employees2 
                SET BaseSalary = new_wage, Position = new_position
                WHERE ID = worker_id;
            END ''')
    cursor.execute(query)
    cnx.commit()

def giveWarning_procedure():

    query='''CREATE PROCEDURE give_warning(IN worker_id INT(11),IN new_warning INT(11))
            BEGIN
                UPDATE Employees2
                SET Warning=new_warning WHERE ID=worker_id;
            END'''
    cursor.execute(query)
    cnx.commit()


def removeWorker_procedure():

    query = ('''CREATE PROCEDURE remove_worker (IN worker_id INT(11))
            BEGIN
                DELETE FROM Employees2 WHERE ID = worker_id;
            END''')
    cursor.execute(query)
    cnx.commit()

#------------------------------------------
def addDrink_procedure():

    query = ('''CREATE PROCEDURE add_drink (IN new_drink char(30),IN new_price DOUBLE)
            BEGIN
                INSERT INTO Beverages2(Drink, Price)
                VALUES(new_drink, new_price);
            END''')
    cursor.execute(query)
    cnx.commit()


def removeDrink_procedure():

    query = ('''CREATE PROCEDURE remove_drink (IN drink_id INT(11))
            BEGIN
                DELETE FROM Beverages2 WHERE NO = drink_id;
            END''')
    cursor.execute(query)
    cnx.commit()

def addLunch_procedure():

    query=('''CREATE PROCEDURE add_lunch(IN new_name CHAR(30),IN new_price DOUBLE)
            BEGIN
                INSERT INTO LunchSpecials2(Name, Price) 
                VALUES (new_name, new_price);
            END               
               ''')
    cursor.execute(query)
    cnx.commit()

def removeLunch_procedure():

    query = ('''CREATE PROCEDURE remove_lunch (IN lunch_id INT(11))
               BEGIN
                   DELETE FROM LunchSpecials2 WHERE NO = lunch_id;
               END''')
    cursor.execute(query)
    cnx.commit()

def addFood_procedure():

    query = ('''CREATE PROCEDURE add_food(IN new_name CHAR(30),IN new_ingre VARCHAR(255), IN new_price DOUBLE, IN new_popularity INT)
             BEGIN
                 INSERT INTO Foods2(FoodName, Ingredients, Price, Popularity) 
                 VALUES (new_name, new_ingre, new_price, new_popularity);
             END               
                ''')
    cursor.execute(query)
    cnx.commit()

def removeFood_procedure():
    query = ('''CREATE PROCEDURE remove_food (IN food_id INT(11))
               BEGIN
                   DELETE FROM Foods2 WHERE No = food_id;
               END''')
    cursor.execute(query)
    cnx.commit()

#------------------------------------------
def modifyGood_procedure():

    query = ('''CREATE PROCEDURE modify_good (IN new_price DOUBLE, IN new_quantity INT(11),IN food CHAR(30))
              BEGIN
                UPDATE Goods2
                SET Price = new_price, Quantity = new_quantity
                WHERE Type = food;
              END''')
    cursor.execute(query)
    cnx.commit()


def removeGood_procedure():

    query = ('''CREATE PROCEDURE remove_good (IN good_type CHAR(30))
               BEGIN
                   DELETE FROM Goods2 WHERE Type = good_type;
               END''')
    cursor.execute(query)
    cnx.commit()


def insertGood_procedure():

    query = ('''CREATE PROCEDURE insert_good (IN new_good CHAR(30),IN new_price DOUBLE, IN new_quantity INT(11))
             BEGIN
                 INSERT INTO Goods2(Type,Price,Quantity) 
                 VALUES (new_good, new_price,new_quantity);
             END               
                ''')
    cursor.execute(query)
    cnx.commit()

def addTransaction():
    #date will be the current datetime
    #transaction will be a tuple contain the current date

    query = ('''CREATE PROCEDURE add_transaction (IN tran_date DATETIME,IN cashier_id INT(11),IN new_foodorder TEXT, IN new_earning DOUBLE)
               BEGIN
                   SET tran_date = CURRENT_TIMESTAMP;
                   INSERT INTO Transactions2(Date, Cashier, FoodOrdered, Earning) 
                   VALUES (tran_date, cashier_id, new_foodorder, new_earning);
               END               
                  ''')
    cursor.execute(query)
    cnx.commit()

def addExpense():

    query = ('''CREATE PROCEDURE add_expenses (IN ex_date DATE,IN new_electricity DOUBLE,IN new_gas DOUBLE, 
    IN new_water DOUBLE,IN new_salary DOUBLE, IN new_rent DOUBLE, IN new_cost_goods DOUBLE)
                 BEGIN
                     INSERT INTO Expenses2(Date, Electricity, Gas, Water, Salaries, Rent, CostofGood) 
                     VALUES (ex_date, new_electricity, new_gas, new_water,new_salary,new_rent,new_cost_goods);
                 END               
                    ''')
    cursor.execute(query)
    cnx.commit()

#--------------------------------------------------------------------------------------------end
#--------------------------------------------------------------------------------------------end
#--------------------------------------------------------------------------------------------end