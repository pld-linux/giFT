Summary:	The generic interface to FastTrack
Summary(pl):	Interfejs do FastTracka
Name:		giFT
Version:	0.9.7
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
The generic interface to FastTrack.

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
The generic interface to FastTrack development files

%package static
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Summary:	The generic interface to FastTrack static libraries
Requires:	%{name}-devel = %{version}

%description static
The generic interface to FastTrack static libraries

%prep
%setup -q

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

gzip -9nf README AUTHORS COPYING TODO ChangeLog INSTALL NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/giFT
%{_includedir}/giFT/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
