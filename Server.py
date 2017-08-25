from socket import *
from select import *
from DB import *
from Message import *
import Server_Info

SERVER_IP = Server_Info.SERVER_IP
SERVER_PORT = Server_Info.SERVER_PORT

class Server:
    __info_list = []

    def __init__(self):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.bind((SERVER_IP, SERVER_PORT))
        self.s.listen(10)
        Server.__info_list.append(self.s)
        self.__listen()

    def __listen(self):
        while Server.__info_list:
            try:
                read_socket, write_socket, error_socket = select(Server.__info_list,[],[],1)

            except (KeyboardInterrupt, OSError):
                self.s.close()
                exit()

            else:
                for sock in read_socket:
                    if sock == self.s:
                        client, address = self.s.accept()
                        Server.__info_list.append(client)
                        for sock_in_list in Server.__info_list:
                            if sock_in_list != self.s and sock_in_list != sock:
                                print("New Client Join")
                    else:
                        continue

server = Server()