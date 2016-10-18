#include "common.hh"

namespace Insertion {
    template <typename RandIter>
    void sort(const RandIter l, const RandIter r, const unsigned gap) {
        for (auto i = l + gap; i < r; i += gap) {
            for (auto j = i; j > l; j -= gap) {
                auto t = j - gap;
                if (*t > *j) {
                    std::swap(*j, *t);
                }
                else break;
            }
        }
    }

    template <typename RandIter>
    void sort(const RandIter l, const RandIter r) {
        sort(l, r, 1);
    }

    template void sort<VItr>(const VItr l, const VItr r);
    template void sort<VItr>(const VItr l, const VItr r, const unsigned gap);
}
