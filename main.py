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
    return render_template('home.html', title = "Home Tab", row = rows, country=ethinicty_country_item, url = '/')

@app.route('/country/<int:id>')
def country(id):
    con = sql.connect("./historical_architecture.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Country;")
    rows = cur.fetchall(); 
    items = (rows[id-1])
    id1s = []
    id2s = []
    id3s = []
    id4s = []
    id5s = []
    for i in rows:
        if i[5] == 1:
            id1s.append(i)
        elif i[5] == 2:
            id2s.append(i)
        elif i[5] == 3:
            id3s.append(i)
        elif i[5] == 4:
            id4s.append(i)
        elif i[5] == 5:
            id5s.append(i)
    return render_template('country.html', title = "Country Tab", row = rows, item = items, id1 = id1s, id2 = id2s, id3 = id3s, id4 = id4s, id5 = id5s)


if __name__ == "__main__":
    app.run(debug = True)
