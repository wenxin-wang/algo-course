#include <vector>
#include <cstdint>
#include <random>

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
