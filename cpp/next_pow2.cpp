/**
Smallest power of 2 greater than or equal to n

Given a number N, Write a program to find a number which is greater than or 
equal to N and is a smallest power of 2.

Input:
First line of input contains a single integer T which denotes the number of 
test cases. Then T test cases follows. First line of each test case contains 
a single integer N.

Output:
For each test case, print a number which is greater than or equal to N and is 
a nearest power of 2.

Constraints:
1<=T<=100
1<=N<=100000

Example:
Input:
4
5
1
17
32
Output:
8
1
32
32

**For More Examples Use Expected Output**

**/

#include<iostream>
using namespace std;

int nextPow2(int n) {
    int r = 1;
    while (r < n) {
        r = r << 1;
    }
    return r; 
}

int main() {
    int num_tests;
    cin >> num_tests;
    while (num_tests--) {
        int num;
        cin >> num;
        cout << nextPow2(num) << endl;
    }
    return 0;
}
