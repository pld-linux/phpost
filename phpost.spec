Summary:	A web based POP mail client written in PHP4
Summary(pl):	Klient POP przez WWW, napisany w PHP4
Name:		phpost
Version:	1.07
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(cs):	S�ov�/Utility
Group(da):	Netv�rks/V�rkt�j
Group(de):	Netzwerkwesen/Dienstprogramme
Group(es):	Red/Utilitarios
Group(fr):	R�seau/Utilitaires
Group(is):	Net/T�l
Group(it):	Rete/Utility
Group(no):	Nettverks/Verkt�y
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
Group(pt):	Rede/Utilidades
Group(ru):	�������/����������
Group(sl):	Omre�ni/Pripomo�ki
Group(sv):	N�tverk/Verktyg
Source0:	http://webgadgets.com/phpost/%{name}-%{version}.tar.gz
Patch0:		%{name}_Polski.patch
Requires:	php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpostdir	/home/httpd/html/%{name}

%description
PHPost is a free PHP4 program that implements a POP mail client. It is
designed to work with any standard POP and SMTP server (for receiving
and sending mail respectively). It is simple and straight-forward, it
doesn't rely on any PHP add-ons or optional modules (although it will
use certain ones if they are available)

%description -l pl
Jest to darmowy klient POP napisany w PHP4. Jest przeznaczony do pracy
ze standardowymi serwerami POP oraz SMTP.

%prep
%setup -q -c
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpostdir}/%{name}_{cache,prefs,temp}

install *.{gif,php,css,inc} $RPM_BUILD_ROOT%{_phpostdir}
install %{name}_cache/.htaccess $RPM_BUILD_ROOT%{_phpostdir}/%{name}_cache/
install %{name}_prefs/.htaccess $RPM_BUILD_ROOT%{_phpostdir}/%{name}_prefs/

ln -sf %{name}.php $RPM_BUILD_ROOT%{_phpostdir}index.php

gzip -9nf CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_phpostdir}
%attr(770,root,http) %{_phpostdir}/%{name}_cache
%attr(770,root,http) %{_phpostdir}/%{name}_prefs
%attr(770,root,http) %{_phpostdir}/%{name}_temp
%{_phpostdir}/*.gif
%{_phpostdir}/*.inc
%{_phpostdir}/*.css
%{_phpostdir}/*.php
