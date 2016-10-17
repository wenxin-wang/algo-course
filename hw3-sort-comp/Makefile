LIBS = test.cc sorts.cc
LINK.o = $(CXX) $(LDFLAGS) $(TARGET_ARCH)

default: stl-sort insertion

stl-sort: stl-sort.cc $(LIBS)
insertion: insertion.cc $(LIBS)

.PHONY: clean install

clean:
	rm -f *.o stl-sort
