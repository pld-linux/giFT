Summary:	The generic interface to FastTrack
Summary(pl):	Interfejs do FastTracka
Name:		giFT
Version:	0.10.0.cvs20020202
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/gift/%{name}-%{version}.tar.gz
URL:		http://giFT.sourceforge.net
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The generic interface to FastTrack network.
This package contains 'giFT' daemon.
After running it you can use some FT client e.g.:
'fiFT-fe' gtk+ client (provided by this package)
'giFTcurs' ncurses client (provided by package giFTcurs)

%description -l pl
Interfejs do FastTracka.

%package devel
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Summary:	The generic interface to FastTrack development files
Summary(pl):	Pliki developerskie dla giFT
Requires:	%{name} = %{version}

%description devel
The generic interface to FastTrack development files.

%description devel -l pl
Pliki developerskie interfejsu do FastTracka.

%package static
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Summary:	The generic interface to FastTrack static libraries
Requires:	%{name}-devel = %{version}

%description static
The generic interface to FastTrack static libraries.

%description static -l pl
Biblioteki statyczne interfejsu do FastTracka.

%prep
%setup -q -n giFT-0.10.0

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install
#install -d $RPM_BUILD_ROOT%{_includedir}
#cp -a lib/

gzip -9nf README AUTHORS COPYING TODO ChangeLog INSTALL NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
# cvs version does not install includes /klakier
# commented temporarily
#%dir %{_includedir}/giFT
#%{_includedir}/giFT/*.h

%files static
%defattr(644,root,root,755)
# this also does not build
#%{_libdir}/*.a
