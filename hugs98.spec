Summary:	Hugs - a Haskell interpreter
Summary(pl):	Hugs - interpreter Haskella
Name:		hugs98
Version:	Feb2001
Release:	2
Epoch:		2
License:	BSD-like
Group:		Development/Languages
Source0:	http://www.cse.ogi.edu/PacSoft/projects/Hugs/downloads/%{name}-%{version}.tar.gz
URL:		http://www.haskell.org/hugs/
Provides:	hugs
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.1
BuildRequires:	automake
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hugs 98 is an interpreter for Haskell, a lazy functional programming
language.

%description -l pl
Hugs 98 jest interpreterem Haskella - funkcjonalnego jêzyka
programowania.

%prep
%setup -q

%build
cd src/unix
aclocal
%configure2_13 \
	--with-readline \
	--enable-internal-prims
cd ..
%{__make} OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} -C src install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	execprefix=$RPM_BUILD_ROOT%{_execprefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

mv -f $RPM_BUILD_ROOT%{_datadir}/hugs/demos \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf docs/{ffi*,obser*,zip*} License Readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.html docs/*.gz *.gz
%attr(755,root,root) %{_bindir}/hugs
%attr(755,root,root) %{_bindir}/runhugs
%{_datadir}/hugs/*
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
