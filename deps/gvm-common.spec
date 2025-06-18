#
# spec file for package gvm-common
#
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gvm-common
Version:        20.8.1
Release:        lp155.1.4
Summary:        Just some shared directories and users
License:        MIT
Group:          Productivity/Networking/Security
Url:            http://www.opensuse.org/
BuildArch:      noarch
Source1:        macros.gvm
Requires(pre):  shadow

%define gvm_user        gvm
%define gvm_group       gvm
%define gvm_home        %{_localstatedir}/lib/gvm
%define gvm_runtimedir  %{_rundir}/gvm

%description
Just some shared directories and users for GVM.

%prep

%build

%install
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.gvm
install -d -m 0750 %{buildroot}%{gvm_home}
install -d -m 0750 %{buildroot}%{_sysconfdir}/gvm
install -d -m 0750 %{buildroot}%{_sysconfdir}/openvas
install -d -m 0750 %{buildroot}%{_localstatedir}/log/gvm
install -d -m 0750 %{buildroot}%{_localstatedir}/lib/gvm/gvmd/gnupg
install -d -m 0750 %{buildroot}%{_localstatedir}/lib/gvm/gvmd/report_formats
install -d -m 0750 %{buildroot}%{_datadir}/gvm
install -d -m 0750 %{buildroot}%{_datadir}/gvm/cert
install -d -m 0750 %{buildroot}%{_datadir}/gvm/gvmd
install -d -m 0750 %{buildroot}%{_datadir}/gvm/gsad
install -d -m 0750 %{buildroot}%{_datadir}/doc/gvm
install -d -m 0750 %{buildroot}%{_datadir}/doc/gvm/html
install -d -m 0750 %{buildroot}%{_localstatedir}/lib/openvas

%pre
# Create gvm user/group
getent group %{gvm_group} >/dev/null || groupadd -r %{gvm_group}
getent passwd %{gvm_user} >/dev/null || useradd -r -g %{gvm_group} -d %{gvm_home} -s /sbin/nologin -c "Greenbone Vulnerability Manager" %{gvm_user}

%files
# RPM macros
%config %{_sysconfdir}/rpm/macros.gvm
# Files/directories
%dir %attr(-,%{gvm_user},%{gvm_group}) %{gvm_home}
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_sysconfdir}/gvm
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_sysconfdir}/openvas
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_localstatedir}/log/gvm
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_localstatedir}/lib/gvm/gvmd
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_localstatedir}/lib/gvm/gvmd/gnupg
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_localstatedir}/lib/gvm/gvmd/report_formats
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_datadir}/gvm
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_datadir}/gvm/cert
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_datadir}/gvm/gvmd
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_datadir}/gvm/gsad
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_datadir}/doc/gvm
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_datadir}/doc/gvm/html
%dir %attr(-,%{gvm_user},%{gvm_group}) %{_localstatedir}/lib/openvas


%changelog
* Sun Aug 30 2020 Martin Hauke <mardnh@gmx.de>
- Initial package
