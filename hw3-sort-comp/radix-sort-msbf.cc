#include "lib/test.hh"
#include "lib/radix.hh"

using namespace std;

int main(int argc, char** argv) {
    test(Radix::msbf::sort, argc, argv);
    return 0;
}
