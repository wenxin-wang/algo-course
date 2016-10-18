#include <vector>
#include <cstdint>
#include <random>
#include <utility>
#include <utility>
#include "common.hh"
#include "insertion.hh"

namespace QuickSort {
    const unsigned INSERTION_THRES = 100;
    std::random_device rd;
    std::mt19937_64 generator{rd()};

    template <typename RandIter>
    RandIter select_pivot(const RandIter l, const RandIter r) {
        std::uniform_int_distribution<unsigned> dist{0, r - l - 1};
        return l + dist(generator);
    }

    template <typename RandIter>
    RandIter partition(const RandIter l, const RandIter r) {
        auto split = select_pivot(l, r);
        const auto piv = *split;
        std::swap(*l, *split);
        split = l;
        for (auto i = l + 1; i < r; i++) {
            if (*i <= piv) {
                std::swap(*i, *(++split));
            }
        } // max(split) = r - 1
        return split;
    }

    template <typename RandIter>
    void sort(const RandIter l, const RandIter r) {
        if (l == r || r - l == 1) return;
        if (r - l <= INSERTION_THRES)
            return Insertion::sort(l, r);
        auto split = partition(l, r);
        sort(l, split + 1);
        sort(split + 1, r);
    }

    template void sort<VItr>(const VItr l, const VItr r);
}
