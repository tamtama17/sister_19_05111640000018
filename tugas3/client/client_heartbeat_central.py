import Pyro4
import uuid
import os
import threading
import time

uri = "PYRONAME:greetserver@localhost:7777"

beat = int(1)
client_id = uuid.uuid1()

def test_with_ns():
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))

def service(perintah=None,isi_file=None):
    gserver = Pyro4.Proxy(uri)
    if perintah == "LIST":
        files = gserver.runperintah(perintah,isi_file)
        for f in files:
            print(f)
    else:
        print(gserver.runperintah(perintah,isi_file))

def inisiasi():
    global client_id
    fserver = Pyro4.Proxy(uri)
    print(fserver.hello(client_id))

def beat_check(a):
    global beat
    global client_id
    while True:
        fserver = Pyro4.Proxy(uri)
        heartbeat_rn = fserver.heartbeat_check(client_id)
        if beat != heartbeat_rn:
            print(fserver.remove_client(client_id))
            print("there's an error")
            os._exit(0)
        else:
            beat+=1
        time.sleep(1)

if __name__=='__main__':
    inisiasi()

    t = threading.Thread(target=beat_check, args=(0,))
    t.start()

    while True:
        print("List Perintah")
        print("1. READ [nama_file] -> untuk melihat isi file")
        print("2. CREATE [nama_file] -> untuk membuat file")
        print("3. DELETE [nama_file] -> untuk menghapus file")
        print("4. UPDATE [nama_file] -> untuk mengubah isi file")
        print("5. LIST -> untuk melihat semua file pada server")
        print("6. BYE -> untuk berhenti")
        perintah = input("Masukan perintah : ")
        if perintah == "BYE":
            print("Terimakasih :)")
            break
        isi_file=''
        cmd = perintah.split(" ")
        if cmd[0] == "CREATE" or cmd[0] == "UPDATE":
            isi_file = input("Isi file : ")
        service(perintah,isi_file)