%define upstream_name    JSON-MaybeXS
%define upstream_version 1.004000

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Use L<Cpanel::JSON::XS> with a fallback to L<JSON::PP>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/JSON/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Cpanel::JSON::XS) >= 2.331.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON::PP) >= 2.273.0
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More) >= 0.880.0
BuildArch:  noarch

%description
This module tries to load the Cpanel::JSON::XS manpage, and if that fails
instead tries to load the JSON::PP manpage. If neither is available, an
exception will be thrown.

It then exports the 'encode_json' and 'decode_json' functions from the
loaded module, along with a 'JSON' constant that returns the class name for
calling 'new' on.

If you're writing fresh code rather than replacing JSON.pm usage, you might
want to pass options as constructor args rather than calling mutators, so
we provide our own 'new' method that supports that.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%__make test

%install
%make_install

%files
%doc Changes META.json META.yml MYMETA.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
