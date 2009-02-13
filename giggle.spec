%define	name	giggle
%define	version	0.4.90
%define	release	%mkrel 1
%define	summary	Gtk frontend for git

Summary:	%summary
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Development/Other
URL:		http://developer.imendio.com/projects/giggle
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2.0-devel 
BuildRequires:	libgtksourceview-2.0-devel
BuildRequires:	libxml2-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	intltool
BuildRequires:	git-core
Requires:	git-core

%description
Giggle is a graphical frontend for the git directory tracker.

%prep
%setup -q 

%build
#gw it doesn't build otherwise
%define _disable_ld_no_undefined 1
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
%find_lang %name

# remove devel files
rm -f %buildroot%_libdir/*.la %buildroot%_libdir/{libgiggle.so,libgiggle-git.so}

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
%{_libdir}/*.so
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libpersonal-details*
%_libdir/%name/plugins/personal-details.xml
%{_datadir}/applications/%name.desktop
%{_datadir}/giggle/glade/main-window.glade
%{_iconsdir}/hicolor/*/apps/*
