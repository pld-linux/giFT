Summary:	The generic interface to FastTrack
Name:		giFT
Version:	0.9.7
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	%{name}-%{version}.tar.gz
URL:		http://giFT.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The generic interface to FastTrack

%package devel
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Summary:	The generic interface to FastTrack development files
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
