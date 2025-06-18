#
# spec file for package gvm-libs
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover 22
Name:           gvm-libs
Version:        22.4.4
Release:        lp155.3.6
Summary:        Support libraries for the Greenbone Vulnerability Management Framework (GVM)
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/greenbone/gvm-libs
#Git-Clone:     https://github.com/greenbone/gvm-libs.git
Source:         https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         gvm-libs-cmake.patch
Source98:       https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz.asc
Source99:       https://www.greenbone.net/GBCommunitySigningKey.asc#/%{name}.keyring
BuildRequires:  cmake
BuildRequires:  graphviz
BuildRequires:  doxygen
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpgme-devel >= 1.7.0
BuildRequires:  libpaho-mqtt-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.42
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gnutls) >= 3.2.15
BuildRequires:  pkgconfig(hiredis) >= 0.10.1
%if 0%{?suse_version} <= 1500
BuildRequires:  libnet-devel
%else
BuildRequires:  pkgconfig(libnet)
%endif
BuildRequires:  pkgconfig(libssh) >= 0.6.0
BuildRequires:  pkgconfig(uuid) >= 2.25.0
BuildRequires:  pkgconfig(zlib) >= 1.2.8
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0
BuildRequires:  pkgconfig(radcli)
BuildRequires:  libpcap-devel


%description
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_base%{sover}
Summary:        Support libraries for GVM
Group:          System/Libraries

%description -n libgvm_base%{sover}
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_base-devel
Summary:        Development files for the GVM base library
Group:          Development/Libraries/C and C++
Requires:       libgvm_base%{sover} = %{version}

%description -n libgvm_base-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_base.

%package -n libgvm_gmp%{sover}
Summary:        Support libraries for GVM
Group:          System/Libraries

%description -n libgvm_gmp%{sover}
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_gmp-devel
Summary:        Development files for the GVM gmp library
Group:          Development/Libraries/C and C++
Requires:       libgvm_gmp%{sover} = %{version}

%description -n libgvm_gmp-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_gmp.

%package -n libgvm_osp%{sover}
Summary:        Support libraries for GVM
Group:          System/Libraries

%description -n libgvm_osp%{sover}
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_osp-devel
Summary:        Development files for the GVM osp library
Group:          Development/Libraries/C and C++
Requires:       libgvm_osp%{sover} = %{version}

%description -n libgvm_osp-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_osp.

%package -n libgvm_util%{sover}
Summary:        Support libraries for GVM
Group:          System/Libraries

%description -n libgvm_util%{sover}
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_util-devel
Summary:        Development files for the GVM util library
Group:          Development/Libraries/C and C++
Requires:       libgvm_util%{sover} = %{version}
Requires:       libpaho-mqtt-devel

%description -n libgvm_util-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_util.

%package -n libgvm_boreas%{sover}
Summary:        Support libraries for the GVM boreas library
Group:          System/Libraries

%description -n libgvm_boreas%{sover}
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_boreas-devel
Summary:        Development files for the GVM boreas library
Group:          Development/Libraries/C and C++
Requires:       libgvm_boreas%{sover} = %{version}

%description -n libgvm_boreas-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_boreas.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DGVM_PID_DIR=%{_rundir}/gvm/
%make_jobs

%install
%cmake_install

%post -n libgvm_base%{sover} -p /sbin/ldconfig
%post -n libgvm_gmp%{sover} -p /sbin/ldconfig
%post -n libgvm_osp%{sover} -p /sbin/ldconfig
%post -n libgvm_util%{sover} -p /sbin/ldconfig
%post -n libgvm_boreas%{sover} -p /sbin/ldconfig
%postun -n libgvm_base%{sover} -p /sbin/ldconfig
%postun -n libgvm_gmp%{sover} -p /sbin/ldconfig
%postun -n libgvm_osp%{sover} -p /sbin/ldconfig
%postun -n libgvm_util%{sover} -p /sbin/ldconfig
%postun -n libgvm_boreas%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc CHANGELOG.md README.md

%files -n libgvm_base%{sover}
%{_libdir}/libgvm_base.so.%{sover}*

%files -n libgvm_gmp%{sover}
%{_libdir}/libgvm_gmp.so.%{sover}*

%files -n libgvm_osp%{sover}
%{_libdir}/libgvm_osp.so.%{sover}*

%files -n libgvm_util%{sover}
%{_libdir}/libgvm_util.so.%{sover}*

%files -n libgvm_boreas%{sover}
%{_libdir}/libgvm_boreas.so.%{sover}*

%files -n libgvm_base-devel
%dir %{_includedir}/gvm
%{_includedir}/gvm/base
%{_libdir}/libgvm_base.so
%{_libdir}/pkgconfig/libgvm_base.pc

%files -n libgvm_gmp-devel
%dir %{_includedir}/gvm
%{_includedir}/gvm/gmp
%{_libdir}/libgvm_gmp.so
%{_libdir}/pkgconfig/libgvm_gmp.pc

%files -n libgvm_osp-devel
%dir %{_includedir}/gvm
%{_includedir}/gvm/osp/
%{_libdir}/libgvm_osp.so
%{_libdir}/pkgconfig/libgvm_osp.pc

%files -n libgvm_util-devel
%dir %{_includedir}/gvm
%{_includedir}/gvm/util
%{_libdir}/libgvm_util.so
%{_libdir}/pkgconfig/libgvm_util.pc

%files -n libgvm_boreas-devel
%dir %{_includedir}/gvm
%{_includedir}/gvm/boreas
%{_libdir}/libgvm_boreas.so
%{_libdir}/pkgconfig/libgvm_boreas.pc

%changelog
* Tue Feb 21 2023 Martin Hauke <mardnh@gmx.de>
- Update to version 22.4.4
  * https://github.com/greenbone/gvm-libs/releases/tag/v22.4.4
* Thu Apr  7 2022 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.4
  Added
  * Add simple method of getting the out iface.
  Changed
  * Create pid file by specifying full path
  Bug Fixes
  * add missing dependency to gvm_util within boreas.
  * Fix getting the wrong out iface.
  * Fix potential dead lock.
  * Always init logger mutex before use.
  * Using deprecation warning for g_memdup in gvm-libs for
    backwards compability, but also allow modern gcc versions.
- Update to version 21.4.3
  * Add function to duplicate host and vhost objects.
* Fri Aug 20 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.2
  * Fix info msg when 0 alive hosts are left to scan and
    max_scan_hosts limit is reached. No message will be generated
    for that case anymore.
* Mon Jun 28 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.1
  Added
  * Possibility to use lcrypt with $6$ (sha512) for authentication.
  * Add function to find and return a host from a host list.
  Changed
  * Make test_alive_hosts_only (Boreas) feature the new default.
  Fixed
  * Unify GLib log domains.
  * Fix double free.
* Fri Apr 16 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 21.4.0
  Added
  * Use dedicated port list for alive detection (Boreas only) if
    supplied via OSP.
  * Allow to re allocate the finish flag in the host queue for
    alive tests.
  * Add multiple severities for nvti.
  * Add support for new OSP element for defining alive test
    methods via separate subelements.
  * Add v3 handling to get_cvss_score_from_base_metrics.
  * Add severity_date tag in epoch time format.
  * Make more scanner preferences available to openvas-nasl.
  * Use memory purge redis command when initializing new kb.
  Changed
  * Add separators for a new (ip address) field in ERRMSG and
    DEADHOST messages.
  * Continuously send dead hosts to ospd-openvas to enable a
    smooth progress bar if only ICMP is chosen as alive test.
  * Retry if response via tls1.3 is still not received.
  * Replace current implementation of alive test arp ping with
    version using libnet.
  * Let setup_log_handlers return an error if it does not have
    write access to some log file or log dir instead of aborting
    immediately.
  * Fix openvas preference name. The option was rename
    to "allow_simultaneous_ips".
  * Do not start the sniffer thread when only consider alive is
    chosen for alive test.
  Fixed
  * Fix finish_signal_on_queue for boreas.
  Removed
  * Remove handling of severity class from auth.
  * Remove version from the nvticache name.
* Sat Mar  6 2021 Martin Hauke <mardnh@gmx.de>
- Update to version 20.8.1
  Added
  * Add function to get duplicated hosts from the hosts list.
  * Add file access tests using effective UID/GID.
  Changed
  * Reduce ping timeout when using test_alive_hosts_only feature.
  * Retry if response via tls1.3 is still not received.
  Fixed
  * Fix port list for tcp pings when using test_alive_hosts_only
    feature.
  * Set source address correctly and do not try to send ARP to
    unreachable destination.
  * Increase minimum gpgme version.
  * Always NULL check ifaddrs->ifa_addr.
  * Correct g_hash_table_remove arg.
  * Accept underscore as valid char in hostname strings.
  * Add throttle for pinging with test_alive_hosts_only feature
    when socket buffer is full.
* Wed Aug 12 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 20.8.0
  Added
  * Add nvti_get_tag()
  * Add nvti_solution_method() and nvti_set_solution_method()
  * Extend osp with target's alive test option.
  * Extend osp with target's reverse_lookup_* options.
  * Add unit tests for osp.
  * Add support for test_alive_hosts_only feature of openvas.
  * Add function to set and get the NVT QoD.
  * Add unit tests for networking.c port list functions.
  * Add gmp_start_task_ext_c.
  * Make log mutex visible.
  * Add new scan status QUEUED.
  * Add gvm_routethrough which is used by Boreas alive detection
    module.
  * Move alive detection module Boreas into gvm-libs.
  * Add new scan status INTERRUPTED.
  * Add sensible default values for osp_get_vts_opts_t.
  * Add cli support for boreas standalone tool.
  Changed
  * Improve validation in is_hostname
  * Use get_vts instead of get_version to get the feed version is
    osp_get_vts_version().
  * Allow all alive test combination for boreas.
  Fixed
  * Fix is_cidr_block().
  * Fix is_cidr6_block() and is_short_range_network().
  * Fix S/MIME keylist and improve error handling.
  * Fix interrupted state by sending correct number of dead hosts..
  Removed
  * Remove parallel from target options.
  * Remove zero padding from version.
* Mon Aug 10 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 11.0.1
  Added
  * Add option to set finished hosts in OSP targets #298
  * Add a fast memory-only XML parser #299
  * Add new function gvm_libs_version #301
  Changed
  * Don't create an entity tree during read_string_c. #305
  Fixed
  * Fix sigsegv when no plugin_feed_info.inc file present. #278
  * Fix missing linking to libgnutls in util/CMakeLists.txt. #291
  * Free string in all error exit cases #308
  * Fix trust and file handling for S/MIME #309
  * Get details with get_reports in gmp_get_report_ext #313
  * Fix escaping entity attributes in print_entity_to_string #318
  * Fix is_cidr_block() #323
* Thu Apr  9 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 11.0.0
  Added
  * Allow to configure the path to the redis socket via CMake
  * A new data model for unified handling of cross references in
    the NVT meta data as been added. All previous API elements to
    handle cve, bid, xref have been removed. #225 #232.
  * Add function to get an osp scan status and a enum type for the
    different status #259
  * API functions for NVTI to handle timestamps #261
  * API function for NVTI to add a single tag #263
  * Add osp_get_performance_ext() function. #262
  * Add libldap2-dev to prerequisites. #249
  * Add function osp_get_vts_filtered(). #251
  * Add explicit attributes in nvti struct. #258
  Changed
  * Handle EAI_AGAIN in gvm_host_reverse_lookup() IPv6 case and
    function refactor. #229
  * Prevent g_strsplit to be called with NULL. #238
  * Timestamps for NVTI modification date and creation date now
    internally handled as seconds since epoch. #265
  * The tag cvss_base is not added to redis anymore. #267
  * Functions in osp.c with error as argument, will set the error
    if the connection is missing. #268
  * Make QoD Type an explicit element of struct nvti. #250
  * Use API to access nvti information. #252
  * Make the nvti struct internal. #253
  * Make solution and solution_type explicit for nvti. #255
  * Internalize struct nvtpref_t. #260
  * Extend redis connection error msg with actual path. #264
  Fixed
  * Prevent g_strsplit to be called with NULL. #238
  * Check filter before using it in osp_get_vts_ext. #266
  Removed
  * Remove inconsistent delays in kb routines. #230
* Mon Apr 15 2019 Martin Hauke <mardnh@gmx.de>
- Initial package, version 10.0.0
