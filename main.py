"""This script contains the structure to app's entry point"""
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from src import api
from src.routes.people import blueprint as people_blueprint
from src.routes.status import blueprint as status_blueprint

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(status_blueprint)
app.register_blueprint(people_blueprint)

api.init_app(app)

if __name__ == "__main__":
    print("*" * 25)
    print("App running successfully!")
    print("Registered urls:")
    url_map_str = str(app.url_map)
    print(" " + url_map_str[5:len(url_map_str) - 2])
    print("*" * 25)
    app.run(host = '127.0.0.1', port = 8080, debug = True)
