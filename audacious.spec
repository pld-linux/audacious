Summary:	Sound player with the WinAmp GUI, for Unix-based systems for GTK+
Summary(hu.UTF-8):	Zenelejátszó WinAmp-szerű felülettel GTK+-t használó rendszerekhez
Summary(pl.UTF-8):	Odtwarzacz dźwięku z interfejsem WinAmpa dla GTK+
Name:		audacious
Version:	3.4.3
Release:	2
License:	BSD
Group:		X11/Applications/Sound
Source0:	http://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
# Source0-md5:	3935e3c1e6bdc2907ce2672a85476f20
Patch0:		%{name}-desktop.patch
URL:		http://audacious-media-player.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.6
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libguess-devel >= 1.1
BuildRequires:	libstdc++-devel
BuildRequires:	pango-devel >= 1:1.20
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
Obsoletes:	audacious-general-mtp_up
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
Obsoletes:	audacious-output-null
Obsoletes:	audacious-output-oss
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
Obsoletes:	beep-media-player
Obsoletes:	bmp
Obsoletes:	bmp-visualization-minilcd
Obsoletes:	bmp-visualization-wmdiscotux
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
Summary:	Audacious media player libraries
Summary(hu.UTF-8):	Audacious médialejátszó könyvtár
Summary(pl.UTF-8):	Biblioteki odtwarzacza multimedialnego Audacious
Group:		X11/Libraries
Requires:	cairo >= 1.6
Requires:	glib2 >= 1:2.28
Requires:	gtk+3 >= 3.0.0
Requires:	pango >= 1:1.20
Obsoletes:	beep-media-player-libs
Obsoletes:	bmp-libs

%description libs
Audacious media player libraries.

%description libs -l hu.UTF-8
Audacious médialejátszó könyvtár.

%description libs -l pl.UTF-8
Biblioteki odtwarzacza multimedialnego Audacious.

%package devel
Summary:	Header files for Audacious media player
Summary(hu.UTF-8):	Az audacious fejlécfájljai
Summary(pl.UTF-8):	Pliki nagłówkowe odtwarzacza multimedialnego Audacious
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo-devel >= 1.6
Requires:	dbus-glib-devel >= 0.60
Requires:	glib2-devel >= 1:2.28
Requires:	gtk+3-devel >= 3.0.0
Requires:	pango-devel >= 1:1.20
Obsoletes:	beep-media-player-devel
Obsoletes:	beep-media-player-static
Obsoletes:	bmp-devel
Obsoletes:	bmp-static

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
%configure \
	--enable-thunar
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/{Container,Effect,General,Input,Output,Transport,Visualization}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/fa{_IR,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/id{_ID,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ml{_IN,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/pt{_PT,}
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
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/audacious
%attr(755,root,root) %{_bindir}/audtool
%{_mandir}/man1/audacious.1*
%{_mandir}/man1/audtool.1*
%dir %{_datadir}/audacious
%{_datadir}/audacious/images
%{_desktopdir}/audacious.desktop
%{_datadir}/Thunar/sendto/thunar-sendto-audacious-playlist.desktop
%{_iconsdir}/hicolor/*/apps/audacious.*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudclient.so.2
%attr(755,root,root) %{_libdir}/libaudcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudcore.so.1
%attr(755,root,root) %{_libdir}/libaudgui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudgui.so.1
%attr(755,root,root) %{_libdir}/libaudtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudtag.so.1
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
