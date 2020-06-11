
hubDir = ../../hub

hgwdevUrl = https://hgwdev.gi.ucsc.edu/~markd/t2t/T2T-CHM13/hub.txt
courtyardUrl = https://courtyard.gi.ucsc.edu/~markd/t2t/T2T-CHM13/hub.txt

ifeq ($(shell hostname),hgwdev)
localUrl = ${hgwdevUrl}
else
localUrl = ${courtyardUrl}
endif

assemblies = t2tChm13_20200602

srcs = $(wildcard *.html *.txt) $(foreach a,${assemblies},$(wildcard $a/*.html $a/*.txt))

all: hub

hub: ${srcs:%=${hubDir}/%}
	hubCheck ${localUrl}

${hubDir}/%: %
	@mkdir -p $(dir $@)
	cp -f $< $@

sync: hub
	@if [ "$$(hostname)" != "hgwdev" ] ; then echo "Error: sync can only be run on hgwdev" ; exit 1 ; fi
	cd ../.. && rsync -a --inplace hub courtyard.gi.ucsc.edu:/nanopore/markd/t2t-chm13/
	hubCheck ${courtyardUrl}
