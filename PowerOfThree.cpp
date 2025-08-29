#include <iostream>
using namespace std;
class solution {
    public:
    bool isPowerOfThree (int n){
        if ( n <= 0) return false;
        while ( n % 3 ==0){
            n/= 3;
        }
        return n ==1;
    }


};
int main() {
    solution obj;  // create object of Solution class

    int n = 27;   // test value
    bool result = obj.isPowerOfThree(n);

    cout << n << " is power of 3? " << (result ? "true" : "false") << endl;

    return 0;
}