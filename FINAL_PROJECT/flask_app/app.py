from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from routes.bp import game_routes

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

#access the environment variables
spotify_client_id = os.getenv("SPOTIPY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")


app = Flask(__name__)

app.secret_key=os.getenv('SECRET_KEY', 'default_secret_key')

@app.route('/')
def startScreen():
    return render_template('startScreen.html')

app.register_blueprint(game_routes)

if __name__ == '__main__':
    app.run(debug=True)
