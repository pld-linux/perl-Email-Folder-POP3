#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Email
%define	pnam	Folder-POP3
Summary:	Email::Folder::POP3 - Email::Folder access to POP3 folders
Summary(pl.UTF-8):	Email::Folder::POP3 - dostęp do katalogów POP3 z poziomu Email::Folder
Name:		perl-Email-Folder-POP3
Version:	1.013
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cdd6956824c72350be95ce6ca648e027
URL:		http://search.cpan.org/dist/Email-Folder-POP3/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Folder >= 0.84
BuildRequires:	perl-Email-FolderType-Net >= 1.02
BuildRequires:	perl(Net::POP3) >= 2.28
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl-URI >= 1.35
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software adds POP3 functionality to Email::Folder. Its interface
is identical to the other Email::Folder::Reader subclasses.

%description -l pl.UTF-8
Ten moduł rozszerza Email::Folder o funkcjonalność POP3. Interfejs
jest identyczny z innymi podklasami Email::Folder::Reader.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/Folder/POP3.pm
%{_mandir}/man3/*
