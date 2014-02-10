# Generated from qpid_proton-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name qpid_proton
%global rubyabi 1.9.1

Summary:       Ruby language bindings for the Qpid Proton messaging framework
Name:          rubygem-%{gem_name}
Version:       0.6
Release:       2%{?dist}
License:       ASL 2.0

URL:           http://qpid.apache.org/proton
# rubygems.org is currently read-only and the newer gem cannot be pushed ATM.
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: qpid-proton-c-devel = %{version}
BuildRequires: libuuid-devel

Requires:      ruby(release)
Requires:      rubygems
Requires:      qpid-proton-c = %{version}

Provides:      rubygem(%{gem_name}) = %{version}

%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard.

# === rubygem-qpid_proton-doc

%package doc
Summary:   Documentation for %{name}
BuildArch: noarch

%description doc
%{summary}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# apply any patches here

%build
gem build %{gem_name}.gemspec

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/lib/
mv %{buildroot}%{gem_instdir}/lib/cproton.so \
   %{buildroot}%{gem_extdir_mri}/lib/

rm -rf %{buildroot}%{gem_instdir}/ext


%check


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/TODO

%changelog
* Mon Feb 10 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.6-2
- Removed requirement on the main package by the doc subpackage.
- Removed Group declarations.

* Fri Jan 17 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.6-1
- Rebased on Proton 0.6.

* Thu Aug 29 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.5-1
- Rebased on Proton 0.5.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  1 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2.2
- Fixed the dependencies to be qpid-proton-c and qpid-proton-c-devel.

* Wed Mar  6 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2.1
- Changed ruby(release) to ruby(abi) for Fedora < 19.
- Resolves: BZ#906843

* Wed Mar  6 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2
- First official build for Fedora.
- Resolves: BZ#906843

* Sat Mar  2 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-1.1
- Changed the BR for Ruby to match F19 packaging guidelines.
- Changed install to use the gem_install macro.
- Fixed the installation of the native library.

* Fri Mar  1 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-1
- Rebased on Proton 0.4.

* Mon Feb 25 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-1.1
- Updated to meet the new Fedora 19 packaging guidelines.

* Fri Feb  1 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-1
- Initial package
