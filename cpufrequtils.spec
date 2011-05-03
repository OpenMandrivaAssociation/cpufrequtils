%define major 0
%define libname %mklibname cpufreq %{major}
%define develname %mklibname cpufreq -d

Summary:	Tools to determine and set cpufreq settings
Name:		cpufrequtils
Version:	008
Release:	%mkrel 2
License:	GPLv2
Group:		System/Base
URL:		http://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufrequtils.html
Source0:	http://www.kernel.org/pub/linux/utils/kernel/cpufreq/%{name}-%{version}.tar.bz2
BuildRequires:	libtool
BuildRequires:	libsysfs-devel
BuildRequires:	gettext
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
