Name:		libkgapi
Version:	0.4.3
Release:	1
Summary:	Library to access various Google services via their public API
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://progdan.cz/category/akonadi-google/
Source:		http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
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

#--------------------------------------------------------------------

%define libkgapi_major 0
%define libkgapi %mklibname kgapi %{libkgapi_major}

%package -n %{libkgapi}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libkgapi}
Runtime Library for %{name}

%files -n %{libkgapi}
%{_kde_libdir}/libkgapi.so.%{libkgapi_major}*

#----------------------------------------------------------------------

%define libkgapi_devel %mklibname -d kgapi

%package -n %{libkgapi_devel}
Summary:	Devel files for libkgapi
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libkgapi} = %{EVRD}

%description -n %{libkgapi_devel}
Devel files for libkgapi

%files -n %{libkgapi_devel}
%{_kde_libdir}/libkgapi.so
%{_kde_includedir}/libkgapi
%{_kde_libdir}/pkgconfig/libkgapi.pc
%{_kde_libdir}/cmake/LibKGAPI

#---------------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

