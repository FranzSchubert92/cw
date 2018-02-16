#include <iostream>
#include <vector>

template <class T>
class Factorial {
  public: 
    static T recursive(T n) {
        return n == 1 ? 1 : n * recursive(n-1);
    }
};


auto main() -> int {
    
    std::vector<long> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20};
    for (auto n: v) {
        auto f = Factorial<long>::recursive(n);
        std::cout << n << "\t" << f << "\n";
    }

}
