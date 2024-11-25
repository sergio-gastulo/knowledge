#include <iostream>
using namespace std;

void modifyByPointer(int* ptr) {
    *ptr = 20; // Change the value at the memory address
}

void modifyByReference(int& ref) {
    ref = 30; // Change the original value directly
}

int main() {
    
    int num = 10;
    cout << "Initial value: " << num << endl;
    cout << "Memmory addess of num: " << &num << endl;

    // Using a pointer
    modifyByPointer(&num); // Pass the address of num
    cout << "After modifyByPointer: " << num << endl;
    cout << "Memmory addess of num: " << &num << endl;

    // Using a reference
    modifyByReference(num); // Pass num directly
    cout << "After modifyByReference: " << num << endl;
    cout << "Memmory addess of num: " << &num << endl;

    return 0;
}
