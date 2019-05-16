import threading
import socket
import struct
import os


# 消息内容
class ClientThread(threading.Thread):

    msg = ''
    newpath = ''
    def __init__(self, msg):

        super().__init__()
        self.msg = msg
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 获取本地主机名
        #host = socket.gethostname()
        #host = '169.254.55.105'
        host = '192.168.137.110'
        # 设置端口号
        port = 8088
        # 连接服务，指定主机和端口
        self.s.connect((host, port))

    def run(self):
        print("starting thread...")
        #self.sendmsg()
        self.getimage()

    def getimage(self):
        fileinfo_size = struct.calcsize('128sl')
        buf = self.s.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sl', buf)
            fn = filename.decode().strip('\x00')
            new_filename = os.path.join('./Myaction/static/img/frompi', 'new_' + fn)
            self.newpath = new_filename
            recvd_size = 0
            fp = open(new_filename, 'wb')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = self.s.recv(1024)
                    recvd_size += len(data)
                else:
                    data = self.s.recv(1024)
                    recvd_size = filesize
                fp.write(data)
            fp.close()


    def sendmsg(self):
        self.s.send(bytes(self.msg, encoding='utf-8'))

    def getimagepath(self):
        return self.newpath

    #向树莓派发送信号
    def sendsignal(self):
        self.s.send(bytes('A', encoding='utf-8'))


    def closeconn(self):
        self.s.close()
