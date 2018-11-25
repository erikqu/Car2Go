from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def register():
    return render_template("register.html")
	
@app.route('/registered', methods=['POST'])
def registered():
    try:
        conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='postgres'")
        cur = conn.cursor()
        email = request.form['email']
        name = request.form['name']
        cur.execute('INSERT INTO customer (emailAddress, name, IATA) VALUES (%s,%s,NULL)', (email, name))
        conn.commit()
    except:
        print("Cannot register!")
    return render_template("registered.html")