#include "lib/test.hh"
#include "lib/stl-sort.hh"

using namespace std;

int main(int argc, char** argv) {
    test(StlSort::sort, argc, argv);
    return 0;
}
