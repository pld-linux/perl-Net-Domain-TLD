#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	PDIR
%define		pnam	PNAM
%include	/usr/lib/rpm/macros.perl
Summary:	Work with TLD names
Name:		perl-Net-Domain-TLD
Version:	1.70
Release:	1
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://search.cpan.org/CPAN/authors/id/A/AL/ALEXP/Net-Domain-TLD-%{version}.tar.gz
# Source0-md5:	025709d5c48461ff8b647254ac3cffbc
URL:		http://search.cpan.org/dist/Net-Domain-TLD/
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Storable)
BuildRequires:	perl(base)
BuildRequires:	perl(constant)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this module is to provide user with current list of
available top level domain names including new ICANN additions and
ccTLDs.

%prep
%setup -q -n Net-Domain-TLD-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Net/Domain/TLD/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/Domain/TLD.pm
%{_mandir}/man3/Net::Domain::TLD.3pm*
