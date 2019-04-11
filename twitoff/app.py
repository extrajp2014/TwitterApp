"""Main application and routing logic for TwitOff."""
from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template
from .models import DB, User

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = getenv('FLASK_ENV')
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')

    @app.route('/user/<name>')
    def user(name):
        tweets = User.query.filter(User.name == name).one().tweets
        return render_template('user.html', title=name, tweets=tweets)

    return app