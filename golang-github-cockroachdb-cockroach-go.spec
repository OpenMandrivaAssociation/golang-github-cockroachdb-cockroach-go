# https://github.com/cockroachdb/cockroach-go
%global goipath         github.com/cockroachdb/cockroach-go
%global commit          59c0560478b705bf9bd12f9252224a0fad7c87df

%global common_description %{expand:
CockroachDB helpers for Go.}

%gometa

Name:           golang-github-cockroachdb-cockroach-go
Version:        0
Release:        0.4%{?dist}
Summary:        CockroachDB helpers for Go
# Detected licences
# - *No copyright* Apache License (v2.0) at 'LICENSE'
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/lib/pq)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
# Tests download binaries from the internet
# %%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181114git59c0560
- Bump to commit 59c0560478b705bf9bd12f9252224a0fad7c87df
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170809gitc806b48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170809gitc806b48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170809gitc806b48
- First package for Fedora
