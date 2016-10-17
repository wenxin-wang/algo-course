#include <vector>
#include <cstdint>
#include <algorithm>

namespace StlSort {
    using namespace std;

    void sort(vector<uint32_t> &l) {
        sort(l.begin(), l.end());
    }
}

namespace Insertion {
    using namespace std;

    void sort(vector<uint32_t> &l) {
        unsigned n = l.size();
        for (unsigned i = 1; i < n; i++) {
            for (unsigned j = i; j > 0; j--) {
                if (l[j-1] > l[j]) {
                    auto t = l[j];
                    l[j] = l[j-1];
                    l[j-1] = t;
                }
                else break;
            }
        }
    }
}
