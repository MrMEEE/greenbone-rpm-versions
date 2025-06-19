
%global python3_pkgversion 3.11

Name:           python-rapidfuzz
Version:        3.13.0
Release:        %autorelease
Summary:        rapid fuzzy string matching

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/rapidfuzz/RapidFuzz
Source:         %{pypi_source rapidfuzz}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rapidfuzz' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-rapidfuzz
Summary:        %{summary}

%description -n python%{python3_pkgversion}-rapidfuzz %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-rapidfuzz all


%prep
%autosetup -p1 -n rapidfuzz-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-rapidfuzz -f %{pyproject_files}


%changelog
%autochangelog