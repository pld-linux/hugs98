Summary:	Hugs - a Haskell interpreter
Name:		hugs98
Version:	Nov1999
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://ftp.cs.nott.ac.uk/pub/haskell/hugs/Hugs98-%{version}.tar.gz
Provides:	hugs
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hugs is a (nearly) Haskell 1.4 interpreter.

%prep
%setup -q -n %{name}

%build
cd src/unix
%configure \
	--with-readline \
	--enable-internal-prims
cd ..
%{__make} OPTFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} -C src install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	execprefix=$RPM_BUILD_ROOT%{_execprefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}

# install docs by hand
install docs/hugs.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf docs/{server.tex,windows-notes.txt} License Readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/server.html docs/{server.tex,windows-notes.txt}.gz License* Readme*
%attr(755,root,root) %{_bindir}/hugs
%attr(755,root,root) %{_bindir}/runhugs
%{_datadir}/hugs/*
%{_mandir}/man1/*
