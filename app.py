from flask import Flask
from flask_cors import CORS
from src.routes.reviews import review_bp
import subprocess


app = Flask(__name__)
CORS(app)

app.register_blueprint(review_bp, url_prefix='/review')


if __name__ == '__main__':
    app.run(debug=True, port=5000)


# python "app.py"