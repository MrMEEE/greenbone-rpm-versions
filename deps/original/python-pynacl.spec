
%global python3_pkgversion 3.11

Name:           python-pynacl
Version:        1.5.0
Release:        %autorelease
Summary:        Python binding to the Networking and Cryptography (NaCl) library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyca/pynacl/
Source:         %{pypi_source PyNaCl}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pynacl' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pynacl
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pynacl %_description


%prep
%autosetup -p1 -n PyNaCl-%{version}


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


%files -n python%{python3_pkgversion}-pynacl -f %{pyproject_files}


%changelog
%autochangelog