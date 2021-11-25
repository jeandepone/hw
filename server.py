import tornado.ioloop
import tornado.web
import motor.motor_tornado
import os

client = motor.motor_tornado.MotorClient(
    os.environ.get("MONGO_URI", "mongodb://localhost:27017")
)


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        self.write(self.request.body)

    def get(self):
        self.write("Hello, world")


tornado.web.Application(
    [
        (r"/", MainHandler),
    ]
).listen(int(os.environ.get("PORT", 8888)))
tornado.ioloop.IOLoop.current().start()
