Summary:	Library to access various Google services via their public API
Name:		libkgapi
Version:	2.0.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://progdan.cz/category/akonadi-google/
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QJson)

%description
LibKGAPI (previously called LibKGoogle) is a C++ library that implements APIs
for various Google services.

Currently supported APIs:
  - Calendar API v3 (https://developers.google.com/google-apps/calendar)
  - Contacts API v3 (https://developers.google.com/google-apps/contacts/v3/)
  - Tasks API v1 (https://developers.google.com/google-apps/tasks)

#----------------------------------------------------------------------------

%define major 1
%define libname %mklibname kgapi %{major}

%package -n %{libname}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libname}
Runtime Library for %{name}.

%files -n %{libname}
%{_kde_libdir}/libkgapi.so.%{major}
%{_kde_libdir}/libkgapi.so.%{version}

#----------------------------------------------------------------------------

%define major2 2
%define libname2 %mklibname kgapi2_ %{major2}

%package -n %{libname2}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libname2}
Runtime Library for %{name}.

%files -n %{libname2}
%{_kde_libdir}/libkgapi2.so.%{major2}
%{_kde_libdir}/libkgapi2.so.%{version}

#----------------------------------------------------------------------------

%define devname %mklibname -d kgapi

%package -n %{devname}
Summary:	Development files for libkgapi
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libname2} = %{EVRD}

%description -n %{devname}
Development files for libkgapi.

%files -n %{devname}
%{_kde_libdir}/libkgapi.so
%{_kde_libdir}/libkgapi2.so
%{_kde_includedir}/*
%{_kde_libdir}/pkgconfig/*.pc
%{_kde_libdir}/cmake/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

