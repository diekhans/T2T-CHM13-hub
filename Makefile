root = .
include ${root}/defs.mk


pyprogs = $(shell file -F $$'\t' bin/* | awk '/Python script/{print $$1}')

lint:
	${FLAKE8} --exclude=bin/RM2Bed.py ${pyprogs}

clean:
	rm -rf ${binDir}/__pycache__
