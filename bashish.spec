Summary:	text console theme engine
Summary(pl.UTF-8):	silnik moytwów dla konsoli tekstowej
Name:		bashish
Version:	2.0.7
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/bashish/%{name}-%{version}.tar.gz
# Source0-md5:	56a4dddb391f207e09b1dbec53d0b3dc
URL:		http://bashish.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
Suggests:	bash
Suggests:	csh
Suggests:	fish
Suggests:	zsh
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq '/bin/bash' '/bin/csh'  '/usr/bin/fish' '/usr/bin/rc'

%description
Bashish is a theme enviroment for text terminals. It can change
colors, font, transparency and background image on a per-application
basis. Additionally Bashish supports prompt changing on common shells
such as bash, zsh and tcsh.

%description -l pl.UTF-8
Bashish to zestaw motywów dla terminali tekstowych. Umożliwia zmianę
kolorów, czcionki, przezroczystości oraz obrazka będącego tłem dla
każdej aplikacji z osobna. Dodatkowo, bashish wspiera zmianę znaku
zachęty na większości popularnych powłok, takich jak bash, zsh czy
tcsh.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/bashish*
