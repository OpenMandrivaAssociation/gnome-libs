%define lib_major		32
%define xmhtml_major		1
%define lib_name		%mklibname gnome %{lib_major}
%define lib_gtkxmhtml		%mklibname gtkxmhtml 1

Summary:	Main GNOME libraries
Name:		gnome-libs
Version: 	1.4.2
Release:	28
License:	LGPL
Group:		System/Libraries
URL:		http://www.gnome.org/
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/stable/%{name}/%{name}-%{version}.tar.bz2
Source1:	gtkrc-default.bz2
BuildRequires:	autoconf2.1
BuildRequires:	automake1.4
BuildRequires:	libtool
BuildRequires:	db1-devel
BuildRequires:	pkgconfig(ORBit)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(gtk+)
BuildRequires:	pkgconfig(imlibgdk)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xpm)
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
# (fc) 1.4.1.4-3mdk fix numeric keypad switching (fix keypad in vim) (Debian)
Patch21:	gnome-libs-1.4.1.4-keypad.patch
# (pablo) 1.4.1.4-4mdk patch to have gnome-terminal switch automatically
# to utf-8 mode if the locale is utf-8
Patch22:	gnome-libs-zvt-utf8-autodetect.patch
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
Patch35:	gnome-libs-1.4.2-libpng15.patch

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
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libgnome-devel = %{version}-%{release}
Provides:	gnome-devel = %{version}-%{release}
Requires:	%{lib_gtkxmhtml} = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}

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
%patch35 -p1 -b .png15

#needed by patches 22 & 23
autoconf-2.13
cd libart_lgpl
autoconf-2.13
cd ..

#needed by patch 6 & 24
automake-1.4

%build
# libjpeg-turbo >= 1.0.90 moves definition of JPEG_LIB_VERSION from jpeglib.h to jconfig.h
# which we explicitly avoid including for own reasons, so we need help finding the definition
EXTRACTED_JPEG_LIB_VERSION=$(echo JPEG_LIB_VERSION | cpp -imacros jpeglib.h -P | awk 'NF > 0')
VISIBLE_JPEG_LIB_VERSION=$(echo JPEG_LIB_VERSION | cpp -DJCONFIG_INCLUDED -imacros jpeglib.h -P | awk 'NF > 0')
if [ "$VISIBLE_JPEG_LIB_VERSION" = "JPEG_LIB_VERSION" ]; then
  JPEG_EXTRA_DEFINE="-DJPEG_LIB_VERSION=$EXTRACTED_JPEG_LIB_VERSION"
fi

export CPPFLAGS="$JPEG_EXTRA_DEFINE"

%define Werror_cflags %nil
%configure --with-kde-datadir=%{_datadir} --disable-alsa --enable-prefer-db1 --disable-gtk-doc

#don't use macro, parallel compilation is broken
%make LIBTOOL='libtool --tag=CC' -j1


%install
%makeinstall_std LIBTOOL=libtool

# multiarch support
%multiarch_binaries %{buildroot}%{_bindir}/gnome-config

%multiarch_includes %{buildroot}%{_includedir}/gnome-1.0/libart_lgpl/art_config.h

mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
cp -f  %{buildroot}%{_docdir}/{gnome-doc,mkstub}  %{buildroot}%{_bindir}
chmod a+x %{buildroot}%{_bindir}/{gnome-doc,mkstub}
cp -f  %{buildroot}%{_docdir}/gnome-doc.el  %{buildroot}%{_datadir}/emacs/site-lisp

# find *.mo files, per language
%find_lang %{name} --with-gnome

# remove unpackaged files
rm -rf %{buildroot}%{_prefix}/doc  %{buildroot}%{_datadir}/doc

%files -n %{lib_gtkxmhtml}
%{_libdir}/libgtkxmhtml*.so.*

%files -f %{name}.lang
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
%{_libdir}/libgnome*.so.*
%{_libdir}/libgnorba*.so.*
%{_libdir}/libzvt*.so.*
%{_libdir}/libart*.so.*

%files -n %{lib_name}-devel
%doc devel-docs/*
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/gnome-config
%{multiarch_bindir}/gnome-config

%{_bindir}/libart-config
%{_bindir}/gnome-doc
%{_bindir}/mkstub
%{_libdir}/lib*.so
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


%changelog
* Sat Mar 17 2012 Andrew Lukoshko <andrew.lukoshko@rosalab.ru> 1.4.2-26mdv2011.0
- workaround for libjpeg-turbo >= 1.0.90
- drop unused gnome-libs-1.4.1.4-zvtescape.patch

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-25mdv2011.0
+ Revision: 610939
- rebuild

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 1.4.2-24mdv2010.1
+ Revision: 492256
- rebuild for new libjpeg v8

* Thu Dec 03 2009 Götz Waschk <waschk@mandriva.org> 1.4.2-23mdv2010.1
+ Revision: 472824
- update build deps
- unfuzz patches
- fix patching
- use system libtool
- disable Werror

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.4.2-22mdv2009.0
+ Revision: 266917
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 28 2008 Anssi Hannula <anssi@mandriva.org> 1.4.2-21mdv2009.0
+ Revision: 212695
- fix linking order in configure test (linking-order.patch)
- fix underlinking issues (underlinking.patch)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

* Tue Sep 11 2007 David Walluck <walluck@mandriva.org> 1.4.2-20mdv2008.0
+ Revision: 84301
- be consistent with tabs
- BuildRequires: autoconf2.1
- change Requires >= %%{version}-%%{release} to = %%{version}-%%{release}
- rebuild for 2008
- bunzip2 patches
- version Obsoletes
- Provides: gnome-devel = %%{version}-%%{release}
- change autoconf calls to autoconf-2.13

  + Thierry Vignaud <tv@mandriva.org>
    - kill icon tag

  + Frederic Crozat <fcrozat@mandriva.com>
    - Import gnome-libs



* Thu Aug 10 2006 Götz Waschk <waschk@mandriva.org> 1.4.2-18mdv2007.0
- fix buildrequires

* Wed Aug  9 2006 Götz Waschk <waschk@mandriva.org> 1.4.2-17mdv2007.0
- drop some explicit devel deps
- fix buildrequires

* Thu Jun 29 2006 Stefan van der Eijk <stefan@eijk.nu> 1.4.2-16
- Buildrequires

* Wed Jun 21 2006 Götz Waschk <waschk@mandriva.org> 1.4.2-15mdk
- Rebuild

* Tue Jan 31 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.4.2-14mdk
- %%mrek
- fix underquoted calls (P32)

* Tue Aug 16 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.4.2-13mdk
- gcc4 fixes, aka remove duplicates

* Thu Mar 10 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.4.2-12mdk
- clean up libdir patch, aka. make libart-config multiarch aware

* Thu Feb 10 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.4.2-11mdk
- libtool fixes
- multiarch (gnome-config)

* Tue Feb 01 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.2-10mdk
- disable parallel build
- multiarch

* Sun Dec 26 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4.2-9mdk
- fix buildrequires

* Mon Jun 21 2004 Götz  Waschk <waschk@linux-mandrake.com> 1.4.2-8mdk
- disable gtk-doc
- fix autotools problems

* Thu Jul 31 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.4.2-7mdk
- BuildRequires: gtk+1.2-devel

* Thu Jul 17 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 1.4.2-6mdk
- Rebuild

* Tue Apr  8 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.4.2-5mdk
- Patch29: Handle biarch struct utmp, just in case someone uses this
  gnome-pty-helper nowadays

* Tue Apr  8 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 1.4.2-4mdk
- Fix dependencies (Thanks to Götz Waschk)

* Fri Mar 14 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 1.4.2-3mdk
- Update patch7 to fix mdk bug 3096
- Patch28 (rawhide) :  Disable xalf by default
- Patch26 (rawhide): disable tearoffs and detachable menubar by default
- Remove patch8 (no longer needed)
- Patch27 (rawhide):  fix segfault in gnome-moz-remote

* Mon Oct  7 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.4.2-2mdk
- Patch25: fix on 64-bit platforms where sizeof(int) != sizeof(size_t)

* Mon Aug 19 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.2-1mdk
- Release 1.4.2
- Regenerate patches 5, 13 (partially merged)
- Remove patch 14 (merged upstream)
- Patch24 : Remove -I/usr/include from CFLAGS

* Mon Aug  5 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.7-4mdk
- Enforce dependencies : it seems we can install libgnome32 with gnome-libs
  installed

* Wed Jul 31 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.7-3mdk
- Ipdate patch23 to fix libart ldflags

* Wed Jul 31 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.7-2mdk
- Regenerate and really apply patch22
- Patch23: don't add -L/usr/lib to ldflags

* Mon Jun  3 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.7-1mdk
- Release 1.4.1.7

* Mon Apr 29 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.6-1mdk
- Release 1.4.1.6

* Mon Apr  8 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.5-1mdk
- Release 1.4.1.5

* Wed Feb 27 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.4-5mdk
- Update patch13 to change fix utf8 detection for .desktop
- Regenerate patch14 (it depends on patch13)

* Fri Feb 22 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 1.4.1.4-4mdk
- integrated Basque translation
- small patch to have gnome-terminal automatically enable the utf-8 mode
  if the locale uses utf-8

* Thu Feb 21 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.4-3mdk
- Patch20 (Debian): fix ANSI escaping in libzvt
  (bug fixed : beep when launching vim in gnome-terminal)
- Patch21 (Debian): fix numeric keypad handling in libzvt
  (bug fixed : numeric keypad unusable in vim in gnome-terminal)

* Thu Feb 14 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.4-2mdk
- Patch19: fix font size with gtk-xmhtml (was causing XFree crashes)

* Fri Jan 25 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.4-1mdk
- Release 1.4.1.4
- Fix installation of gnome-doc file

* Mon Jan 14 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.3-1mdk
- Release 1.4.1.3
- Remove patches 2, 9, 11, 12, 15, 17 (merged upstream)
- Regenerate patch 18 (some parts are already merged)
- Split man pages between -devel and main package

* Mon Jan  7 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.2-11mdk
- Grr, don't use makeinstall_std macro, otherwise locales are lost (Thanks to Goetz Waschk)

* Fri Jan  4 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.2-10mdk
- Patch18: fix missing prototypes

* Tue Dec  4 2001 Stefan van der Eijk <stefan@eijk.nu> 1.4.1.2-9mdk
- %%{_datadir}/pixmaps --> %%{_datadir}/pixmaps/*

* Mon Oct 29 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.2-8mdk
- Patch17 (GNOME CVS): fix parallel installation with GNOME2
- Libification

* Wed Oct 17 2001 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.1.2-7mdk
- rebuilt with libpng3

* Mon Sep 17 2001 Stefan van der Eijk <stefan@eijk.nu> 1.4.1.2-6mdk
- BuildRequires: db1-devel
- Remove redundant BuildRequires

* Fri Sep 14 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.4.1.2-5mdk
- rebuild with fixed fontsets for CJK

* Fri Sep 14 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.4.1.2-4mdk
- rebuild including latest translations

* Fri Sep 14 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.2-3mdk
- Patch15 (GNOME CVS) : fix gnome-metadata locking

* Mon Sep 10 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.2-2mdk
- Patch13 (rawhide): fix utf8 in menu reading
- Patch14 (rawhide): better handle KDE menu

* Mon Sep 10 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.2-1mdk
- Release 1.4.1.2

* Wed Aug 22 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.1.1-1mdk
- Release 1.4.1.1
- Remove patch10 (merged upstream)

* Tue Aug 21 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.13-4mdk
- Patch8 (rawhide) : hack for nautilus root window
- Patch9 (rawhide) : Clean up if master client is destroyed
- Patch10 (rawhide) : Fix problem with imlib memory management
- Patch11 (rawhide) : Fix problem displaying mdash in help browser
- Patch12 (rawhide) : Fix problem displaying mdash in help browser

* Fri Aug 17 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.13-3mdk
- Fix dependencies in gnome-libs-devel

* Mon Jul 23 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.13-2mdk
- Patch 7 : fix bug 3730 (nautilus draws desktop when call as help-browser)

* Wed Mar 21 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.13-1mdk
- Release 1.2.13
- Remove patch 7 (merged upstream)

* Wed Mar  7 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.12-2mdk
- Regenerated against latest glib/gtk

* Tue Feb 27 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.12-1mdk
- Release 1.2.12

* Thu Jan 25 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.11-1mdk
- Release 1.2.11
- No longer apply patch4 (xalf), has been merged upstream

* Mon Jan 22 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.9-1mdk
- Release 1.2.9

* Fri Jan 19 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.8-4mdk
- Move gtkrc files to their own directory (+ patch gnome-init )

* Wed Dec 13 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.8-3mdk
- Put libgtkxmhtml in separate package

* Wed Nov 29 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.8-2mdk
- Correct requires

* Tue Oct 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.8-1mdk
- Release 1.2.8

* Wed Oct 18 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.6-1mdk
- Release 1.2.6
- don't apply merged patches (3 & 6)
- Regenerate patch 4

* Thu Oct  5 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-8mdk
- Provides main gnome directories (close bug #614)

* Tue Sep 19 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-7mdk
- Change search for icons for new KDE2 paths

* Tue Sep 12 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-6mdk
- Merge fixes from RedHat for gnome-terminal (set background, delete key)

* Mon Sep 11 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-5mdk
- Search icons in /usr/share/icons subdirectories first

* Thu Aug 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-4mdk
- enhance support for xalf (start application notifier)
- add noreplace for config file

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.4-3mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-2mdk
- Don't install gtkrc file (was breaking some gtk themes)

* Tue Jul 25 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-1mdk
- release 1.2.4 (from Helix)

* Tue Jul 25 2000 dam's <damien@mandrakesoft.com> 1.2.3-4mdk
- added disable-alsa.

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 1.2.3-3mdk
- BM + macrozification.

* Tue Jul 18 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.3-2mdk
- added patch to support fontsets in scores and wizards windows

* Wed Jun 21 2000 dam's <damien@mandrakesoft.com> 1.2.3-1mdk
- updated to 1.2.3

* Tue Jun 20 2000 dam's <damien@mandrakesoft.com> 1.2.1-3mdk
- Rebuild due to bad provides.

* Tue Jun 20 2000 dam's <damien@mandrakesoft.com> 1.2.1-2mdk
- Rebuild due to bad provides.

* Fri Jun  9 2000 dam's <damien@mandrakesoft.com> 1.2.1-1mdk
- update from helix release.

* Thu Apr 06 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.58-1mdk
- build release 1.0.58

* Fri Mar 31 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.56-1mdk
- from Helix stuffs
- build release 1.0.56
