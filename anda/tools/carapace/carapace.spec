%define debug_package %nil
%define go_version 1.23.1

Name:           carapace-bin
Version:        1.1.1
Release:        1%?dist
Summary:        Argument completion for multiple CLI commands
License:        MIT
URL:            https://github.com/carapace-sh/carapace-bin
Source0:        %url//archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang git go2rpm
Provides:       carapace

%description
Carapace-bin provides argument completion for multiple CLI commands, and works across multiple POSIX and non-POSIX shells.

%prep
%autosetup -n carapace-bin-%version

# Fix the Go version in go.mod before running go mod download

# Ensure Go modules are enabled
export GO111MODULE=on

# Download the Go modules
go mod download -x

%build
mkdir -p build/bin

# Set GOROOT to the correct path
export GOROOT=$(go env GOROOT)
export PATH=$GOROOT/bin:$PATH

# Build the project
go build -ldflags "-s -w" -v -x -buildmode=pie -o build/bin/carapace-bin ./cmd/carapace

%install
mkdir -p %buildroot%_bindir
install -pm755 build/bin/carapace-bin %buildroot%_bindir/

%files
%doc README.md
%license LICENSE
%_bindir/carapace-bin

%changelog
* Fri Dec 20 2024 Owen-sz <owen@fyralabs.com>
- Package Carapace-bin
