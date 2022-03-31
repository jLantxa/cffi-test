#ifndef _KLASS_HPP_
#define _KLASS_HPP_

#include <iostream>

class Klass {
public:
    Klass(int number);
    void SayHello() const;
    int Square(int n) const;

private:
    int m_number;
};

#endif  // _KLASS_HPP_
