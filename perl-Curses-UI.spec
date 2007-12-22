%define name	perl-Curses-UI
%define module  Curses-UI
%define version	0.96
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A curses based perl OO user interface framework
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Curses/%{module}-%{version}.tar.gz
Patch0: Curses-UI-0.95-more-Listbox-alike-Popupmenu.patch
Patch2: Curses-UI-0.95-add-method-to-modify-button-label.patch
Patch3: Curses-UI-0.95-allow-setting-active-line.patch
Patch4: Curses-UI-0.95-focus-up-and-focus-down.patch
Patch5: Curses-UI-0.95-make-dialog-message-focusable-if-scrolled.patch
Patch6: Curses-UI-0.95-new-Container-method--delete_object.patch
Patch7: Curses-UI-0.95-do-not-replace-last-char-with-overflow-char.patch
Patch8: Curses-UI-0.95-gpm-does-not-work--hide-error-for-now.patch
Patch9: Curses-UI-0.95-only-redraw-Listbox-when-needed-otherwise-it-occurs-after-focus-next.patch
Requires:	perl-Curses
Requires:	perl-Term-ReadKey
BuildRequires:  perl-Test-Pod
BuildRequires:  perl-Term-ReadKey
BuildRequires:  perl-Curses
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A UI framework based on the curses library. Curses::UI contains
several widgets which can be used to build a user interface.

%prep
%setup -q -n %{module}-%{version}
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

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

%check
# need setting COLUMNS and LINES to help it getting "Terminal Size" under nohup or iurt
COLUMNS=80 LINES=25 make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README examples CREDITS BUGS Changes
%{perl_vendorlib}/Curses
%{_mandir}/*/*
