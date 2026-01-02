#include <vector>
#include <iostream>
#include <cstdlib>

int main(int argc, char** argv) {
    long n = atol(argv[1]);
    std::vector<long> data(n, 1);

    long sum = 0;
    for (long i = 0; i < n; i++) {
        sum += data[i];
    }

    std::cout << sum << std::endl;
}
