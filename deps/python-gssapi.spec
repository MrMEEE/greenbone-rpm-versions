
%global python3_pkgversion 3.11

Name:           python-gssapi
Version:        1.9.0
Release:        %autorelease
Summary:        Python GSSAPI Wrapper

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pythongssapi/python-gssapi
Source:         %{pypi_source gssapi}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc heimdal-devel krb5-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gssapi' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-gssapi
Summary:        %{summary}

%description -n python%{python3_pkgversion}-gssapi %_description


%prep
%autosetup -p1 -n gssapi-%{version}


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


%files -n python%{python3_pkgversion}-gssapi -f %{pyproject_files}


%changelog
%autochangelog
