from flask import Flask,request,render_template,send_file
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket
import third

app = Flask(__name__,template_folder="../templates",static_folder="../static")

@app.route("/index/<uid>")
def index(uid):  # 接收uid
    # 获取请求的WebSocket对象
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    print(user_socket)
    # print(request.remote_addr)  # 远程ip地址
    while True:
        # 接收消息
        msg = user_socket.receive()
        if type(msg) == bytearray:
            # 写入文件123.wav
            with open("123.wav", "wb") as f:
                f.write(msg)

            # 将音频文件转换为文字
            res_q = third.audio2text("123.wav")
            # 调用my_nlp函数,内部调用图灵机器人
            res_a = third.my_nlp(res_q,uid)
            # 将文字转换为音频文件
            file_name = third.text2audio(res_a)
            # 发送文件名给前端
            user_socket.send(file_name)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/get_file/<file_name>")  # 获取音频文件
def get_file(file_name):  # 此方法用于前端调取后端的音频文件,用于自动播放
    return send_file(file_name)

if __name__ == "__main__":
    http_serv = WSGIServer(("0.0.0.0",5300),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()