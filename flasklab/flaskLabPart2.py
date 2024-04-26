from flask import Flask
from flask import render_template
import psycopg2
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index2.html")

"""@app.route('/randomS')
def randomS():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")
    
    cur = conn.cursor()
    sql = "select staPop from USStatesPop where code = %s"
    cur.execute(sql)
    return render_template("flaskLabPT2Random.html", randNum = num)"""

if __name__ == '__main__':
    my_port = 5104
    app.run(host='0.0.0.0', port = my_port) 
