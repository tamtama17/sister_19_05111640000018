import Pyro4
import threading
import time
import os

uri = "PYRONAME:greetserver@localhost:7777"


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

def pingack(a):
    counter = 0
    while True:
        try:
            fserver = Pyro4.Proxy(uri)
            fserver.test()
            counter = 0
        except:
            counter+=1
            if counter>2:
                print("\nCan't reach server")
                os._exit(0)
        time.sleep(1)



if __name__=='__main__':
    t = threading.Thread(target=pingack, args=(1,))
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