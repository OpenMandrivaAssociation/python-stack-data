Name:		python-stack-data
Version:	0.6.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/stack_data/stack_data-%{version}.tar.gz
Summary:	Extract data from python stack frames and tracebacks for informative displays
URL:		https://pypi.org/project/stack-data/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Extract data from python stack frames and tracebacks for informative displays

%files
%{py_sitedir}/stack_data
%{py_sitedir}/stack_data-*.*-info
