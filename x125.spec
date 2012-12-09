Summary:	A printer driver for the Lexmark X125 All-in-one printer/scanner/fax
Name:		x125
Version:	0.2.3
Release:	%mkrel 9
Group:		System/Printing
License:	GPL
URL:		http://sourceforge.net/projects/x125-linux/
Source0:	http://heanet.dl.sourceforge.net/sourceforge/x125-linux/x125-drv-0.2.3.tar.gz
Source1:	http://heanet.dl.sourceforge.net/sourceforge/x125-linux/x125-drv-network-0.2.0.tar.gz
Patch0:		x125-0.2.3-LDFLAGS.diff
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A printer driver for the Lexmark X125 All-in-one printer/scanner/fax.

%prep

%setup -q -c -T -a0 -a1
%patch0 -p1 -b .LDFLAGS

%build
cd drv_x125/src
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
cd ../..
cd drv_x125_network/src
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
cd ../..

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 drv_x125/src/x125_cmyk %{buildroot}%{_bindir}/
install -m0755 drv_x125/src/x125_cmyk_print.sh %{buildroot}%{_bindir}/
install -m0755 drv_x125_network/src/x125_network %{buildroot}%{_bindir}/

cp drv_x125/README README.drv_x125
cp drv_x125/FAQ FAQ.drv_x125
cp drv_x125/ChangeLog ChangeLog.drv_x125
cp drv_x125_network/README README.drv_x125_network
cp drv_x125_network/FAQ FAQ.drv_x125_network
cp drv_x125_network/ChangeLog ChangeLog.drv_x125_network

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc drv_x125/LICENSE README.* FAQ.* ChangeLog.*
%attr(0755,root,root) %{_bindir}/*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-9mdv2011.0
+ Revision: 671246
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-8mdv2011.0
+ Revision: 608178
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-7mdv2010.1
+ Revision: 524370
- rebuilt for 2010.1

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-6mdv2009.1
+ Revision: 321070
- use %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-5mdv2009.0
+ Revision: 226013
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-4mdv2008.1
+ Revision: 179611
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-3mdv2008.0
+ Revision: 75359
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-2mdv2008.0
+ Revision: 64177
- use the new System/Printing RPM GROUP

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-1mdv2008.0
+ Revision: 61503
- Import x125



* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-1mdv2008.0
- initial Mandriva package
