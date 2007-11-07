#
# Conditional build:
%bcond_with	gconf		# build without gconf support

Summary:	Sound player with the WinAmp GUI, for Unix-based systems for GTK+2
Summary(pl.UTF-8):	Odtwarzacz dźwięku z interfejsem WinAmpa dla GTK+2
Name:		audacious
Version:	1.4.0
Release:	0.2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tbz2
# Source0-md5:	75b34e88cd2c4b335a2f18070bae56f6
Source1:	mp3license
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-home_etc.patch
URL:		http://audacious-media-player.org/
%{?with_gconf:BuildRequires:	GConf2-devel >= 2.6.0}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	home-etc-devel
BuildRequires:	libglade2-devel >= 2.3.1
BuildRequires:	libmowgli-devel >= 0.4.0
BuildRequires:	libsamplerate-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mcs-devel >= 0.4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-libs = %{version}-%{release}
Requires:	audacious-output-plugin
Obsoletes:	audacious-container-mms
Obsoletes:	audacious-container-stdio
Obsoletes:	audacious-general-audioscrobbler
Obsoletes:	audacious-general-curl
Obsoletes:	audacious-input-cdaudio
Obsoletes:	audacious-input-flac
Obsoletes:	audacious-input-mikmod
Obsoletes:	audacious-input-mpc
Obsoletes:	audacious-input-mpg123
Obsoletes:	audacious-input-sap
Obsoletes:	audacious-output-ALSA
Obsoletes:	audacious-output-OSS
Obsoletes:	audacious-output-disk
Obsoletes:	audacious-output-lame
Obsoletes:	audacious-static
Obsoletes:	audacious-transport-curl
Obsoletes:	audacious-visualization-rovascope
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audacious is a media player based on BMP. Since the development of the
former project had been terminated, this fork was created.

%description -l pl.UTF-8
Audacious to odtwarzacz mediów oparty na BMP. Powstał on ponieważ
rozwój pierwowzoru został zakończony.

%package libs
Summary:	Audacious media player library
Summary(pl.UTF-8):	Biblioteka odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound

%description libs
Audacious media player library.

%description libs -l pl.UTF-8
Biblioteka odtwarzacza multimedialnego Audacious.

%package devel
Summary:	Header files for Audacious media player
Summary(pl.UTF-8):	Pliki nagłówkowe odtwarzacza multimedialnego Audacious
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.6.0
Requires:	home-etc-devel
Requires:	mcs-devel

%description devel
Header files required for compiling Audacious media player plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania wtyczek odtwarzacza
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
	--enable-samplerate \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/{Container,Effect,General,Input,Output,Transport,Visualization}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# there is already .desktop in %{_desktopdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/audacious/applications

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
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
%{_datadir}/audacious/glade
%dir %{_datadir}/audacious/images
%{_datadir}/audacious/images/*
%{_datadir}/audacious/Skins
%{_datadir}/audacious/ui
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudclient.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libaudclient.so.?
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/Container
%dir %{_libdir}/%{name}/Effect
%dir %{_libdir}/%{name}/General
%dir %{_libdir}/%{name}/Input
%dir %{_libdir}/%{name}/Output
%dir %{_libdir}/%{name}/Transport
%dir %{_libdir}/%{name}/Visualization
%attr(755,root,root) %{_libdir}/%{name}/libaudid3tag.so.*.*.*
%attr(755,root,root) %{_libdir}/%{name}/libaudid3tag.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudclient.so
%attr(755,root,root) %{_libdir}/%{name}/libaudid3tag.so
%{_includedir}/audacious
%{_pkgconfigdir}/audacious.pc
%{_pkgconfigdir}/audclient.pc
