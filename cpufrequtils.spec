%define major		0
%define libname 	%mklibname cpufreq %major
%define develname	%mklibname cpufreq -d

Name:         cpufrequtils
URL:          http://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufrequtils.html
Version:      002
Release:      %mkrel 3
Summary:      Tools to determine and set cpufreq settings
License:      GPLv2
Group:        System/Base
Source:       http://www.kernel.org/pub/linux/utils/kernel/cpufreq/%{name}-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

BuildRequires: libsysfs-devel 
BuildRequires: libtool

%description
To make access to the Linux kernel cpufreq subsystem easier for users
and cpufreq userspace tools, the cpufrequtils package was created. It
contains a library used by other programs (libcpufreq), command line
tools to determine current CPUfreq settings and to modify them
(cpufreq-info and cpufreq-set), and debug tools.

%package -n %{libname}
Summary:        Dynamic library for programs accessing cpufreq subsystem
Group:          %{group}

%description -n %{libname}
Dynamic library for programs accessing cpufreq subsystem.

%package -n     %{develname}
Summary:        Static libraries, include files for cpufrequtils
Group:          Development/C
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       libcpufreq-devel = %{version}-%{release}
Requires:       %{libname} = %{version}
Obsoletes:	%{mklibname cpufreq 0 -d}

%description -n %{develname}
Static libraries, include files for cpufrequtils.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall localedir=%{buildroot}%{_datadir}/locale

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*


