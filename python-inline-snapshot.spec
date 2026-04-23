%define module inline-snapshot
%define oname inline_snapshot

%bcond tests 1

Name:		python-inline-snapshot
Version:	0.32.7
Release:	1
Summary:	Create and update inline snapshots in your python tests
License:	MIT
Group:		Development/Python
URL:		https://github.com/15r10nk/inline-snapshot/
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(asttokens)
BuildRequires:	python%{pyver}dist(black)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(dirty-equals)
BuildRequires:	python%{pyver}dist(executing)
BuildRequires:	python%{pyver}dist(hypothesis)
BuildRequires:	python%{pyver}dist(isort)
BuildRequires:	python%{pyver}dist(mypy)
BuildRequires:	python%{pyver}dist(pydantic)
BuildRequires:	python%{pyver}dist(pyright)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-freezer)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(pytest-xdist)
BuildRequires:	python%{pyver}dist(rich)
BuildRequires:	python%{pyver}dist(typing-extensions)
%endif
Suggests:	python%{pyver}dist(black) >= 23.3.0
Suggests:	python%{pyver}dist(dirty-equals) >= 0.9.0

%description
Create and update inline snapshots in your python tests.

inline-snapshot boosts efficiency when writing tests by generating code with
the expected values and simplifies snapshot tests with pytest.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
export PYTHONWARNINGS='ignore::DeprecationWarning'
# We dont need to test upstream linting or docs.
# test_typing requires internet access via pyright, disable it.
skiptests+="not test_typing and not test_pydantic"
skiptests+=" and not test_format_command_fail and not test_docs"
pytest -k "$skiptests"
%endif

%files
%doc README.md
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
