%define		module	pyspi
Summary:	Python bindings for AT-SPI
Summary(pl.UTF-8):	Dowiązania Pythona do AT-SPI
Name:		python-%{module}
Version:	0.5.4
Release:	4
License:	LGPL
Group:		Libraries/Python
Source0:	http://people.redhat.com/zcerza/dogtail/releases/%{module}-%{version}.tar.gz
# Source0-md5:	a9db16d5830e621fc966f93d303fb83e
BuildRequires:	at-spi-devel
BuildRequires:	python >= 2.2.1
BuildRequires:	python-Pyrex >= 0.9.4.2
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AT-SPI allows assistive technologies to access GTK-based applications.
It exposes the internals of applications for automation, so tools such
as screen readers and scripting interfaces can query and interact with
GUI controls.

pyspi allows the Python language to be used to script AT-SPI-aware
applications (currently mostly GTK+ based.)

%description -l pl.UTF-8
AT-SPI pozwala na korzystanie z urządzeń wspomagających w celu dostępu
do aplikacji opartych na GTK+. Udostępnia wewnętrzne interfejsy
aplikacji w celu automatyzacji, więc urządzenia takie jak czytniki
ekranu czy interfejsy skryptowe mogą odpytywać i współpracować z
kontrolkami interfejsu graficznego.

pyspi pozwala na używanie języka Python do oskryptowania aplikacji
zgodnych z AT-API (aktualnie w większości opartych na GTK+).

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{py_sitedir}/*.so
