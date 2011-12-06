%define lib_major		32
%define xmhtml_major		1
%define lib_name		%mklibname gnome %{lib_major}
%define lib_gtkxmhtml		%mklibname gtkxmhtml 1

Summary:	Main GNOME libraries
Name:		gnome-libs
Version: 	1.4.2
Release:	%mkrel 26
License:	LGPL
Group:		System/Libraries
BuildRequires:	ORBit-devel
BuildRequires:	autoconf2.1
BuildRequires:	automake1.4
BuildRequires:	db1-devel
BuildRequires:	esound-devel
BuildRequires:	gtk+1.2-devel
BuildRequires:	gdkimlib-devel
BuildRequires:	libxt-devel
BuildRequires:	xpm-devel
BuildRequires:	libtool
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/stable/%{name}/%{name}-%{version}.tar.bz2
Source1:	gtkrc-default.bz2
URL:		http://www.gnome.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:	ORBit

# Red Hat patches
Patch0:		RH-gnome-libs-rhsnddefs.patch
# allow reading UTF-8 encoded .desktop
Patch13:	gnome-libs-1.4.2-utf8menu.patch

# Mandriva patch
#(fred c)
# search icons first in /usr/share/icons/large, normal and small
Patch5:		gnome-libs-1.4.2-iconspath.patch
# (fc) 1.2.8-4mdk move gtkrc files to /usr/share/gtkrc
Patch6:		gnome-libs-1.2.8-gtkrc.patch
# (fc) 1.4.2-3mdk use yelp or galeon to display help 
Patch7:		gnome-libs-1.4.1.2.90-ghelp.patch
# (pablo) better fontsets in gtkrc.* files
Patch16:	gnome-libs-rclocale.bz2
# (fc) 1.4.1.2-10mdk fix missing prototypes
Patch18:	gnome-libs-1.4.1.3-prototypes.patch
# (fc) 1.4.1.4-2mdk fix font size in gtk-xmhtml
Patch19:	gnome-libs-1.4.1.4-fonts.patch
# (fc) 1.4.1.4-3mdk fix parsing of escape sequence (beep when launching vim) (Debian)
Patch20:	gnome-libs-1.4.1.4-zvtescape.patch
# (fc) 1.4.1.4-3mdk fix numeric keypad switching (fix keypad in vim) (Debian)
Patch21:	gnome-libs-1.4.1.4-keypad.patch
# (pablo) 1.4.1.4-4mdk patch to have gnome-terminal switch automatically
# to utf-8 mode if the locale is utf-8
Patch22:	http://noa.tm/utf-8/patches/gnome-libs-zvt-utf8-autodetect.patch
# (fc) 1.4.1.7-2mdk don't add -L/usr/lib to ldflags
# (gb) 1.4.2-12mdk update to remove unused libdir in libart-config
Patch23:	gnome-libs-1.4.2-libdir.patch
# (fc) 1.4.2-1mdk remove -I/usr/include from cflags
Patch24:	gnome-libs-1.4.2-includedir.patch
# (gb) 1.4.2-2mdk fix on 64-bit platforms where sizeof(int) != sizeof(size_t)
Patch25:	gnome-libs-1.4.2-64bit-fixes.patch
# (fc) 1.4.2-3mdk disable tearoffs and detachable menubar by default
Patch26:	gnome-libs-1.2.13-notearoffs.patch
# (fc) 1.4.2-3mdk fix segfault in gnome-moz-remote (rawhide)
Patch27:	gnome-libs-1.4.1.2.90-moz-remote-fix.patch
# (fc) 1.4.2-3mdk Disable xalf by default (rawhide)
Patch28:	gnome-libs-1.2.13-noxalf.patch
# (gb) 1.4.2-5mdk handle biarch struct utmp
Patch29:	gnome-libs-1.4.2-biarch-utmp.patch
# (gb) 1.4.2-11mdk libtool fixes, don't bother with older aclocal, patch aclocal.m4 directly
Patch30:	gnome-libs-1.4.2-libtool.patch
# (gb) 1.4.2-13mdk gcc4 fixes, aka remove duplicates
Patch31:	gnome-libs-1.4.2-gcc4.patch
# (peroyvind) 1.4.2-14mdk fix underquoted calls, aka get rid of aclocal warnings
Patch32:	gnome-libs-1.4.2-fix-underquoted-calls.patch
# (anssi) fix linking order for --as-needed
Patch33:	gnome-libs-1.4.2-linking-order.patch
# (anssi) fix underlinking
Patch34:	gnome-libs-1.4.2-underlinking.patch

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  The gnome-libs package
includes libraries that are needed to run GNOME.

%package -n	%{lib_name}
Summary:	Libraries and headers for GNOME application development
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  The gnome-libs package
includes libraries that are needed to run GNOME.

This package contains main library for GNOME

%package -n	%{lib_name}-devel


Summary:	Libraries and headers for GNOME application development
Group:		Development/GNOME and GTK+
Requires:	db1-devel
Obsoletes:	%{name}-devel < %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libgnome-devel = %{version}-%{release}
Provides:	gnome-devel = %{version}-%{release}
Requires:	%{lib_gtkxmhtml} = %{version}
Requires:	%{lib_name} = %{version}

%description -n	%{lib_name}-devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The gnome-libs-devel package
includes the libraries and include files that you will need to develop
GNOME applications.

You should install the gnome-libs-devel package if you would like to
develop GNOME applications.  You don't need to install gnome-libs-devel
if you just want to use the GNOME desktop environment.

%package -n	%{lib_gtkxmhtml}
Summary:	Libraries for gtkxmHTML
Group:		System/Libraries

%description -n	%{lib_gtkxmhtml}
This package provides library for gtkxmHTML

%prep
%setup -q
%patch0 -p1 -b .foo
%patch5 -p1 -b .icons
%patch6 -p1 -b .gtkrc
# better fontsets in gtkrc.* files -- pablo
%patch16 -p1 -b .rclocale
%patch7 -p1 -b .ghelp
%patch13 -p1 -b .utf8
%patch18 -p1 -b .prototypes
%patch19 -p1 -b .fonts
#%patch20 -p1 -b .zvtescape
%patch21 -p1 -b .keypad
%patch22 -p1 -b .zvtutf8
%patch23 -p1 -b .libdir
%patch24 -p1 -b .includedir
%patch25 -p1 -b .64bit-fixes
%patch26 -p1 -b .notearoffs
%patch27 -p1 -b .moz-remote
%patch28 -p1 -b .noxalf
%patch29 -p1 -b .biarch-utmp
%patch30 -p1 -b .libtool
%patch31 -p1 -b .gcc4
%patch32 -p1 -b .underquoted
%patch33 -p1 -b .linking-order
%patch34 -p1 -b .underlinking

#needed by patches 22 & 23
autoconf-2.13
cd libart_lgpl
autoconf-2.13
cd ..

#needed by patch 6 & 24
automake-1.4

%build
%define Werror_cflags %nil
%configure --with-kde-datadir=%{_datadir} --disable-alsa --enable-prefer-db1 --disable-gtk-doc

#parallel build is broken
make LIBTOOL=libtool

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std LIBTOOL=libtool

# multiarch support
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/gnome-config
%multiarch_includes $RPM_BUILD_ROOT%{_includedir}/gnome-1.0/libart_lgpl/art_config.h

mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
cp -f  $RPM_BUILD_ROOT%{_docdir}/{gnome-doc,mkstub}  $RPM_BUILD_ROOT%{_bindir}
chmod a+x $RPM_BUILD_ROOT%{_bindir}/{gnome-doc,mkstub}
cp -f  $RPM_BUILD_ROOT%{_docdir}/gnome-doc.el  $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp

# find *.mo files, per language
%find_lang %{name} --with-gnome

# remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc  $RPM_BUILD_ROOT%{_datadir}/doc 

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post  -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post  -n %{lib_gtkxmhtml}  -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_gtkxmhtml} -p /sbin/ldconfig
%endif

%files -n %{lib_gtkxmhtml}
%defattr(-,root,root)
%{_libdir}/libgtkxmhtml*.so.*

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/dns-helper
%{_bindir}/gconfigger
%{_bindir}/gnome-bug
%{_bindir}/gnome-dump-metadata
%{_bindir}/gnome-gen-mimedb
%{_bindir}/gnome-moz-remote
%{_bindir}/gnome-name-service
%{_bindir}/gnome_segv
%{_bindir}/goad-browser
%{_bindir}/loadshlib
%{_bindir}/new-object
%attr(2755, root, utmp) %{_sbindir}/gnome-pty-helper
%{_datadir}/idl/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/gtkrc
%config(noreplace) %{_datadir}/gtkrc/gtkrc*
%{_datadir}/mime-info
%{_datadir}/type-convert
%config(noreplace) %{_sysconfdir}/*
%{_mandir}/man1/dns-helper*
%{_mandir}/man1/gconfigger*
%{_mandir}/man1/gnome-bug*
%{_mandir}/man1/gnome-dump-metadata*
%{_mandir}/man1/gnome-gen-mimedb*
%{_mandir}/man1/gnome-moz-remote*
%{_mandir}/man1/gnome-name-service*
%{_mandir}/man1/gnome_segv*
%{_mandir}/man1/goad-browser*
%{_mandir}/man1/loadshlib*
%{_mandir}/man1/new-object*
%{_mandir}/man1/gnome-pty-helper*
%{_mandir}/man1/gnome.*

%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/libgnome*.so.*
%{_libdir}/libgnorba*.so.*
%{_libdir}/libzvt*.so.*
%{_libdir}/libart*.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc devel-docs/*
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/gnome-config
%multiarch %{multiarch_bindir}/gnome-config
%{_bindir}/libart-config
%{_bindir}/gnome-doc
%{_bindir}/mkstub
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/*.a
%{_libdir}/*.sh
%{_libdir}/gnome-libs
%{_includedir}/*
%{_datadir}/aclocal/*
%{_mandir}/man1/gnome-doc*
%{_mandir}/man1/gnome-mkstub*
%{_mandir}/man1/gnome-config*
%{_mandir}/man1/libart-config*
%{_mandir}/man5/*
%{_datadir}/gnome/help/*
%{_datadir}/gnome/html/*
%{_datadir}/emacs/site-lisp/*
