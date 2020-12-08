import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    #change name of conn
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        #print("success") #take out if works
    except Error as e:
        print(e)
    return conn

def closeConnection(_conn, _dbFile):
    try:
        _conn.close()
        #print("success") #take out if works
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
        if not data:
            newval = 0
            print("Entry not found")
            print("1. Try again")
            print("2. Sign Up as New Customer")
            newval = int(input("Select a number:\n"))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            if newval == 1:
                userReturn(_conn,id)
            if newval == 2:
                userSign(_conn,id)
        print("Welcome", name, "!")
        #print(data) #prints user data
    except Error as e:
        print(e)

def carChoice(_conn,id):
    try:
        cursor = _conn.cursor()
        print('Please select a Car Brand')
        print("1. Toyota")
        print("2. Ford")
        print("3. Mercedes")
        print("4. Jeep")
        print("5. Honda")
        print("6. Mazda")
        bc = int(input("Please select one: "))
        if bc == 1:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Toyota';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
            ToyotaModel(_conn,id)
        #---------------------------------------------------------------------
        elif bc == 2:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Ford';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
            FordModel(_conn,id)
        #---------------------------------------------------------------------
        elif bc == 3:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Mercedes';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
            MercedesModel(_conn,id)
        #---------------------------------------------------------------------
        elif bc == 4:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Jeep';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
            JeepModel(_conn,id)
        #---------------------------------------------------------------------
        elif bc == 5:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Honda';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
            HondaModel(_conn,id)
        #---------------------------------------------------------------------
        elif bc == 6:
            sql = (""" SELECT b_price FROM Brand WHERE b_name = 'Mazda';""")
            cursor.execute(sql)
            _conn.commit()
            brandprice = cursor.fetchall()
            for row in brandprice:
                print("The base price will be: $",row[0])
            MazdaModel(_conn,id)
        else:
            print("Invalid input, try again")
            carChoice(_conn,id)
    except Error as e:
        print(e) 

        #---------------------------------------------------------------------        
        #-----------------------START OF TOYOTA CHOICE------------------------
        #---------------------------------------------------------------------

def ToyotaModel(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Model""")
        print("1. Corolla")
        print("2. RAV4")
        mc = int(input("Please select one: "))
        #---------
        if mc == 1:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'Corolla';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            ToyotaCorollaPackage(_conn,id)
        elif mc == 2:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'RAV4';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            ToyotaRAVPackage(_conn,id)
        else:
            print('Not a valid number')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            ToyotaModel(_conn,id)
    except Error as e:
        print(e)
    

def ToyotaCorollaPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. LE Convenience""")
        print("""2. SE Premium""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 200;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Toyota'
                AND m_name = 'Corolla'
                AND e_name = 'LE Convenience';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 201;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Toyota'
                AND m_name = 'Corolla'
                AND e_name = 'SE Premium';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Toyota'
                AND m_name = 'Corolla';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  

    except Error as e:
        print(e)

def ToyotaRAVPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. XLE Grader Convenience""")
        print("""2. XLE Grader Weather""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 202;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Toyota'
                AND m_name = 'RAV4'
                AND e_name = 'XLE Grader Convenience';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 203;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Toyota'
                AND m_name = 'RAV4'
                AND e_name = 'XLE Grader Weather';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Toyota'
                AND m_name = 'RAV4';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
    except Error as e:
        print(e)
        #---------------------------------------------------------------------        
        #------------------------END OF TOYOTA CHOICE-------------------------
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------        
        #------------------------START OF FORD CHOICE-------------------------
        #---------------------------------------------------------------------

def FordModel(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Model""")
        print("1. Mustang")
        print("2. Fusion")
        mc = int(input("Please select one: "))
        #---------
        if mc == 1:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'Mustang';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            FordMustangPackage(_conn,id)
        elif mc == 2:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'Fusion';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            FordFusionPackage(_conn,id)
        else:
            print('Not a valid number')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            FordModel(_conn,id)
    except Error as e:
        print(e)
    

def FordMustangPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. GT Performance""")
        print("""2. Carbon Sport Interior""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 204;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Ford'
                AND m_name = 'Mustang'
                AND e_name = 'GT Performance';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 205;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Ford'
                AND m_name = 'Mustang'
                AND e_name = 'Carbon Sport Interior';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Ford'
                AND m_name = 'Mustang';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  

    except Error as e:
        print(e)

def FordFusionPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. All-Wheel-Drive""")
        print("""2. Co-Pilot360""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 206;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Ford'
                AND m_name = 'Fusion'
                AND e_name = 'All-Wheel-Drive';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 207;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Ford'
                AND m_name = 'Fusion'
                AND e_name = 'Co-Pilot360';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Ford'
                AND m_name = 'Fusion';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
    except Error as e:
        print(e)
        #---------------------------------------------------------------------        
        #-------------------------END OF FORD CHOICE--------------------------
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------        
        #------------------------START OF MERCEDES CHOICE---------------------
        #---------------------------------------------------------------------

def MercedesModel(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Model""")
        print("1. AMG GT")
        print("2. GLE SUV")
        mc = int(input("Please select one: "))
        #---------
        if mc == 1:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'AMG GT';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            MercedesAMGPackage(_conn,id)
        elif mc == 2:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'GLE SUV';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            MercedesGLEPackage(_conn,id)
        else:
            print('Not a valid number')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            FordModel(_conn,id)
    except Error as e:
        print(e)
    

def MercedesAMGPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. Aerodynamics""")
        print("""2. Lane Tracking""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 208;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Mercedes'
                AND m_name = 'AMG GT'
                AND e_name = 'Aerodynamics';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 209;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Mercedes'
                AND m_name = 'AMG GT'
                AND e_name = 'Lane Tracking';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Mercedes'
                AND m_name = 'AMG GT';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  

    except Error as e:
        print(e)

def MercedesGLEPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. Comfort""")
        print("""2. Driver Assistance""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 210;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Mercedes'
                AND m_name = 'GLE SUV'
                AND e_name = 'Comfort';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 211;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Mercedes'
                AND m_name = 'GLE SUV'
                AND e_name = 'Driver Assistance';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Mercedes'
                AND m_name = 'GLE SUV';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
    except Error as e:
        print(e)
        #---------------------------------------------------------------------        
        #-------------------------END OF MERCEDES CHOICE----------------------
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------        
        #------------------------START OF JEEP CHOICE---------------------
        #---------------------------------------------------------------------

def JeepModel(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Model""")
        print("1. Wrangler")
        print("2. Renegade")
        mc = int(input("Please select one: "))
        #---------
        if mc == 1:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'Wrangler';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            JeepWranglerPackage(_conn,id)
        elif mc == 2:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'Renegade';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            JeepRenegadePackage(_conn,id)
        else:
            print('Not a valid number')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            FordModel(_conn,id)
    except Error as e:
        print(e)
    

def JeepWranglerPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. Heavy-Duty Electrical""")
        print("""2. Smokers""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 212;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Jeep'
                AND m_name = 'Wrangler'
                AND e_name = 'Heavy-Duty Electrical';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 213;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Jeep'
                AND m_name = 'Wrangler'
                AND e_name = 'Smokers';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Jeep'
                AND m_name = 'Wrangler';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  

    except Error as e:
        print(e)

def JeepRenegadePackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. Advanced Technology""")
        print("""2. Uconnect 8.4""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 214;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Jeep'
                AND m_name = 'Renegade'
                AND e_name = 'Advanced Technology';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 215;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Jeep'
                AND m_name = 'Renegade'
                AND e_name = 'Uconnect 8.4';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Jeep'
                AND m_name = 'Renegade';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
    except Error as e:
        print(e)
        #---------------------------------------------------------------------        
        #-------------------------END OF JEEP CHOICE--------------------------
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------        
        #------------------------START OF HONDA CHOICE------------------------
        #---------------------------------------------------------------------

def HondaModel(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Model""")
        print("1. Accord")
        print("2. Civic")
        mc = int(input("Please select one: "))
        #---------
        if mc == 1:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'Accord';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            HondaAccordPackage(_conn,id)
        elif mc == 2:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'Civic';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            HondaCivicPackage(_conn,id)
        else:
            print('Not a valid number')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            FordModel(_conn,id)
    except Error as e:
        print(e)
    

def HondaAccordPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. All-Season Protection""")
        print("""2. Accord Protection""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 216;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Honda'
                AND m_name = 'Accord'
                AND e_name = 'All-Season Protection';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 217;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Honda'
                AND m_name = 'Accord'
                AND e_name = 'Accord Protection';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Honda'
                AND m_name = 'Accord';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  

    except Error as e:
        print(e)

def HondaCivicPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. All-Season ProPack""")
        print("""2. Civic Protection""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 218;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Honda'
                AND m_name = 'Civic'
                AND e_name = 'All-Season ProPack';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 219;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Honda'
                AND m_name = 'Civic'
                AND e_name = 'Civic Protection';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Honda'
                AND m_name = 'Civic';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
    except Error as e:
        print(e)
        #---------------------------------------------------------------------        
        #-------------------------END OF HONDA CHOICE-------------------------
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------        
        #------------------------START OF MAZDA CHOICE------------------------
        #---------------------------------------------------------------------

def MazdaModel(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Model""")
        print("1. MX-5 Miata")
        print("2. Mazda6")
        mc = int(input("Please select one: "))
        #---------
        if mc == 1:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'MX-5 Miata';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            MazdaMiataPackage(_conn,id)
        elif mc == 2:
            sql = ("""SELECT m_price FROM model WHERE m_name = 'Mazda6';""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            Mazda6Package(_conn,id)
        else:
            print('Not a valid number')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            FordModel(_conn,id)
    except Error as e:
        print(e)
    

def MazdaMiataPackage(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. Black Trim""")
        print("""2. OffRoad Engine""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 221;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Mazada'
                AND m_name = 'MX-5 Miata'
                AND e_name = 'Black Trim';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 222;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Mazda'
                AND m_name = 'MX-5 Miata'
                AND e_name = 'OffRoad Engine';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Mazda'
                AND m_name = 'MX-5 Miata';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  

    except Error as e:
        print(e)

def Mazda6Package(_conn,id):
    try:
        cursor = _conn.cursor()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(""" Please select a Car Package""")
        print("""1. Matte Paint""")
        print("""2. Mazda Care""")
        print("""3. NONE""")
        ec = int(input("Please select one: "))
        if ec == 1:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 223;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Mazda'
                AND m_name = 'Mazda6'
                AND e_name = 'Matte Paint';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 2:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 224;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price + e_price) as estimateTOTAL
                FROM Brand,Model,extraPackages
                WHERE b_brandkey = m_brandkey
                AND m_modelkey = e_modelkey
                AND b_name = 'Mazda'
                AND m_name = 'Mazda6'
                AND e_name = 'Mazda Care';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
        if ec == 3:
            sql = ("""SELECT e_price FROM extraPackages WHERE e_packkey = 220;""")
            cursor.execute(sql)
            _conn.commit()
            modelprice = cursor.fetchall()
            for row in modelprice:
                print("The base price will be: $",row[0])
            print("Are you satisfied with your choices?")
            choice = input("Y or N:\n")
            if choice == 'Y':
                sql = """SELECT (b_price + m_price) as estimateTOTAL
                FROM Brand,Model
                WHERE b_brandkey = m_brandkey
                AND b_name = 'Mazda'
                AND m_name = 'Mazda6';"""
                cursor.execute(sql)
                _conn.commit()
                estimateprice = cursor.fetchall()
                for row in estimateprice:
                    print("The estimate total will be: $",row[0])
                return
            if choice == 'N':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                carChoice(_conn,id)  
    except Error as e:
        print(e)
        #---------------------------------------------------------------------        
        #-------------------------END OF MERCEDES CHOICE----------------------
        #---------------------------------------------------------------------



def connector(_conn):
    id = 0
    val = 0
    bc = 0
    print("~~~~~~~ Vo & Duong Car Dealership ~~~~~~~")
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
    #if id != 0:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    id = carChoice(_conn,id)
    
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