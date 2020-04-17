from flask import Flask, request

app = Flask(__name__)

from src.IO.telegram import TelegramIO


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/telegram')
def telegram():
    content = request.json()
    telegram_obj = TelegramIO(content)
    telegram_obj.run_reply()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    # from flask import Flask
    # from flask_restful import reqparse, abort, Api, Resource
    #
    # app = Flask(__name__)
    # api = Api(app)
    #
    #
    #
    # from bot_telegram.bot_class import TelegramBot
    #
    #
    #
    # api.add_resource(TelegramBot, '/telegram')
    #
    #
    # if __name__ == '__main__':
    #     app.run(debug=True)
