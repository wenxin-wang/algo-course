#ifndef SORTS_H
#define SORTS_H

#include <vector>
#include <cstdint>

namespace StlSort {
    void sort(std::vector<uint32_t> &l);
}

namespace Insertion {
    void sort(std::vector<uint32_t> &l);
}

namespace QuickSort {
    void sort(std::vector<uint32_t> &l);
}

#endif /* SORTS_H */
