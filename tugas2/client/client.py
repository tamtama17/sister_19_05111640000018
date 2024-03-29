import Pyro4
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


if __name__=='__main__':
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