Summary:	Sound player with the WinAmp GUI, for Unix-based systems for GTK+2
Summary(hu.UTF-8):	Zenelejátszó WinAmp-szerű felülettel GTK+2-t használó rendszerekhez
Summary(pl.UTF-8):	Odtwarzacz dźwięku z interfejsem WinAmpa dla GTK+2
Name:		audacious
Version:	3.1
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tar.gz
# Source0-md5:	a20fdf5d0348235e0a5e22c5aca69629
Patch0:		%{name}-desktop.patch
URL:		http://audacious-media-player.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	home-etc-devel
BuildRequires:	libguess-devel
BuildRequires:	libmowgli-devel >= 0.9.0
BuildRequires:	libstdc++-devel
BuildRequires:	mcs-devel >= 0.4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-libs = %{version}-%{release}
Requires:	audacious-output-plugin
Requires:	audacious-transport-unix_io
Suggests:	%{name}-general-skins
Obsoletes:	audacious-container-mms
Obsoletes:	audacious-container-stdio
Obsoletes:	audacious-general-audioscrobbler
Obsoletes:	audacious-general-curl
Obsoletes:	audacious-general-evdev
Obsoletes:	audacious-general-lirc
Obsoletes:	audacious-general-streambrowser
Obsoletes:	audacious-general-vfstrace
Obsoletes:	audacious-input-alac
Obsoletes:	audacious-input-cdaudio
Obsoletes:	audacious-input-cube
Obsoletes:	audacious-input-demac
Obsoletes:	audacious-input-flac
Obsoletes:	audacious-input-mikmod
Obsoletes:	audacious-input-mpc
Obsoletes:	audacious-input-mpg123
Obsoletes:	audacious-input-mplayer
Obsoletes:	audacious-input-musepack
Obsoletes:	audacious-input-sap
Obsoletes:	audacious-input-timidity
Obsoletes:	audacious-input-tta
Obsoletes:	audacious-input-wav
Obsoletes:	audacious-input-wma
Obsoletes:	audacious-output-ALSA
Obsoletes:	audacious-output-OSS
Obsoletes:	audacious-output-arts
Obsoletes:	audacious-output-disk
Obsoletes:	audacious-output-icecast
Obsoletes:	audacious-output-lame
Obsoletes:	audacious-static
Obsoletes:	audacious-transport-curl
Obsoletes:	audacious-visualization-iris
Obsoletes:	audacious-visualization-moodbar
Obsoletes:	audacious-visualization-paranormal
Obsoletes:	audacious-visualization-projectM
Obsoletes:	audacious-visualization-rocklight
Obsoletes:	audacious-visualization-rootvis
Obsoletes:	audacious-visualization-rovascope
Obsoletes:	audacious-visualization-spectrum
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audacious is a media player based on BMP. Since the development of the
former project had been terminated, this fork was created.

%description -l hu.UTF-8
Audacious egy BMP-n alapuló médialejátszó. Amióta a kiinduló projekt
fejlesztése abbamaradt, ez a leszármazott létrejött.

%description -l pl.UTF-8
Audacious to odtwarzacz mediów oparty na BMP. Powstał on ponieważ
rozwój pierwowzoru został zakończony.

%package libs
Summary:	Audacious media player library
Summary(hu.UTF-8):	Audacious médialejátszó könyvtár
Summary(pl.UTF-8):	Biblioteka odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	gtk+2 >= 2:2.6.0
Requires:	libmowgli >= 0.4.0

%description libs
Audacious media player library.

%description libs -l hu.UTF-8
Audacious médialejátszó könyvtár.

%description libs -l pl.UTF-8
Biblioteka odtwarzacza multimedialnego Audacious.

%package devel
Summary:	Header files for Audacious media player
Summary(hu.UTF-8):	Az audacious fejlécfájljai
Summary(pl.UTF-8):	Pliki nagłówkowe odtwarzacza multimedialnego Audacious
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-glib-devel
Requires:	gtk+2-devel >= 2:2.6.0
Requires:	home-etc-devel
Requires:	libmowgli-devel >= 0.4.0
Requires:	mcs-devel

%description devel
Header files required for compiling Audacious media player plugins.

%description devel -l hu.UTF-8
Az audacious fejlécfájljai.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania wtyczek odtwarzacza
multimedialnego Audacious.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/{Container,Effect,General,Input,Output,Transport,Visualization}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
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
%{_mandir}/man*/*
%dir %{_datadir}/audacious
%dir %{_datadir}/audacious/images
%{_datadir}/audacious/images/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/audacious.*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.svg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudclient.so.?
%attr(755,root,root) %{_libdir}/libaudcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudcore.so.?
%attr(755,root,root) %{_libdir}/libaudgui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudgui.so.?
%attr(755,root,root) %{_libdir}/libaudtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudtag.so.?
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/Container
%dir %{_libdir}/%{name}/Effect
%dir %{_libdir}/%{name}/General
%dir %{_libdir}/%{name}/Input
%dir %{_libdir}/%{name}/Output
%dir %{_libdir}/%{name}/Transport
%dir %{_libdir}/%{name}/Visualization

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudclient.so
%attr(755,root,root) %{_libdir}/libaudcore.so
%attr(755,root,root) %{_libdir}/libaudgui.so
%attr(755,root,root) %{_libdir}/libaudtag.so
%{_includedir}/audacious
%{_includedir}/libaudcore
%{_includedir}/libaudgui
%{_pkgconfigdir}/audacious.pc
%{_pkgconfigdir}/audclient.pc
