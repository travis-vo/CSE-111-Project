import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    #change name of conn
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success") #take out if works
    except Error as e:
        print(e)
    return conn

def closeConnection(_conn, _dbFile):
    try:
        _conn.close()
        print("success") #take out if works
    except Error as e:
        print(e)

def userSign(_conn,id):
    try:
        cursor = _conn.cursor()
        name = input("Please type in your first and last name:\n")
        phone = input("Insert your phone number:\n")
        address = input("Insert your address:\n")
        sql = ("""INSERT INTO Customer(c_name,c_phone,c_address, c_ordernumber, c_custkey)
        VALUES(?,?,?,1005,6)""")
        args = [name,phone,address]
        cursor.execute(sql,args)
        _conn.commit()
    except Error as e:
        print(e)

def userReturn(_conn,id):
    try:
        cursor = _conn.cursor()
        name = input("Please input your name:\n")
        #get user name,brand,model,extra
        sql = (""" SELECT * FROM Customer WHERE c_name = ?;""")
        args = [name]
        cursor.execute(sql,args)
        _conn.commit()
        data = cursor.fetchall()
        #print(data) #prints user data
    except Error as e:
        print(e)

def brandChoice(_conn,id):
    try:
        bc = 0
        cursor = _conn.cursor()
        print("1. Toyota")
        print("2. Ford")
        print("3. Mercedes")
        print("4. Jeep")
        print("5. Honda")
        print("6. Mazda")
        bc = int(input("Please select one:"))
        if bc == 1:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Toyota';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
        if bc == 2:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Ford';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
        if bc == 3:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Mercedes';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
        if bc == 4:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Jeep';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
        if bc == 5:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Honda';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
        if bc == 6:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Mazda';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
    except Error as e:
        print(e)

def connector(_conn):
    id = 0
    val = 0
    brandval = 0
    print("Welcome to the Vo & Duong Car Dealership!")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('1. New Customer')
    print('2. Returning Customer')
    #print(id)
    val = int(input("Select a number\n"))
    if val == 1:
        id = userSign(_conn,id)
    if val == 2:
        id = userReturn(_conn,id)
    #print(id)
    if id != 0:
        print('3. Select a Car Brand')
        val = int(input("Select a number\n"))
        if val == 3:
            id = brandChoice(_conn,id)
    
def main():
    database = r"Phase2/database.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        connector(conn)
        #option(conn)
        #change print statement
        #print('You have now exit out of the application')
    closeConnection(conn, database)

if __name__ == '__main__':
    main()