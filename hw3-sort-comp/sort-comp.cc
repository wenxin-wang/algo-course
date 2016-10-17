#include <iostream>
#include "stl-sort.hh"
using namespace std;

template < class T >
inline std::ostream& operator << (std::ostream& os, const std::vector<T>& v)
{
    os << "[";
    for (auto ii = v.begin(); ii != v.end(); ii++)
    {
        os << " " << *ii;
    }
    os << " ]";
    return os;
}

int main() {
    vector<int32_t> v = {3, 65, 12, 123};
    stl_sort(v);
    cout << v << endl;
    return 0;
}
