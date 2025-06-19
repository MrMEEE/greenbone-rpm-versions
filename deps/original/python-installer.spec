
%global python3_pkgversion 3.11

Name:           python-installer
Version:        0.7.0
Release:        %autorelease
Summary:        A library for installing Python wheels.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/installer/
Source:         %{pypi_source installer}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'installer' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-installer
Summary:        %{summary}

%description -n python%{python3_pkgversion}-installer %_description


%prep
%autosetup -p1 -n installer-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-installer -f %{pyproject_files}


%changelog
%autochangelog