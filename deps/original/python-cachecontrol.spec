
%global python3_pkgversion 3.11

Name:           python-cachecontrol
Version:        0.14.3
Release:        %autorelease
Summary:        httplib2 caching for requests

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/CacheControl/
Source:         %{pypi_source cachecontrol}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cachecontrol' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-cachecontrol
Summary:        %{summary}

%description -n python%{python3_pkgversion}-cachecontrol %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-cachecontrol dev,filecache,redis


%prep
%autosetup -p1 -n cachecontrol-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,filecache,redis


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-cachecontrol -f %{pyproject_files}


%changelog
%autochangelog