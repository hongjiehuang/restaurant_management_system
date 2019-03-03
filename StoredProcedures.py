import datetime
import mysql.connector

# This is one of the two main parts of the second project where we put all the functions that
# we need to create tables in 3NF forms, triggers, and all the other store procedures are
# in the QueryFunction file
config = {
        "user": 'JCSP18HU7224',
        "password": '23427224',
        "host": '127.0.0.1',
        "port": '9999',
        "database": 'JCS18336HandL'
    }

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
####################################################################################################
# Beverage table and its triggers
def create_beverages():
    query=('''CREATE TABLE Beverages2(
            Drink VARCHAR(255) UNIQUE,
            Price DOUBLE,
             FOREIGN KEY (Drink)
                REFERENCES Goods2(Type)
                ON DELETE SET NULL
                ON UPDATE CASCADE);''')
    cursor.execute(query)
    cnx.commit()

def beverages_price_trigger1():
    query=('''CREATE TRIGGER beverages_trigger1 BEFORE UPDATE ON Beverages2         
            FOR EACH ROW
            BEGIN
                DECLARE OLDPRICE DOUBLE;    
                SELECT Price
                INTO OLDPRICE
                FROM Goods2 
                WHERE Type=New.Drink;
                IF NEW.Price>OLDPRICE
                THEN
                SET NEW.Price=OLDPRICE;
                ELSEIF New.Price<0
                THEN
                SET NEW.Price=OLDPRICE; 
                END IF;
            END''')
    cursor.execute(query)
    cnx.commit()

def beverages_price_trigger2():
    query=('''CREATE TRIGGER beverages_trigger2 BEFORE INSERT ON Beverages2         
            FOR EACH ROW
            BEGIN
                DECLARE OLDPRICE DOUBLE;    
                SELECT Price
                INTO OLDPRICE
                FROM Goods2 
                WHERE Type=New.Drink;
                IF NEW.Price>OLDPRICE
                THEN
                SET NEW.Price=OLDPRICE;
                ELSEIF New.Price<0
                THEN
                SET NEW.Price=OLDPRICE;             
                END IF;
            END''')
    cursor.execute(query)
    cnx.commit()


'''
# old trigger used when beverage was not fk of goods
def beverage_trigger():
    query=(CREATE TRIGGER beverage_trigger AFTER INSERT ON Beverages2
            FOR EACH ROW
            BEGIN 
                IF NEW.Drink not in (
                 SELECT Type FROM Goods2 WHERE Type=NEW.Drink)
                THEN
                INSERT INTO Goods2 (Type) VALUES (NEW.Drink);
                END IF;
            END
            )
            '''
####################################################################################################
# Employee table and its triggers

def create_employee():
    query = ('''CREATE TABLE Employees2 (
            ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            Name CHAR(30) NOT NULL,
            DOB DATE NOT NULL,
            BaseSalary INT NOT NULL,
            Position CHAR(30),
            Warning INT DEFAULT 0);''')
    cursor.execute(query)
    cnx.commit()

def basesalary_trigger():
    query=('''CREATE TRIGGER basesalary_trigger BEFORE UPDATE ON Employees2
       FOR EACH ROW
       BEGIN
	        IF NEW.BaseSalary < 0
           THEN
           SET NEW.BaseSalary = 0;
           END IF;
        END ''')
    cursor.execute(query)
    cnx.commit()

def basesalary_trigger2():
    query = ('''CREATE TRIGGER basesalary_trigger2 BEFORE INSERT ON Employees2
           FOR EACH ROW
           BEGIN
    	        IF NEW.BaseSalary < 0
               THEN
               SET NEW.BaseSalary = 0;
               END IF;
            END ''')
    cursor.execute(query)
    cnx.commit()

def warning_trigger():
    query=('''CREATE TRIGGER warning_trigger BEFORE UPDATE ON Employees2
       FOR EACH ROW
       BEGIN
	        IF NEW.Warning < 0
           THEN
           SET NEW.Warning = 0;
           END IF;
        END ''')
    cursor.execute(query)
    cnx.commit()

def warning_trigger2():
    query = ('''CREATE TRIGGER warning_trigger2 BEFORE INSERT ON Employees2
           FOR EACH ROW
           BEGIN
    	        IF NEW.Warning < 0
               THEN
               SET NEW.Warning = 0;
               END IF;
            END ''')
    cursor.execute(query)
    cnx.commit()

def birthdate_trigger():
    query=('''CREATE TRIGGER birthdate_trigger BEFORE UPDATE ON Employees2
             FOR EACH ROW
             BEGIN
                IF NEW.DOB > CURDATE()
                THEN
                SET NEW.DOB=NULL;
                ELSEIF NEW.DOB<'1900-01-01'
                THEN
                SET NEW.DOB=NULL;
                END IF;
             END ''')
    cursor.execute(query)
    cnx.commit()

def birthdate_trigger2():
    query=('''CREATE TRIGGER birthdate_trigger2 BEFORE INSERT
     ON Employees2
             FOR EACH ROW
             BEGIN
                IF NEW.DOB > CURDATE()
                THEN
                SET NEW.DOB=NULL;
                ELSEIF NEW.DOB<'1900-01-01'
                THEN
                SET NEW.DOB=NULL;
                END IF;
             END ''')
    cursor.execute(query)
    cnx.commit()


####################################################################################################
# Expenses table and its triggers
def create_expenses():
    query=('''CREATE TABLE Expenses2(
            Date DATE PRIMARY KEY,
            Electricity DOUBLE,
            Gas DOUBLE,
            Water DOUBLE,
            Salaries DOUBLE,
            Rent DOUBLE,
            CostofGood DOUBLE,
            Total DOUBLE);''')
    cursor.execute(query)
    cnx.commit()


def total_expenses_trigger():
    query=('''CREATE TRIGGER total_expense BEFORE INSERT ON Expenses2
            FOR EACH ROW
            BEGIN
               SET NEW.Total= NEW.Electricity + NEW.Gas + NEW.Water+ NEW.Salaries+ NEW.Rent + NEW.CostofGood;
            END''')
    cursor.execute(query)
    cnx.commit()


def total_expenses2_trigger():
    query=('''CREATE TRIGGER before_expense BEFORE UPDATE ON Expenses2
            FOR EACH ROW
            BEGIN
               SET NEW.Total= NEW.Electricity + NEW.Gas + NEW.Water+ NEW.Salaries+ NEW.Rent + NEW.CostofGood;
            END ''')
    cursor.execute(query)
    cnx.commit()


####################################################################################################
# Food table and its triggers
def create_food():
    query=('''CREATE TABLE Foods2(
            No INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            FoodName CHAR(30) NOT NULL UNIQUE,
            Ingredients VARCHAR(255),
            Price DOUBLE,
            Popularity INT  DEFAULT 0);''')
    cursor.execute(query)
    cnx.commit()

def foods_triggers():
    query=('''CREATE TRIGGER foods_trigger BEFORE DELETE ON Foods2
            FOR EACH ROW
            BEGIN
                DELETE FROM LunchSpecials2 WHERE Name = OLD.FoodName;
            END
         ''')

    cursor.execute(query)
    cnx.commit()

####################################################################################################
# Lunch specials and its triggers
def create_lunchspecials():
    query=('''CREATE TABLE LunchSpecials2(
            NO INT PRIMARY KEY AUTO_INCREMENT,
            Name CHAR(30) UNIQUE,
            Price DOUBLE,
            FOREIGN KEY (Name)
                REFERENCES Foods2(FoodName)
                ON DELETE SET NULL
                ON UPDATE CASCADE);''')
    cursor.execute(query)
    cnx.commit()

'''
old trigger used when lunchspecial is not a fk of foods
def lunch_food_trigger():
    query=(CREATE TRIGGER lunch_food_trigger AFTER INSERT ON LunchSpecials2
            FOR EACH ROW
            BEGIN 
                IF NEW.Name not in (
                 SELECT FoodName FROM Foods2 WHERE Type=NEW.Name)
                THEN
                INSERT INTO Foods2 (FoodName) VALUES (NEW.Name);
                END IF;
            END
            )
    cursor.execute(query)
    cnx.commit()'''

def lunch_trigger():
    query=('''CREATE TRIGGER lunch_trigger BEFORE UPDATE ON LunchSpecials2         
            FOR EACH ROW
            BEGIN
                DECLARE OLDPRICE DOUBLE;    
                SELECT Price
                INTO OLDPRICE
                FROM Foods2 
                WHERE FoodName=New.Name;
                IF NEW.Price>OLDPRICE
                THEN
                SET NEW.Price=OLDPRICE;
                END IF;
            END''')
    cursor.execute(query)
    cnx.commit()

def lunch_trigger2():
    query=('''CREATE TRIGGER lunch_trigger2 BEFORE INSERT ON LunchSpecials2         
            FOR EACH ROW
            BEGIN
                DECLARE OLDPRICE DOUBLE;    
                SELECT Price
                INTO OLDPRICE
                FROM Foods2 
                WHERE FoodName=New.Name;
                IF NEW.Price>OLDPRICE
                THEN
                SET NEW.Price=OLDPRICE;
                END IF;
            END''')
    cursor.execute(query)
    cnx.commit()

####################################################################################################
def create_goods():
    query=('''CREATE TABLE Goods2(
            Type CHAR(30) PRIMARY KEY,
            Price DOUBLE NOT NULL,
            Quantity INT DEFAULT 0);''')
    cursor.execute(query)
    cnx.commit()

def goods_triggers():
    query=('''CREATE TRIGGER goods_trigger BEFORE DELETE ON Goods2
            FOR EACH ROW
            BEGIN
                DELETE FROM Beverages2 WHERE Drink = OLD.Type;
            END
         ''')

    cursor.execute(query)
    cnx.commit()

####################################################################################################
def create_transactions():
    query=('''CREATE TABLE Transactions2 (
            Order_ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            Date DATETIME,
            Cashier INT,
            FoodOrdered TEXT,
            Earning DOUBLE,
            FOREIGN KEY (Cashier)
                REFERENCES Employees2(ID)
                ON DELETE SET NULL
                ON UPDATE CASCADE);
            ''')
      
    cursor.execute(query)
    cnx.commit()

def earning_trigger():
    query=('''CREATE TRIGGER earning_trigger BEFORE UPDATE ON Transactions2
        FOR EACH ROW
        BEGIN
            IF NEW.Earning<0
            THEN
            SET NEW.Earning=0;
            END IF;
        END''')
    cursor.execute(query)
    cnx.commit()

############################################################################################
# End of StoredProcedures
############################################################################################
