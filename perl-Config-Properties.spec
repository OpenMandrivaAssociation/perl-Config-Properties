%define upstream_name    Config-Properties
%define upstream_version 1.80
Name:		perl-%{upstream_name}
Version:	1.80
Release:	1

Summary:	Configuration using Java style properties

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/salva/p5-Config-Properties
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SALVA/Config-Properties-1.80.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Wrap)
BuildArch:	noarch

%description
Config::Properties is a near implementation of the java.util.Properties
API. It is designed to allow easy reading, writing and manipulation of
Java-style property files.

The format of a Java-style property file is that of a key-value pair
seperated by either whitespace, the colon (:) character, or the equals (=)
character. Whitespace before the key and on either side of the seperator is
ignored.

Lines that begin with either a hash (#) or a bang (!) are considered
comment lines and ignored.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


