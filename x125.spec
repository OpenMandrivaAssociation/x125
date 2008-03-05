Summary:	A printer driver for the Lexmark X125 All-in-one printer/scanner/fax
Name:		x125
Version:	0.2.3
Release:	%mkrel 4
Group:		System/Printing
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
URL:		http://sourceforge.net/projects/x125-linux/
Source0:	http://heanet.dl.sourceforge.net/sourceforge/x125-linux/x125-drv-0.2.3.tar.gz
Source1:	http://heanet.dl.sourceforge.net/sourceforge/x125-linux/x125-drv-network-0.2.0.tar.gz
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007

%description
A printer driver for the Lexmark X125 All-in-one printer/scanner/fax.

%prep

%setup -q -c -T -a0 -a1

%build
perl -p -i -e "s/gcc/gcc %{optflags}/" drv_x125*/src/Makefile

cd drv_x125/src
%make
cd ../..
cd drv_x125_network/src
%make
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
