import os
import random

from flask import Flask


def create_app(test_config=None):
    # this function creates the Flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="Haderach",
        DATABASE=os.path.join(app.instance_path, "quiz.sqlite"),
        TODODATABASE=os.path.join(app.instance_path, "db.json"),
    )

    if test_config is None:
        # if test_config is true, use supplied config, if not revert to
        # instance config
        app.config.from_pyfile("config.py", silent=True)
        # config.py should be used to store anything confidential
    else:
        app.config.from_mapping(test_config)

    # this code checks to make sure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple Hello World page
    @app.route("/hello")
    def hello():
        return "Hello, World! \r\n Your random number of the day is: " + str(
            random.randrange(1, 32767)
        )

    # from . import cooper
    # cooper.init_app(app)

    # from . import auth
    # app.register_blueprint(auth.bp)

    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')

    from . import radioquiz

    app.register_blueprint(radioquiz.bp)

    from . import todo

    app.register_blueprint(todo.bp)

    return app
