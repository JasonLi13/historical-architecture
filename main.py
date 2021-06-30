from flask import Flask, render_template, url_for
import sqlite3 as sql

app = Flask(__name__)
country_items = []


@app.route('/')
def home():
    con = sql.connect("./historical_architecture.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Ethnicity ORDER BY id;")
    rows = cur.fetchall(); 

    cur.execute("SELECT ethnicity.id, country.name, country.photo, country.id FROM Ethnicity join country ON ethnicity.id = country.ethnicityid ORDER BY ethnicity.id;")
    country_items = cur.fetchall(); 
    ethinicty_country_item = []
    t = None
    for i in country_items:
        if i[0] == t:
            ethinicty_country_item[-1].append(i)
        else:
            t = i[0]
            ethinicty_country_item.append([i])
    return render_template('home.html', title = "Home Tab", row = rows, country=ethinicty_country_item, url='/')

@app.route('/country/<int:id>')
def country(id):
    con = sql.connect("./historical_architecture.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Country;")
    rows = cur.fetchall(); 
    items = (rows[id-1])
    print(rows[id-1])
    return render_template('country.html', title = "Country Tab", row = rows, item = items)


if __name__ == "__main__":
    app.run(debug = True)
