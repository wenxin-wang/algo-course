#ifndef INSERTION_H
#define INSERTION_H

#include <iterator>
#include <utility>

namespace Insertion {
    template <typename RandIter>
    inline void sort(const RandIter l, const RandIter r) {
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
}

#endif /* INSERTION_H */
