#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v16
# autospec commit: b858a2a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : syndication
Version  : 6.4.0
Release  : 78
URL      : https://download.kde.org/stable/frameworks/6.4/syndication-6.4.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.4/syndication-6.4.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.4/syndication-6.4.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : RSS/Atom parser library
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: syndication-data = %{version}-%{release}
Requires: syndication-lib = %{version}-%{release}
Requires: syndication-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains valid feeds that are known to cause problems with libsyndication. They are separated from
the regression tests as they shouldn't be executed in "make test" runs. As soon as they succeed, move them to the
respective regression test folder.

%package data
Summary: data components for the syndication package.
Group: Data

%description data
data components for the syndication package.


%package dev
Summary: dev components for the syndication package.
Group: Development
Requires: syndication-lib = %{version}-%{release}
Requires: syndication-data = %{version}-%{release}
Provides: syndication-devel = %{version}-%{release}
Requires: syndication = %{version}-%{release}

%description dev
dev components for the syndication package.


%package lib
Summary: lib components for the syndication package.
Group: Libraries
Requires: syndication-data = %{version}-%{release}
Requires: syndication-license = %{version}-%{release}

%description lib
lib components for the syndication package.


%package license
Summary: license components for the syndication package.
Group: Default

%description license
license components for the syndication package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n syndication-6.4.0
cd %{_builddir}/syndication-6.4.0
pushd ..
cp -a syndication-6.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720819691
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720819691
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/syndication
cp %{_builddir}/syndication-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/syndication/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/syndication-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/syndication/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/syndication-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/syndication/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/syndication-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/syndication/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/syndication-%{version}/autotests/LICENSE.UNITTESTS %{buildroot}/usr/share/package-licenses/syndication/02e5e301efb9adac8a5f1ba32855c8d02d5abd7d || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/syndication.categories
/usr/share/qlogging-categories6/syndication.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/Syndication/Syndication/AbstractParser
/usr/include/KF6/Syndication/Syndication/Atom/Atom
/usr/include/KF6/Syndication/Syndication/Atom/Category
/usr/include/KF6/Syndication/Syndication/Atom/Constants
/usr/include/KF6/Syndication/Syndication/Atom/Content
/usr/include/KF6/Syndication/Syndication/Atom/Document
/usr/include/KF6/Syndication/Syndication/Atom/Entry
/usr/include/KF6/Syndication/Syndication/Atom/Generator
/usr/include/KF6/Syndication/Syndication/Atom/Link
/usr/include/KF6/Syndication/Syndication/Atom/Parser
/usr/include/KF6/Syndication/Syndication/Atom/Person
/usr/include/KF6/Syndication/Syndication/Atom/Source
/usr/include/KF6/Syndication/Syndication/Category
/usr/include/KF6/Syndication/Syndication/Constants
/usr/include/KF6/Syndication/Syndication/DataRetriever
/usr/include/KF6/Syndication/Syndication/DocumentSource
/usr/include/KF6/Syndication/Syndication/DocumentVisitor
/usr/include/KF6/Syndication/Syndication/ElementWrapper
/usr/include/KF6/Syndication/Syndication/Enclosure
/usr/include/KF6/Syndication/Syndication/Feed
/usr/include/KF6/Syndication/Syndication/Global
/usr/include/KF6/Syndication/Syndication/Image
/usr/include/KF6/Syndication/Syndication/Item
/usr/include/KF6/Syndication/Syndication/Loader
/usr/include/KF6/Syndication/Syndication/Mapper
/usr/include/KF6/Syndication/Syndication/ParserCollection
/usr/include/KF6/Syndication/Syndication/Person
/usr/include/KF6/Syndication/Syndication/SpecificDocument
/usr/include/KF6/Syndication/Syndication/SpecificItem
/usr/include/KF6/Syndication/Syndication/SpecificItemVisitor
/usr/include/KF6/Syndication/Syndication/Syndication
/usr/include/KF6/Syndication/Syndication/Tools
/usr/include/KF6/Syndication/syndication/abstractparser.h
/usr/include/KF6/Syndication/syndication/atom/atom.h
/usr/include/KF6/Syndication/syndication/atom/category.h
/usr/include/KF6/Syndication/syndication/atom/constants.h
/usr/include/KF6/Syndication/syndication/atom/content.h
/usr/include/KF6/Syndication/syndication/atom/document.h
/usr/include/KF6/Syndication/syndication/atom/entry.h
/usr/include/KF6/Syndication/syndication/atom/generator.h
/usr/include/KF6/Syndication/syndication/atom/link.h
/usr/include/KF6/Syndication/syndication/atom/parser.h
/usr/include/KF6/Syndication/syndication/atom/person.h
/usr/include/KF6/Syndication/syndication/atom/source.h
/usr/include/KF6/Syndication/syndication/category.h
/usr/include/KF6/Syndication/syndication/constants.h
/usr/include/KF6/Syndication/syndication/dataretriever.h
/usr/include/KF6/Syndication/syndication/documentsource.h
/usr/include/KF6/Syndication/syndication/documentvisitor.h
/usr/include/KF6/Syndication/syndication/elementwrapper.h
/usr/include/KF6/Syndication/syndication/enclosure.h
/usr/include/KF6/Syndication/syndication/feed.h
/usr/include/KF6/Syndication/syndication/global.h
/usr/include/KF6/Syndication/syndication/image.h
/usr/include/KF6/Syndication/syndication/item.h
/usr/include/KF6/Syndication/syndication/loader.h
/usr/include/KF6/Syndication/syndication/mapper.h
/usr/include/KF6/Syndication/syndication/parsercollection.h
/usr/include/KF6/Syndication/syndication/person.h
/usr/include/KF6/Syndication/syndication/specificdocument.h
/usr/include/KF6/Syndication/syndication/specificitem.h
/usr/include/KF6/Syndication/syndication/specificitemvisitor.h
/usr/include/KF6/Syndication/syndication/syndication.h
/usr/include/KF6/Syndication/syndication/syndication_export.h
/usr/include/KF6/Syndication/syndication/tools.h
/usr/include/KF6/Syndication/syndication_version.h
/usr/lib64/cmake/KF6Syndication/KF6SyndicationConfig.cmake
/usr/lib64/cmake/KF6Syndication/KF6SyndicationConfigVersion.cmake
/usr/lib64/cmake/KF6Syndication/KF6SyndicationTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Syndication/KF6SyndicationTargets.cmake
/usr/lib64/libKF6Syndication.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Syndication.so.6.4.0
/usr/lib64/libKF6Syndication.so.6
/usr/lib64/libKF6Syndication.so.6.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/syndication/02e5e301efb9adac8a5f1ba32855c8d02d5abd7d
/usr/share/package-licenses/syndication/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/syndication/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/syndication/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/syndication/e712eadfab0d2357c0f50f599ef35ee0d87534cb
