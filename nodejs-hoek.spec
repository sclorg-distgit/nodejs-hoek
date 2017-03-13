%{?scl:%scl_package nodejs-hoek}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-hoek
Version:    2.16.3
Release:    1%{?dist}
Summary:    General purpose Node.js utilities
License:    BSD
URL:        https://github.com/spumko/hoek
Source0:    http://registry.npmjs.org/hoek/-/hoek-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This package contains some general purpose Node.js utilities, including
utilities for working with objects, timers, binary encoding/decoding, escaping
characters, errors, and loading files.

%prep
%setup -q -n package

#fix perms
chmod 0644 README.md LICENSE images/* lib/* package.json

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/hoek
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/hoek

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%files
%{nodejs_sitelib}/hoek
%doc README.md LICENSE images

%changelog
* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.16.3-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.9.1-4
- rebuilt

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.9.1-3
- replace provides and requires with macro


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
