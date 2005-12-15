#
# Conditional build:
%bcond_with	gconf		# build without gconf support
%bcond_with	gnome_vfs	# build without GNOME VFS support
#
Summary:	Sound player with the WinAmp GUI, for Unix-based systems for GTK+2
Summary(pl):	Odtwarzacz d¼wiêku z interfejsem WinAmpa dla GTK+2
Name:		audacious
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://audacious.nenolod.net/release/%{name}-%{version}.tgz
# Source0-md5:	df8ebff8d60c5d48d2685dd4bb06ad88
Source1:	mp3license
Source2:	%{name}.png
Patch0:		%{name}-xmms-skins-dir.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-home_etc.patch
URL:		http://audacious.nenolod.net/
%{?with_gconf:BuildRequires:  GConf2-devel >= 2.6.0}
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.8
BuildRequires:	flac-devel >= 1.1.2
%{?with_gnome_vfs:BuildRequires:  gnome-vfs2-devel >= 2.6.0}
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	home-etc-devel
BuildRequires:	id3lib-devel
BuildRequires:	libglade2-devel >= 2.3.1
BuildRequires:	libmodplug-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsidplay-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvisual
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	lirc-devel
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	audacious-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audacious is a media player based on BMP. Since the development of the
former project had been terminated, this fork was created.

%description -l pl
Audacious to odtwarzacz mediów oparty na BMP. Powsta³ on poniewa¿
rozwój pierwowzoru zosta³ zakoñczony.

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
Summary(pl):	Pliki nag³ówkowe odtwarzacza multimedialnego Audacious
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.0
Requires:	home-etc-devel

%description devel
Header files required for compiling Audacious media player plugins.

%description devel -l pl
Pliki nag³ówkowe potrzebne do kompilowania wtyczek odtwarzacza
multimedialnego Audacious.

%package static
Summary:	Audacious media player static library
Summary(pl):	Statyczna biblioteka odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of Audacious media player library.

%description static -l pl
Statyczna wersja biblioteki odtwarzacza multimedialnego Audacious.


%package effect-ladspa
Summary:	Audacious media player - LADSPA plugin
Summary(pl):	Wtyczka LADSPA odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description effect-ladspa
LADSPA plugin for Audacious media player.

%description effect-ladspa -l pl
Wtyczka LADSPA dla odtwarzacza multimedialnego Audacious.

%package general-lirc
Summary:	Audacious media player - LIRC plugin
Summary(pl):	Wtyczka LIRC odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description general-lirc
LIRC plugin for Audacious media player.

%description general-lirc -l pl
Wtyczka LIRC dla odtwarzacza multimedialnego Audacious.

%package general-song-change
Summary:	Audacious media player - song change plugin
Summary(pl):	Wtyczka zmiany utworu odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description general-song-change
Song change plugin for Audacious media player.

%description general-song-change -l pl
Wtyczka zmiany utworu dla odtwarzacza multimedialnego Audacious.

%package input-aac
Summary:	Audacious media player - AAC input plugin
Summary(pl):	Wtyczka do odtwarzania plików AAC odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description input-aac
AAC input plugin for Audacious media player.

%description input-aac -l pl
Wtyczka dla odtwarzacza multimedialnego Audacious do obs³ugi plików
AAC.

%package input-cdaudio
Summary:	Audacious media player - cdaudio input plugin
Summary(pl):	Wtyczka wej¶ciowa cdaudio odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-cdaudio
cdaudio input plugin for Audacious media player.

%description input-cdaudio -l pl
Wtyczka wej¶ciowa cdaudio dla odtwarzacza multimedialnego Audacious.

%package input-console
Summary:	Audacious media player - console input plugin
Summary(pl):	Wtyczka do odtwarzania plików konsolowych odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description input-console
SPC, GYM, NSF, VGM and GBS input plugin for Audacious media player.

%description input-console -l pl
Wtyczka dla odtwarzacza multimedialnego Audacious do obs³ugi plików
SPC, GYM, NSF, VGM i GBS.

%package input-flac
Summary:	Audacious media player - FLAC input plugin
Summary(pl):	Wtyczka do odtwarzania plików FLAC odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description input-flac
FLAC input plugin for Audacious media player.

%description input-flac -l pl
Wtyczka dla odtwarzacza multimedialnego Audacious do obs³ugi plików
FLAC.

%package input-modplug
Summary:	Audacious media player - modplug input plugin
Summary(pl):	Wtyczka wej¶ciowa modplug odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	audacious-input-mikmod

%description input-modplug
modplug input plugin for Audacious media player.

%description input-modplug -l pl
Wtyczka wej¶ciowa modplug dla odtwarzacza multimedialnego Audacious.

%package input-mpg123
Summary:	Audacious media player - mpg123 input plugin
Summary(pl):	Wtyczka wej¶ciowa mpg123 odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-mpg123
mpg123 input plugin for Audacious media player.

%description input-mpg123 -l pl
Wtyczka wej¶ciowa mpg123 dla odtwarzacza multimedialnego Audacious.

%package input-sid
Summary:	Audacious media player - SID input plugin
Summary(pl):	Wtyczka wej¶ciowa SID odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-sid
SID input plugin for Audacious media player.

%description input-sid -l pl
Wtyczka wej¶ciowa SID dla odtwarzacza multimedialnego Audacious.

%package input-tonegen
Summary:	Audacious media player - input plugin to generate sound of given frequency
Summary(pl):	Wtyczka do generowania d¼wiêków o danej czêstotliwo¶ci odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description input-tonegen
Input plugin to generate sound of given frequency for Audacious media
player.

%description input-tonegen -l pl
Wtyczka do generowania d¼wiêków o danej czêstotliwo¶ci dla odtwarzacza
multimedialnego Audacious.

%package input-vorbis
Summary:	Audacious media player - Vorbis input plugin
Summary(pl):	Wtyczka wej¶ciowa Vorbis odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-vorbis
Vorbis input plugin for Audacious media player.

%description input-vorbis -l pl
Wtyczka wej¶ciowa Vorbis dla odtwarzacza multimedialnego Audacious.

%package input-wav
Summary:	Audacious media player - WAV input plugin
Summary(pl):	Wtyczka do odtwarzania plików WAV odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description input-wav
WAV input plugin for Audacious media player.

%description input-wav -l pl
Wtyczka dla odtwarzacza multimedialnego Audacious do obs³ugi plików
WAV.

%package input-wma
Summary:	Audacious media player - WMA input plugin
Summary(pl):	Wtyczka do odtwarzania plików WMA odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description input-wma
WMA input plugin for Audacious media player.

%description input-wma -l pl
Wtyczka dla odtwarzacza multimedialnego Audacious do obs³ugi plików
WMA.

%package output-alsa
Summary:	Audacious media player - ALSA output plugin
Summary(pl):	Wtyczka wyj¶ciowa ALSA odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	audacious-output-plugin
Obsoletes:	audacious-output-ALSA

%description output-alsa
Output ALSA plugin for Audacious media player.

%description output-alsa -l pl
Wtyczka wyj¶ciowa ALSA dla odtwarzacza multimedialnego Audacious.

%package output-crossfade
Summary:	Audacious media player - crossfade output plugin
Summary(pl):	Wtyczka wyj¶ciowa crossfade odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description output-crossfade
Output crossfade plugin for Audacious media player.

%description output-crossfade -l pl
Wtyczka wyj¶ciowa crossfade dla odtwarzacza multimedialnego Audacious.

%package output-oss
Summary:	Audacious media player - OSS output plugin
Summary(pl):	Wtyczka wyj¶ciowa OSS odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	audacious-output-plugin
Obsoletes:	audacious-output-OSS

%description output-oss
Output OSS plugin for Audacious media player.

%description output-oss -l pl
Wtyczka wyj¶ciowa OSS dla odtwarzacza multimedialnego Audacious.

%package output-disk
Summary:	Audacious media player - disk-writer output plugin
Summary(pl):    Wtyczka wyj¶ciowa zapisu na dysk odtwarzacza multimedialnego Audacious
Group:          X11/Applications/Sound
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       audacious-output-plugin

%description output-disk
Output disk-writer plugin for Audacious media player.

%description output-disk -l pl
Wtyczka wyj¶ciowa zapisu na dysk dla odtwarzacza multimedialnego
Audacious.

%package output-esd
Summary:	Audacious media player - esd output plugin
Summary(pl):	Wtyczka wyj¶ciowa esd odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	audacious-output-plugin

%description output-esd
Output esd plugin for Audacious media player.

%description output-esd -l pl
Wtyczka wyj¶ciowa esd dla odtwarzacza multimedialnego Audacious.

%package visualization-blur-scope
Summary:	Audacious media player - Blur scope visualization plugin
Summary(pl):	Wtyczka graficzna Blur scope odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description visualization-blur-scope
Blur scope visualization plugin.

%description visualization-blur-scope -l pl
Wtyczka graficzna Blur scope.

%package visualization-libvisual-proxy
Summary:	Audacious media player - libvisual-proxy visualization plugin
Summary(pl):	Wtyczka graficzna libvisual-proxy odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description visualization-libvisual-proxy
libvisual-proxy visualization plugin.

%description visualization-libvisual-proxy -l pl
Wtyczka graficzna libvisual-proxy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
%ifarch %{ix86}
%ifnarch i386 i486
	--enable-simd \
%endif
%else
	--disable-simd \
%endif
%if %{with gnome_vfs}
	--enable-gnome-vfs \
%endif
%if %{with gconf}
	--enable-gconf \
%endif
	--enable-shared \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/audacious/General,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/audacious/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
Remember to install appropriate input plugins for files
you want to play!
EOF

umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
if [ $1 = 0 ]; then
    umask 022
    [ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audacious
%dir %{_libdir}/audacious
%dir %{_libdir}/audacious/General
%dir %{_libdir}/audacious/Input
%dir %{_libdir}/audacious/Output
%dir %{_libdir}/audacious/Visualization

%{_mandir}/man*/*

%dir %{_datadir}/audacious
%dir %{_datadir}/audacious/glade
%dir %{_datadir}/audacious/images
%dir %{_datadir}/audacious/Skins
%{_datadir}/audacious/glade/*
%{_datadir}/audacious/images/*
%{_datadir}/audacious/Skins/Default
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudacious.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudacious.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files effect-ladspa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/libladspa.so

%files general-lirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/liblirc.so

%files general-song-change
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libsong_change.so

%files input-aac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libaac.so

%files input-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libcdaudio.so

%files input-console
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libconsole.so

%files input-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libflac.so

%files input-modplug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmodplug.so

%files input-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libsid.so

%files input-tonegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libtonegen.so

%files input-mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmpg123.so

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libvorbis.so

%files input-wav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libwav.so

%files input-wma
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libwma.so

%files output-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libALSA.so

%files output-crossfade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libcrossfade.so*

%files output-disk
%defattr(644,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libdisk_writer.so

%files output-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libesdout.so

%files output-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libOSS.so

%files visualization-blur-scope
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/libbscope.so

%files visualization-libvisual-proxy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/libvisual_proxy.so
