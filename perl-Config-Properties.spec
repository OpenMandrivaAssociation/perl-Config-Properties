
%define realname   Config-Properties
%define version    1.70
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Configuration using Java style properties
Source:     http://www.cpan.org/modules/by-module/Config/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Wrap)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*



