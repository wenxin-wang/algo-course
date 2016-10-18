#include "common.hh"
#include "insertion.hh"

namespace Shell {
    template <typename RandIter>
    void sort(const RandIter l, const RandIter r) {
        unsigned k = 2, gap = 0, n = r - l;
        do {
            k *= 2;
            gap = 2 * (n / k) + 1;
            for (unsigned i = 0; i < gap; i++) {
                Insertion::sort(l + i, r, gap);
            }
        } while (gap > 1);
    }

    template void sort<VItr>(const VItr l, const VItr r);
}
