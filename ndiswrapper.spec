#global pre rc1

Summary:	Ndiswrapper wraps around Windows WLAN drivers within Linux
Name:		ndiswrapper
Version:	1.63
Release:	10%{?pre}%{?dist}
License:	GPLv2
URL:		http://ndiswrapper.sourceforge.net
Source0:	http://downloads.sf.net/ndiswrapper/ndiswrapper-%{version}%{?pre}.tar.gz
BuildRequires:	perl-generators
BuildRequires:	gcc

Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}

ExclusiveArch:	%{ix86} x86_64

%description
The ndiswrapper project makes it possible to use WLAN-Hardware 
with Linux by means of a loadable kernel module that "wraps
around" NDIS (Windows network driver API) drivers.  These rpms contain
just the kernel module and loader. You will also need the Windows driver 
for your card.

WARNING: Fedora-Kernels use 4K size stack. Many Windows drivers
will need at least 8K size stacks. For details read the wiki on:
http://ndiswrapper.sourceforge.net


%prep
%setup -q -n %{name}-%{version}%{?pre}


%build
%make_build -C utils CFLAGS="%{optflags} -I`pwd`/driver"


%install
%make_install -C utils
mkdir -m755 -p %{buildroot}%{_sysconfdir}/ndiswrapper


%files
%doc README AUTHORS ChangeLog INSTALL
%dir %{_sysconfdir}/ndiswrapper
%{_sbindir}/ndiswrapper
/sbin/loadndisdriver
%{_sbindir}/ndiswrapper-buginfo


%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.63-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.63-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.63-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.63-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Nov 11 2022 Leigh Scott <leigh123linux@gmail.com> - 1.63-6
- rebuilt

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1.63-1
- Update to 1.63

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Leigh Scott <leigh123linux@gmail.com> - 1.62-1
- Update to 1.62

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.61-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.61-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.61-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Paul Howarth <paul@city-fan.org> - 1.61-2
- Perl 5.26 rebuild

* Wed Jun 28 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.61-1
- Update to 1.61

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Paul Howarth <paul@city-fan.org> - 1.60-2
- BR: perl-generators for proper dependency generation
  (https://fedoraproject.org/wiki/Changes/Build_Root_Without_Perl)
- Fix rpmlint warning about mixed use of spaces and tabs

* Sun Jun 19 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.60-1
- Update to 1.60

* Sun Dec 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.59-1
- Update to 1.59

* Thu Feb 21 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.58-1
- Update to 1.58

* Wed Jan 11 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.57-1
- Update to 1.57

* Tue Nov 01 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.57-0.1rc1
- Update to 1.57rc1

* Sun Feb 13 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.56-1
- Update to 1.56

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.54-2
- rebuild for new F11 features

* Sat Feb 21 2009 Xavier Lamien <lxtnow@gmail.com> - 0.54-1
- Update release.

* Sat Oct 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.53-2
- rebuild for rpm fusion

* Tue Jul 15 2008 kwizart < kwizart at gmail.com > - 1.53-1
- Update to 1.53

* Sat Feb 16 2008 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.52-1
- Update to 1.52

* Sun Jan 20 2008 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.51-1
- Update to 1.51

* Wed Oct 03 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.48-1
- Update to 1.48

* Tue May 15 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.43-1
- Update to 1.43

* Tue Mar 13 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.38-1
- Update to 1.38

* Sat Oct 07 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.25-1
- Update to 1.25
- ExcludeArch: ppc

* Mon Jun 26 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.18-1
- Update to 1.18

* Sun May 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.13-2
- Require ndiswrapper-kmod instead of kmod-ndiswrapper (#970).

* Sun Apr 09 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.13-1
- Update to 1.13

* Wed Apr 05 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.12-1
- Update to 1.12

* Sat Mar 18 2006 <fedora[AT]leemhuis.info> - 1.10-2
- drop 0.lvn

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sun Feb 12 2006 <fedora[AT]leemhuis.info> - 1.10-0.lvn.2
- split into packages for userland and kmod
- Drop epoch

* Sun Feb 12 2006 <fedora[AT]leemhuis.info> - 0:1.10-0.lvn.1
- Update to 1.10

* Sat Feb 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 0:1.9-0.lvn.2
- Fix doc dir modes.

* Sat Feb 11 2006 <fedora[AT]leemhuis.info> - 0:1.9-0.lvn.1
- Update to 1.9

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0:1.8-0.lvn.2
- Temporary hack for 2.6.16/2.6.15 version skew in FC5test* kernels.
- Fix doc file modes.

* Tue Jan 17 2006 <fedora[AT]leemhuis.info> - 0:1.8-0.lvn.1
- Update to 1.8

* Sat Dec 10 2005 <fedora[AT]leemhuis.info> - 0:1.7-0.lvn.1
- Update to 1.7

* Sat Dec 03 2005 <fedora[AT]leemhuis.info> - 0:1.6-0.lvn.1
- Update to 1.6
- New BR: libusb-devel for new file load_fw_ar5523

* Sat Nov 05 2005 <fedora[AT]leemhuis.info> - 0:1.5-0.lvn.1
- Update to 1.5

* Sun Oct 16 2005 <fedora[AT]leemhuis.info> - 0:1.4-0.lvn.1
- Update to 1.4
- strip kernel-module

* Fri Jun 17 2005 <fedora[AT]leemhuis.info> - 0:1.2-0.lvn.3
- Pass KSRC to make install call, too

* Fri Jun 17 2005 Dams <anvil[AT]livna.org> - 0:1.2-0.lvn.2
- Fixed Source0 URL.

* Mon Jun 13 2005 <fedora[AT]leemhuis.info> - 0:1.2-0.lvn.1
- Update to 1.2
- Rework installation
- Rework kernel-devel usage

* Tue Mar 22 2005 <aaron.bennett@olin.edu> - 0:1.1-0.lvn.1
- Updated to version 1.1

* Mon Jan 31 2005  <aaron.bennett@olin.edu> - 0:1.0-0.lvn.1
- updated to version 1.0

* Fri Nov 26 2004 Thorsten Leemhuis <fedora AT leemhuis DOT info> 0:0.12-0.lvn.1
- Update to 0.12
- Trim Doc in header
- Trim description and add 4k-Warning 
- Depend on /boot/vmlinuz correctly
- use --without driverp to skip utiliy/core-Package
- Remove the included fedora-kmodhelper
- Make modpath readable for normal users

* Mon Nov 8 2004 <aaron.bennett@olin.edu> 0:0.11-0.lvn.2
- changed make to use %{?_smp_mflags}

* Sun Oct 24 2004 <fedora AT leemhuis DOT info> 0:0.11-0.lvn.1
- Use fedora-kmodhelper like in other rlo packages like ati-fglrx
- Update to 0.11

* Sun Aug 29 2004 <fedora AT leemhuis DOT info> 0:0.10-0.lvn.1
- Integrate fedora-kmodhelper as long as fedora.us version is not ready
- Use correct kernel-headers to build
- Allow separate building of tools and kernel-module
- show fedora-kmodhelper diag
- some minor fixes

* Mon Jun 14 2004 <aaron.bennett@olin.edu> 0:0.8-0.fdr.2
- removed extra kmodhelper stuff
- removed old depmod flag from 2.4 kernel

* Thu Jun 10 2004 <aaron.bennett@olin.edu> 0:0.8-0.fdr.1
- moved /usr/sbin/loadndisdriver to /sbin/loadndisdriver
- revised new build with version 0.8 of ndiswrapper from upstream

* Tue Jun 8 2004 <aaron.bennett@olin.edu> - 0:0.7-0.fdr.2
- changed ndiswrapper.o to ndiswrapper.ko for 2.6 kernel
- added Requires: ndiswrapper to kernel module ndiswrapper

* Thu Jun 3 2004  <aaron.bennett@olin.edu> - 0:0.7-0.fdr.1
- Initial build.


