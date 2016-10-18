#include <vector>
#include <iostream>
#include "common.hh"
#include "insertion.hh"

namespace Merge {
    const unsigned INSERTION_THRES = 100;

    template <typename RandIter, typename BuffIter>
    void merge(RandIter l, const RandIter split, const RandIter r, BuffIter bi) {
        auto k = split;
        while (l != split && k != r) {
            if (*l <= *k) *(bi++) = *(l++);
            else *(bi++) = *(k++);
        }
        std::copy(k, r, std::copy(l, split, bi));
    }

    template <typename RandIter>
    void sort(const RandIter l, const RandIter r) {
        if (r - l <= 1) return;
        typename std::vector<typename RandIter::value_type> buff;
        unsigned n = r - l;
        buff.reserve(n);
        for (unsigned i = 0; i < n; i += INSERTION_THRES) {
            Insertion::sort(l + i, std::min(r, l + i + INSERTION_THRES));
        }
        auto a = l, b = buff.begin();
        for (unsigned width = INSERTION_THRES; width < n; width *= 2) {
            for (unsigned i = 0; i < n; i += 2*width) {
                merge(a + i, std::min(a + n, a + i + width), std::min(a + n, a + i + 2*width), b + i);
            }
            std::swap(a, b);
        }
        if (b == l) std::copy(a, a+n, l);
    }

    template void sort<VItr>(const VItr l, const VItr r);
}
