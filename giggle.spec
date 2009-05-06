%define	name	giggle
%define	version	0.4.91
%define	release	%mkrel 2
%define	summary	Gtk frontend for git

%define libname %mklibname %name %version
%define develname %mklibname -d %name

Summary:	%summary
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Development/Other
URL:		http://live.gnome.org/giggle
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0:		giggle-0.4.91-linkage.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2.0-devel 
BuildRequires:	libgtksourceview-2.0-devel
BuildRequires:	libxml2-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	intltool
BuildRequires:	git-core
#gw libtool dep (GConf2?)
BuildRequires:	dbus-glib-devel
Requires:	git-core
Requires: %libname >= %version-%release

%description
Giggle is a graphical frontend for the git directory tracker.

%package -n %libname
Summary: %summary
Group: System/Libraries

%description -n %libname
Giggle is a graphical frontend for the git directory tracker.

%package -n %develname
Summary: %summary
Group: Development/C
Provides: lib%name-devel = %version-%release
Provides: %name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %develname
Giggle is a graphical frontend for the git directory tracker.


%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
%find_lang %name

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libpersonal-details*
%_libdir/%name/plugins/personal-details.xml
%{_datadir}/applications/%name.desktop
%{_datadir}/giggle/glade/main-window.glade
%{_iconsdir}/hicolor/*/apps/*

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*-%version.so

%files -n %develname
%defattr(-,root,root)
%_libdir/*.la
%_libdir/libgiggle.so
%_libdir/libgiggle-git.so
%_includedir/%name

