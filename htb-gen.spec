#
# TODO:
# - package web-frontend
#
Summary:	htb-gen - easy bandwidth management tool
Summary(pl):	htb-gen - �atwe w u�yciu narz�dzie do zarz�dzania pasmem
Name:		htb-gen
Version:	0.8.3
Release:	0.5
License:	GPL v2
Group:		Applications
Source0:	http://www.praga.org.ar/dev/htb-gen/packages/%{name}-%{version}.tar.gz
# Source0-md5:	99848cb1310a9cfd1d79df005af955cc
URL:		http://www.praga.org.ar/wacko/DevPraga/htbgen/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
htb-gen is meant to be an easy, scalable, yet powerful, bandwidth
management tool. You can set up/down portions of bandwith for each
host or network, that goes through your router/firewall. Prioritary
traffic (web, mail, gaming, FTP, VoIP, streaming) is preferred over
Junk traffic (kazaa, emule, etc.). Also dynamic bandwith borrow and
re-assignation is done between host thanks to HTB boundaries. All bash
based so it can be used in embedded routers/firewalls
(wired/wireless).

Two backend are available:
 - generates raw tc commands
 - generates htb-init conf files (util for integration)

%description -l pl
htb-gen jest �atwym w u�yciu, skalowalnym lecz pot�nym narz�dziem do
zarz�dzania pasmem. Mo�na przypisywa� cz�� pasma w obu kierunkach dla
poszczeg�lnych host�w lub sieci pod��czonych przez router/firewall.
Ruch priorytetowy (WWW, poczta, gry, FTP, VoIP, strumienie) jest
preferowany w stosunku do ruchu za�miecaj�cego (kazaa, emule itp.).
Dzi�ki ograniczeniom HTB mo�liwe jest tak�e dynamiczne po�yczanie i
przekazywanie pasma. Wszystko jest oparte na bashu, co pozwala na
zastosowanie we wbudowanych routerach/firewallach (przewodowych lub
bezprzewodowych).

Dost�pne s� dwa backendy:
 - generuj�cy czyste polecenia tc
 - generuj�cy pliki konfiguracyjne htb-init (narz�dzia do integracji)

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/htb-gen
install htb-{gen,stats} $RPM_BUILD_ROOT%{_bindir}
install htb-gen*.conf $RPM_BUILD_ROOT%{_sysconfdir}/htb-gen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ README TODO
%dir %{_sysconfdir}/htb-gen
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/htb-gen/*
%attr(755,root,root) %{_bindir}/*
