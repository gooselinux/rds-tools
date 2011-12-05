Name:		rds-tools
Summary:	RDS support tools 
Version:	1.5
Release:	2%{?dist}
License:	GPLv2+ or BSD
Group:		Applications/System
URL:		http://oss.oracle.com/projects/rds/
# As per the rds site above, the RDS user space tools are distributed through
# the OpenFabrics Enterprise Distribution (OFED).  In order to get the
# current rds-tools tarball, you need to download the current OFED distribution,
# unpack it, install the rds-tools src rpm, then grab the tarball from your
# rpm SOURCES directory.  The OFED distribution can be downloaded from:
# http://www.openfabrics.org/downloads/OFED/
Source:		rds-tools-%{version}-1.tar.gz
Patch0:		rds-tools-1.4-debug.patch
Patch1:		rds-tools-1.5-pfhack.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:	s390 s390x

%description
Various tools for support of the RDS (Reliable Datagram Socket) API.  RDS
is specific to InfiniBand and iWARP networks and does not work on non-RDMA
hardware.

%prep
%setup -q -n rds-tools-%{version}-1
%patch0 -p1 -b .debug
%patch1 -p1 -b .pf

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
chmod 0755 %{buildroot}%{_bindir}/*
rm -fr %{buildroot}%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README docs examples stap
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Fri Feb 19 2010 Doug Ledford <dledford@redhat.com> - 1.5-2
- Remove include file as we don't provide a real devel environment
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 1.5-1
- Update to latest upstream version
- Related: bz518218

* Tue Jul 21 2009 Doug Ledford <dledford@redhat.com> - 1.4-2
- Enable debug output during build so debuginfo package isn't empty
- Resolves: bz500627

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 1.4-1.el5
- Initial version for Red Hat Enterprise Linux 5
- Related: bz459652

