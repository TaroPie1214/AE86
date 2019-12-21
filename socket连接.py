import network, usocket,pyb


SSID='studyGod' # Network SSID
KEY='ljrsb666'  # Network key

socket_node = 0

# Init wlan module and connect to network
print("Trying to connect... (may take a while)...")

wlan = network.WINC()
wlan.connect(SSID, key=KEY, security=wlan.WPA_PSK)

# We should have a valid IP now via DHCP
print(wlan.ifconfig())

#创建 socket 连接，连接成功后发送“Hello 01Studio！”给服务器。
client=usocket.socket()
addr=('10.122.226.244',10000) #服务器 IP 和端口
client.connect(addr)
client.send('Hello 01Studio!')

#开启定时器，周期 100ms,重复执行 socket 通信接收任务
def fun(tim):
    global socket_node
    socket_node = 1
    pyb.LED(3).toggle()

tim = pyb.Timer(4,freq=10)
tim.callback(fun)


while True:

    if socket_node:
        text=client.recv(128) #单次最多接收 128 字节
        if text == '':
            pass

        else: #打印接收到的信息为字节，可以通过 decode('utf-8')转成字符串
            print(text)
            client.send('I got:'+text.decode('utf-8'))

        socket_node=0
