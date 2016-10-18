CXXFLAGS = -g -O2
src = stl-sort.cc insertion.cc quick-sort.cc merge-sort.cc lib/stl-sort.cc lib/insertion.cc lib/quick-sort.cc lib/merge.cc lib/common.cc lib/test.cc
LIBS = lib/common.o lib/test.o
LINK.o = $(CXX) $(LDFLAGS) $(TARGET_ARCH)

default: stl-sort insertion quick-sort merge-sort

stl-sort: lib/stl-sort.o $(LIBS)
insertion: lib/insertion.o $(LIBS)
quick-sort: lib/quick-sort.o lib/insertion.o $(LIBS)
merge-sort: lib/merge.o lib/insertion.o $(LIBS)

.PHONY: clean install

clean:
	rm -f *.d *.o lib/*.o lib/*.d stl-sort insertion quick-sort

include $(subst .cc,.d,$(src))

%.d: %.cc
	$(CXX) -M $(CXXFLAGS) $< > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$
