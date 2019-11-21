from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.db_mars
collection = db.mars

@app.route("/")
def index():
    mars = list(db.mars.find())
    print(mars)
    return render_template("index.html", mars = mars)

@app.route('/scrape')
def scrape():
    mars = scrape_mars.scrape()
    db.mars.insert_one(mars)
    return 'ok'

if __name__ == "__main__":
	app.run(debug=True)
