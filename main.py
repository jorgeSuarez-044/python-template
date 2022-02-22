"""This script contains the structure to app's entry point"""
from src import app
from src.routes.people import blueprint as people_blueprint
from src.routes.status import blueprint as status_blueprint
from src.routes.bigquery import blueprint as chats_blueprint

app.register_blueprint(status_blueprint)
app.register_blueprint(people_blueprint)
app.register_blueprint(chats_blueprint)

if __name__ == "__main__":
    print("*" * 25)
    print("App running successfully!")
    print("Registered urls:")
    url_map_str = str(app.url_map)
    print(" " + url_map_str[5:len(url_map_str) - 2])
    print("*" * 25)
    app.run(host = '127.0.0.1', port = 8080, debug = True)
