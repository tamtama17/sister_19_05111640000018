import os
import base64

class FileServer(object):
    def __init__(self):
        pass

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def get_repl_mng_object(self):
        uri = "PYRONAME:repl_mng@localhost:7777"
        fserver = Pyro4.Proxy(uri)
        return fserver

    def list(self):
        print("list ops")
        try:
            daftarfile = []
            for x in os.listdir():
                if x[0:4]=='FFF-':
                    daftarfile.append(x[4:])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self, name, darimana):
        nama='FFF-{}' . format(name)
        print("create ops {}" . format(nama))
        try:
            if os.path.exists(name):
                return self.create_return_message('102', 'OK','File Exists')
            f = open(nama,'wb',buffering=0)
            f.close()
            if darimana=='client':
                repl_mng_server = self.get_repl_mng_object()
                repl_mng_server.replication('fileserver2','create',name,None)
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    def read(self,name):
        nama='FFF-{}' . format(name)
        print("read ops {}" . format(nama))
        try:
            f = open(nama,'r+b')
            contents = f.read().decode()
            f.close()
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')
    def update(self,name,content, darimana):
        nama='FFF-{}' . format(name)
        print("update ops {}" . format(nama))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open(nama,'w+b')
            f.write(content.encode())
            f.close()
            if darimana=='client':
                repl_mng_server = self.get_repl_mng_object()
                repl_mng_server.replication('fileserver2','update',name,content)
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name, darimana):
        nama='FFF-{}' . format(name)
        print("delete ops {}" . format(nama))

        try:
            os.remove(nama)
            if darimana=='client':
                repl_mng_server = self.get_repl_mng_object()
                repl_mng_server.replication('fileserver2','delete',name,None)
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')