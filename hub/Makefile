
hubDir = ../../hub

hgwdevUrl = https://hgwdev.gi.ucsc.edu/~markd/t2t/T2T-CHM13/hub.txt
courtyardUrl = https://courtyard.gi.ucsc.edu/~markd/t2t/T2T-CHM13/hub.txt
t2tUrl = https://t2t.gi.ucsc.edu/chm13/hub/hub.txt

ifeq ($(shell hostname),hgwdev)
localUrl = ${hgwdevUrl}
else
localUrl = ${courtyardUrl}
endif

assemblies = t2tChm13_20200602 HG002-X-v1.0 t2tChm13_20200611 t2tChm13_20200727 t2t-chm13-v1.0 GRCh38

srcs = $(wildcard *.html *.txt) $(foreach a,${assemblies},$(wildcard $a/*.txt $a/*.html $a/*/*.txt $a/*/*.html))

hgdev_udc_dir = ${TMPDIR}/${USER}_t2t_hgwdev_udc
t2t_udc_dir = ${TMPDIR}/${USER}_t2t_t2t_udc

all: hub

hub: ${srcs:%=${hubDir}/%}
	@rm -rf ${hgdev_udc_dir}
	hubCheck -udcDir=${hgdev_udc_dir} ${localUrl}

${hubDir}/%: %
	@mkdir -p $(dir $@)
	cp -f $< $@

define hgwdev_check
@if [ "$$(hostname)" != "hgwdev" ] ; then echo "Error: sync can only be run on hgwdev" ; exit 1 ; fi
endef

sync: sync-t2t

# progress = --progress
sync-t2t: ${srcs:%=${hubDir}/%}
	${hgwdev_check}
	cd ../.. && rsync -v -aH --partial ${progress} --no-owner --no-group hub t2t.gi.ucsc.edu:/data/chm13
	@rm -rf ${t2t_udc_dir}
	hubCheck -udcDir=${t2t_udc_dir} ${t2tUrl}
