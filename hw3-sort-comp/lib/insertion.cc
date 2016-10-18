#include <iterator>
#include <utility>
#include "common.hh"

namespace Insertion {
    template <typename RandIter>
    void sort(const RandIter l, const RandIter r) {
        for (auto i = l + 1; i != r; i++) {
            for (auto j = i; j != l; j--) {
                auto t = j-1;
                if (*t > *j) {
                    std::swap(*j, *t);
                }
                else break;
            }
        }
    }

    template void sort<VItr>(const VItr l, const VItr r);
}
