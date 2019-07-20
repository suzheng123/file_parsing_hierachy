#include <iostream>
#include "HelloWorldHelper.hpp"
using namespace std; 

int main() {
    cout << "Hello World!" << endl;
    test_message();


    int code = get_code();
    if (code >= 1) {
        for (int i = 0; i < code; i++){
            cout<< "FOR_LOOP: iter:"<<i<<endl;
        }
    }
    else{
        myPrint("ERROR");
    }
    return 0;
}