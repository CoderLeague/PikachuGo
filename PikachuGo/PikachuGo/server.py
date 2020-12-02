# -*- coding: utf-8 -*-
from gevent import monkey

monkey.patch_all()
from ws4py.websocket import WebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
import queue
import threading,time


class CalllbackWebSocket(WebSocket):
    callback_fun = None
    response_q = queue.Queue()
    def received_message(self, message):
        """
        Automatically sends back the provided ``message`` to
        its originating endpoint.
        """
        self.callback_fun(message.data, message.is_binary)
        while True:
            try:
                line = self.response_q.get()
            except EOFError:
                break

            if line == '' or line == None:
                time.sleep(1)
                continue
            print("response: ",line)
            self.send(bytes(line,encoding="utf-8"),False)
            break

def test():
    ws_receive_queue = queue.Queue()

    def ws_callback(self_place, byte_data, is_bin):
        data = str(byte_data, encoding="utf-8")
        ws_receive_queue.put(data)

    app = WebSocketWSGIApplication(handler_cls=CalllbackWebSocket)
    app.handler_cls.callback_fun = ws_callback
    server = WSGIServer(('10.105.137.57', 8021), app)
    td = threading.Thread(target=server.serve_forever)
    td.start()
    while True:
        try:
            line = ws_receive_queue.get()
        except EOFError:
            break

        if line == '' or line == None:
            time.sleep(1)
            continue
        print(line)
        app.handler_cls.response_q.put(line)


    td.join()

def debug():
    def ws_callback(self_place, data, is_bin):
        print("data=",type(data),data)
        print("data=", type(data), data)

    app = WebSocketWSGIApplication(handler_cls=CalllbackWebSocket)
    app.handler_cls.callback_fun  = ws_callback
    server = WSGIServer(('10.105.137.57', 8021), app)
    server.serve_forever()

if __name__ == '__main__':
    test()