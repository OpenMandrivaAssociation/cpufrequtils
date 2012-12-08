%define major 0
%define libname %mklibname cpufreq %{major}
%define develname %mklibname cpufreq -d

Summary:	Tools to determine and set cpufreq settings
Name:		cpufrequtils
Version:	008
Release:	4
License:	GPLv2
Group:		System/Base
URL:		http://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufrequtils.html
Source0:	http://www.kernel.org/pub/linux/utils/kernel/cpufreq/%{name}-%{version}.tar.bz2
BuildRequires:	libtool
BuildRequires:	sysfsutils-devel
BuildRequires:	gettext

%description
To make access to the Linux kernel cpufreq subsystem easier for users
and cpufreq userspace tools, the cpufrequtils package was created. It
contains a library used by other programs (libcpufreq), command line
tools to determine current CPUfreq settings and to modify them
(cpufreq-info and cpufreq-set), and debug tools.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		%{group}

%description -n %{libname}
Dynamic library for programs accessing cpufreq subsystem.

%package -n     %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	libcpufreq-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname cpufreq 0 -d}

%description -n %{develname}
Static libraries, include files for cpufrequtils.

%prep
%setup -q

%build
%setup_compile_flags
%make

%install
rm -rf %{buildroot}
%makeinstall localedir=%{buildroot}%{_datadir}/locale

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%doc README AUTHORS
%defattr (-,root,root)
%{_mandir}/man1/*
%{_bindir}/*

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%{_libdir}/*.so
%{_includedir}/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 008-2mdv2011.0
+ Revision: 663419
- mass rebuild

* Sun Jul 25 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 008-1mdv2011.0
+ Revision: 559064
- update to new version 008
- spec file clean
- add buildrequires on libsysfs-devel and gettext
- update file list

* Sat Feb 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 007-2mdv2010.1
+ Revision: 512373
- pass our CFLAGS

* Sat Feb 13 2010 Sandro Cazzaniga <kharec@mandriva.org> 007-1mdv2010.1
+ Revision: 505247
- update to 007

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 006-1mdv2010.1
+ Revision: 482833
- Update to new version 006
- Remove parallel build fix: fixed upstream

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 005-4mdv2010.0
+ Revision: 424371
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Aug 13 2008 Olivier Blin <oblin@mandriva.com> 005-2mdv2009.0
+ Revision: 271582
- fix parallel build

* Mon Aug 11 2008 Frederik Himpe <fhimpe@mandriva.org> 005-1mdv2009.0
+ Revision: 270854
- update to new version 005

* Wed Aug 06 2008 Frederik Himpe <fhimpe@mandriva.org> 004-1mdv2009.0
+ Revision: 264525
- New version 004
- Does not requires libsysfs anymore

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 003-2mdv2009.0
+ Revision: 264372
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 trem <trem@mandriva.org> 003-1mdv2009.0
+ Revision: 211254
- update to 003

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 002-3mdv2008.1
+ Revision: 149134
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 14 2007 Adam Williamson <awilliamson@mandriva.org> 002-2mdv2008.0
+ Revision: 85776
- rebuild for 2008
- package docs
- protect against major change in file list
- new devel policy
- Fedora license policy


* Fri Dec 29 2006 Olivier Blin <oblin@mandriva.com> 002-1mdv2007.0
+ Revision: 102472
- buildrequire libtool
- new release 002 (which is greater than 0.4)
- Import cpufrequtils

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 0.4-3mdk
- rebuild for sparc

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-2mdk
- Fix BuildRequires

* Tue Dec 20 2005 Lenny Cartier <lenny@mandriva.com> 0.4-1mdk
- 0.4

* Sun Aug 07 2005 Frederic Crozat <fcrozat@mandriva.com> 0.3-1mdk 
- First mdk package (based on SUSE package)

