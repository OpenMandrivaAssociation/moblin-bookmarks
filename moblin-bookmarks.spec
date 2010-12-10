Name:           moblin-bookmarks
Version:        2
Release:        %mkrel 2
Summary:        Moblin bookmarks
Group:          Networking/WWW
License:        GFDL
URL:            http://moblin.org/
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for Fedora.

%prep
# We are nihilists, Lebowski.  We believe in nassing.

%build
# We are nihilists, Lebowski.  We believe in nassing.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html
