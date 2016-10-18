#include "lib/test.hh"
#include "lib/shell.hh"

using namespace std;

int main(int argc, char** argv) {
    test(Shell::sort, argc, argv);
    return 0;
}
