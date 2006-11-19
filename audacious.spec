#
# Conditional build:
%bcond_with	gconf		# build without gconf support
#
Summary:	Sound player with the WinAmp GUI, for Unix-based systems for GTK+2
Summary(pl):	Odtwarzacz d�wi�ku z interfejsem WinAmpa dla GTK+2
Name:		audacious
Version:	1.2.2
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://audacious-media-player.org/release/%{name}-%{version}.tgz
# Source0-md5:	e774afbda04220e6e1b0a9bff350522e
Source1:	mp3license
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-home_etc.patch
URL:		http://audacious-media-player.org/
%{?with_gconf:BuildRequires:	GConf2-devel >= 2.6.0}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	gettext-devel
BuildRequires:	home-etc-devel
BuildRequires:	libglade2-devel >= 2.3.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires:	%{name}-libs = %{version}-%{release}
Requires:	audacious-output-plugin
Requires(post,postun):	desktop-file-utils
Obsoletes:	audacious-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audacious is a media player based on BMP. Since the development of the
former project had been terminated, this fork was created.

%description -l pl
Audacious to odtwarzacz medi�w oparty na BMP. Powsta� on poniewa�
rozw�j pierwowzoru zosta� zako�czony.

%package libs
Summary:	Audacious media player library
Summary(pl):	Biblioteka odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound

%description libs
Audacious media player library.

%description libs -l pl
Biblioteka odtwarzacza multimedialnego Audacious.

%package devel
Summary:	Header files for Audacious media player
Summary(pl):	Pliki nag��wkowe odtwarzacza multimedialnego Audacious
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.6.0
Requires:	home-etc-devel

%description devel
Header files required for compiling Audacious media player plugins.

%description devel -l pl
Pliki nag��wkowe potrzebne do kompilowania wtyczek odtwarzacza
multimedialnego Audacious.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	--%{?with_gconf:en}%{!?with_gconf:dis}able-gconf \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/audacious/{Container,Effect,General,Input,Output,Visualization}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
Remember to install appropriate input plugins for files
you want to play!
EOF

%update_desktop_database_post

%postun
%update_desktop_database_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audacious
%attr(755,root,root) %{_bindir}/audtool
%dir %{_libdir}/audacious
%dir %{_libdir}/audacious/Container
%dir %{_libdir}/audacious/Effect
%dir %{_libdir}/audacious/General
%dir %{_libdir}/audacious/Input
%dir %{_libdir}/audacious/Output
%dir %{_libdir}/audacious/Visualization

%{_mandir}/man*/*

%dir %{_datadir}/audacious
%{_datadir}/audacious/glade
%dir %{_datadir}/audacious/images
%{_datadir}/audacious/images/*
%{_datadir}/audacious/Skins
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudacious.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudacious.so
%{_includedir}/audacious
%{_pkgconfigdir}/audacious.pc
