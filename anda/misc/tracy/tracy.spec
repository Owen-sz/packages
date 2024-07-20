Name:			tracy
Version:		0.10
Release:		1%?dist
Summary:		A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.
License:		BSD-3-Clause
URL:			https://github.com/wolfpld/tracy
Source0:		https://github.com/wolfpld/tracy/archive/refs/tags/v%version.tar.gz
BuildRequires:  cmake meson gcc gcc-c++ libxkbcommon dbus-devel libglvnd glfw-devel freetype-devel pkgconfig(capstone) pkgconfig(libunwind) pkgconfig(libdebuginfod) pkgconfig(tbb)
Patch:          https://github.com/wolfpld/tracy/commit/1a971d867d6fa5bf6dc57d705dcbbc6020031e7a.patch

%description
A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.*
%{_datadir}/tracy
