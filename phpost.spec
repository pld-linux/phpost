Summary:	A web based POP mail client written in PHP4
Summary(pl):	Klient POP przez WWW, napisany w PHP4
Name:		phpost
Version:	1.10
Release:	1.beta
License:	GPL
Group:		Networking/Utilities
Source0:	http://webgadgets.com/phpost/%{name}.tar.gz
# Source0-md5:	a5cbec332c1d55296d0b84f48e9715b5
Source1:        %{name}.conf
Patch0:		%{name}_Polski.patch
Requires:	php
Requires:	php-pcre
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpostdir      %{_datadir}/%{name}
%define         _sysconfdir     /etc/%{name}


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
#%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpostdir}/%{name}_{cache,prefs,temp} \
        $RPM_BUILD_ROOT{%{_sysconfdir},/etc/httpd}

install *.{gif,php,css,inc} $RPM_BUILD_ROOT%{_phpostdir}
install %{name}_cache/.htaccess $RPM_BUILD_ROOT%{_phpostdir}/%{name}_cache/
install %{name}_prefs/.htaccess $RPM_BUILD_ROOT%{_phpostdir}/%{name}_prefs/
rm -f $RPM_BUILD_ROOT%{_phpostdir}/phpost.inc.php

cp phpost.inc.php $RPM_BUILD_ROOT%{_sysconfdir}
ln -sf %{_sysconfdir}/phpost.inc.php $RPM_BUILD_ROOT%{_phpostdir}/phpost.inc.php

ln -sf %{name}.php $RPM_BUILD_ROOT%{_phpostdir}/index.php

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
        echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
elif [ -d /etc/httpd/httpd.conf ]; then
        ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
        /usr/sbin/apachectl restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
        umask 027
        if [ -d /etc/httpd/httpd.conf ]; then
                rm -f /etc/httpd/httpd.conf/99_%{name}.conf
        else
                grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
                        /etc/httpd/httpd.conf.tmp
                mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
                if [ -f /var/lock/subsys/httpd ]; then
                        /usr/sbin/apachectl restart 1>&2
                fi
        fi
fi


%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%dir %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%config(noreplace) %verify(not size mtime md5) /etc/httpd/%{name}.conf
%dir %{_phpostdir}
%attr(770,root,http) %{_phpostdir}/%{name}_cache
%attr(770,root,http) %{_phpostdir}/%{name}_prefs
%attr(770,root,http) %{_phpostdir}/%{name}_temp
%{_phpostdir}/*.gif
%{_phpostdir}/*.inc
%{_phpostdir}/*.css
%{_phpostdir}/*.php
