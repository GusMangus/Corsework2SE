from flask import Flask, request, render_template, send_from_directory

from views import main_blueprint

post_path = "/data/posts.json"

app = Flask(__name__)

app.register_blueprint(main_blueprint)


if __name__ == "__main__":
    app.run()