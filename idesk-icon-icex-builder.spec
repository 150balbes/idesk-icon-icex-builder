Name: idesk-icon-icex-builder
Version: 0.0.2
Release: alt1

Summary: Icon for idesk icex-builder
Group: Graphical desktop/Icewm
License: GPL
Url: https://www.github.com/150balbes/idesk-icon
Packager: Oleg Ivanov <Leo-sp150@yandex.ru>

Requires: idesk >= 0.7.5-alt10

Source0: icon.tar.gz

BuildArch: noarch

%description
Icon for idesk icex-builder

%prep
%build
%install
mkdir -p %buildroot%_sysconfdir/skel
tar -xzf %SOURCE0 -C %buildroot%_sysconfdir/skel

%files
%dir %_sysconfdir/skel/.idesktop
%_sysconfdir/skel/idesktop/*

%changelog
* Sun Mar 02 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.2-alt1
- new ver

* Sun Jan 03 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt4
- add nemiver.lnk

* Sun Dec 31 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt3
- add distrohelper.lnk

* Sun Nov 18 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt2
- init
