build:
	rpmdev-setuptree 
	cp python-devutils.spec SPECS
	rpmbuild -v -ba SPECS/python-devutils.spec
