Summary: a random password generator
%define name randpw
Name: %{name}
%define version 0.0.1
%define release 1
Epoch: 8
Version: %{version}
Release: %{release}%{?dist}
License: GPL
URL: http://www.contribs.org
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}
Requires: e-smith-release >= 8.0
Buildrequires: e-smith-devtools
AutoReqProv: no

%description
a random password generator created by Hsing-Foo Wang hsingfoo@gmail.com

%changelog
* Thu Oct 07 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1-1
- Initial relase, idea from Hsing-Foo Wang hsingfoo@gmail.com

%prep
%setup
%build

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --file /usr/bin/randpw 'attr(0754,root,root)' \
$RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

