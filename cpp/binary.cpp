#include<iostream>
using namespace std;

void binary(int n) {
    int rem;
    if (n < 2) {
        cout << n;
        return;
    }
    rem = n % 2;
    binary(n / 2);
    cout << rem;
}

int main() {
    int num_tests;
    cin >> num_tests;
    while (num_tests--) {
        int d;
        cin >> d;
        binary(d);
        cout << endl;
    }
    return 0;
}
