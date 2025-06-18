
%global python3_pkgversion 3.11

Name:           python-poetry-core
Version:        2.1.3
Release:        %autorelease
Summary:        Poetry PEP 517 Build Backend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-poetry/poetry-core
Source:         %{pypi_source poetry_core}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'poetry-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-poetry-core
Summary:        %{summary}

%description -n python%{python3_pkgversion}-poetry-core %_description


%prep
%autosetup -p1 -n poetry_core-%{version}


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


%files -n python%{python3_pkgversion}-poetry-core -f %{pyproject_files}


%changelog
%autochangelog