#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(){

    cout << "Find size of fundamental datatypes" << endl;
    cout << "----------------------------------" << endl;
    cout << "the size of char is "<< sizeof(char) << " bytes." << endl;
    cout << "the size of short is "<< sizeof(short) << " bytes." << endl;
    cout << "the size of int is "<< sizeof(int) << " bytes." << endl;
    cout << "the size of long is "<< sizeof(long) << " bytes." << endl;
    cout << "the size of long long is "<< sizeof(long long ) << " bytes." << endl;
    cout << "the size of float is "<< sizeof(float) << " bytes." << endl;
    cout << "the size of double is "<< sizeof(double) << " bytes." << endl;
    cout << "the size of long double is "<< sizeof(long double ) << " bytes." << endl;
    cout << "the size of bool is "<< sizeof(bool) << " bytes." << endl;

    return 0;
}