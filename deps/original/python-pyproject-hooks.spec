
%global python3_pkgversion 3.11

Name:           python-pyproject-hooks
Version:        1.2.0
Release:        %autorelease
Summary:        Wrappers to call pyproject.toml-based build backend hooks.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/pyproject-hooks/
Source:         %{pypi_source pyproject_hooks}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyproject-hooks' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyproject-hooks
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyproject-hooks %_description


%prep
%autosetup -p1 -n pyproject_hooks-%{version}


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


%files -n python%{python3_pkgversion}-pyproject-hooks -f %{pyproject_files}


%changelog
%autochangelog