#ifndef RADIX_H
#define RADIX_H

#include "common.hh"

namespace Radix {
    namespace lsbf {
        void sort(const VItr l, const VItr r);
    }
    namespace msbf {
        void sort(const VItr l, const VItr r);
    }
}

#endif /* RADIX_H */
