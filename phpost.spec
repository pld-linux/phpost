Summary:	A web based POP mail client written in PHP4
Summary(pl):	Klient POP przez WWW, napisany w PHP4
Name:		phpost
Version:	1.07
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	http://webgadgets.com/phpost/phpost-1.07.tar.gz
Patch0:		%{name}_Polski.patch
Requires:	php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpostdir	/home/httpd/html/%{name}/

%description
PHPost is a free PHP4 program that implements a POP mail client.  It is
designed to work with any standard POP and SMTP server (for receiving and
sending mail respectively).  It is simple and straight-forward, it doesn't
rely on any PHP add-ons or optional modules (although it will use certain
ones if they are available)

%description -l pl
Jest to darmowy klinet POP'a napisany w PHP4. Jest przeznaczony do pracy ze
standartowymi serwerami POP oraz SMTP.

%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p0

%build

%install
install -d $RPM_BUILD_ROOT%{_phpostdir}/{%{name}_cache,%{name}_prefs,%{name}_temp}
cp *.{gif,php,css,inc} $RPM_BUILD_ROOT%{_phpostdir}
cp %{name}_cache/.htaccess $RPM_BUILD_ROOT%{_phpostdir}%{name}_cache/
cp %{name}_prefs/.htaccess $RPM_BUILD_ROOT%{_phpostdir}%{name}_prefs/
ln -sf %{name}.php $RPM_BUILD_ROOT%{_phpostdir}index.php

gzip -9nf {CHANGES,LICENSE,README,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo ""
echo "Don't forget to edit /home/httpd/html/phpost/phpost.inc !"

%files
%defattr(640,root,http,755)
%attr(770,root,http)%{_phpostdir}%{name}_cache
%attr(770,root,http)%{_phpostdir}%{name}_prefs
%attr(770,root,http)%{_phpostdir}%{name}_temp
%attr(644,root,http)%{_phpostdir}*.gif
%attr(644,root,http)%{_phpostdir}*.inc
%attr(644,root,http)%{_phpostdir}*.css
%attr(644,root,http)%{_phpostdir}*.php

%doc *.gz
