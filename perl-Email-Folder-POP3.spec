#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Folder-POP3
Summary:	Email::Folder::POP3 - Email::Folder Access to POP3 Folders
Summary(pl):	Email::Folder::POP3 - Dostêp do katalogów POP3 z poziomu Email::Folder
Name:		perl-Email-Folder-POP3
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7671212bb0f13506890fe7f9ef3f3fe4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Email::Folder) >= 0.84
BuildRequires:	perl(Email::FolderType::Net) >= 1.02
BuildRequires:	perl(Net::POP3) >= 2.28
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(URI) >= 1.35
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software adds POP3 functionality to Email::Folder. Its interface
is identical to the other Email::Folder::Reader subclasses.

%description -l pl
Ten modu³ rozszerza Email::Folder o funkcjonalno¶æ POP3. Interfejs
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
