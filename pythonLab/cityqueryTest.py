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

def testQueryNum1():
	
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
            
print (testQueryNum1())
