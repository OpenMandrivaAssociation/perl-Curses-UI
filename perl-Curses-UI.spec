%define upstream_name    Curses-UI
%define upstream_version 0.9607

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A curses based perl OO user interface framework
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Curses/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Curses-UI-0.95-more-Listbox-alike-Popupmenu.patch
Patch2:		Curses-UI-0.95-add-method-to-modify-button-label.patch
Patch3:		Curses-UI-0.95-allow-setting-active-line.patch
Patch4:		Curses-UI-0.9607-focus-up-and-focus-down.patch
Patch5:		Curses-UI-0.95-make-dialog-message-focusable-if-scrolled.patch
Patch6:		Curses-UI-0.95-new-Container-method--delete_object.patch
Patch7:		Curses-UI-0.95-do-not-replace-last-char-with-overflow-char.patch
Patch8:		Curses-UI-0.9607-gpm-does-not-work--hide-error-for-now.patch
Patch9:		Curses-UI-0.95-only-redraw-Listbox-when-needed-otherwise-it-occurs-after-focus-next.patch

BuildRequires:	perl(Curses)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl-devel
BuildArch:	noarch
Requires:	perl(Curses)
Requires:	perl(Term::ReadKey)
# temporary dep due to the perl-5.14 bump
BuildRequires:	perl-Curses >= 1.280.0-6

%description
A UI framework based on the curses library. Curses::UI contains
several widgets which can be used to build a user interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

%check
# need setting COLUMNS and LINES to help it getting "Terminal Size" under nohup or iurt
COLUMNS=80 LINES=25 make test

%install
%makeinstall_std

%files
%doc README examples CREDITS Changes
%{perl_vendorlib}/Curses
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.960.700-4mdv2012.0
+ Revision: 765141
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x
- force it
- rebuild
- mass rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.9607
    - update to new version 0.9607

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 0.960.700-2
+ Revision: 650063
- rebuild

* Fri Jul 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.960.700-1mdv2010.0
+ Revision: 399503
- forgot to rename patch names in spec file
- update to 0.9607
- rediffed patch Curses-UI-0.95-focus-up-and-focus-down.patch against 0.9607
- rediffed patch Curses-UI-0.95-gpm-does-not-work--hide-error-for-now.patch against 0.9607
- using %%perl_convert_version
- fixed license field

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.96-3mdv2009.1
+ Revision: 351699
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.96-2mdv2009.0
+ Revision: 223587
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.96-1mdv2008.1
+ Revision: 136774
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Frederic Crozat <fcrozat@mandriva.com> 0.95-8mdv2008.0
+ Revision: 89536
- Rebuild

* Mon Jun 11 2007 Pixel <pixel@mandriva.com> 0.95-7mdv2008.0
+ Revision: 38027
- fix patch hiding gpm error (#26852)


* Tue Dec 19 2006 Pixel <pixel@mandriva.com> 0.95-6mdv2007.0
+ Revision: 99831
- only redraw Listbox when needed, otherwise it occurs after focus next (in drakxtools)

* Thu Nov 02 2006 Pixel <pixel@mandriva.com> 0.95-5mdv2007.1
+ Revision: 75452
- disable gpm, it does not work anyway (#26852)

* Sat Oct 21 2006 Pixel <pixel@mandriva.com> 0.95-4mdv2007.1
+ Revision: 71564
- help "make test" under nohup or iurt
- add many fixes/enhancements (mostly to make it more usable in drakxtools)
- Import perl-Curses-UI

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.95-3mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.95-2mdk
- Rebuild

* Wed Feb 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.95-1mdk
- 0.95
- enable tests

* Thu Dec 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.94-2mdk
- fix deps

* Thu Dec 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.94-1mdk
- initial mandrake import

* Fri Sep 03 2004 Francis J. Lacoste <flacoste@logreport.org> 0.93-1
- Upstream ugprade to 0.93.
  - Rebuilt on Fedora Core 2.

* Sat Apr 10 2004 Francis J. Lacoste <flacoste@logreport.org> 0.92-1
- Initial packaging.

