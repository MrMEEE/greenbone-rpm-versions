
%global python3_pkgversion 3.11

Name:           python-hatchling
Version:        1.27.0
Release:        %autorelease
Summary:        Modern, extensible Python build backend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://hatch.pypa.io/latest/
Source:         %{pypi_source hatchling}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hatchling' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-hatchling
Summary:        %{summary}

%description -n python%{python3_pkgversion}-hatchling %_description


%prep
%autosetup -p1 -n hatchling-%{version}


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


%files -n python%{python3_pkgversion}-hatchling -f %{pyproject_files}


%changelog
%autochangelog