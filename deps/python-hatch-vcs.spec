
%global python3_pkgversion 3.11

Name:           python-hatch-vcs
Version:        0.5.0
Release:        %autorelease
Summary:        Hatch plugin for versioning with your preferred VCS

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/hatch-vcs/
Source:         %{pypi_source hatch_vcs}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hatch-vcs' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-hatch-vcs
Summary:        %{summary}

%description -n python%{python3_pkgversion}-hatch-vcs %_description


%prep
%autosetup -p1 -n hatch_vcs-%{version}


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


%files -n python%{python3_pkgversion}-hatch-vcs -f %{pyproject_files}


%changelog
%autochangelog