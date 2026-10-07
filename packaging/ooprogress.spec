Name:           ooprogress
Version:        0.1.0
Release:        1%{?dist}
Summary:        Piped progress bar listener updating terminals cleanly from concurrent streams.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooprogress
Source0:        ooprogress-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooprogress is a sovereign, capability-bounded ASYNC PROGRESS written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooprogress
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooprogress-uninstall

%files
/usr/bin/ooprogress
/usr/bin/ooprogress-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
