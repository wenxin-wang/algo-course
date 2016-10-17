src = sort-comp.cc stl-sort.cc
LINK.o = $(CXX) $(LDFLAGS) $(TARGET_ARCH)

default: sort-comp

sort-comp: $(subst .cc,.o,$(src))

.PHONY: clean install

clean:
	rm -f *.o *.d sort-comp

include $(subst .cc,.d,$(src))

%.d: %.cc
	$(CXX) -M $(CXXFLAGS) $< > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$
