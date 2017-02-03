# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name taffybar

Name:           %{pkg_name}
Version:        0.4.6
Release:        3%{?dist}
Summary:        A desktop bar similar to xmobar, but with more GUI

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-HStringTemplate-devel
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-X11-devel
BuildRequires:  ghc-cairo-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-dbus-devel
BuildRequires:  ghc-dyre-devel
BuildRequires:  ghc-enclosed-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-gtk-devel
BuildRequires:  ghc-gtk-traymanager-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-locale-compat-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-xdg-basedir-devel
BuildRequires:  ghc-xmonad-contrib-devel
BuildRequires:  ghc-xmonad-devel
BuildRequires:  pkgconfig(gtk+-2.0)
# End cabal-rpm deps

%description
A somewhat fancier desktop bar than xmobar. This bar is based on gtk2hs and
provides several widgets (including a few graphical ones). It also sports an
optional snazzy system tray.


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package contains the Haskell %{name} library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       ghc-%{name} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gtk+-2.0)
# End cabal-rpm deps

%description -n ghc-%{name}-devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post -n ghc-%{name}-devel
%ghc_pkg_recache


%postun -n ghc-%{name}-devel
%ghc_pkg_recache


%files
%license LICENSE
%doc README.md CHANGELOG.md taffybar.hs.example taffybar.rc
%{_bindir}/%{name}
/usr/share/taffybar-0.4.6/taffybar.rc


%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files


%changelog
* Tue Nov 03 2015 Martin Bukatovič <martin.bukatovic@gmail.com> -  0.4.5-3
- patching network-uri hack out (ghc-taffybar* packages were not installable)

* Sun Nov 01 2015 Martin Bukatovič <martin.bukatovic@gmail.com> -  0.4.5-2
- first actuall build of the package
- spec file changed to follow BinLib package guidelines
- cabal flag 'network-uri' set to False

* Sun Nov  1 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.4.5-1
- spec file generated by cabal-rpm-0.9.6
