#
# Conditional build:
%bcond_with	pda	# use PDA-style app folder setup (rather than Desktop)
#
Summary:	Common files for Matchbox desktop
Summary(pl):	Wspólne pliki dla ¶rodowiska Matchbox
Name:		matchbox-common
Version:	0.9.1
Release:	1
License:	GPL(?)
Group:		X11/Applications
Source0:	http://projects.o-hand.com/matchbox/sources/matchbox-common/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	8e8ba0ee170a9ac78fdc583b00ccf76b
URL:		http://projects.o-hand.com/matchbox/
# just to check for png support in libmatchbox
BuildRequires:	libmatchbox-devel >= 1.1
BuildRequires:	pkgconfig
Requires:	matchbox-desktop >= 0.9
Requires:	matchbox-panel >= 0.9
Requires:	matchbox-window-manager >= 0.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common files for Matchbox desktop.

%description -l pl
Wspólne pliki dla ¶rodowiska Matchbox.

%prep
%setup -q

%build
%configure \
	%{?with_pda:--enable-pda-folders}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/matchbox-session
%{_datadir}/matchbox/vfolders/*.directory
%{_datadir}/matchbox/vfolders/Root.order
%{_iconsdir}/blondie
%{_pixmapsdir}/*.png
