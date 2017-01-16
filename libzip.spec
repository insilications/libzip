#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libzip
Version  : 1.1.3
Release  : 1
URL      : https://nih.at/libzip/libzip-1.1.3.tar.xz
Source0  : https://nih.at/libzip/libzip-1.1.3.tar.xz
Summary  : library for handling zip archives
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libzip-bin
Requires: libzip-lib
Requires: libzip-doc
BuildRequires : cmake
BuildRequires : zlib-dev

%description
This is libzip, a C library for reading, creating, and modifying zip
archives.  Files can be added from data buffers, files, or compressed
data copied directly from other zip archives.  Changes made without
closing the archive can be reverted.  The API is documented by man
pages.

%package bin
Summary: bin components for the libzip package.
Group: Binaries

%description bin
bin components for the libzip package.


%package dev
Summary: dev components for the libzip package.
Group: Development
Requires: libzip-lib
Requires: libzip-bin
Provides: libzip-devel

%description dev
dev components for the libzip package.


%package doc
Summary: doc components for the libzip package.
Group: Documentation

%description doc
doc components for the libzip package.


%package lib
Summary: lib components for the libzip package.
Group: Libraries

%description lib
lib components for the libzip package.


%prep
%setup -q -n libzip-1.1.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484611126
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1484611126
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/zipcmp
/usr/bin/zipmerge
/usr/bin/ziptool

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libzip.so
/usr/lib64/libzip/include/zipconf.h
/usr/lib64/pkgconfig/libzip.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libzip.so.4
/usr/lib64/libzip.so.4.0.0
