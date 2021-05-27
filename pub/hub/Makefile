
hubDir = ../../hub

hgwdevUrl = https://hgwdev.gi.ucsc.edu/~markd/t2t/hub/hub.txt
t2tUrl = https://t2t.gi.ucsc.edu/chm13/hub/hub.txt

localUrl = ${hgwdevUrl}

assemblies =  GRCh38

srcs = $(wildcard *.html *.txt) $(foreach a,${assemblies},$(wildcard $a/*.txt $a/*.html $a/*/*.txt $a/*/*.html $a/*.html $a/*/*/*.txt $a/*/*/*.html))

hgdev_udc_dir = ${TMPDIR}/${USER}_t2t_hgwdev_udc
t2t_udc_dir = ${TMPDIR}/${USER}_t2t_t2t_udc

all: hub

hub: ${srcs:%=${hubDir}/%}
	@rm -rf ${hgdev_udc_dir}
	${MAKE} hubCheckAll

hubCheckAll: ${assemblies:%=hubCheck_%}

hubCheck_%:
	hubCheck -genome=$* -udcDir=${hgdev_udc_dir} ${localUrl}

${hubDir}/%: %
	@mkdir -p $(dir $@)
	cp -f $< $@

define hgwdev_check
@if [ "$$(hostname)" != "hgwdev" ] ; then echo "Error: sync can only be run on hgwdev" ; exit 1 ; fi
endef

sync:
	@echo NOT READY TO SYNC >&2
	exit 1


#sync-t2t

# progress = --progress
sync-t2t: ${srcs:%=${hubDir}/%}
	${hgwdev_check}
	cd ../.. && rsync -v -aH --partial ${progress} --no-owner --no-group hub t2t.gi.ucsc.edu:/data/chm13
	@rm -rf ${t2t_udc_dir}
	hubCheck -udcDir=${t2t_udc_dir} ${t2tUrl}
