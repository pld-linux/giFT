Summary:	The generic interface to FastTrack
Summary(pl):	Interfejs do FastTracka
Name:		giFT
Version:	0.11.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gift/%{name}-%{version}.tar.bz2
# Source0-md5:	84a03d803abd0f93634f588e37340d6f
#Source0:	%{name}-%{version}.tar.gz
URL:		http://giFT.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The generic interface to FastTrack network. This package contains
'giFT' daemon. After running it you can use some FT client e.g.:
'fiFT-fe' gtk+ client (provided by this package) 'giFTcurs' ncurses
client (provided by package giFTcurs)

%description -l pl
Interfejs do FastTracka.

%package devel
Group:		Applications/Communications
Summary:	The generic interface to FastTrack development files
Summary(pl):	Pliki do rozwoju programów korzystaj±cych z giFT
Requires:	%{name} = %{version}

%description devel
The generic interface to FastTrack development files.

%description devel -l pl
Pliki do rozwoju programów korzystaj±cego z interfejsu do FastTracka.

%package static
Group:		Applications/Communications
Summary:	The generic interface to FastTrack static libraries
Summary(pl):	Biblioteki statyczne giFT
Requires:	%{name}-devel = %{version}

%description static
The generic interface to FastTrack static libraries.

%description static -l pl
Biblioteki statyczne interfejsu do FastTracka.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_datadir}/%{name}
%{_mandir}/man?/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
