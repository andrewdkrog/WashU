from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.store_inventory

# Drops collection if available to remove duplicates
db.produce.drop()

# Creates a collection in the database and inserts two documents
db.produce.insert_many(
    [
        {
            "type": "apples",
            "cost": .23,
            "stock": 333
        },
        {
            "type": "bananas",
            "cost": .43,
            "stock": 64
        }
    ]
)


# Set route
@app.route('/')
def index():
    # Store the entire produce collection in a list
    produce = list(db.produce.find())
    print(produce)

    # Return the template with the teams list passed in
    return render_template('index.html', inventory=produce)

if __name__ == "__main__":
    app.run(debug=True)
