#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x96B047156338B6D4 (psmith@gnu.org)
#
Name     : make
Version  : 4.2.1
Release  : 27
URL      : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz
Source0  : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz
Source99 : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.0
Requires: make-bin
Requires: make-doc
Requires: make-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : guile
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: skip-tests-features-archive.patch
Patch2: 0002-Fix_tests.patch
Patch3: configure.ac-Support-GLIBC-glob-interface-version-2.patch

%description
This directory contains the 4.2.1 release of GNU Make.
See the file NEWS for the user-visible changes from previous releases.
In addition, there have been bugs fixed.

%package bin
Summary: bin components for the make package.
Group: Binaries

%description bin
bin components for the make package.


%package dev
Summary: dev components for the make package.
Group: Development
Requires: make-bin
Provides: make-devel

%description dev
dev components for the make package.


%package doc
Summary: doc components for the make package.
Group: Documentation

%description doc
doc components for the make package.


%package locales
Summary: locales components for the make package.
Group: Default

%description locales
locales components for the make package.


%prep
%setup -q -n make-4.2.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519084398
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1519084398
rm -rf %{buildroot}
%make_install
%find_lang make

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/make

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files locales -f make.lang
%defattr(-,root,root,-)

