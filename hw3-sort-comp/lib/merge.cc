#include <vector>
#include <iostream>
#include "common.hh"

namespace Merge {
    template <typename RandIter, typename BuffIter>
    void sort(const RandIter l, const RandIter r, const BuffIter bi) {
        if (r - l <= 1) return;
        const auto split = l + (r - l) / 2;
        Merge::sort(l, split, bi);
        Merge::sort(split, r, bi + (r - l) / 2);
        auto i = l, j = split, k = bi;
        while (i != split && j != r) {
            if (*i <= *j) *(k++) = *(i++);
            else *(k++) = *(j++);
        }
        // Either one or none of the following should happen
        std::copy(j, r, std::copy(i, split, k));
        std::copy(bi, bi + (r - l), l);
    }

    template <typename RandIter>
    void sort(const RandIter l, const RandIter r) {
        if (r - l <= 1) return;
        typename std::vector<typename RandIter::value_type> buff;
        buff.reserve(r - l);
        Merge::sort(l, r, buff.begin());
        std::copy(buff.begin(), buff.end(), l);
    }

    template void sort<VItr>(const VItr l, const VItr r);
}
