#
# Conditional build:
%bcond_without	gtk	# GTK+ support
%bcond_without	qt	# Qt support
#
Summary:	Sound player with the WinAmp GUI, for GTK+/Qt
Summary(hu.UTF-8):	Zenelejátszó WinAmp-szerű felülettel GTK+/Qt-t használó rendszerekhez
Summary(pl.UTF-8):	Odtwarzacz dźwięku z interfejsem WinAmpa dla GTK+/Qt
Name:		audacious
Version:	4.3.1
Release:	1
License:	BSD
Group:		X11/Applications/Sound
Source0:	https://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
# Source0-md5:	751a002964907c3a8fc2f571ffc00ec7
URL:		https://audacious-media-player.org/
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5.2
BuildRequires:	Qt5Gui-devel >= 5.2
BuildRequires:	Qt5Widgets-devel >= 5.2
BuildRequires:	qt5-build >= 5.2
%endif
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_cairo:BuildRequires:	cairo-devel >= 1.6}
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.32
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.24}
BuildRequires:	libguess-devel >= 1.2
# -std=gnu++11 is minimum, -std=gnu++17 preferred
BuildRequires:	libstdc++-devel >= 6:4.7
%{?with_gtk:BuildRequires:	pango-devel >= 1:1.20}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-libs = %{version}-%{release}
Requires:	audacious-output-plugin
Suggests:	audacious-general-gtkui = %{version}-%{release}
Suggests:	audacious-general-qtui = %{version}-%{release}
Obsoletes:	audacious-container-mms < 1.4
Obsoletes:	audacious-container-stdio < 1.4
Obsoletes:	audacious-effect-mixdown < 3.1
Obsoletes:	audacious-general-curl < 1.4
Obsoletes:	audacious-general-evdev < 3.0
Obsoletes:	audacious-general-gnomeshortcuts < 3.10
Obsoletes:	audacious-general-mtp_up < 3.3
Obsoletes:	audacious-general-streambrowser < 3.0
Obsoletes:	audacious-general-vfstrace < 2.4
Obsoletes:	audacious-input-alac < 2.3
Obsoletes:	audacious-input-cube < 1.4
Obsoletes:	audacious-input-demac < 2.3
Obsoletes:	audacious-input-sap < 1.4
Obsoletes:	audacious-input-timidity < 2.3
Obsoletes:	audacious-input-tta < 2.3
Obsoletes:	audacious-input-wma < 2.3
Obsoletes:	audacious-output-OSS < 0.1.1-1
Obsoletes:	audacious-output-disk < 1.4
Obsoletes:	audacious-output-icecast < 2.4
Obsoletes:	audacious-output-lame < 1.4
Obsoletes:	audacious-output-null < 3.3
Obsoletes:	audacious-static < 1.2
Obsoletes:	audacious-transport-curl < 1.4
Obsoletes:	audacious-transport-lastfm < 2.3
Obsoletes:	audacious-transport-unix_io < 3.6
Obsoletes:	audacious-visualization-iris < 1.4
Obsoletes:	audacious-visualization-libvisual-proxy < 1.1
Obsoletes:	audacious-visualization-moodbar < 3.1
Obsoletes:	audacious-visualization-paranormal < 3.0
Obsoletes:	audacious-visualization-projectM < 3.0
Obsoletes:	audacious-visualization-rocklight < 3.1
Obsoletes:	audacious-visualization-rootvis < 2.1
Obsoletes:	audacious-visualization-rovascope < 1.4
Obsoletes:	audacious-visualization-spectrum < 3.0
Obsoletes:	beep-media-player < 1
Obsoletes:	bmp < 1
Obsoletes:	bmp-visualization-minilcd < 1
Obsoletes:	bmp-visualization-wmdiscotux < 1
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
Obsoletes:	beep-media-player-libs < 1
Obsoletes:	bmp-libs < 1

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
Obsoletes:	beep-media-player-devel < 1
Obsoletes:	beep-media-player-static < 1
Obsoletes:	bmp-devel < 1
Obsoletes:	bmp-static < 1

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
Pliki nagłówkowe graficznego interfejsu Qt odtwarzacza multimedialnego
Audacious.

%prep
%setup -q

# verbose build
%{__sed} -i -e '/^\.SILENT:/d' -e '/MAKE/ s/ -s / /' buildsys.mk.in

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	%{!?with_gtk:--disable-gtk} \
	%{!?with_qt:--disable-qt}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/{Container,Effect,General,Input,Output,Transport,Visualization}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/audacious/{AUTHORS,COPYING}
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/audacious.desktop
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

From version 4.0 audacious by default uses QT interface.
To use audacious with GTK interface, run: audacious -G.

EOF

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
