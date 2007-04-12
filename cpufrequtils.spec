%define lib_name %mklibname cpufreq 0

Name:         cpufrequtils
URL:          http://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufrequtils.html
Version:      002
Release:      %mkrel 1
Summary:      Tools to determine and set CPUfreq settings
License:      GPL
Group:        System/Base
Source:       http://www.kernel.org/pub/linux/utils/kernel/cpufreq/%{name}-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

BuildRequires: libsysfs-devel libtool

%description
To make access to the Linux kernel cpufreq subsystem easier for users
and cpufreq userspace tools, the cpufrequtils package was created. It
contains a library used by other programs (libcpufreq), command line
tools to determine current CPUfreq settings and to modify them
(cpufreq-info and cpufreq-set), and debug tools.

%package -n %{lib_name}
Summary:        Dynamic library for programs accessing cpufreq subsystem
Group:          %{group}

%description -n %{lib_name}
Dynamic library for programs accessing cpufreq subsystem.

%package -n     %{lib_name}-devel
Summary:        Static libraries, include files for cpufrequtils
Group:          Development/C
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       libcpufreq-devel = %{version}-%{release}
Requires:       %{lib_name} = %{version}

%description -n %{lib_name}-devel
Static libraries, include files for cpufrequtils



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

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr (-,root,root)
%{_mandir}/man1/*
%{_bindir}/*

%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*


