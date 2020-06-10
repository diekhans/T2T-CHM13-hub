
hubDir = ../../hub

hgwdevUrl = https://hgwdev.gi.ucsc.edu/~markd/t2t/T2T-CHM13/hub.txt

assemblies = t2tChm13_20200602

srcs = $(wildcard *.html *.txt) $(foreach a,${assemblies},$(wildcard $a/*.html $a/*.txt))

all: hub

hub: ${srcs:%=${hubDir}/%}
	hubCheck ${hgwdevUrl}

${hubDir}/%: %
	@mkdir -p $(dir $@)
	cp -f $< $@

sync: hub
	@if [ "$$(hostname)" != "hgwdev" ] ; then echo "Error: sync can only be run on hgwdev" ; exit 1 ; fi
	cd ../.. && rsync -a hub courtyard.gi.ucsc.edu:/nanopore/markd/t2t-chm13/
