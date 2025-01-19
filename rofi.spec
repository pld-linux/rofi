#
# Conditional build:
%bcond_without	tests		# don't build tests

Summary:	A window switcher, application launcher and dmenu replacement
Name:		rofi
Version:	1.7.8
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://github.com/davatorium/rofi/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	030b3bc92392a3f2212e8f5b0f8987c7
URL:		https://github.com/davatorium/rofi
BuildRequires:	bison
BuildRequires:	cairo-devel
%{?with_tests:BuildRequires:	check-devel >= 0.11.0}
BuildRequires:	flex >= 2.5.39
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel >= 1:2.72
BuildRequires:	librsvg-devel
BuildRequires:	libxcb-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	startup-notification-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.1
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glib2 >= 1:2.72
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
	--disable-silent-rules \
	%{__enable_disable check}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README.md
%attr(755,root,root) %{_bindir}/rofi
%attr(755,root,root) %{_bindir}/rofi-sensible-terminal
%attr(755,root,root) %{_bindir}/rofi-theme-selector
%{_desktopdir}/rofi.desktop
%{_desktopdir}/rofi-theme-selector.desktop
%{_iconsdir}/hicolor/scalable/apps/rofi.svg
%{_datadir}/rofi
%{_mandir}/man1/rofi.1*
%{_mandir}/man1/rofi-sensible-terminal.1*
%{_mandir}/man1/rofi-theme-selector.1*
%{_mandir}/man5/rofi-debugging.5*
%{_mandir}/man5/rofi-dmenu.5*
%{_mandir}/man5/rofi-keys.5*
%{_mandir}/man5/rofi-script.5*
%{_mandir}/man5/rofi-theme.5*
%{_mandir}/man5/rofi-thumbnails.5*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rofi
%{_pkgconfigdir}/rofi.pc
