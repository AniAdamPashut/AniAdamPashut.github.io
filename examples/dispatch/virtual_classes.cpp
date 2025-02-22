class A {
public:
    int moshiko;
    virtual int a() = 0;
};

class B {
public:
    virtual int b() = 0;
};

class Child : public A, B {
int bigger;
public:
    Child() {
    }

    int a() override {
        return 1;
    }

    int b() override {
        return 2;
    }
};

#include <iostream>

int main() {
    Child* c = new Child();
    c->a();
    c->b();
    int x = c->moshiko;
    std::cout << x;
}