#include<iostream>

using namespace std;

bool isPalindrome(int x) {
    int i=x, n=0;
    while(i>0)
    {
        n=i%10+n*10;
        i/=10;
    }
    return n==x;
};


int main(){

    int x = 123454321;
    
    cout << "is palindrome? " << isPalindrome(x) << endl;
    
}