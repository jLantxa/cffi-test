#include "klass.hpp"

Klass::Klass(int n) : m_number(n) {
}

void Klass::SayHello() const {
    printf("Hello! This is %d\n", m_number);
}

int Klass::Square(int n) const {
    return n*n;
}
