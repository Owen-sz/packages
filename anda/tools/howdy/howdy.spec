# %define debug_package %nil

%global commit aa75c7666c040c6a7c83cd92b9b81a6fea4ce97c
%global commit_date 20240504
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           howdy
Version:        %commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Windows Hello™ style facial authentication for Linux
License:        MIT
URL:            https://github.com/boltgolt/howdy
Source0:        %url/archive/%commit.tar.gz
Requires:       meson bash gcc python3 python3-pip python3-setuptools python3-wheel pam-devel inih-devel libevdev-devel python3-devel opencv-devel

%description
Howdy provides Windows Hello™ style authentication for Linux. Use your built-in IR emitters and camera in combination with facial recognition to prove who you are.

Using the central authentication system (PAM), this works everywhere you would otherwise need your password: Login, lock screen, sudo, su, etc.

%prep
%autosetup -n howdy-%commit

%build
%{meson}
%{meson_build}
# meson setup build
# meson compile -C build
ls -l

%install
cd %buildroot
ls -l
meson install -C build
#install -Dm755 %buildroot/howdy/src/pam/pam_howdy.so            /usr/local/lib64/security
#install -Dm755 %buildroot/howdy/src/../howdy.1                  /usr/local/share/man/man1
#install -Dm755 %buildroot/howdy-gtk/src/authsticky.py           /usr/local/lib64/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/authsticky.py           /usr/local/lib64/howdy-gtk
#install -Dm755 %buildroot/howdy/howdy-gtk/src/init.py           /usr/local/lib64/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/onboarding.py           /usr/local/lib64/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/paths_factory.py        /usr/local/lib64/howdy-gtk
#nstall -Dm755 %buildroot/howdy-gtk/src/tab_models.py           /usr/local/lib64/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/tab_video.py            /usr/local/lib64/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/window.py               /usr/local/lib64/howdy-gtk
#install -Dm755 %buildroot/build/howdy-gtk/paths.py              /usr/local/lib64/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/logo.png                /usr/local/share/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/logo_about.png          /usr/local/share/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/main.glade              /usr/local/share/howdy-gtk
#install -Dm755 %buildroot/howdy-gtk/src/onboarding.glade        /usr/local/share/howdy-gtk
#install -Dm755 %buildroot/build/howdy-gtk/howdy-gtk             /usr/local/bin
#install -Dm755 %buildroot/howdy/src/cli/__init__.py             /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/add.py                  /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/clear.py                /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/config.py               /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/disable.py              /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/list.py                 /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/remove.py               /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/set.py                  /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/snap.py                 /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli/test.py                 /usr/local/lib64/howdy/cli
#install -Dm755 %buildroot/howdy/src/cli.py                      /usr/local/lib64/howdy
#install -Dm755 %buildroot/howdy/src/compare.py                  /usr/local/lib64/howdy
#install -Dm755 %buildroot/howdy/src/i18n.py                     /usr/local/lib64/howdy
#install -Dm755 %buildroot/howdy/src/paths_factory.py            /usr/local/lib64/howdy
#install -Dm755 %buildroot/howdy/src/snapshot.py                 /usr/local/lib64/howdy
#install -Dm755 %buildroot/build/howdy/src/paths.py              /usr/local/lib64/howdy
#install -Dm755 %buildroot/howdy/src/recorders/__init__.py       /usr/local/lib64/howdy/recorders
#install -Dm755 %buildroot/howdy/src/recorders/ffmpeg_reader.py  /usr/local/lib64/howdy/recorders
#install -Dm755 %buildroot/howdy/src/recorders/pyv4l2_reader.py  /usr/local/lib64/howdy/recorders
#install -Dm755 %buildroot/howdy/src/recorders/v4l2.py           /usr/local/lib64/howdy/recorders
#install -Dm755 %buildroot/howdy/src/recorders/video_capture.py  /usr/local/lib64/howdy/recorders
#install -Dm755 %buildroot/howdy/src/rubberstamps/__init__.py    /usr/local/lib64/howdy/rubberstamps
#install -Dm755 %buildroot/howdy/src/rubberstamps/hotkey.py      /usr/local/lib64/howdy/rubberstamps
#install -Dm755 %buildroot/howdy/src/rubberstamps/nod.py         /usr/local/lib64/howdy/rubberstamps
#install -Dm755 %buildroot/howdy/src/logo.png                    /usr/local/share/howdy
#install -Dm755 %buildroot/build/howdy/src/autocomplete          /usr/local/share/bash-completion/completions
#install -Dm755 %buildroot/howdy/src/config.ini                  /usr/local/etc/howdy
#install -Dm755 %buildroot/howdy/src/dlib-data/install.sh        /usr/local/share/dlib-data
#install -Dm755 %buildroot/howdy/src/dlib-data/Readme.md         /usr/local/share/dlib-data
#install -Dm755 %buildroot/build/howdy/src/howdy                 /usr/local/bin

%files
%doc README.md
%license LICENSE
/usr/local/lib64/security
/usr/local/share/man/man1
/usr/local/lib64/howdy-gtk
/usr/local/share/howdy-gtk
/usr/local/bin
/usr/local/lib64/howdy/cli
/usr/local/lib64/howdy
/usr/local/lib64/howdy/recorders
/usr/local/lib64/howdy/rubberstamps
/usr/local/share/howdy
/usr/local/share/bash-completion/completions
/usr/local/etc/howdy
/usr/local/share/dlib-data
/usr/local/bin

%changelog
* Sat Dec 21 2024 Owen-sz <owen@fyralabs.com>
- package howdy