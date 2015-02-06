%define major 0
%define libname %mklibname %{name} %{major}
%define libgit %mklibname %{name}-git %{major}
%define devname %mklibname -d %{name}

Summary:	Gtk frontend for git
Name:		giggle
Version:	0.7
Release:	2
License:	GPLv2+
Group:		Development/Other
Url:		https://wiki.gnome.org/giggle
Source0:	https://download.gnome.org/sources/%name/%{name}-%{version}.tar.xz
Patch0:		giggle-0.7-gtksourceview-3.8.patch
Patch1:		giggle-0.7-gettext-usage.patch
BuildRequires:	git-core
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.40.0
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	xsltproc
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(gdk-3.0) >= 3.3.12
BuildRequires:	pkgconfig(gdk-pixbuf-2.0) >= 2.22
BuildRequires:	pkgconfig(gio-2.0) >= 2.30
BuildRequires:	pkgconfig(glib-2.0) >= 2.30
BuildRequires:	pkgconfig(gthread-2.0) >= 2.30
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.3.12
BuildRequires:	pkgconfig(gtksourceview-3.0) >= 3.8
BuildRequires:	pkgconfig(libebook-1.2) >= 3.2
BuildRequires:	pkgconfig(vte-2.90) >= 0.28
Requires:	git-core

%description
Giggle is a graphical frontend for the git directory tracker.

%files -f %{name}.lang
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{version}
%{_libdir}/%{name}/plugins/%{version}/libpersonal-details*
%{_libdir}/%{name}/plugins/%{version}/libterminal-view*
%{_libdir}/%{name}/plugins/%{version}/*.xml
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared libraries for Giggle
Group:		System/Libraries

%description -n %{libname}
Giggle is a graphical frontend for the git directory tracker.

%files -n %{libname}
%{_libdir}/libgiggle.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgit}
Summary:	Shared libraries for Giggle
Group:		System/Libraries
Conflicts:	%{_lib}giggle0 < 0.7

%description -n %{libgit}
Giggle is a graphical frontend for the git directory tracker.

%files -n %{libgit}
%{_libdir}/libgiggle-git.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for Giggle
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libgit} = %{EVRD}

%description -n %{devname}
Giggle is a graphical frontend for the git directory tracker.

%files -n %{devname}
%{_libdir}/libgiggle.so
%{_libdir}/libgiggle-git.so
%{_includedir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

