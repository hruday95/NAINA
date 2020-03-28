# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     return "Hello World!"
#
# if __name__ == '__main__':
#     app.run()
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)



from bot_telegram.bot_class import TelegramBot



api.add_resource(TelegramBot, '/telegram')


if __name__ == '__main__':
    app.run(debug=True)




