import cffi

class Klass(object):
    def __init__(self, number):
        self.ffi = cffi.FFI()
        self.lib = self.ffi.dlopen("./libklass.so")
        self.ffi.cdef("""
            typedef struct _Klass Klass;
            Klass* Klass_New(int n);
            void Klass_Delete(Klass* klass);
            void Klass_SayHello(Klass* klass);
            int Klass_Square(Klass* klass, int n);
        """)

        self.obj = self.lib.Klass_New(number)

    def __del__(self):
        self.lib.Klass_Delete(self.obj)

    def SayHello(self):
        self.lib.Klass_SayHello(self.obj)

    def Square(self, num):
        return self.lib.Klass_Square(self.obj, num)
