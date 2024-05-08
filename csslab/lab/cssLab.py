from flask import Flask
from flask import render_template
import psycopg2
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Hello! Here you can get a random sentence by use of an sql Query about when some fruits where first used as a weapon"
    message = message + " And change the colour to the background of the page to whatever colour you write"
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")
    
    cur = conn.cursor()
    num = random.randint(1, 5)
    rYear = random.randint(-9999, 9999)
    print(num)
    sql = "select rName from randomN where rNum = %s"
    cur.execute(sql, [num])
    #The only caveat that I have with this is that I am not aware of how to fetch the data and not the () that come
    #with the fetchone function, but everything else works
    gh = cur.fetchone()
    
	
    return render_template("paginaInicial.html", randFood = gh[0], randYear = rYear)


if __name__ == '__main__':
    my_port = 5104
    app.run(host='0.0.0.0', port = my_port) 