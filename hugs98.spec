%define version_txt Sep2006
%define version_dir 2006-09
Summary:	Hugs - a Haskell interpreter
Summary(pl.UTF-8):	Hugs - interpreter Haskella
Name:		hugs98
Version:	%(echo %{version_dir} | tr -d -)
Release:	1
Epoch:		2
License:	BSD-like
Group:		Development/Languages
Source0:	http://cvs.haskell.org/Hugs/downloads/%{version_dir}/%{name}-plus-%{version_txt}.tar.gz
# Source0-md5:	e03e0ad79750d037237c47ebe33fa20e
Patch0:		%{name}-tinfo.patch
URL:		http://haskell.org/hugs/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	freealut-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.1
BuildRequires:	sgml-common
BuildRequires:	xorg-lib-libX11-devel
Provides:	hugs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hugs 98 is a functional programming system based on Haskell 98, the de facto
standard for non-strict functional programming languages. Hugs 98 provides an
almost complete implementation of Haskell 98, including:

* Lazy evaluation, higher order functions, and pattern matching.

* A wide range of built-in types, from characters to bignums, and lists to
  functions, with comprehensive facilities for defining new datatypes and type
  synonyms.

* An advanced polymorphic type system with type and constructor class
  overloading.

* All of the features of the Haskell 98 expression and pattern syntax including
  lambda, case, conditional and let expressions, list comprehensions,
  do-notation, operator sections, and wildcard, irrefutable and ‘as’ patterns.

* An implementation of the Haskell 98 primitives for monadic I/O, with support
  for simple interactive programs, access to text files, handle-based I/O, and
  exception handling.

* An almost complete implementation of the Haskell module system. Hugs 98 also
  supports a number of advanced and experimental extensions including
  multi-parameter classes, extensible records, rank-2 polymorphism,
  existentials, scoped type variables, and restricted type synonyms.

%description -l pl.UTF-8
Hugs 98 to interpreter języka Hakell 98, standardu de facto leniwych,
funkcyjnych języków programowania. Hugs 98 dostarcza niemal pełnej
implementacji Haskella 98, w szczególności:

* Leniwej ewaluacji, funkcji wyższych rzędów i dopasowywania wzorców.

* Szerokiego zbioru wbudowanych typów, od znaków do dużych liczb, od
  list do funkcji, z konstrukcjami językowymi do definiowania nowych
  typów i synonimów typów.

* Zaawansowanego polimorficznego systemu typów, z przeciążaniem za
  pomocą klas typów i klas konstruktorów typów.

* Wszelkich elementów składni wyrażeń i wzorców Haskella 98,
  w tym lambdy, case, wyrażeń warunkowych, let, składania list
  (list comprehensions), notacji „do”, sekcji operatorów, wzorców
  „_”, „~” i „@”.

* Implementacji funkcji pierwotnych Haskella 98 dotyczących
  monadycznego we/wy, ze wsparciem dla prostych programów
  interakcyjnych, dostępem do plików tekstowych, we/wy opartym na
  uchwytach i obsługą wyjątków.

* Niemal pełnej implementacji systemu modułów Haskella. Hugs 98
  wspiera także wiele zaawansowanych i eksperymentalnych rozszerzeń
  jezyka: wieloparametrowe klasy, rozszerzalne rekordy, polimorfizm
  rzędu 2, kwantyfikatory egzystencjalne, lokalne zmienne typowe
  i synonimy typów o zakresie stosowania ograniczonym do danego kodu.

%prep
%setup -q -n %{name}-plus-%{version_txt}
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--enable-ffi \
	--with-pthreads

%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install_all_but_docs
%{__make} -C docs DESTDIR=$RPM_BUILD_ROOT install_man

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a hugsdir/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

find $RPM_BUILD_ROOT%{_libdir}/hugs -name "*.so" | xargs chmod +x
# For Requires

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Credits Readme docs/{ffi,libraries}-notes.txt docs/*.html
%doc docs/users_guide/users_guide
%attr(755,root,root) %{_bindir}/*
%{_libdir}/hugs
%{_datadir}/hsc2hs-*
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}
