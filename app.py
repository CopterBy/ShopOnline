from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy()

class Item(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Colum(db.Integer, nullable=False)
    isActive = db.Colum(db.Integer, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)