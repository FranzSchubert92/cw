#include<iostream>
using namespace std;

bool isPowerOf(long long n, int p=8) {
    long long result = 1;
    for (int i = 1; result < n; ++i) {
        result *= p;
    }
    return n == result;
}

int main() {
    int num_tests;
    cin >> num_tests;
    while (num_tests--) {
        long long n;
        cin >> n;
        if (isPowerOf(n)) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
    return 0;
}
