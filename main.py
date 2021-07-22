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
    return render_template('home.html', title = "Home Tab", row = rows, country = ethinicty_country_item, url = '/')

@app.route('/country/<int:id>')
def country(id):
    con = sql.connect("./historical_architecture.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Country;")
    rows = cur.fetchall(); 
    items = (rows[id-1])
    cur.execute("SELECT ethnicityid, id, name FROM Country ORDER BY ethnicityid;")
    row2s = cur.fetchall(); 
    id = []
    t = None
    for i in row2s:
        if i[0] == t:
            id[-1].append(i)
        else:
            t = i[0]
            id.append([i])
    cur.execute("SELECT building.photo, building.id, building.name FROM country JOIN building ON country.id = building.countryid ORDER BY country.id")
    row3s = cur.fetchall(); 
    builds = []
    for i in row3s:
        if i[0] == t:
            builds[-1].append(i)
        else:
            t = i[0]
            builds.append([i])
    return render_template('country.html', title = "Country Tab", row = rows, item = items, id1 = id[0], id2 = id[1], id3 = id[2], id4 = id[3], id5 = id[4], build = builds)

@app.route('/building/<int:id>')
def building(id):
    con = sql.connect("./historical_architecture.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM building;")
    rows = cur.fetchall(); 
    return render_template('building.html', title = "Building Tab", row = rows)

if __name__ == "__main__": 
    app.run(debug = True)
