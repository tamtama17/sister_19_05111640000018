import Pyro4
import base64
import json
import sys

def get_fileserver_object():
    namainstance = input("Namainstance : ")
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    while True:
        print("List Perintah")
        print("1. LIST -> untuk melihat semua file pada server")
        print("2. READ [nama_file] -> untuk melihat isi file")
        print("3. CREATE [nama_file] -> untuk membuat file")
        print("4. DELETE [nama_file] -> untuk menghapus file")
        print("5. UPDATE [nama_file] -> untuk mengubah isi file")
        print("6. BYE -> untuk berhenti")
        perintah = input("Masukan perintah : ")
        if perintah == "BYE":
            print("Terimakasih :)")
            break
        isi_file=''
        cmd = perintah.split(" ")
        if cmd[0] == "UPDATE":
            isi_file = input("Isi file : ")
            f.update(cmd[1], isi_file, 'client')
        elif cmd[0] == "LIST":
            print(f.list())
        elif cmd[0] == "READ":
            print(f.read(cmd[1]))
        elif cmd[0] == "CREATE":
            f.create(cmd[1], 'client')
        elif cmd[0] == "DELETE":
            f.delete(cmd[1], 'client')
        elif cmd[0] == "BYE":
            print("Terimakasih :)")
            break