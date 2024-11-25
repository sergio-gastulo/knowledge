#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> vec = {10, 20, 30};

    vec.push_back(40);      // Add an element at the end
    vec.pop_back();         // Remove the last element
    cout << "Size: " << vec.size() << endl;      // Current size
    cout << "Capacity: " << vec.capacity() << endl; // Storage capacity
    
    for (auto i = vec.begin(); i != vec.end(); ++i)
    {
        cout << *i << endl;
    }
    
    for( int v: vec){
        cout << v << endl; 
    }
    
    vec.clear();            // Remove all elements
    return 0;
}