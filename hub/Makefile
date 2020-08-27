
hubDir = ../../hub

hgwdevUrl = https://hgwdev.gi.ucsc.edu/~markd/t2t/T2T-CHM13/hub.txt
courtyardUrl = https://courtyard.gi.ucsc.edu/~markd/t2t/T2T-CHM13/hub.txt
t2tUrl = http://t2t.gi.ucsc.edu/chm13/hub/hub.txt

ifeq ($(shell hostname),hgwdev)
localUrl = ${hgwdevUrl}
else
localUrl = ${courtyardUrl}
endif

assemblies = t2tChm13_20200602 t2tChm13_20200611 t2tChm13_20200727

srcs = $(wildcard *.html *.txt) $(foreach a,${assemblies},$(wildcard $a/*.html $a/*.txt))

all: hub

hub: ${srcs:%=${hubDir}/%}
	hubCheck ${localUrl}

${hubDir}/%: %
	@mkdir -p $(dir $@)
	cp -f $< $@

define hgwdev_check
@if [ "$$(hostname)" != "hgwdev" ] ; then echo "Error: sync can only be run on hgwdev" ; exit 1 ; fi
endef

sync: sync-t2t

# progress = --progress
sync-courtyard:
	${hgwdev_check}
	cd ../.. && rsync -aH --partial ${progress} hub courtyard.gi.ucsc.edu:/nanopore/markd/t2t-chm13/
	hubCheck ${courtyardUrl}

sync-t2t:
	${hgwdev_check}
	cd ../.. && rsync -aH --partial ${progress} --no-owner --no-group hub t2t.gi.ucsc.edu:/data/chm13
	hubCheck ${t2tUrl}
