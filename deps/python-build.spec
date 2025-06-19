
%global python3_pkgversion 3.11

Name:           python-build
Version:        1.2.2^post1
Release:        %autorelease
Summary:        A simple, correct Python build frontend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/build/
Source:         %{pypi_source build 1.2.2.post1}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'build' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-build
Summary:        %{summary}

%description -n python%{python3_pkgversion}-build %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n build-1.2.2.post1


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
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


%files -n python%{python3_pkgversion}-build -f %{pyproject_files}


%changelog
%autochangelog