Tutorial
https://buildmedia.readthedocs.org/media/pdf/pyro4/stable/pyro4.pdf


### Aktifasi virtualenv
Jika menggunakan ubuntu
install python3-venv dengan mengetikan
```   
apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Menjalankan program
1. Menjalankan pyro nameserver   
`pyro4-ns -n localhost -p 7777`
2. Masuk ke folder server lalu jalankan [server.py](https://github.com/tamtama17/sister_19_05111640000018/blob/master/tugas2/server/server.py)   
`python server.py`
3. Selanjutnya pindah ke folder client lalu jalankan [client.py](https://github.com/tamtama17/sister_19_05111640000018/blob/master/tugas2/client/client.py)   
`python client.py`