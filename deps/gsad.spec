#
# spec file for package gsad
#
# Copyright (c) 2022, Martin Hauke <mardnh@gmx.de>
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


Name:           gsad
Version:        22.4.1
Release:        lp155.1.7
Summary:        Greenbone Security Assistant
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.openvas.org
#Git-Clone:     https://github.com/greenbone/gsad.git
Source:         https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        gsad.sysconfig
Source3:        gsad.service
Source98:       https://github.com/greenbone/gsad/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source99:       https://www.greenbone.net/GBCommunitySigningKey.asc#/%{name}.keyring
BuildRequires:  cmake
BuildRequires:  gvm-common >= 20.8.0
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  xmltoman
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gnutls) >= 3.2.15
BuildRequires:  pkgconfig(libgvm_base) >= 22.4
BuildRequires:  pkgconfig(libgvm_gmp) >= 22.4
BuildRequires:  pkgconfig(libgvm_util) >= 22.4
BuildRequires:  pkgconfig(libmicrohttpd) >= 0.9.0
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       gvm-common >= 20.8.0
Recommends:     logrotate
%{?systemd_ordering}

%description
The Greenbone Security Assistant is the web interface developed for the
Greenbone Security Manager appliances.
It connects to the Greenbone Vulnerability Manager GVM to provide a
full-featured user interface for vulnerability management.

Greenbone Security Assistant consists of:
 * GSA  - The webpage written in React
 * GSAD - The HTTP server talking to the GVM daemon

%prep
%setup -q

%build
%cmake \
    -DLOCALSTATEDIR=%{_localstatedir} \
    -DGVM_RUN_DIR=%{gvm_runtimedir} \
    -DGSAD_PID_DIR=%{gvm_runtimedir} \
    -DSYSCONFDIR=%{_sysconfdir} \
    -DDEFAULT_CONFIG_DIR=%{_sysconfdir}/default \
    -DLOGROTATE_DIR=%{_sysconfdir}/logrotate.d \
    -DSYSTEMD_SERVICE_DIR=%{_unitdir}
%make_jobs

%install
%cmake_install
install -D -m 0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.gsad
# Use our own service file
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/gsad.service
install -d %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcgsad

%pre
%service_add_pre gsad.service

%post
%fillup_only -n gsad
%service_add_post gsad.service

%preun
%service_del_preun gsad.service

%postun
%service_del_postun gsad.service

%files
%license LICENSE
%doc README.md RELEASE.md
%config(noreplace) %{_sysconfdir}/gvm/gsad_log.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/gsad
%{_sbindir}/gsad
%{_sbindir}/rcgsad
%{_mandir}/man8/gsad.8%{?ext_man}
%{_unitdir}/gsad.service
%{_fillupdir}/sysconfig.gsad

%changelog
* Tue Feb 21 2023 Martin Hauke <mardnh@gmx.de>
- Update to version 22.4.1
  Added
  * Add tests for "name" and "comment" field validations.
  Changed
  * Use different return values for gvm_validate.
  * Extract initializing the validators int own C file.
  * Change service start up type from forking to exec.
  Bug Fixes
  * Initialize libgcrypt only once.
  * Allow brackets and en dash Unicode character in name and
    comment fields.
  * Fix regex for new glib2.0 >= 2.73.2
- Update to version 22.4.0
  Removed
  * Removing the OSP scanners in gsad.
  Changed
  * Set runtime directory and mode for systemd service file.
  * Add RuntimeDirectory=gsad to systemd service file.
  * Remove Group directive from service file.
  * Don't create runtime directory with make install.
  * Add status 503 case to set_http_status_from_entity.
  * Change GVM_RUN_DIR to GSAD_RUN_DIR, GVMD_RUN_DIR
  * Use full path GSAD_PID_PATH for PID files.
  Bug Fixes
  * Changed the order of the parameters of MHD_start_daemon (...)
  * Use correct PID path in service file.
  * severity field within gmp_authenticate_info_opts_t got deleted.
* Thu Apr  7 2022 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.4
  * Removing gsad from gsa repository.
- Update to version 21.4.3
  Added
  * Add new handler for single performance report.
  Changed
  * Changed conditions for enabling CreateTicketIcon on results
    detailspage.
  Fixed
  * Don't crash target table when port_list is undefined.
* Fri Aug 20 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.2
  Added
  * Added new InfoIcon and use it in TargetDialog for information
    about the elevate credential feature.
  Changed
  * Changed defaults for installation locations
    + LOCALSTATEDIR is /var by default now
    + SYSCONFDIR is /etc by default now
    + GVM_RUN_DIR and GSAD_PID_DIR are /run/gvm by default now
    + SYSTEMD_SERVICE_DIR is /lib/systemd/system by default now
  Removed
  * Removed gsad.default file and adjusted gsad.service file
    accordingly.
  * Packagers should patch gsad.service file to adjust it on their
    requirements or just ship their own.
  Fixed
  * Initialize severity value with 0 in powerfilter
    SeverityValuesGroup.
  * Make SSH elevate credential optional in gsad.
* Tue Jun 29 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.1
  Added
  * Added SSH Elevate credential to target row.
  * Added isDeprecated() method to NVT model and use it in details.
  * Added @testing-library/user-event as a dev-dependency.
  * Set SameSite=strict for the session cookie to avoid CSRF.
  Changed
  * Disallow using the same credential for ssh and elevate
    credential in targets.
  * Properly space and linebreak roles and groups in users table
    row.
  * Make HorizontalSep component wrappable.
  * Use greenbone sensor as default scanner type when opening the
    dialog if available.
  Fixed
  * Fall back to cvss_base when severity subelement is missing
    from NVT severities.
  * Fix loading NVT information in result details.
  * Fixed setting whether to include related resources for new
    permissions.
  * Fixed number-only names within schedules/dialog.
  * Fixed changing Trend and Select for NVT-families and whole
    selection only.
  * Fixed missing name for CVE results on result detailspage.
  * Fixed setting secret key in RADIUS dialog.
  * Fixed setting result UUID in notes dialog.
* Fri Apr 16 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.0
  Added
  * Allow to set unix socket permissions for gsad
  * Added CVSS date to NVT details
  * Add option to allow to scan simultaneous IPs to targets
  * Added CVSS origin to NVT details
  * Added the CVSS v3.1 BaseScore calculator to the /cvsscalculator
    page in the Help section.
  Changed
  * Revert the changes from integer score to a float severity
  * Show StartIcon for scheduled tasks
  * Remove solution from log NVTs
  * Don't show empty sections in result details
  * Move error message and adjust design on login page
  * Refactored useFormValidation hook
  * Updated copyright and footer layout
  * New login page layout
  * CVE Tables Page can now be used with the updated xml-format
    and CVSSv3(.1).
  * The CVSS v2 BaseScore calculator calculates the score on the
    client side now.
  Fixed
  * Fixed setting comments of business process nodes
  * Added the deprecatedBy field to CPEs
  * Fixed the severity for different advisories
  Removed
  * Removed Edge <= 18 support
  * Removed Internet Explorer 11 support
  * Removed support for uncontrolled form fields
  * Drop gmp scanner type from GSA
  * Removed filter element "autofp"
  * Drop dynamic severity classes
* Sat Mar  6 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 20.8.1
  Added
  * Added icon to host detailspage to link to TLS certificates.
  * Added form validation for user setting "rows per page".
  * Added option for "Start Task" event upon "New SecInfo arrived"
    condition in alerts dialog.
  Changed
  * Ensure superadmins can edit themselves.
  * Disable clone icon for superadmins.
  * Allow äüöÄÜÖß in form validation rule for "name".
  * Show "Filter x matches at least y results" condition to task
    events in alert dialog.
  * Always send sort=name with delta report request filters.
  * Changed trash icon to delete icon on host detailspage.
  * Change tooltip of override icon in result details.
  * For edit config/policy dialog, only send name and comment if
    config or policy is in use, and add in use notification.
  * Changed visual appearance of compliance status bar.
  * Changed delete icons on report format detailspage and schedule
    detailspage to trashcan icons.
  * Use to disable feed object editing and filter creation on feed
    status page.
  Fixed
  * Stop growing of toolbars which only have the help icon.
  * Fixed initial value of dropdown for including related resources
    for permissions.
  * Fixed compiling gsad with libmicrohttp 0.9.71 and later.
  * Fixed display of alert condition "Severity changed".
  * Fixed sanity check for port ranges.
  * Allow to delete processes without having had edges in BPM.
  * Fixed TLS certificate download for users with permissions.
  * Fixed form validation error tooltips.
  * Only show schedule options in advanced and modify task wizard
    if user has correct permissions.
  * Replace deprecated sys_siglist with strsignal.
  Removed
  * Remove secinfo filter from user settings dialog and elsewhere.
  * Removed export/download for report formats.
* Tue Aug 11 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 20.8.0
* Thu Jul 18 2019 Martin Hauke <mardnh@gmx.de>
- Update to version 8.0.1
* Mon Apr 15 2019 Martin Hauke <mardnh@gmx.de>
- Initial package, version 8.0.0
