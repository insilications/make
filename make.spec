#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x96B047156338B6D4 (psmith@gnu.org)
#
Name     : make
Version  : 4.2.1
Release  : 34
URL      : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz
Source0  : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz
Source99 : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.0
Requires: make-bin = %{version}-%{release}
Requires: make-license = %{version}-%{release}
Requires: make-locales = %{version}-%{release}
Requires: make-man = %{version}-%{release}
Requires: make-doc
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
Patch3: glob-Do-not-assume-glibc-glob-internals.patch
Patch4: configure.ac-Support-GLIBC-glob-interface-version-2.patch

%description
This directory contains the 4.2.1 release of GNU Make.
See the file NEWS for the user-visible changes from previous releases.
In addition, there have been bugs fixed.

%package bin
Summary: bin components for the make package.
Group: Binaries
Requires: make-license = %{version}-%{release}
Requires: make-man = %{version}-%{release}

%description bin
bin components for the make package.


%package dev
Summary: dev components for the make package.
Group: Development
Requires: make-bin = %{version}-%{release}
Provides: make-devel = %{version}-%{release}

%description dev
dev components for the make package.


%package doc
Summary: doc components for the make package.
Group: Documentation
Requires: make-man = %{version}-%{release}

%description doc
doc components for the make package.


%package license
Summary: license components for the make package.
Group: Default

%description license
license components for the make package.


%package locales
Summary: locales components for the make package.
Group: Default

%description locales
locales components for the make package.


%package man
Summary: man components for the make package.
Group: Default

%description man
man components for the make package.


%prep
%setup -q -n make-4.2.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541442225
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1541442225
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/make
cp COPYING %{buildroot}/usr/share/package-licenses/make/COPYING
cp glob/COPYING.LIB %{buildroot}/usr/share/package-licenses/make/glob_COPYING.LIB
cp tests/COPYING %{buildroot}/usr/share/package-licenses/make/tests_COPYING
%make_install
%find_lang make
## install_append content
ln -s make %{buildroot}/usr/bin/gmake
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gmake
/usr/bin/make

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/make/COPYING
/usr/share/package-licenses/make/glob_COPYING.LIB
/usr/share/package-licenses/make/tests_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/make.1

%files locales -f make.lang
%defattr(-,root,root,-)

