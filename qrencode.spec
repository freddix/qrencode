Summary:	QR Code encoder into PNG image
Name:		qrencode
Version:	3.4.1
Release:	1
License:	LGPL v2.1+
Group:		Applications/File
Source0:	http://megaui.net/fukuchi/works/qrencode/%{name}-%{version}.tar.bz2
# Source0-md5:	219b146d3b365a56a0f4ef58a718f295
URL:		http://megaui.net/fukuchi/works/qrencode/index.en.html
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qrencode is a utility software using libqrencode to encode string data
in a QR Code and save as a PNG image.

%package libs
Summary:	A C library for encoding data in a QR Code symbol
Group:		Libraries

%description libs
qrencode library.

%package devel
Summary:	The development files for the qrencode library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the development files for the qrencode library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-tests
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qrencode
%{_mandir}/man1/qrencode.1*

%files libs
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libqrencode.so.3
%attr(755,root,root) %{_libdir}/libqrencode.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqrencode.so
%{_includedir}/qrencode.h
%{_pkgconfigdir}/libqrencode.pc

