%define oname		AudioCompress

Summary:		Simple dynamic range compressor
Name:			audiocompress
Version:		2.0
Release:		%mkrel 2
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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-2mdv2011.0
+ Revision: 616636
- the mass rebuild of 2010.0 packages

* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 2.0-1mdv2010.0
+ Revision: 384189
- new version 2.0
- drop xmms sub-package (functionnality no more provided)
- drop patches
- clean spec file
- fix license
- lowercase AudioCompress

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.5.2-4mdv2009.0
+ Revision: 226199
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5.2-3mdv2008.1
+ Revision: 140690
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import AudioCompress

