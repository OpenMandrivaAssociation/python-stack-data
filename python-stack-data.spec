Name:		python-stack-data
Version:	0.6.3
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/stack_data/stack_data-%{version}.tar.gz
Summary:	Extract data from python stack frames and tracebacks for informative displays
URL:		https://pypi.org/project/stack-data/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	git-core
BuildArch:	noarch
# Make the dependency on executing optional to avoid cyclical dependency loop
# stack-data requires executing, which requires ipython, which requires stack-data
%define __requires_exclude .*executing.*
Recommends:	python%{pyver}dist(executing)

%description
Extract data from python stack frames and tracebacks for informative displays

%prep -a
# Trick setuptools-scm into reporting the correct version number
git init
git config user.name "OpenMandriva Builder"
git config user.email info@openmandriva.org
git add .
git commit -am "Import %{version}"
git tag -a %{version} -m %{version}

%files
%{py_sitedir}/stack_data
%{py_sitedir}/stack_data-%{version}.dist-info
