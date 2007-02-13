
%define		sname	gift

Summary:	The generic interface to FastTrack
Summary(pl.UTF-8):	Interfejs do FastTracka
Name:		giFT
Version:	0.11.8.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gift/%{sname}-%{version}.tar.bz2
# Source0-md5:	1c70477af403af142359d07ee4a03348
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-createdirs.patch
URL:		http://giFT.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	db-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmagic-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The generic interface to FastTrack network. This package contains
'giFT' daemon. After running it you can use some FT client e.g.:
'fiFT-fe' GTK+ client or 'giFTcurs' ncurses client (provided by
package giFTcurs).

%description -l pl.UTF-8
Ogólny interfejs do sieci FastTrack. Ten pakiet zawiera demona giFT.
Po jego uruchomieniu można używać któregoś z klientów FT, np. giFT-fe
opartego na GTK+ czy giFTcurs opartego na ncurses (dostępnego w
pakiecie giFTcurs).

%package devel
Summary:	The generic interface to FastTrack development files
Summary(pl.UTF-8):	Pliki do rozwoju programów korzystających z giFT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel

%description devel
The generic interface to FastTrack development files.

%description devel -l pl.UTF-8
Pliki do rozwoju programów korzystającego z interfejsu do FastTracka.

%package static
Summary:	The generic interface to FastTrack static libraries
Summary(pl.UTF-8):	Biblioteki statyczne giFT
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The generic interface to FastTrack static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne interfejsu do FastTracka.

%prep
%setup -q -n %{sname}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libmagic \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mkdir $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
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
