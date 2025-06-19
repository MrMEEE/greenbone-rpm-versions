
%global python3_pkgversion 3.11

Name:           python-pbs-installer
Version:        2025.6.12
Release:        %autorelease
Summary:        Installer for Python Build Standalone

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/pbs-installer/
Source:         %{pypi_source pbs_installer}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pbs-installer' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pbs-installer
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pbs-installer %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-pbs-installer all,download,install


%prep
%autosetup -p1 -n pbs_installer-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,download,install


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pbs-installer -f %{pyproject_files}


%changelog
%autochangelog