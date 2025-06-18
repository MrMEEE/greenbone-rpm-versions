#
# spec file for package gvmd
#
# Copyright (c) 2019-2023, Martin Hauke <mardnh@gmx.de>
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

%define sover 22
Name:           gvmd
Version:        22.4.2
Release:        lp155.1.7
Summary:        Greenbone Vulnerability Manager
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.openvas.org
Source:         https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Git-Clone:     https://github.com/greenbone/gvmd.git
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        gvm.tmpfiles.d
Source98:       https://github.com/greenbone/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source99:       https://www.greenbone.net/GBCommunitySigningKey.asc#/%{name}.keyring
Patch0:         gvmd-postgresql-header-location.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  libgpgme-devel >= 1.1.2
BuildRequires:  libxslt-tools
BuildRequires:  perl-XML-Twig
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  xmltoman
BuildRequires:  libbsd-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gnutls) >= 3.2.15
BuildRequires:  pkgconfig(libgvm_base) >= 22.4
BuildRequires:  pkgconfig(libgvm_gmp) >= 22.4
BuildRequires:  pkgconfig(libgvm_osp) >= 22.4
BuildRequires:  pkgconfig(libgvm_util) >= 22.4
BuildRequires:  pkgconfig(libical) >= 1.00
BuildRequires:  pkgconfig(systemd)
BuildRequires:  gvm-common >= 20.8.0
Requires:       gnutls
Requires:       libgvm-pg-server%{sover}
Requires:       libxslt-tools
Requires:       gvm-common >= 20.8.0
Recommends:     logrotate
# for xml_split
Requires:       perl-XML-Twig
%if 0%{?suse_version} >= 1500
BuildRequires:  postgresql-server-devel
%endif
%{?systemd_ordering}

%description
The Greenbone Vulnerability Manager is the central management service between
security scanners and the user clients.
It manages the storage of any vulnerability management configurations and of the
scan results. Access to data, control commands and workflows is offered via the
XML-based Greenbone Management Protocol (GMP). The primary scanner OpenVAS
Scanner is controlled directly via protocol OTP while any other remote scanner
is coupled with the Open Scanner Protocol (OSP).

%package -n libgvm-pg-server%{sover}
Summary:        PostgreSQL extesion for GVM
Group:          System/Libraries
Recommends:     %{name}-extentions = %{version}

%description -n libgvm-pg-server%{sover}
PostgreSQL extension for GVM.

%package -n gvm-pg-server-devel
Summary:        Development files for libgvm-pg-server
Group:          Development/Libraries/C and C++
Requires:       libgvm-pg-server%{sover} = %{version}

%description -n gvm-pg-server-devel
PostgreSQL extension for GVM.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm-pg-server.

%prep
%setup -q
%patch0 -p1
sed -i 's|#!%{_bindir}/env python3|#!%{_bindir}/python3|g' \
  src/alert_methods/SMB/alert \
  src/alert_methods/TippingPoint/report-convert.py

%build
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
    -DGVM_LIB_INSTALL_DIR=%{_libdir} \
    -DLOCALSTATEDIR=%{_localstatedir} \
    -DGVM_RUN_DIR=%{gvm_runtimedir} \
    -DSYSCONFDIR=%{_sysconfdir} \
    -DDEFAULT_CONFIG_DIR=%{_sysconfdir}/default \
    -DLOGROTATE_DIR=%{_sysconfdir}/logrotate.d \
    -DSYSTEMD_SERVICE_DIR=%{_unitdir}
%make_jobs

%install
%cmake_install
%fdupes -s %{buildroot}/%{_datadir}/gvm
install -Dpm 0644 %{_sourcedir}/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 %{_sourcedir}/%{name}.sysconfig %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/gvm.conf

%pre
%service_add_pre %{name}.service

%post
%fillup_only %{name}
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/gvm.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%post   -n libgvm-pg-server%{sover} -p /sbin/ldconfig
%postun -n libgvm-pg-server%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_tmpfilesdir}/gvm.conf
%dir %attr(-,%{gvm_user},%{gvm_group}) %ghost %{gvm_runtimedir}
%config(noreplace) %{_sysconfdir}/gvm/gvmd_log.conf
%config(noreplace) %{_sysconfdir}/gvm/pwpolicy.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/gvmd
%{_bindir}/gvm-manage-certs
%{_sbindir}/greenbone-certdata-sync
%{_sbindir}/greenbone-scapdata-sync
%{_sbindir}/greenbone-feed-sync
%{_sbindir}/rcgvmd
%{_sbindir}/gvmd
%{_datadir}/gvm/cert/cert_bund_getbyname.xsl
%{_datadir}/gvm/cert/dfn_cert_getbyname.xsl
%{_datadir}/gvm/gvm-lsc-deb-creator
%{_datadir}/gvm/gvm-lsc-exe-creator
%{_datadir}/gvm/gvm-lsc-rpm-creator
%{_datadir}/gvm/gvmd/global_alert_methods
%{_datadir}/gvm/gvmd/global_schema_formats
%{_datadir}/gvm/gvmd/template.nsis
%{_datadir}/gvm/gvmd/wizards
%{_datadir}/gvm/scap
%{_mandir}/man1/gvm-manage-certs.1%{?ext_man}
%{_mandir}/man8/greenbone-certdata-sync.8%{?ext_man}
%{_mandir}/man8/greenbone-scapdata-sync.8%{?ext_man}
%{_mandir}/man8/gvmd.8%{?ext_man}
%{_datadir}/doc/gvm/example-gvm-manage-certs.conf
%{_datadir}/doc/gvm/html/gmp.html
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}

%files -n libgvm-pg-server%{sover}
%{_libdir}/libgvm-pg-server.so.%{sover}*

%files -n gvm-pg-server-devel
%{_libdir}/libgvm-pg-server.so

%changelog
* Tue Feb 21 2023 Martin Hauke <mardnh@gmx.de>
- Update to version 22.4.2
  * https://github.com/greenbone/gvmd/releases/tag/v22.4.2
* Thu Apr  7 2022 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.5
  Added
  * Backtrace output when a sigsegv occurs.
  * Improve handling osp connection errors.
  Changed
  * Use GVMD_RUN_DIR instead of GVM_RUN_DIR.
  * Use full path GVMD_PID_PATH for PID files.
  * Replace blocking table locks with a non-blocking retry loop.
  * Change some migration and OSP warnings to info.
  * Change failed call to xsltproc to a warning.
  Bug Fixes
  * Test if location is null in cve_scan_host to prevent an
    assertion error.
  * Choose correct scan launch function for OSP scans.
- Update to version 21.4.4
  Added
  * Add --rebuild-gvmd-data command line option.
  Fixed
  * Ensure gvmd sends error messages if gvmcg fails.
  * Fix resume task.
  * Added a dedicated error message for the create ticket dialogue
    when the create permission permission is missing.
  * Fix import of report results / errors without host.
* Fri Aug 20 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.3
  Fixed
  * Fix sending prefs for whole, growing VT families.
  * Add trash columns for target "elevate" credential.
  Added
  * Add --optimize add-/cleanup-feed-permissions.
  Changed
  * Use less report cache SQL when adding results.
  Fixed
  * Fix VTs hash check and add --dump-vt-verification.
  * Solved a performance problem when filtering results by tags.
  * Fix VTs hash check and add --dump-vt-verification.
  * Fix memory errors in modify_permission.
  * Fix sensor connection for performance reports on failure.
  * Sort the "host" column by IPv4 address if possible.
  * Fix for parse_iso_time_tz error with musl library.
- Update to version 21.4.2
  Fixed
  * Amended Test, if the ssh elevate credential is different from
    the ssh credential.
  * Added the missing GMP documentation for the ssh elevate
    credential.
* Mon Jun 28 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.1
  Added
  * Add NVT tag "deprecated".
  * Extend GMP for new privilege escalation credential.
  * Include new ssh elevate (escalation) credential in OSP request.
  * Add test if the ssh elevate credential is different from the
    ssh credential.
  Changed
  * Update default log config.
  Fixed
  * Improve VT version handling for CVE & OVAL results.
  * Fix migration to DB version 242 from gvmd 20.08.
  * Update subject alternative name in certificate generation.
  * Fix whole-only config family selection.
  * Migrate GMP Scanners to OSP Sensors.
  * Solved a peformance problem for tasks after scanning lots of
    hosts.
  * Solved a performance problem when filtering results by tags.
* Fri Apr 16 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.0
  Added
  * Extend GMP for extended severities
  * Parameter --db-user to set a database user
  * Add allow_simultaneous_ips field for targets
  * Speed up GET_VULNS
  * Speed up result counting iterator
  * Speed up result iterator
  * Improve GMP docs around users
  * Cache report counts when Dynamic Severity is enabled
  * Detection entry detection while importing reports
  Changed
  * Move EXE credential generation to a Python script
  * Clarify documentation for --scan-host parameter
  * In result iterator access severity directly if possible
  * Change SCAP and CERT data to use "severity" consistently
  * Expect report format scripts to exit with code 0
  * Send entire families to ospd-openvas using VT_GROUP
  * Limit "whole-only" config families to "growing" and "every nvt"
  * Access current user with an SQL function
  * Refactor modify_config, allowing multiple simultaneous changes
  * Add retry on a deadlock within sql#sql
  * Don't require report format plugin for XML report
  * Wording of Rebuilding NVTs because integrity check failed
  Fixed
  * Use GMP version with leading zero for feed dirs
  * Check db version before creating SQL functions
  * Fix severity_in_level SQL function
  * Fix and simplify SecInfo migration
  * Prevent CPE/NVD_ID from being "(null)"
  * Check DB versions before CERT severity updates
  * Add owner checks to report_count queries
  Removed
  * Remove solution element from VT tags
  * Drop GMP scanners
  * Reduce Severity Classes
  * Removed Severity Classes
  * Remove remaining use of "Severity Class" in where_levels_auto
  * Remove the functionality "autofp" (Auto False Positives)
  * Remove severity type "debug"
  * Remove element "threat" of element "notes"
* Sat Mar  6 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 20.8.1
  See https://github.com/greenbone/gvmd/blob/master/CHANGELOG.md
  for all changes
* Wed Aug 12 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 20.8.0
  See https://github.com/greenbone/gvmd/blob/master/CHANGELOG.md
  for all changes
- Add patch:
  * gvmd-postgresql-header-location.patch
* Tue Aug 11 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 9.0.1
  Added
  * Add option --optimize migrate-relay-sensors
  * Add host_id filter for tls_certificates
  * Allow use of public key auth in SCP alert
  * Refuse to import config with missing NVT preference ID
  * Add "Base" scan config
  * Add setting "BPM Data"
  * Add --optimize option cleanup-result-encoding
  * Add --rebuild
  * Lock a file around the NVT sync
  * Add --rebuild-scap option
  Changed
  * Extend command line options for managing scanners
  * Update SCAP and CERT feed info in sync scripts
  * Try authentication when verifying GMP scanners
  * Try importing private keys with libssh if GnuTLS fails
  * Allow resuming OSPd-based OpenVAS tasks
  * Require PostgreSQL 9.6 as a minimum
  * Speed up the SCAP sync
  * Change rows of built-in default filters to -2 (use "Rows Per
    Page" setting)
  * Force NVT update in migrate_219_to_220
  * Use temp tables to speed up migrate_213_to_214
  * Add a delay for re-requesting scan information via osp
  * Count only best OS matches for OS asset hosts
  * Clean up NVTs set to name in cleanup-result-nvts
  * New Community Feed download URL in sync tools
  * Do not ignore empty hosts_allow and ifaces_allow
  Fixed
  * Consider results_trash when deleting users
  * Try to get NVT preferences by id in create_config
  * Fix preference ID in "Host Discovery" config
  * Fix order of fingerprints in get_tls_certificates
  * Update config preferences after updating NVTs
  * Fix asset host details insertion SQL
  * Fix notes XML for lean reports
  * MODIFY_USER saves comment when COMMENT is empty
  * MODIFY_PERMISSION saves comment when COMMENT is empty
  * Fix result diff generation to ignore white space in delta reports
  * Fix resource type checks for permissions
  * Fix result_nvt for new OSP and slave results
  * Use right format specifier for merge_ovaldef version
  * Fix creation of "Super" permissions
  * Setup general task preferences to launch an osp openvas task.
  * Add tags used for result NVTs to update_nvti_cache
  * Apply usage_type of tasks in get_aggregate
  * Setup target's alive test setting to launch an osp openvas task
  * Remove incorrect duplicates from config preference migrator
  * Correct pref ID in migrate_219_to_220
  * Fix alive test. Target's alive test setting has priority over scan
    config
  * Set run status only after getting OSP-OpenVAS scan
  * Fix get_system_reports for GMP scanners
  * Use stop_osp_task for SCANNER_TYPE_OSP_SENSOR
  * Setup target's reverse_lookup_* settings to launch an osp
    openvas task
  * Always use details testing alerts with a report
  * Remove extra XML declaration in Anonymous XML
  * Fix Verinice ISM report format and update version
  * Fix SCP alert authentication and logging
  * Accept expanded scheme OIDs in parse_osp_report
  * Fix SCAP update not finishing when CPEs are older
  * Add user limits on hosts and ifaces to OSP prefs
  * Fix scanner_options not inserted correctly when starting ospd
    task
  * Fix QoD handling in NVTi cache and sensor scans
  * Fix doc of get_tasks in GMP doc
  * Fix deletion of OVAL definition data
  Removed
  * Remove 1.3.6.1.4.1.25623.1.0.90011 from Discovery
    config (9.0)
- Add patch:
  * gvmd-postgresql-header-location.patch
* Thu Apr  9 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 9.0.0
  This is the first release of the gvmd module 9.0 for the
  Greenbone Vulnerability Management (GVM) framework.
  Added
  * Added TLS certificates as a new resource type
  * Update NVTs via OSP #392 #609 #626 #753 #767
  * Handle addition of ID to NVT preferences. #413 #744
  * Add setting 'OMP Slave Check Period' #491
  * Document switching between releases when using Postgres. #563
  * Cgreen based unit tests for gvmd has been added. #579
  * New usage_type property to distinguish normal scan tasks and
    configs from compliance audits and policies #613 #625 #633
  * Command cleanup-report-formats for --optimize option #652
  * Enable SecInfo alert checks #670
  * Add an explicit solution column to NVTs #681 #702 #730
  * Document container tasks in GMP doc #688
  * Add explicit columns for the NVT tags "summary", "insight",
    "detection", "impact" and "affected" #719 #746
  * Add lean option to GET_REPORTS #745
  * Add scanner relays and OSP sensor scanner type #756 #759
  Changed
  * Always convert iCalendar strings to use UTC. #777
  * Check if NVT preferences exist before inserting. #406
  * Raise minimum version for SQL functions. #420
  * Run OpenVAS scans via OSP instead of OTP.
  * Request nvti_cache update only at very end of NVT update. #426
  * Consolidate NVT references into unified "refs" element.
  * Update gvm-libs version requirements to v11.0. #480
  * Adjust to use new API for vt references. #526
  * Expect NVT sync script in bin directory. #546
  * Change internal handling of NVT XML to use nvti_t. #562
  * Change NVT references like CVEs and BID to general vt_refs.
  * Update Postgres to SQLite migration. #581 #601 #604 #605
  * Update result diff generation at delta reports #650
  * Check and create default permissions individually #671
  * Add -f arg to sendmail call in email alert #676 #678
  * Change get_tickets to use the status text for filtering. #697
  * Made checks to prevent duplicate user names stricter. #708 #722
  * Send delete command to ospd after stopping the task. #710
  * Check whether hosts are alive and have results when adding
    them in slave scans. #717 #726 #736 #771
  * Use explicit nvti timestamps #725
  * New columns Ports, Apps, Distance, and Auth in the CSV Hosts
    report format #733
  * The details attribute of GET_REPORTS now defaults to 0 #747
  * Incoming VT timestamps via OSP are now assumed to be seconds
    since epoch #754
  * Accelerate NVT feed update #757
  Fixed
  * Make get_settings return only one setting when setting_id is
    given #779
  * A PostgreSQL statement order issue #611 has been addressed #642
  * Fix iCalendar recurrence and timezone handling #654
  * Fix issues with some scheduled tasks by using iCalendar more
    instead of old period fields #656
  * Fix an issue in getting the reports from GMP scanners #659 #665
  * Fix GET_SYSTEM_REPORTS using slave_id #668
  * Fix RAW_DATA when calling GET_INFO with type NVT without
    attributes name or info_id #682
  * Fix ORPHAN calculations in GET_TICKETS #684 #692
  * Fix assignment of orphaned tickets to the current user #685
  * Fix response from GET_VULNS when given vuln_id does not exists
  * Make bulk tagging with a filter work if the resources are
    already tagged #711
  * Check if the scan finished before deleting it and ensure that
    the task is set to done #714
  * Fix columnless search phrase filter keywords with quotes #715
  * Fix issues importing results or getting them from slaves if
    they contain "%%s" #723
  * Fix sorting by numeric filter columns #751
  * Fix array index error when modifying roles and groups #762
  * Add NULL check in nvts_feed_version_epoch #773
  * Fix percent sign escaping in report_port_count #782
  * If the nvt preference is "file" type, encode it into Base64
    format #785
  Removed
  * The handling of NVT updates via OTP has been removed. #575
  * Bid and xref have been removed from table nvts. #582
  * Database migration from revisions before 185 has been removed.
  * Drop SQLite support #610 #612 #614
  * Remove create report task creation #616
  * Remove --backup command line option #615
  * Remove GET_REPORTS type "assets" #617 #620
  * Remove errors for unknown elements #619
  * Remove unused reports column nbefile #675
  * Eliminate get_tag() and parse_tags() #743
  * Remove helper functions and other code for handling OTP
  * Remove stray prototype nvt_iterator_copyright #721
* Mon Apr 15 2019 Martin Hauke <mardnh@gmx.de>
- Initial package, version 8.0.0
