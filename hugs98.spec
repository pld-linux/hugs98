Summary:	Hugs - a Haskell interpreter
Summary(pl.UTF-8):   Hugs - interpreter Haskella
Name:		hugs98
Version:	Nov2003
Release:	3
Epoch:		2
License:	BSD-like
Group:		Development/Languages
Source0:	http://cvs.haskell.org/Hugs/downloads/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	86ed68ada4ff1d455213a851256437fc
Patch0:		%{name}-docbook.patch
URL:		http://www.haskell.org/hugs/
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.1
Provides:	hugs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hugs 98 is an interpreter for Haskell, a lazy functional programming
language.

%description -l pl.UTF-8
Hugs 98 jest interpreterem Haskella - leniwego, funkcyjnego języka
programowania.

%prep
%setup -q
%patch0 -p1

%build
cd src/unix
cp -f /usr/share/automake/config.* .
%configure \
	--target= \
	--with-readline \
	--with-pthreads \
	--with-preprocessor \
	--enable-internal-prims \
	--enable-ffi
cd ..
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

cd src
# hack to make it build with different final location
HUGSDIR=..
export HUGSDIR
cp HsFFI.h ../include
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..

rm -rf $RPM_BUILD_ROOT%{_libdir}/hugs/{docs,Credits,License,Readme}
mv $RPM_BUILD_ROOT%{_libdir}/hugs/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.html docs/{ffi,libraries}-notes.txt License Readme Credits
%attr(755,root,root) %{_bindir}/hugs
%attr(755,root,root) %{_bindir}/ffihugs
%attr(755,root,root) %{_bindir}/runhugs
%{_libdir}/hugs
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}
