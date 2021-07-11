from flask import Flask, request, jsonify
from redis_provider import RedisProvider


def create_app():
    app = Flask(__name__)
    app.config["SCRIPT_NAME"] = "/messages"
    provider = RedisProvider("redis", 6379)

    @app.route('/messages/publish', methods=["POST"])
    def publish():
        content = request.json["content"]
        provider.publish(content)
        return "OK"

    @app.route('/messages/getLast')
    def get_last():
        return provider.get_last()

    @app.route('/messages/getByTime')
    def get_by_time():
        start = request.args.get('start', default='-inf')
        end = request.args.get('end', default='inf')
        return jsonify(provider.get_by_time(start, end))

    return app

