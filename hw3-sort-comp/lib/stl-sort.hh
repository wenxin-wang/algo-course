#ifndef STL_SORT_H
#define STL_SORT_H

#include <algorithm>

namespace StlSort {
    template <class RandIter>
    void sort(RandIter l, RandIter r){
        std::sort(l, r);
    }
}

#endif /* STL_SORT_H */
