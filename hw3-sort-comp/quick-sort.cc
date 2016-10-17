#include "lib/test.hh"
#include "lib/quick-sort.hh"

int main(int argc, char** argv) {
    test(QuickSort::sort, argc, argv);
    return 0;
}
