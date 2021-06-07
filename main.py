from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    con = sql.connect("./historical_architecture.db")
    cur = con.cursor()
    cur.execute("select * from Ethnicity ORDER BY id;")
    
    rows = cur.fetchall(); 
    cur.execute("select * from Ethnicity join country on ethnicity.id = country.ethnicityid ORDER BY ethnicity.id, country.id;")
    datas = cur.fetchall
    return render_template('home.html', title = "Home Tab", row = rows, data = datas)

@app.route('/country')
def country():
    return render_template('country.html', title = "country Tab")


if __name__ == "__main__":
    app.run(debug = True)
