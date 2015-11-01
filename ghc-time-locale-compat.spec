# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name time-locale-compat

Name:           ghc-%{pkg_name}
Version:        0.1.1.0
Release:        1%{?dist}
Summary:        Compatibility of TimeLocale between old-locale and time-1.5

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-time-devel
# End cabal-rpm deps

%description
This package contains wrapped name module for TimeLocale.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files


%changelog
* Sat Oct 31 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.1.0-1
- spec file generated by cabal-rpm-0.9.6