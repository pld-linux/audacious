#
# Conditional build:
%bcond_without	gconf		# build without gconf support
%bcond_without	vfs	        # build without VFS support
#
Summary:	Sound player with the WinAmp GUI, for Unix-based systems for GTK+2
Summary(pl):	Odtwarzacz d¼wiêku z interfejsem WinAmpa dla GTK+2
Name:		audacious
Version:	0.1
Release:	0.2
License:	GPL
Group:		Applications/Sound
Source0:	http://audacious.nenolod.net/release/%{name}-%{version}.tgz
# Source0-md5:	540865e944f41a5bb082b13c6b8fd686
Source1:	mp3license
Patch0:		%{name}-xmms-skins-dir.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-home_etc.patch
URL:		http://audacious.nenolod.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.8
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	home-etc-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libglade2-devel >= 2.0.0
%if %{with gconf}
BuildRequires:  GConf2-devel >= 2.4.0
%endif
%if %{with vfs}
BuildRequires:  gnome-vfs2-devel >= 2.4.0
%endif
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
Requires:	gtk+2-devel
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

%package input-vorbis
Summary:	Audacious media player - Vorbis input plugin
Summary(pl):	Wtyczka wej¶ciowa Vorbis odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-vorbis
Vorbis input plugin for Audacious media player.

%description input-vorbis -l pl
Wtyczka wej¶ciowa Vorbis dla odtwarzacza multimedialnego Audacious.

%package input-mpg123
Summary:	Audacious media player - mpg123 input plugin
Summary(pl):	Wtyczka wej¶ciowa mpg123 odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-mpg123
mpg123 input plugin for Audacious media player.

%description input-mpg123 -l pl
Wtyczka wej¶ciowa mpg123 dla odtwarzacza multimedialnego Audacious.

%package input-cdaudio
Summary:	Audacious media player - cdaudio input plugin
Summary(pl):	Wtyczka wej¶ciowa cdaudio odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-cdaudio
cdaudio input plugin for Audacious media player.

%description input-cdaudio -l pl
Wtyczka wej¶ciowa cdaudio dla odtwarzacza multimedialnego Audacious.

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

%package input-flac
Summary:	Audacious media player - FLAC input plugin
Summary(pl):	Wtyczka do odtwarzania plikow FLAC odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} >= %{epoch}:%{version}-%{release}

%description input-flac
FLAC input plugin for Audacious media player.

%description input-flac -l pl
Wtyczka dla odtwarzacza multimedialnego Audacious do obs³ugi plików
FLAC.

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

%package output-OSS
Summary:	Audacious media player - OSS output plugin
Summary(pl):	Wtyczka wyj¶ciowa OSS odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	audacious-output-plugin

%description output-OSS
Output OSS plugin for Audacious media player.

%description output-OSS -l pl
Wtyczka wyj¶ciowa OSS dla odtwarzacza multimedialnego Audacious.

%package output-ALSA
Summary:	Audacious media player - ALSA output plugin
Summary(pl):	Wtyczka wyj¶ciowa ALSA odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	audacious-output-plugin

%description output-ALSA
Output ALSA plugin for Audacious media player.

%description output-ALSA -l pl
Wtyczka wyj¶ciowa ALSA dla odtwarzacza multimedialnego Audacious.

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -rf autom4te.cache
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
%if %{with vfs}
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
install -d $RPM_BUILD_ROOT%{_libdir}/audacious/General

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

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
%attr(755,root,root) %{_libdir}/audacious/Visualization/libbscope*
%{_mandir}/man*/*
%{_desktopdir}/*
%dir %{_datadir}/audacious
%dir %{_datadir}/audacious/images
%{_datadir}/audacious/images/*
%dir %{_datadir}/audacious/Skins
%{_datadir}/audacious/Skins/Default
%dir %{_datadir}/audacious/glade
%{_datadir}/audacious/glade/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudacious.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudacious.so.*.*
%attr(755,root,root) %{_libdir}/libmp4v2.so.*.*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files input-mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmpg123*

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libvorbis*

%files input-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libcdaudio*

%files input-wav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libwav*

%files input-aac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libaac*

%files input-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libflac*

%files input-tonegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libtonegen*

%files output-OSS
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libOSS*

%files output-ALSA
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libALSA*

%files output-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libesdout*

%files output-disk
%defattr(644,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libdisk_writer*
