CXXFLAGS = -g -O2
src = stl-sort.cc insertion.cc quick-sort.cc merge-sort.cc shell-sort.cc radix-sort.cc radix-sort-msbf.cc lib/stl-sort.cc lib/insertion.cc lib/quick-sort.cc lib/merge.cc lib/shell.cc lib/radix.cc lib/test.cc
LIBS = lib/test.o
LINK.o = $(CXX) $(LDFLAGS) $(TARGET_ARCH)

BINS = stl-sort insertion quick-sort merge-sort shell-sort radix-sort radix-sort-msbf
default: $(BINS)

stl-sort: lib/stl-sort.o $(LIBS)
insertion: lib/insertion.o $(LIBS)
quick-sort: lib/quick-sort.o lib/insertion.o $(LIBS)
merge-sort: lib/merge.o lib/insertion.o $(LIBS)
shell-sort: lib/shell.o lib/insertion.o $(LIBS)
radix-sort: lib/radix.o $(LIBS)
radix-sort-msbf: lib/radix.o $(LIBS)

.PHONY: clean install

clean:
	rm -f *.d *.o lib/*.o lib/*.d $(BINS)

include $(subst .cc,.d,$(src))

%.d: %.cc
	$(CXX) -M $(CXXFLAGS) $< > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$
