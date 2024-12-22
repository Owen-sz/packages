# %global goipath		github.com/arduino/serial-monitor
%define debug_package	%nil

Name:          arduino-serial-monitor
Version:       0.14.1
Release:       1%?dist
Summary:       Arduino pluggable monitor for serial ports.
License:       GPLv3
Packager:      Owen Zimmerman <owen@fyralabs.com>
Url:           https://github.com/arduino/serial-monitor
Source0:       %url/archive/refs/tags/v%version.tar.gz
BuildRequires: golang git go-rpm-macros anda-srpm-macros
Provides:      serial-monitor

%description
The serial-monitor tool is a command line program that interacts via stdio. It accepts commands as plain ASCII strings terminated with LF \n and sends response as JSON.

%prep
%autosetup -n serial-monitor-%version

%build
mkdir -p bin
go get go.bug.st/serial@v1.3.2
go get github.com/arduino/pluggable-monitor-protocol-handler@v0.9.1
go get github.com/hashicorp/errwrap@v1.0.0
go get golang.org/x/sys@v0.0.0-20210823070655-63515b42dcdf

%go_build_online
# go build
# %{goipath}
# %gobuild -o %{gobuilddir}/bin/serial-monitor

%install
%gopkginstall
# install -m 0755 -vd                     %{buildroot}%{_bindir}
# install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# %gopkginstall
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 serial-monitor %{buildroot}%{_bindir}/serial-monitor

# symlink arduino-serial-monitor to serial-monitor
ln -sf %buildroot%{_bindir}/serial-monitor arduino-serial-monitor

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/serial-monitor
%{_bindir}/arduino-serial-monitor

%changelog
* Thu Dec 5 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-serial-monitor
