
%global python3_pkgversion 3.11

Name:           python-cython
Version:        3.1.2
Release:        %autorelease
Summary:        The Cython compiler for writing C extensions in the Python language.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://cython.org/
Source:         %{pypi_source cython}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cython' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-cython
Summary:        %{summary}

%description -n python%{python3_pkgversion}-cython %_description


%prep
%autosetup -p1 -n cython-%{version}


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


%files -n python%{python3_pkgversion}-cython -f %{pyproject_files}


%changelog
%autochangelog