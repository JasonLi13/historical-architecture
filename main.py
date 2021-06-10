from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)
country_items = []


@app.route('/')
def home():
    con = sql.connect("./historical_architecture.db")
    cur = con.cursor()
    cur.execute("select * from Ethnicity ORDER BY id;")
    rows = cur.fetchall(); 

    cur.execute("select ethnicity.id, country.name, country.photo from Ethnicity join country on ethnicity.id = country.ethnicityid ORDER BY ethnicity.id;")
    country_items = cur.fetchall(); 
    ethinicty_country_item = []
    t = None
    for i in country_items:
        if i[0] == t:
            ethinicty_country_item[-1].append(i)
        else:
            t = i[0]
            ethinicty_country_item.append([i])
    print(ethinicty_country_item)
    return render_template('home.html', title = "Home Tab", row = rows, country=ethinicty_country_item)

@app.route('/country')
def country():
    return render_template('country.html', title = "country Tab")


if __name__ == "__main__":
    app.run(debug = True)
