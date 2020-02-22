from pynput import keyboard
import socket
import time


def on_press(key):
    try:
        # print('Key {0} pressed'.format(key.char))
        global myKey
        global keyReleased
        myKey = key.char
        keyReleased = False
        # print(myKey)
    except AttributeError:
        print('Special key {0} pressed'.format(key))
        myKey = '{0}'.format(key)


def on_release(key):
    # print('{0} released'.format(key))
    global keyReleased
    keyReleased = True
    if key == keyboard.Key.esc:
        return False


def switch_case(argument):

    switcher = {
        0: "zero",
        1: "one",
        2: "two",
        "w": "forward"
    }

    return switcher.get(argument, "nothing")


myKey = ''
keyReleased = True

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET represents IPV4, SOCK_STREAM represents TCP

# s.connect(("127.0.0.1", 1994))
# print('Connected')
s.connect(("192.168.43.84", 1995))
# for server side
# s.bind(("127.0.0.1", 1995))  # ip address, port
#
# s.listen(5)

while True:
    if myKey == 'Key.esc':
        break
    if myKey != '':
        print('The last Key was ' + myKey)
    if not keyReleased:
        s.send(bytes(myKey, "utf-8"))
    else:
        s.send(bytes("nope", "utf-8"))
        # clientSocket, address = s.accept()
        # print(f"Connection from {address} has been established")
        # clientSocket.send(bytes("Welcome to the local host!", "utf-8"))  # send data to client
    time.sleep(.01)




#
# while True:
#     listener = keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release)
#     listener.start()
#     listener.join()



#
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()
