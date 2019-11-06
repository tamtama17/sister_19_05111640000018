import os
import base64

serverlist = []

class FileServer(object):
    def __init__(self):
        pass

    def new_server(self, namainstance):
        serverlist.append(namainstance)

    def list_server(self):
        return serverlist

    def get_fileserver_object(self, namainstance):
        uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
        fserver = Pyro4.Proxy(uri)
        return fserver

    def replication(self, darisiapa, perintah, filename, isi):
        print("darisiapa")
        for server in serverlist:
            if str(darisiapa) != str(server):
                fserver=self.get_fileserver_object(server)
                if perintah=='create':
                    fserver.create(filename,'repl_mng')
                elif perintah=='update':
                    fserver.update(filename, isi,'repl_mng')
                elif perintah=='delete':
                    fserver.delete(filename,'repl_mng')