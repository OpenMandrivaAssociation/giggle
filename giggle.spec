%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	Gtk frontend for git
Name:		giggle
Version:	0.6.1
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		http://live.gnome.org/giggle
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	git-core
BuildRequires:  gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(vte-2.90)
Requires:	git-core

%description
Giggle is a graphical frontend for the git directory tracker.

%package -n %{libname}
Summary: %summary
Group: System/Libraries

%description -n %{libname}
Giggle is a graphical frontend for the git directory tracker.

%package -n %{devname}
Summary: %summary
Group: Development/C
Provides: %{name}-devel = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}

%description -n %{devname}
Giggle is a graphical frontend for the git directory tracker.

%prep
%setup -q

%build
%configure2_5x

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{version}
%{_libdir}/%{name}/plugins/%{version}/libpersonal-details*
%{_libdir}/%{name}/plugins/%{version}/libterminal-view*
%{_libdir}/%{name}/plugins/%{version}/*.xml
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/glade/
%{_datadir}/%{name}/glade/main-window.ui
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*

%files -n %{libname}
%{_libdir}/libgiggle.so.%{major}*
%{_libdir}/libgiggle-git.so.%{major}*

%files -n %{devname}
%{_libdir}/libgiggle.so
%{_libdir}/libgiggle-git.so
%{_includedir}/%{name}

