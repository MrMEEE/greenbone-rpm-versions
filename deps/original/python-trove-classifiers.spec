
%global python3_pkgversion 3.11

Name:           python-trove-classifiers
Version:        2025.5.9.12
Release:        %autorelease
Summary:        Canonical source for classifiers on PyPI (pypi.org).

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pypa/trove-classifiers
Source:         %{pypi_source trove_classifiers}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'trove-classifiers' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-trove-classifiers
Summary:        %{summary}

%description -n python%{python3_pkgversion}-trove-classifiers %_description


%prep
%autosetup -p1 -n trove_classifiers-%{version}


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


%files -n python%{python3_pkgversion}-trove-classifiers -f %{pyproject_files}


%changelog
%autochangelog