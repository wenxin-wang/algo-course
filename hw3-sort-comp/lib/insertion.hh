#ifndef INSERTION_H
#define INSERTION_H

namespace Insertion {
    template <typename RandIter>
    void sort(const RandIter l, const RandIter r);

    template <typename RandIter>
    void sort(const RandIter l, const RandIter r, const unsigned gap);
}

#endif /* INSERTION_H */
