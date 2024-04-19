import psycopg2

def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return None

def testCreateTable():
    
	conn = psycopg2.connect(
        host="localhost",
        port=5432,   
    	database="penalemesc",
        user="penalemesc",
		password="bird739square"
	)
     
	cur = conn.cursor()
     
	createTableStatesSQL = "CREATE TABLE USStatesPop (code char(2) NOT NULL, stateName varchar(25) NOT NULL, staPop int NOT NULL, PRIMARY KEY (code));"

	insertIntoStatesSQL = "\copy USStatesPop from 'us-state-pop.csv' DELIMITER ',' CSV"
    
	createTableCitiesSQL = "CREATE TABLE USCitiesTop1k (city varchar(75) NOT NULL, stateName varchar(25) NOT NULL, cityPop int NOT NULL, lat real NOT NULL, lot real NOT NULL, PRIMARY KEY (city, stateName));" 
    
	insertIntoCitiesSQL = "\copy USCitiesTop1k from 'us-cities-top-1k.csv' DELIMITER ',' CSV"
	
	cur.execute( createTableStatesSQL )

	cur.execute( createTableCitiesSQL )
     
	cur.execute( insertIntoStatesSQL )
    
	cur.execute( insertIntoCitiesSQL )
     
	conn.commit()