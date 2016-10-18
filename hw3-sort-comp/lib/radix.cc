#include "common.hh"
#include "insertion.hh"
#include <cmath>
#include <iostream>

namespace Radix {
    const unsigned INT_BITS = 32;
    const unsigned SMALL_BITS = 10;

    typedef unsigned (*CKEY)(uint32_t x, const unsigned i, const unsigned bits);

    void sortc(const VItr l, const VItr r, const VItr b, CKEY ckey, const unsigned bi, const unsigned bits, Vect& c) {
        if (r - l <= 1) {
            std::copy(l, r, b);
            return;
        }
        std::fill(c.begin(), c.end(), 0);
        for (auto i = l; i < r; i++) {
            c[ckey(*i, bi, bits)] += 1;
        }
        const unsigned len = c.size();
        for (unsigned i = 1; i < len; i++) {
            c[i] += c[i-1];
        }
        for (auto i = r; i > l; i--) {
            auto t = *(i - 1);
            *(b + (--c[ckey(t, bi, bits)])) = t;
        }
    }

    unsigned get_bits(unsigned n) {
        unsigned t = std::log2(n);
        return t < SMALL_BITS ? SMALL_BITS : t;
    }

    namespace lsbf {
        inline unsigned ckey(uint32_t x, const unsigned i, const unsigned bits) {
            unsigned s = (i+1) * bits;
            auto t = (x << (INT_BITS > s ? INT_BITS - s : 0)) >> (INT_BITS > s ? INT_BITS - bits : i * bits);
            return t;
        }

        void sort(const VItr l, const VItr r) {
            const unsigned n = r - l;
            if (n <= 1) return;
            const unsigned bits = get_bits(n);
            Vect buff(n), c(1 << bits);
            auto a = l, b = buff.begin();
            for (unsigned i = 0; i * bits < INT_BITS; i++) {
                sortc(a, a + n, b, ckey, i, bits, c);
                swap(a, b);
            }
            if (b == l) std::copy(a, a + n, l);
        }
    }

    // MSB First really is not a good idea
    // Counting sort performs better with larger batch of numbers
    // MSB First split one sort per run into multiple ones
    namespace msbf {
        inline unsigned ckey(uint32_t x, const unsigned i, const unsigned bits) {
            unsigned s = (i+1) * bits;
            auto t = (x << i * bits) >> (INT_BITS > s ? INT_BITS - bits : i * bits);
            return t;
        }

        inline unsigned get_prefix(uint32_t x, const unsigned i, const unsigned bits) {
            return x >> (INT_BITS - i * bits);
        }

        void sort(const VItr l, const VItr r) {
            const unsigned n = r - l;
            if (n <= 1) return;
            const unsigned bits = get_bits(n);
            Vect buff(n), c(1 << bits);
            auto a = l, b = buff.begin();
            sortc(a, a + n, b, ckey, 0, bits, c);
            swap(a, b);
            for (unsigned i = 1; i * bits < INT_BITS; i++) {
                auto pl = a, pr = a + 1;
                unsigned prefix = get_prefix(*pl, i, bits);
                for (; pr < a + n; pr++) {
                    unsigned tprefix = get_prefix(*pr, i, bits);
                    if (tprefix != prefix) {
                        sortc(pl, pr, b + (pl - a), ckey, i, bits, c);
                        prefix = tprefix;
                        pl = pr;
                    }
                }
                sortc(pl, pr, b + (pl - a), ckey, i, bits, c);
                swap(a, b);
            }
            if (b == l) std::copy(a, a + n, l);
        }
    }
}
