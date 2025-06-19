
%global python3_pkgversion 3.11

Name:           python-dulwich
Version:        0.22.8
Release:        %autorelease
Summary:        Python Git Library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://www.dulwich.io/
Source:         %{pypi_source dulwich}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dulwich' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-dulwich
Summary:        %{summary}

%description -n python%{python3_pkgversion}-dulwich %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n dulwich-%{version}


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


%files -n python%{python3_pkgversion}-dulwich -f %{pyproject_files}


%changelog
%autochangelog