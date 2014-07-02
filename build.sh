#!/bin/bash

mkdir -p BUILD RPMS SRPMS BUILDROOT
#rpmbuild -ba --define="_topdir $PWD" python-devutils.spec
rpmbuild -v -bb --define "_topdir $(pwd)" --buildroot $(pwd)/BUILDROOT python-devutils.spec
