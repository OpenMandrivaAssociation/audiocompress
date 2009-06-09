%define name AudioCompress
%define version 1.5.2
%define release %mkrel 4

Summary:		Simple dynamic range compressor
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source:			http://trikuare.cx/~magenta/projects/%{name}-%{version}.tar.bz2
#	1.3-3mdk: Disable debugging in compilation
#	1.3-4mdk: Add optflags...
#	1.5-1mdk: Regenerate...
Patch0:			AudioCompress-1.5-1mdk-Makefile.patch.bz2
#	1.5-2mdk: Disable monitor by default
Patch1:			AudioCompress-1.5-2mdk-Monitor.patch.bz2
License:		LGPL
Group:			Sound
BuildRequires:	xmms-devel, gtk+-devel, esound-devel
BuildRoot:		%{_tmppath}/%{name}-buildroot

URL:			http://trikuare.cx/code/AudioCompress.html

%description
AudioCompress is (essentially) a very gentle, 1-band dynamic range
compressor intended to keep audio output at a consistent volume without
introducing any audible artifacts.  It can either accept input on
standard input and output audio to standard output or bind to the esound
daemon and apply its effect to all esd output.

Install this if you want a nice way to keep your
audio at a consistent volume level.

%package xmms
Summary:	AudioCompress plugin for xmms
Requires:	xmms
Obsoletes:	xmms-compress <= 1.1
Provides:	xmms-compress > 1.1
License:	LGPL
Group:		Sound

%description xmms
This xmms effect plugin utilizes AudioCompress to (essentially) normalize
audio played through xmms.

%prep
%setup
%patch0 -p0 -b .makefile
%patch1 -p0 -b .monitor

%build
%make CFLAGS="%optflags -fPIC -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/xmms/Effect
cp AudioCompress $RPM_BUILD_ROOT/%{_bindir}
cp libcompress.so $RPM_BUILD_ROOT/%{_libdir}/xmms/Effect/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/AudioCompress

%files xmms
%defattr (-,root,root,0755)
%doc COPYING
%{_libdir}/xmms/Effect/libcompress.so

