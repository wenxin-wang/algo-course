CXXFLAGS = -g -O2
LIBS = lib/common.o lib/test.o
LINK.o = $(CXX) $(LDFLAGS) $(TARGET_ARCH)

default: stl-sort insertion quick-sort

stl-sort: $(LIBS)
insertion: $(LIBS)
quick-sort: $(LIBS)

.PHONY: clean install

clean:
	rm -f *.o lib/*.o stl-sort insertion quick-sort
