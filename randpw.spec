Summary: a random password generator
%define name randpw
Name: %{name}
%define version 0.1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
URL: http://www.contribs.org
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}
AutoReqProv: no
Requires: openssl
%description
a random password generator created by Hsing-Foo Wang hsingfoo@gmail.com

%changelog
* Sat Jul 25 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.0-1
- openssl is now used to generate the password
- You must give an argument greater or equal than 8

* Wed Oct 08 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3-1
- new options added to prevent No argument, a negative number,
- zero and non integer argument or a no integer argument part
- -1 0 123abc and abc by Hsing-Foo Wang hsingfoo@gmail.com

* Tue Oct 07 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1-1
- Initial relase, idea from Hsing-Foo Wang hsingfoo@gmail.com

%prep
%setup
%build

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
echo "%doc COPYING" >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun
%post
%postun

%files
%defattr(-,root,root)
%attr(754, root,root) /usr/bin/randpw

