%global srcname sphinx-math-dollar

Name:           python-%{srcname}
Version:        1.2
Release:        7%{?dist}
Summary:        Sphinx extension to enable LaTeX math with $$

License:        MIT
URL:            https://www.sympy.org/%{srcname}/
Source0:        https://github.com/sympy/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Update versioneer.py to fix FTBFS with python 3.11
# See https://github.com/sympy/sphinx-math-dollar/issues/27
Patch0:         %{name}-versioneer.patch
# Drop the dependency on upstream dead sphinx-testing, use sphinx.testing instead
# https://github.com/sympy/sphinx-math-dollar/commit/2a66b0b694
# https://github.com/sympy/sphinx-math-dollar/pull/29
Patch1:         %{name}-sphinx-testing.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pytest-doctestplus}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wheel}

%global _desc %{expand:
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math
using $$.}

%description %_desc

%package     -n python3-%{srcname}
Summary:        Sphinx extension to enable LaTeX math with $$

%description -n python3-%{srcname} %_desc

%package        doc
Summary:        Documentation for %{srcname}

%description    doc
Documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%pyproject_wheel

# Build the documentation
make -C docs html
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html
rst2html --no-datestamp README.rst README.html
rm -f docs/_build/html/.{buildinfo,nojekyll}

%install
%pyproject_install

%check
%pytest

%files       -n python3-%{srcname}
%doc CHANGELOG.html README.html
%license LICENSE
%{python3_sitelib}/sphinx_math_dollar*

%files          doc
%doc docs/_build/html
%license LICENSE

%changelog
* Thu Feb 17 2022 Miro Hrončok <mhroncok@redhat.com> - 1.2-7
- Drop the dependency on upstream dead sphinx-testing, use sphinx.testing instead

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Jerry James <loganjerry@gmail.com> - 1.2-5
- Add -versioneer patch to fix FTBFS with python 3.11
- Update python macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Jerry James <loganjerry@gmail.com> - 1.2-1
- Version 1.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  2 2020 Jerry James <loganjerry@gmail.com> - 1.1.1-1
- Initial RPM
