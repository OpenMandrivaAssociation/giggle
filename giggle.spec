%define	name	giggle
%define	version	0.4
%define	release	%mkrel 3
%define	summary	Gtk frontend for git

Summary:	%summary
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Development/Other
URL:		http://developer.imendio.com/projects/giggle
Source0:	http://ftp.imendio.com/pub/imendio/giggle/src/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel perl-XML-Parser gettext
BuildRequires:	libgnomeprint-devel libglade2.0-devel libgtksourceview-2.0-devel libxml2-devel
BuildRequires:	git-core
Requires:	git-core

%description
Giggle is a graphical frontend for the git directory tracker.

%prep
%setup -q 

%build
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
%find_lang %name

# remove devel files
rm -f %buildroot%_libdir/*.la %buildroot%_libdir/libgiggle.so

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
%{_datadir}/applications/%name.desktop
%{_datadir}/giggle/glade/main-window.glade
%{_iconsdir}/hicolor/*/apps/*
