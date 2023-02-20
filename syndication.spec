#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : syndication
Version  : 5.103.0
Release  : 57
URL      : https://download.kde.org/stable/frameworks/5.103/syndication-5.103.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.103/syndication-5.103.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.103/syndication-5.103.0.tar.xz.sig
Summary  : RSS/Atom parser library
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: syndication-data = %{version}-%{release}
Requires: syndication-lib = %{version}-%{release}
Requires: syndication-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcodecs-dev
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
%setup -q -n syndication-5.103.0
cd %{_builddir}/syndication-5.103.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676872461
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676872461
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/syndication
cp %{_builddir}/syndication-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/syndication/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/syndication-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/syndication/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/syndication-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/syndication/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/syndication-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/syndication/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/syndication-%{version}/autotests/LICENSE.UNITTESTS %{buildroot}/usr/share/package-licenses/syndication/02e5e301efb9adac8a5f1ba32855c8d02d5abd7d || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/syndication.categories
/usr/share/qlogging-categories5/syndication.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Syndication/Syndication/AbstractParser
/usr/include/KF5/Syndication/Syndication/Atom/Atom
/usr/include/KF5/Syndication/Syndication/Atom/Category
/usr/include/KF5/Syndication/Syndication/Atom/Constants
/usr/include/KF5/Syndication/Syndication/Atom/Content
/usr/include/KF5/Syndication/Syndication/Atom/Document
/usr/include/KF5/Syndication/Syndication/Atom/Entry
/usr/include/KF5/Syndication/Syndication/Atom/Generator
/usr/include/KF5/Syndication/Syndication/Atom/Link
/usr/include/KF5/Syndication/Syndication/Atom/Parser
/usr/include/KF5/Syndication/Syndication/Atom/Person
/usr/include/KF5/Syndication/Syndication/Atom/Source
/usr/include/KF5/Syndication/Syndication/Category
/usr/include/KF5/Syndication/Syndication/Constants
/usr/include/KF5/Syndication/Syndication/DataRetriever
/usr/include/KF5/Syndication/Syndication/DocumentSource
/usr/include/KF5/Syndication/Syndication/DocumentVisitor
/usr/include/KF5/Syndication/Syndication/ElementWrapper
/usr/include/KF5/Syndication/Syndication/Enclosure
/usr/include/KF5/Syndication/Syndication/Feed
/usr/include/KF5/Syndication/Syndication/Global
/usr/include/KF5/Syndication/Syndication/Image
/usr/include/KF5/Syndication/Syndication/Item
/usr/include/KF5/Syndication/Syndication/Loader
/usr/include/KF5/Syndication/Syndication/Mapper
/usr/include/KF5/Syndication/Syndication/ParserCollection
/usr/include/KF5/Syndication/Syndication/Person
/usr/include/KF5/Syndication/Syndication/Rdf/ContentVocab
/usr/include/KF5/Syndication/Syndication/Rdf/Document
/usr/include/KF5/Syndication/Syndication/Rdf/DublinCore
/usr/include/KF5/Syndication/Syndication/Rdf/DublinCoreVocab
/usr/include/KF5/Syndication/Syndication/Rdf/Image
/usr/include/KF5/Syndication/Syndication/Rdf/Item
/usr/include/KF5/Syndication/Syndication/Rdf/Literal
/usr/include/KF5/Syndication/Syndication/Rdf/Model
/usr/include/KF5/Syndication/Syndication/Rdf/ModelMaker
/usr/include/KF5/Syndication/Syndication/Rdf/Node
/usr/include/KF5/Syndication/Syndication/Rdf/NodeVisitor
/usr/include/KF5/Syndication/Syndication/Rdf/Parser
/usr/include/KF5/Syndication/Syndication/Rdf/Property
/usr/include/KF5/Syndication/Syndication/Rdf/Rdf
/usr/include/KF5/Syndication/Syndication/Rdf/RdfVocab
/usr/include/KF5/Syndication/Syndication/Rdf/Resource
/usr/include/KF5/Syndication/Syndication/Rdf/ResourceWrapper
/usr/include/KF5/Syndication/Syndication/Rdf/RssVocab
/usr/include/KF5/Syndication/Syndication/Rdf/Sequence
/usr/include/KF5/Syndication/Syndication/Rdf/Statement
/usr/include/KF5/Syndication/Syndication/Rdf/SyndicationInfo
/usr/include/KF5/Syndication/Syndication/Rdf/SyndicationVocab
/usr/include/KF5/Syndication/Syndication/Rdf/TextInput
/usr/include/KF5/Syndication/Syndication/Rss2/Category
/usr/include/KF5/Syndication/Syndication/Rss2/Cloud
/usr/include/KF5/Syndication/Syndication/Rss2/Document
/usr/include/KF5/Syndication/Syndication/Rss2/Enclosure
/usr/include/KF5/Syndication/Syndication/Rss2/Image
/usr/include/KF5/Syndication/Syndication/Rss2/Item
/usr/include/KF5/Syndication/Syndication/Rss2/Parser
/usr/include/KF5/Syndication/Syndication/Rss2/Rss2
/usr/include/KF5/Syndication/Syndication/Rss2/Source
/usr/include/KF5/Syndication/Syndication/Rss2/TextInput
/usr/include/KF5/Syndication/Syndication/SpecificDocument
/usr/include/KF5/Syndication/Syndication/SpecificItem
/usr/include/KF5/Syndication/Syndication/SpecificItemVisitor
/usr/include/KF5/Syndication/Syndication/Syndication
/usr/include/KF5/Syndication/Syndication/Tools
/usr/include/KF5/Syndication/syndication/abstractparser.h
/usr/include/KF5/Syndication/syndication/atom/atom.h
/usr/include/KF5/Syndication/syndication/atom/category.h
/usr/include/KF5/Syndication/syndication/atom/constants.h
/usr/include/KF5/Syndication/syndication/atom/content.h
/usr/include/KF5/Syndication/syndication/atom/document.h
/usr/include/KF5/Syndication/syndication/atom/entry.h
/usr/include/KF5/Syndication/syndication/atom/generator.h
/usr/include/KF5/Syndication/syndication/atom/link.h
/usr/include/KF5/Syndication/syndication/atom/parser.h
/usr/include/KF5/Syndication/syndication/atom/person.h
/usr/include/KF5/Syndication/syndication/atom/source.h
/usr/include/KF5/Syndication/syndication/category.h
/usr/include/KF5/Syndication/syndication/constants.h
/usr/include/KF5/Syndication/syndication/dataretriever.h
/usr/include/KF5/Syndication/syndication/documentsource.h
/usr/include/KF5/Syndication/syndication/documentvisitor.h
/usr/include/KF5/Syndication/syndication/elementwrapper.h
/usr/include/KF5/Syndication/syndication/enclosure.h
/usr/include/KF5/Syndication/syndication/feed.h
/usr/include/KF5/Syndication/syndication/global.h
/usr/include/KF5/Syndication/syndication/image.h
/usr/include/KF5/Syndication/syndication/item.h
/usr/include/KF5/Syndication/syndication/loader.h
/usr/include/KF5/Syndication/syndication/mapper.h
/usr/include/KF5/Syndication/syndication/parsercollection.h
/usr/include/KF5/Syndication/syndication/person.h
/usr/include/KF5/Syndication/syndication/rdf/contentvocab.h
/usr/include/KF5/Syndication/syndication/rdf/document.h
/usr/include/KF5/Syndication/syndication/rdf/dublincore.h
/usr/include/KF5/Syndication/syndication/rdf/dublincorevocab.h
/usr/include/KF5/Syndication/syndication/rdf/image.h
/usr/include/KF5/Syndication/syndication/rdf/item.h
/usr/include/KF5/Syndication/syndication/rdf/literal.h
/usr/include/KF5/Syndication/syndication/rdf/model.h
/usr/include/KF5/Syndication/syndication/rdf/modelmaker.h
/usr/include/KF5/Syndication/syndication/rdf/node.h
/usr/include/KF5/Syndication/syndication/rdf/nodevisitor.h
/usr/include/KF5/Syndication/syndication/rdf/parser.h
/usr/include/KF5/Syndication/syndication/rdf/property.h
/usr/include/KF5/Syndication/syndication/rdf/rdf.h
/usr/include/KF5/Syndication/syndication/rdf/rdfvocab.h
/usr/include/KF5/Syndication/syndication/rdf/resource.h
/usr/include/KF5/Syndication/syndication/rdf/resourcewrapper.h
/usr/include/KF5/Syndication/syndication/rdf/rssvocab.h
/usr/include/KF5/Syndication/syndication/rdf/sequence.h
/usr/include/KF5/Syndication/syndication/rdf/statement.h
/usr/include/KF5/Syndication/syndication/rdf/syndicationinfo.h
/usr/include/KF5/Syndication/syndication/rdf/syndicationvocab.h
/usr/include/KF5/Syndication/syndication/rdf/textinput.h
/usr/include/KF5/Syndication/syndication/rss2/category.h
/usr/include/KF5/Syndication/syndication/rss2/cloud.h
/usr/include/KF5/Syndication/syndication/rss2/document.h
/usr/include/KF5/Syndication/syndication/rss2/enclosure.h
/usr/include/KF5/Syndication/syndication/rss2/image.h
/usr/include/KF5/Syndication/syndication/rss2/item.h
/usr/include/KF5/Syndication/syndication/rss2/parser.h
/usr/include/KF5/Syndication/syndication/rss2/rss2.h
/usr/include/KF5/Syndication/syndication/rss2/source.h
/usr/include/KF5/Syndication/syndication/rss2/textinput.h
/usr/include/KF5/Syndication/syndication/specificdocument.h
/usr/include/KF5/Syndication/syndication/specificitem.h
/usr/include/KF5/Syndication/syndication/specificitemvisitor.h
/usr/include/KF5/Syndication/syndication/syndication.h
/usr/include/KF5/Syndication/syndication/syndication_export.h
/usr/include/KF5/Syndication/syndication/tools.h
/usr/include/KF5/Syndication/syndication_version.h
/usr/lib64/cmake/KF5Syndication/KF5SyndicationConfig.cmake
/usr/lib64/cmake/KF5Syndication/KF5SyndicationConfigVersion.cmake
/usr/lib64/cmake/KF5Syndication/KF5SyndicationTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Syndication/KF5SyndicationTargets.cmake
/usr/lib64/libKF5Syndication.so
/usr/lib64/qt5/mkspecs/modules/qt_Syndication.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Syndication.so.5
/usr/lib64/libKF5Syndication.so.5.103.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/syndication/02e5e301efb9adac8a5f1ba32855c8d02d5abd7d
/usr/share/package-licenses/syndication/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/syndication/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/syndication/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/syndication/e712eadfab0d2357c0f50f599ef35ee0d87534cb
