Summary:	Library to access various Google services via their public API
Name:		libkgapi
Version:	5.0.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.dvratil.cz/category/akonadi-google/
Source0:	http://download.kde.org/stable/libkgapi/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		libkgapi-2.2.0-pkgconfig.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)

%description
LibKGAPI (previously called LibKGoogle) is a C++ library that implements APIs
for various Google services.

Currently supported APIs:
  - Calendar API v3 (https://developers.google.com/google-apps/calendar)
  - Contacts API v3 (https://developers.google.com/google-apps/contacts/v3/)
  - Tasks API v1 (https://developers.google.com/google-apps/tasks)
  - Latitude API v1 (https://developers.google.com/latitude/v1/)
  - Static Google Maps API v2
    (https://developers.google.com/maps/documentation/staticmaps/)
  - Drive API v2 (https://developers.google.com/drive/v2/reference)

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

%define devname %mklibname kgapi -d

%package -n %{devname}
Summary:	Development files for libkgapi
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname2} = %{EVRD}

%description -n %{devname}
Development files for libkgapi.

%files -n %{devname}
%{_kde_libdir}/libkgapi2.so
%{_kde_includedir}/*
%{_kde_libdir}/pkgconfig/*.pc
%{_kde_libdir}/cmake/*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

