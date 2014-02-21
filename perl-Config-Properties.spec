%define upstream_name    Config-Properties
%define upstream_version 1.76

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Configuration using Java style properties
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/Config-Properties-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.720.0-1mdv2011
+ Revision: 690245
- update to new version 1.72

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.710.0-2
+ Revision: 658742
- rebuild for updated spec-helper

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.710.0-1mdv2011.0
+ Revision: 553077
- update to 1.71

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.700.0-1mdv2010.0
+ Revision: 401701
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70-1mdv2010.0
+ Revision: 369678
- update to new version 1.70

* Tue Dec 02 2008 Jérôme Quelin <jquelin@mandriva.org> 1.69-1mdv2009.1
+ Revision: 309189
- update to new version 1.69

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.68-2mdv2009.0
+ Revision: 268401
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Jérôme Quelin <jquelin@mandriva.org> 1.68-1mdv2009.0
+ Revision: 201992
- import perl-Config-Properties




