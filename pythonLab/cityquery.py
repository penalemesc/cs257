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

	row = cur.execute (sql)

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

	rowList = cur.execute(sql)

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

	rowList = cur.execute(sql)
	return rowList

def query4():
	conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")

	cur = conn.cursor()

	sql = """ DROP VIEW if EXISTS furthestWest;

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
);

   SELECT UCT.city AS furthestWest
     FROM USCitiesTop1k UCT,
          furthestWest FW
    WHERE UCT.lot = Fw.Fwest;

   SELECT UCT.city AS furthestEast
     FROM USCitiesTop1k UCT,
          furthestEast FE
    WHERE UCT.lot = FE.FEast;

	SELECT UCT.city AS furthestNorth
     FROM USCitiesTop1k UCT,
          furthestNorth FN
    WHERE UCT.lat = FN.FNorth;

	SELECT UCT.city AS furthestSouth
     FROM USCitiesTop1k UCT,
          furthestSouth FS
    WHERE UCT.lat = FS.FSouth;"""

	cur.execute(sql)

	

print (query1())
print (query2())
print (query3())
print (query4())

