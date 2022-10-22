Name:           factory-bookmarks
Version:        36
Release:        300%{?dist}
Summary:        Factory bookmarks
License:        MIT
URL:            http://factorylinux.com/

Source0:        default-bookmarks.html
BuildArch:      noarch

Provides:       system-bookmarks
Obsoletes:      fedora-bookmarks < %{version}


%description
This package contains the default bookmarks for Factory Linux.


%prep


%build


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%files
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html


%changelog
* Sat Oct 22 2022 Factory Linux Developers <info@factorylinux.com> 
- Built For The Factory Linux!
