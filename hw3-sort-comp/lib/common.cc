#include <vector>
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
