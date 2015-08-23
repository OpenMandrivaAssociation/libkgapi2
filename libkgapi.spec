Summary:	Library to access various Google services via their public API
Name:		libkgapi
Version:	5.0.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.dvratil.cz/category/akonadi-google/
Source0:	http://download.kde.org/stable/libkgapi/%{version}/src/%{name}-%{version}.tar.xz
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

%files -f libkgapi_qt.lang
%{_sysconfdir}/xdg/libkgapi.categories
%{_libname}/qt5/mkspecs/modules/*.pri


%dependinglibpackage KF5GAPIBlogger 5
%dependinglibpackage KF5GAPICalendar 5
%dependinglibpackage KF5GAPIContacts 5
%dependinglibpackage KF5GAPICore 5
%dependinglibpackage KF5GAPIDrive 5
%dependinglibpackage KF5GAPILatitude 5
%dependinglibpackage KF5GAPIMaps 5
%dependinglibpackage KF5GAPITasks 5

%define devname %mklibname kgapi -d

%package -n %{devname}
Summary:	Development files for libkgapi
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{mklibname KF5GAPIBlogger 5} = %{EVRD}
Requires:	%{mklibname KF5GAPICalendar 5} = %{EVRD}
Requires:	%{mklibname KF5GAPIContacts 5} = %{EVRD}
Requires:	%{mklibname KF5GAPICore 5} = %{EVRD}
Requires:	%{mklibname KF5GAPIDrive 5} = %{EVRD}
Requires:	%{mklibname KF5GAPILatitude 5} = %{EVRD}
Requires:	%{mklibname KF5GAPIMaps 5} = %{EVRD}
Requires:	%{mklibname KF5GAPITasks 5} = %{EVRD}

%description -n %{devname}
Development files for libkgapi.

%files -n %{devname}
%dir %{_includedir}/KF5/KGAPI
%{_includedir}/KF5/KGAPI/KGAPI
%{_includedir}/KF5/KGAPI/kgapi
%{_includedir}/KF5/kgapi_version.h
%{_libdir}/libKF5GAPIBlogger.so
%{_libdir}/libKF5GAPICalendar.so
%{_libdir}/libKF5GAPIContacts.so
%{_libdir}/libKF5GAPICore.so
%{_libdir}/libKF5GAPIDrive.so
%{_libdir}/libKF5GAPILatitude.so
%{_libdir}/libKF5GAPIMaps.so
%{_libdir}/libKF5GAPITasks.so
%{_libdir}/cmake/KF5GAPI/*.cmake

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libkgapi_qt
