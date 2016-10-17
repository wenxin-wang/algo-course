#include <vector>
#include <cstdint>
#include <algorithm>
#include <random>
#include <iostream>

template < class T >
inline std::ostream& operator << (std::ostream& os, const std::vector<T>& v)
{
    for (auto ii = v.begin(); ii != v.end(); ii++)
    {
        os << *ii << std::endl;
    }
    return os;
}

namespace StlSort {
    void sort(std::vector<uint32_t> &v) {
        std::sort(v.begin(), v.end());
    }
}

namespace Insertion {
    void sort(std::vector<uint32_t> &v) {
        unsigned n = v.size();
        for (unsigned i = 1; i < n; i++) {
            for (unsigned j = i; j > 0; j--) {
                if (v[j-1] > v[j]) {
                    auto t = v[j];
                    v[j] = v[j-1];
                    v[j-1] = t;
                }
                else break;
            }
        }
    }
}

namespace QuickSort {
    std::random_device rd;
    std::mt19937_64 generator{rd()};

    unsigned select_pivot(const unsigned l, const unsigned r) {
        std::uniform_int_distribution<unsigned> dist{l, r};
        return dist(generator);
    }

    void swap(std::vector<uint32_t> &v, const unsigned i, const unsigned j) {
        if (i == j) return;
        auto t = v[i];
        v[i] = v[j];
        v[j] = t;
    }

    unsigned partition(std::vector<uint32_t> &v, const unsigned l, const unsigned r) {
        unsigned split = select_pivot(l, r);
        const auto piv = v[split];
        swap(v, l, split);
        split = l;
        for (unsigned i = l + 1; i <= r; i++) {
            if (v[i] <= piv) {
                swap(v, ++split, i);
            }
        }
        return split;
    }

    void sort(std::vector<uint32_t> &v, const unsigned l, const unsigned r) {
        if (l >= r) return;
        if (r - l == 1) {
            if (v[r] < v[l]) swap(v, l, r);
            return;
        }
        auto split = partition(v, l, r);
        sort(v, l, split);
        sort(v, split + 1, r);
    }

    void sort(std::vector<uint32_t> &v) {
        unsigned n = v.size();
        if (n < 2) return;
        sort(v, 0, n - 1);
    }
}
