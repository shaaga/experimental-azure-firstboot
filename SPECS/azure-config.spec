Name:           azure-config
Version:        1.0
Release:        0
Summary:        Give network devices names based on physical location of the connector of the hardware

Group:          Tools
License:        GPL v3
URL:            none
Source0:        azure-config.tar.gz
BuildArch:      noarch

Requires:       /bin/bash
%{?systemd_requires}

BuildRequires: systemd

%description
This adds a single udev rule to produce network device names based on physical location of the connector of the hardware

It is meant to be used on certain Azure hardware based instances to provide
a network naming environment that is similar to other operating systems used
in the Azure environment.

%prep
%setup -q -n azure-config


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/etc/udev/rules.d
install -m 644 etc/udev/rules.d/80-net-name-slot.rules  ${RPM_BUILD_ROOT}/etc/udev/rules.d/80-net-name-slot.rules
#chcon -u system_u -t initrc_exec_t ${RPM_BUILD_ROOT}/etc/init.d/azfirstboot.sh


%files
%defattr(-,root,root,-)
/etc/udev/rules.d/80-net-name-slot.rules

%changelog
* Tue Aug 18 2020 Ian McLeod <imcleod@redhat.com> - 0.6-6
- Initial re-packaging of udev rule as RPM
