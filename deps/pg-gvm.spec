#
# spec file for package pg-gvm
#
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           pg-gvm
Version:        22.4.0
Release:        lp155.1.17
Summary:        Greenbone Library for helper functions in PostgreSQL
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.openvas.org
Source:         https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Git-Clone:     https://github.com/greenbone/pg-gvm.git
Source98:       https://github.com/greenbone/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source99:       https://www.greenbone.net/GBCommunitySigningKey.asc#/%{name}.keyring
BuildRequires:  cmake
BuildRequires:  gvm-common >= 20.8.0
BuildRequires:  pkgconfig
BuildRequires:  postgresql-server-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(libgvm_base) >= 22.4
BuildRequires:  pkgconfig(libical) >= 1.00
Requires:       gvm-common >= 20.8.0

%description
Greenbone Library for helper functions in PostgreSQL

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/postgresql15/lib64/libpg-gvm.so
%{_datadir}/postgresql15/extension/pg-gvm--1.0--22.4.0.sql
%{_datadir}/postgresql15/extension/pg-gvm--22.4.0.sql
%{_datadir}/postgresql15/extension/pg-gvm.control

%changelog
* Tue Feb 21 2023 Martin Hauke <mardnh@gmx.de>
- Initial package, version 22.4.0
