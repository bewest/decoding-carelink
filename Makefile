TESTS = $(wildcard decocare/*.py decocare/*/*.py)
test:
	python -m doctest -v ${TESTS}

install:
	python setup.py develop
	install 80-medtronic-carelink.rules /etc/udev/rules.d/
	udevadm control --reload-rules

docs:
	(cd docs; make)
travis: test
	# do the travis dance

.PHONY: test docs
