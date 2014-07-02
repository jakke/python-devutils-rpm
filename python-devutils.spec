Name: python-devutils          
Version: eta1        
Release:        1%{?dist}
Summary: virtual + dev tools       

Group: Applications/Development          
License: GPL
URL:http://wms.cc.kuleuven.be/            
Source: %{name}-%{version}.tar.gz
NoSource: 0

BuildRequires:zlib-devel, gcc
BuildRequires:python27-python-devel
BuildRequires:python27-python-libs
BuildRequires:zlib-devel, gcc
AutoReqProv: no

%define installdir /opt/python27_tools_virtualenv
%define toolsdir /opt/python27_tools
%define python /opt/rh/python27/root/usr/bin/python
%define virtualenv /opt/rh/python27/root/usr/bin/virtualenv
%define builddir $RPM_BUILD_ROOT%{installdir}

%description

%build
echo "-----------------------"
echo $RPM_BUILD_ROOT
echo "-----------------------"
rm -rf $RPM_BUILD_ROOT
mkdir -p %{builddir}
cd %{builddir}

source /opt/rh/python27/enable
%{virtualenv} .
bin/easy_install setuptools==2.1
bin/easy_install zest.releaser==3.49
bin/easy_install pep8
bin/easy_install pyflakes
bin/easy_install cheetah
bin/easy_install zopeskel
%{virtualenv} --relocatable .
mkdir $RPM_BUILD_ROOT/%{toolsdir}

%post
#enabeling python2.7 & dev tools for non root user
#grep -q "/opt/rh/python27/enable" /etc/profile; rc=$?
#if [ $rc -ne 0 ]; then
if [ ! -f /etc/profile.d/py27.sh ]; then
cat << EOF >> /etc/profile.d/py27.sh
if [ \$(id -u) -ne 0 ]; then
        export PATH="/opt/python27_tools/:$PATH" 
        source /opt/rh/python27/enable
fi
EOF
fi

%install
# reconsider the symlink folder to put in the path
# maybe the virtualenv folder can be put into the path, if the order of the 
# python 2.7 enable and virtualenv insertion in the path is right
#cd $RPM_BUILD_ROOT%{toolsdir}
ln -sf %{installdir}/bin/fullrelease $RPM_BUILD_ROOT/%{toolsdir}/fullrelease
ln -sf %{installdir}/bin/longtest $RPM_BUILD_ROOT/%{toolsdir}/longtest
ln -sf %{installdir}/bin/paster $RPM_BUILD_ROOT/%{toolsdir}/paster
ln -sf %{installdir}/bin/pep8 $RPM_BUILD_ROOT/%{toolsdir}/pep8
ln -sf %{installdir}/bin/postrelease $RPM_BUILD_ROOT/%{toolsdir}/postrelease
ln -sf %{installdir}/bin/prerelease $RPM_BUILD_ROOT/%{toolsdir}/prerelease
ln -sf %{installdir}/bin/pyflakes $RPM_BUILD_ROOT/%{toolsdir}/pyflakes
ln -sf %{installdir}/bin/release $RPM_BUILD_ROOT/%{toolsdir}/release
ln -sf %{installdir}/bin/templer $RPM_BUILD_ROOT/%{toolsdir}/templer
ln -sf %{installdir}/bin/zopeskel $RPM_BUILD_ROOT/%{toolsdir}/zopeskel

%check

%clean
rm -rf $RPM_BUILD_ROOT%{installdir}


%files
%defattr(-, plone, plone, 0755)
/opt/python27_tools_virtualenv
/opt/python27_tools


%changelog
