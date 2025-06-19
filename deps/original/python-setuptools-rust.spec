
%global python3_pkgversion 3.11

Name:           python-setuptools-rust
Version:        1.11.1
Release:        %autorelease
Summary:        Setuptools Rust extension plugin

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/PyO3/setuptools-rust
Source:         %{pypi_source setuptools_rust}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools-rust' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-setuptools-rust
Summary:        %{summary}

%description -n python%{python3_pkgversion}-setuptools-rust %_description


%prep
%autosetup -p1 -n setuptools_rust-%{version}


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


%files -n python%{python3_pkgversion}-setuptools-rust -f %{pyproject_files}


%changelog
%autochangelog