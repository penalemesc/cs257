"""
Edited by Conrado Peña Lemes
Uses flask to return queries on a website
"""
import flask
import psycopg2

app = flask.Flask(__name__)

#app.route es lo que se deberia ejecutar de la pagina web
@app.route('/hello')
def my_function():
    return "Hello World!"

#Esto funciona porque le damos parametros 2 palabras que en este caso son random y las devuelve, pero
#se podria usar con palabras especificas para que muestre una cosa especifica
@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

#Here start the queries created by Conrado Peña Lemes
#Esto devuelve la suma de 2 numeros que pasamos por la ruta
@app.route('/add/<num1>/<num2Str>')
def addTwoNums(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    added = num1 + num2
    added = str(added)
    return added

#Esto devuelve la poblacion de un estado que le pasamos por la ruta 
@app.route('/pop/<abbrev>')
def populationCount(abbrev):
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="penalemesc",
        user="penalemesc",
        password="bird739square")
    
    cur = conn.cursor()
    sql = "select staPop from USStatesPop where code = %s"
    cur.execute(sql, [abbrev.upper()])
    return cur.fetchall()
    
if __name__ == '__main__':
    my_port = 5104
    app.run(host='0.0.0.0', port = my_port) 
