from flask import Flask
from flask import render_template
import psycopg2
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index2.html")

@app.route('/randomS')
def randomS():
    
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
    return render_template("flaskLabPT2Random.html", randFood = cur.fetchone(), randYear = rYear)

if __name__ == '__main__':
    my_port = 5104
    app.run(host='0.0.0.0', port = my_port) 
