Summary:	A window switcher, application launcher and dmenu replacement
Name:		rofi
Version:	1.6.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://github.com/davatorium/rofi/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8e2c08873f802a14c8b8e5d43f2a1261
URL:		https://github.com/davatorium/rofi
BuildRequires:	bison
BuildRequires:	cairo-devel
BuildRequires:	check
BuildRequires:	flex >= 2.5.39
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	librsvg-devel
BuildRequires:	libxcb-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xcb-util-xrm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.1
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
Requires:	glib2 >= 1:2.40
Requires:	xorg-lib-libxkbcommon >= 0.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rofi is a dmenu replacement. Rofi, like dmenu, will provide the user
with a textual list of options where one or more can be selected. This
can either be, running an application, selecting a window or options
provided by an external script.

%package devel
Summary:	Header files for rofi
Group:		Development/Libraries

%description devel
Header files for rofi.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env bash,/bin/bash,' script/rofi-{sensible-terminal,theme-selector}

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README.md
%attr(755,root,root) %{_bindir}/rofi
%attr(755,root,root) %{_bindir}/rofi-sensible-terminal
%attr(755,root,root) %{_bindir}/rofi-theme-selector
%{_datadir}/rofi
%{_mandir}/man1/rofi.1*
%{_mandir}/man1/rofi-sensible-terminal.1*
%{_mandir}/man1/rofi-theme-selector.1*
%{_mandir}/man5/rofi-script.5*
%{_mandir}/man5/rofi-theme.5*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rofi
%{_pkgconfigdir}/rofi.pc
