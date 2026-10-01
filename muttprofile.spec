Name:           muttprofile
BuildArch:      noarch
Version:        1.0.1
Release:        0+mike1%{?dist}
Summary:        choose mutt profile interactively

License:        GPL
URL:            http://www.iki.fi/martti.rahkila/mutt/
Source0:        %{name}-%{version}.tar.gz

%description
muttprofile is a simple utility to choose a profile to be used with Mutt
email-client.  It has two operating modes: command-line and interactive.


%prep
%autosetup -n %{name}-%{version}.orig


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1
install muttprofile $RPM_BUILD_ROOT/%{_bindir}
install muttprofile.1 $RPM_BUILD_ROOT/%{_mandir}/man1


%files
%doc muttprofile.html
%{_bindir}/muttprofile
%{_mandir}/man1/muttprofile.1*


%changelog
* Sun Jan  1 2017 Mike Gerber <mike@sprachgewalt.de>
- First package
