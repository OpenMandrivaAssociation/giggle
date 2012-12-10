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



%changelog
* Fri Jun 15 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.6.1-1
+ Revision: 805921
- new version 0.6.1
- cleaned up spec

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.5-2mdv2011.0
+ Revision: 568225
- rebuild for new e-d-s

* Wed Apr 21 2010 Götz Waschk <waschk@mandriva.org> 0.5-1mdv2010.1
+ Revision: 537705
- update to new version 0.5

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 0.4.97-1mdv2010.1
+ Revision: 516901
- update to new version 0.4.97

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 0.4.96-1mdv2010.1
+ Revision: 503236
- update to new version 0.4.96

* Tue Jan 26 2010 Götz Waschk <waschk@mandriva.org> 0.4.95-2mdv2010.1
+ Revision: 496509
- new version
- rediff patch
- update file list
- update build deps

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.4.91-3mdv2010.0
+ Revision: 437690
- rebuild

  + Götz Waschk <waschk@mandriva.org>
    - update URL

* Mon Feb 16 2009 Funda Wang <fwang@mandriva.org> 0.4.91-2mdv2009.1
+ Revision: 341157
- fix linakge

* Mon Feb 16 2009 Götz Waschk <waschk@mandriva.org> 0.4.91-1mdv2009.1
+ Revision: 340783
- new version
- libify the package

* Fri Feb 13 2009 Götz Waschk <waschk@mandriva.org> 0.4.90-1mdv2009.1
+ Revision: 340030
- new version
- fix build
- fix installation
- update file list
- fix build deps
- fix source URL

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4-3mdv2009.0
+ Revision: 246122
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Funda Wang <fwang@mandriva.org>
    - no need rm cache file

* Sun Dec 16 2007 Funda Wang <fwang@mandriva.org> 0.4-1mdv2008.1
+ Revision: 120555
- add more doc files
- fix file list
- New version 0.4
- BR gtksourceview2

* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 0.3-2mdv2008.1
+ Revision: 119926
- require the proper version of gtksourceview-devel
- rebuild b/c of missing package on ia32

* Thu May 10 2007 Frederic Crozat <fcrozat@mandriva.com> 0.3-1mdv2008.0
+ Revision: 26037
- Release 0.3
- Add dependency on git-core

* Thu May 03 2007 Pascal Terjan <pterjan@mandriva.org> 0.2-1mdv2008.0
+ Revision: 21683
- BuildRequires git-core
- 0.2


* Wed Mar 07 2007 Pascal Terjan <pterjan@mandriva.org> 0.1-1mdv2007.1
+ Revision: 134882
- Import giggle

* Wed Mar 07 2007 Pascal Terjan <pterjan@mandriva.org> 0.1-1mdv2007.1
- First Package

