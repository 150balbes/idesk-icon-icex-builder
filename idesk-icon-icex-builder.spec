Name: idesk-icon-icex-builder
Version: 0.0.1
Release: alt3

Summary: Icon for idesk icex-builder
Group: Graphical desktop/Icewm
License: GPL
Url: https://www.github.com/150balbes/idesk-icon
Packager: Oleg Ivanov <Leo-sp150@yandex.ru>

Requires: idesk >= 0.7.5-alt10

Source0: icon.tar

BuildArch: noarch

%description
Icon for idesk icex-builder

%prep
%build
%install
mkdir -p %buildroot%_sysconfdir/idesk.d/icon
tar xf %SOURCE0 -C %buildroot%_sysconfdir/idesk.d/

%files
%dir %_sysconfdir/idesk.d/icon
%_sysconfdir/idesk.d/icon/*

%changelog
* Sun Dec 31 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt3
- add distrohelper.lnk

* Sun Nov 18 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt2
- init
