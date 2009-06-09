%define oname		AudioCompress

Summary:		Simple dynamic range compressor
Name:			audiocompress
Version:		2.0
Release:		%mkrel 1
URL:			http://beesbuzz.biz/code/audiocompress.php
Source:			http://beesbuzz.biz/code/%{name}/%{oname}-%{version}.tar.gz
License:		LGPLv2
Group:			Sound
BuildRoot:		%{_tmppath}/%{name}-buildroot
Provides:		%{oname}
Obsoletes:		%{oname}
Obsoletes:		%{oname}-xmms

%description
AudioCompress is (essentially) a very gentle, 1-band dynamic range
compressor intended to keep audio output at a consistent volume without
introducing any audible artifacts.  It can either accept input on
standard input and output audio to standard output or bind to the esound
daemon and apply its effect to all esd output.

Install this if you want a nice way to keep your
audio at a consistent volume level.

%prep
%setup -q -n %{oname}-%{version}

%build
%make CFLAGS="%optflags -fPIC"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
cp %{oname} %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root,0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/%{oname}


