%define major	0
%define libname %mklibname kgapi %{major}
%define devname %mklibname -d kgapi

Summary:	Library to access various Google services via their public API
Name:		libkgapi
Version:	0.4.3
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

%package -n %{libname}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libname}
Runtime Library for %{name}

%package -n %{devname}
Summary:	Devel files for	libkgapi
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Devel files for	libkgapi

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_kde_libdir}/libkgapi.so.%{major}*

%files -n %{devname}
%{_kde_libdir}/libkgapi.so
%{_kde_includedir}/libkgapi
%{_kde_libdir}/pkgconfig/libkgapi.pc
%{_kde_libdir}/cmake/LibKGAPI

