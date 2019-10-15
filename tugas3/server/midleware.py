import os
import threading
import time

clist = []

class GreetServer(object):
    def __init__(self):
        pass

    def test(self):
        return "oke"

    def heartbeating(a):
        global clist
        panjang = len(clist)
        while True:
            for x in range(panjang):
                clist[x][1]+=int(1)
            time.sleep(1)

    def heartbeat_check(self,client_id):
        panjang = len(clist)
        for x in range(panjang):
            if clist[x][0] == client_id:
                return int(clist[x][1])

    def hello(self,client_id):
        global clist
        list2 = [client_id, int(1)]
        clist.append(list2)
        return(str(client_id)+"listed")

    def remove_client(self,client_id):
        global clist
        panjang = len(clist)
        for x in range(panjang):
            if clist[x][0] == client_id:
                del clist[x]
                return(str(client_id)+" removed")

    def runperintah(self,perintah=None,isi_file=None):
        perintah = perintah.split(" ")
        file_ga_ada = "File tidak ditemukan"
        if perintah[0] == "READ":
            if os.path.exists(perintah[1]):
                file = open(perintah[1], "r")
                isinya = file.read()
                file.close()
                return isinya
            else:
                return file_ga_ada
        elif perintah[0] == "CREATE":
            if os.path.exists(perintah[1]):
                return "File sudah ada, gunakan nama lain"
            else:
                file = open(perintah[1], "w")
                file.write(isi_file)
                file.close()
                return "File terbuat"
        elif perintah[0] == "DELETE":
            if os.path.exists(perintah[1]):
                os.remove(perintah[1])
                return "File terhapus"
            else:
                return file_ga_ada
        elif perintah[0] == "UPDATE":
            if os.path.exists(perintah[1]):
                file = open(perintah[1], "a")
                file.write("\n")
                file.write(isi_file)
                file.close()
                return "File terupdate"
            else:
                return file_ga_ada
        elif perintah[0] == "LIST":
            path = os.getcwd()
            files = []
            for r, d, f in os.walk(path):
                for file in f:
                    files.append(os.path.join(r, file))
                for dir in d:
                    files.append(os.path.join(r, dir))
            return files


if __name__ == '__main__':
    k = GreetServer()
    print(k.get_greet('royyana'))
    t = threading.Thread(target=heartbeating, args=(1,))
    t.start()
