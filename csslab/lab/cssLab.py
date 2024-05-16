from flask import Flask
from flask import render_template
from flask import request
import psycopg2


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def citiesInState():
    if request.method == 'POST':
        staCode = request.form['stateCode']
        conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")

        cur = conn.cursor()
        sql = "select city from USCitiesTop1k USC, USStatesPop USS where USC.stateName = USS.stateName and code = %s"
        cur.execute(sql, [staCode.upper()])
        ciudad = cur.fetchall()
        #If writing a state that doesnt exist, it will return what we wrote and an empty array
        return render_template("CitiesInState.html", cities = ciudad, state = staCode)
    
    else:
        return render_template("CitiesInState.html")
    

if __name__ == '__main__':
    my_port = 5104
    app.run(host='0.0.0.0', port = my_port) 
