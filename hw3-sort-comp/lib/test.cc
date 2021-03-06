#include "common.hh"
#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <cstdlib>
#include <ctime>
#include <random>

using namespace std;

void usage(char **argv) {
    cerr << argv[0] << "N [input] [output]"<< endl;
    cerr << "N: size of uint32 list to be sorted"<< endl;
    cerr << "input: list of uint32, one in each line. If no input, generate numbers randomly"<< endl;
    cerr << "output: sorted list of uint32, one in each line"<< endl;
}

void gen_numbers(vector<uint32_t> &v, long int N) {
    random_device rd;
    mt19937_64 generator{rd()};
    std::uniform_int_distribution<unsigned> dist;
    for (unsigned i = 0; i < N; i++)
        v.push_back(dist(generator));
}

int read_file(vector<uint32_t> &v, char *name, long int N) {
    int i = 0;
    string line;
    ifstream in(name);
    if (in.is_open()) {
        while (i < N && getline(in, line)) {
            v.push_back(stol(line));
            i++;
        }
    }
    else {
        cerr << "Unable to open input file: " << name << endl;
        return 1;
    }

    if (i < N) {
        cerr << "The size of input file " << name << " is smaller than " << N << endl;
        return 1;
    }

    return 0;
}

int write_file(vector<uint32_t> &v, char *name) {
    string line;
    ofstream out(name);
    if (out.is_open()) {
        for (auto it = v.begin(); it != v.end(); it++)
            out << *it << endl;
    }
    else {
        cerr << "Unable to open output file: " << name << endl;
        return 1;
    }
    return 0;
}

void test(void (*f)(VItr l, VItr r), int argc, char** argv) {
    if (argc < 2) {
        cerr << "N is needed" << endl;
        usage(argv);
        exit(1);
    }
    long int N = strtol(argv[1], NULL, 10);
    vector<uint32_t> v;
    v.reserve(N);
    if (argc >= 3) {
        if (read_file(v, argv[2], N)) {
            usage(argv);
            exit(1);
        }
    }
    else
        gen_numbers(v, N);
    clock_t start = clock();
    f(v.begin(), v.end());
    clock_t end = clock();
    cout << end - start << endl;
    if (argc > 3) {
        if (write_file(v, argv[3])) {
            usage(argv);
            exit(1);
        }
    }
}
