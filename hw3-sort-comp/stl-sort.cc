#include "test.hh"
#include <vector>
#include <cstdint>
#include <algorithm>

using namespace std;

void stl_sort(vector<uint32_t> &l) {
    sort(l.begin(), l.end());
}

int main(int argc, char** argv) {
    test(stl_sort, argc, argv);
    return 0;
}
