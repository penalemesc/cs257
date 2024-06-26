"""
cityquery.py
Created by @author Conrado Peña Lemes
Returns queries requested in the assignment pyhtonLab
Queries were originally created in sql, that is why queries such as number 4 are so long
"""

import psycopg2

def query1():
	conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")

	cur = conn.cursor()

	sql = "select lot, lat from USCitiesTop1k where city = 'Northfield';"

	cur.execute(sql)
	row = cur.fetchall()

	if row is None:
		print("Sorry northfield is not on the Database.")
	
	cur.close()

	return row

def query2():
	
	conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")

	cur = conn.cursor()

	sql = "WITH maxCityPop AS (SELECT max(cityPop) AS MaxCP FROM USCitiesTop1k) SELECT city AS BiggestCity FROM USCitiesTop1k, maxCityPop WHERE cityPop = MaxCP;"
	cur.execute(sql)
	
	rowList = cur.fetchall()
	
	return rowList

def query3():
	
	conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")

	cur = conn.cursor()

	sql = """ WITH minCityPop AS (
             SELECT min(cityPop) AS MinCP
               FROM USCitiesTop1k
              WHERE stateName = 'Minnesota'
          )
   SELECT city AS SmallestCityInMinnesota
     FROM USCitiesTop1k,
          minCityPop
    WHERE cityPop = MinCP;"""

	cur.execute(sql)
	rowList = cur.fetchall()
	return rowList

def query4():
	conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")

	cur = conn.cursor()

	createViewsSql = """ DROP VIEW if EXISTS furthestWest;

DROP VIEW if EXISTS furthestEast;

DROP VIEW if EXISTS furthestNorth;

DROP VIEW if EXISTS furthestSouth;

   CREATE VIEW furthestEast AS (
   SELECT min(lot) AS FEast
     FROM USCitiesTop1k
);

   CREATE VIEW furthestNorth AS (
   SELECT max(lat) AS FNorth
     FROM USCitiesTop1k
);

   CREATE VIEW furthestSouth AS (
   SELECT min(lat) AS FSouth
     FROM USCitiesTop1k
);
   CREATE VIEW furthestWest AS (
   SELECT max(lot) AS FWest
     FROM USCitiesTop1k
);"""
	northSQL = """SELECT UCT.city AS furthestNorth
     FROM USCitiesTop1k UCT,
          furthestNorth FN
    WHERE UCT.lat = FN.FNorth;"""
	southSQL = """SELECT UCT.city AS furthestSouth
     FROM USCitiesTop1k UCT,
          furthestSouth FS
    WHERE UCT.lat = FS.FSouth;"""
	eastSQL = """SELECT UCT.city AS furthestEast
     FROM USCitiesTop1k UCT,
          furthestEast FE
    WHERE UCT.lot = FE.FEast;"""
	westSQL = """SELECT UCT.city AS furthestWest
     FROM USCitiesTop1k UCT,
          furthestWest FW
    WHERE UCT.lot = Fw.Fwest;"""
	cur.execute(createViewsSql)
	cur.execute(northSQL)
	north = cur.fetchall()
	cur.execute(southSQL)
	south = cur.fetchall()
	cur.execute(eastSQL) 
	east = cur.fetchall()
	cur.execute(westSQL)
	west = cur.fetchall()
	return north, south, east, west

def query5():
	conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")

	cur = conn.cursor()
	print("Hi please write a State or state abbreviation to look for in the database")
	input1 = input()
	if len(input1) == 2:
		
		sql = "select stateName, staPop from USStatesPop where code = %s"
		#upper hace lo que toUpperCase hace en java, ergo, pone todo en mayuscula
		cur.execute(sql, [input1.upper()])
		
		return cur.fetchall()
	#capitalize hace que la primera letra sea en mayuscula pero no el resto	
	else:
		sql = "select staPop from USStatesPop where stateName = %s"
		cur.execute(sql, [input1.capitalize()])
		return cur.fetchall()
		
print (query1())
print (query2())
print (query3())
print (query4())
print (query5())

