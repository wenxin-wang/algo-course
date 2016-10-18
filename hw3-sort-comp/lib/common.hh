#ifndef COMMON_H
#define COMMON_H

#include <vector>
#include <iostream>

typedef std::vector<uint32_t> Vect;
typedef std::vector<uint32_t>::iterator VItr;
template < class T >
inline std::ostream& operator << (std::ostream& os, const std::vector<T>& v)
{
    for (auto ii = v.begin(); ii != v.end(); ii++)
    {
        os << *ii << std::endl;
    }
    return os;
}

#endif /* COMMON_H */
