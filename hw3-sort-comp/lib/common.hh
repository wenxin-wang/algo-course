#ifndef COMMON_H
#define COMMON_H

#include <vector>
#include <iostream>

typedef std::vector<uint32_t>::iterator VItr;
template < class T >
inline std::ostream& operator << (std::ostream& os, const std::vector<T>& v);

#endif /* COMMON_H */
