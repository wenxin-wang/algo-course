#include <algorithm>
#include "common.hh"

namespace StlSort {
    template <class RandIter>
    void sort(RandIter l, RandIter r){
        std::sort(l, r);
    }

    template void sort<VItr>(const VItr l, const VItr r);
}
