from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db

app = Flask(__name__)

# # Create data base
# Defining the Engine
# engine = db.create_engine('sqlite:///shop.db', echo=True)
#
# # Create the Metadata Object
# metadata_obj = db.MetaData()
#
# # Define the profile table
#
# # database name
# profile = db.Table(
#     'profile',
#     metadata_obj,
#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('title', db.String(100), nullable=False),
#     db.Column('price', db.Integer, nullable=False),
#     db.Column('isActive', db.Boolean, default=True),
# )
#
# # Create the profile table
# metadata_obj.create_all(engine)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    # text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article %r' % self.id


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)