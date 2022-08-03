
hubDir = ../../../hubs/dev

hgwdevUrl = https://hgwdev.gi.ucsc.edu/~markd/t2t/dev/hub.txt
t2tUrl = https://t2t.gi.ucsc.edu/chm13/dev/hub.txt

localUrl = ${hgwdevUrl}

assemblies = HG002-X-v1.0 t2t-chm13-v1.0 t2t-chm13-v1.1 t2t-chm13-v2.0 GRCh38 hg38
# t2tChm13_20200727
# t2tChm13_20200602 t2tChm13_20200611


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

sync: sync-t2t

# sync both dev
sync-t2t: ${srcs:%=${hubDir}/%}
	${hgwdev_check}
	cd ../../../hubs && rsync -v -aH --partial --no-owner --no-group dev t2t.gi.ucsc.edu:/data/chm13/
	@rm -rf ${t2t_udc_dir}
	hubCheck -udcDir=${t2t_udc_dir} ${t2tUrl}
