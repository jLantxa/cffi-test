#include "klass.hpp"

extern "C" {

Klass* Klass_New(int n) {
    return new Klass(n);
}

void Klass_Delete(Klass* klass) {
    delete klass;
}

void Klass_SayHello(Klass* klass) {
    klass->SayHello();
}
int Klass_Square(Klass* klass, int n) {
    return klass->Square(n);
}

}  // extern "C"
