#
# Conditional build:
%bcond_without	gtk	# GTK+ support
%bcond_without	qt	# Qt support
#
Summary:	Sound player with the WinAmp GUI, for GTK+/Qt
Summary(hu.UTF-8):	Zenelejátszó WinAmp-szerű felülettel GTK+/Qt-t használó rendszerekhez
Summary(pl.UTF-8):	Odtwarzacz dźwięku z interfejsem WinAmpa dla GTK+/Qt
Name:		audacious
Version:	3.9
Release:	1
License:	BSD
Group:		X11/Applications/Sound
Source0:	http://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
# Source0-md5:	11d2b36f66c79e60ada9e1f6208abf19
URL:		http://audacious-media-player.org/
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5.2
BuildRequires:	Qt5Gui-devel >= 5.2
BuildRequires:	Qt5Widgets-devel >= 5.2
%endif
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_cairo:BuildRequires:	cairo-devel >= 1.6}
BuildRequires:	gettext-tools
# -std=gnu++11
BuildRequires:	gcc-c++ >= 6:4.7
BuildRequires:	glib2-devel >= 1:2.32
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.24}
BuildRequires:	libguess-devel >= 1.2
BuildRequires:	libstdc++-devel >= 6:4.7
%{?with_gtk:BuildRequires:	pango-devel >= 1:1.20}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-libs = %{version}-%{release}
Requires:	audacious-output-plugin
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
Obsoletes:	audacious-transport-unix_io
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
Group:		Libraries
%{?with_qt:Requires:	Qt5Core >= 5.2}
Requires:	glib2 >= 1:2.32
Requires:	libguess >= 1.2
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
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32
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

%package libs-gtk
Summary:	Audacious GTK+ GUI library
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu GTK+ odtwarzacza multimedialnego Audacious
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo >= 1.6
Requires:	gtk+2 >= 2:2.24
Requires:	pango >= 1:1.20

%description libs-gtk
Audacious GTK+ GUI library.

%description libs-gtk -l pl.UTF-8
Biblioteka graficznego interfejsu GTK+ odtwarzacza multimedialnego
Audacious.

%package libs-gtk-devel
Summary:	Header files for Audacious GTK+ GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe graficznego interfejsu GTK+ odtwarzacza multimedialnego Audacious
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-libs-gtk = %{version}-%{release}
Requires:	cairo-devel >= 1.6
Requires:	gtk+2-devel >= 2:2.24
Requires:	pango-devel >= 1:1.20

%description libs-gtk-devel
Header files for Audacious GTK+ GUI library.

%description libs-gtk-devel -l pl.UTF-8
Pliki nagłówkowe graficznego interfejsu GTK+ odtwarzacza
multimedialnego Audacious.

%package libs-qt
Summary:	Audacious Qt GUI library
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu Qt odtwarzacza multimedialnego Audacious
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	Qt5Gui >= 5.2
Requires:	Qt5Widgets >= 5.2

%description libs-qt
Audacious Qt GUI library.

%description libs-qt -l pl.UTF-8
Biblioteka graficznego interfejsu Qt odtwarzacza multimedialnego
Audacious.

%package libs-qt-devel
Summary:	Header files for Audacious Qt GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe graficznego interfejsu Qt odtwarzacza multimedialnego Audacious
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-libs-qt = %{version}-%{release}
Requires:	Qt5Gui-devel >= 5.2
Requires:	Qt5Widgets-devel >= 5.2

%description libs-qt-devel
Header files for Audacious Qt GUI library.

%description libs-qt-devel -l pl.UTF-8
Pliki nagłówkowe graficznego interfejsu Qt odtwarzacza
multimedialnego Audacious.

%prep
%setup -q

# verbose build
%{__sed} -i '/^\.SILENT:/d' buildsys.mk.in

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	%{!?with_gtk:--disable-gtk} \
	%{?with_qt:--enable-qt} \
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
# outdated version of sr
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sr_RS
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

%post	libs-gtk -p /sbin/ldconfig
%postun	libs-gtk -p /sbin/ldconfig

%post	libs-qt -p /sbin/ldconfig
%postun	libs-qt -p /sbin/ldconfig

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
%{_iconsdir}/hicolor/*/apps/audacious.*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudcore.so.5
%attr(755,root,root) %{_libdir}/libaudtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudtag.so.3
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
%attr(755,root,root) %{_libdir}/libaudcore.so
%attr(755,root,root) %{_libdir}/libaudtag.so
%{_includedir}/audacious
%{_includedir}/libaudcore
%{_pkgconfigdir}/audacious.pc

%if %{with gtk}
%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudgui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudgui.so.5

%files libs-gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudgui.so
%{_includedir}/libaudgui
%endif

%if %{with qt}
%files libs-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudqt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudqt.so.2

%files libs-qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudqt.so
%{_includedir}/libaudqt
%endif
