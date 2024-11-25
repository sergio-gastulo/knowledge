#include <iostream>

using namespace std;

void swapper_failure(int x, int y){
    int temp = x;
    x = y;
    y = temp;
}

void swapper_shouldWork(int &a, int &b){
    int temp = a;    
    a = b;
    b = temp;
}

void swapByPointer(int* a, int* b) {
    if (a == nullptr || b == nullptr) return; // Handle invalid pointers
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int x = 5, y = 10;
    int* px = &x;
    int* py = &y;

    cout << "px: " << px << " py: " << py << endl;
    cout << "x: " << x << " y: " << y << endl;

    // swapper_failure(x,y);
    // cout << "x: " << x << " y: " << y << endl;

    swapByPointer(px, py);
    cout << "px: " << px << " py: " << py << endl;
    cout << "x: " << x << " y: " << y << endl;

    // swapper_shouldWork(x,y);
    // cout << "x: " << x << " y: " << y << endl;

    return 0;
}
