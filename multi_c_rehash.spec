Name: multi_c_rehash
Version: 1.1
Release: 1
Summary: A c_rehash implementation in C
Group: System/Libraries
License: Public domain
URL: http://www.j10n.org/
Source0: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(libcrypto)
Patch0: hash-crt-files.patch
Patch1: less-noisy-by-default.patch

%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_bindir}/*

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i 's,/usr/local,/usr,g' Makefile

%build
make CFLAGS=-DCERTDIR=\\\"/etc/ssl/certs\\\"

%install
make DESTDIR=%{buildroot} install
