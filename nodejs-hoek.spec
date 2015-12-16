%{?scl:%scl_package nodejs-hoek}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-hoek
Version:    0.9.1
Release:    2.sc1%{?dist}
Summary:    General purpose Node.js utilities
License:    BSD
Group:      Development/Libraries
URL:        https://github.com/spumko/hoek
Source0:    http://registry.npmjs.org/hoek/-/hoek-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This package contains some general purpose Node.js utilities, including
utilities for working with objects, timers, binary encoding/decoding, escaping
characters, errors, and loading files.

%prep
%setup -q -n package

#fix perms
chmod 0644 README.md LICENSE images/* lib/* index.js package.json

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/hoek
cp -pr lib index.js package.json %{buildroot}%{nodejs_sitelib}/hoek

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/hoek
%doc README.md LICENSE images

%changelog

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.1-1
- new upstream release 0.9.1

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.1-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.1-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.8.1-2
- Add support for software collections

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.1-1
- initial package
