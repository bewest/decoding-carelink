TESTS = $(wildcard decocare/*.py decocare/*/*.py)
test:
	python -m doctest -v ${TESTS}

install:
	python setup.py develop
	install decocare/etc/80-medtronic-carelink.rules /etc/udev/rules.d/
	udevadm control --reload-rules

ci-install:
	sudo python setup.py develop

docs:
	(cd doc; make)
travis: test
	# do the travis dance

.PHONY: test docs
