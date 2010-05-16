#
%define		pkgname	jdepend
#
Summary:	JDepend utility
Summary(pl.UTF-8):	Narzędzie JDepend
Name:		java-%{pkgname}
Version:	2.9
Release:	2
License:	BSD
Group:		Development/Languages/Java
Source0:	http://www.clarkware.com/software/%{pkgname}-%{version}.zip
# Source0-md5:	4e979c0dda766ba1dd719905ca975c7b
URL:		http://www.clarkware.com/software/JDepend.html
BuildRequires:	ant
%buildrequires_jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jpackage-utils
Obsoletes:	jdepend
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JDepend traverses Java class file directories and generates design
quality metrics for each Java package. JDepend allows you to
automatically measure the quality of a design in terms of its
extensibility, reusability, and maintainability to manage package
dependencies effectively.

%description -l pl.UTF-8
JDepend wędruje po katalogach z plikami klas Javy i generuje metryki
jakości projektu dla każdego pakietu Javy. Pozwala automatycznie
szacować jakość projektu w zakresie rozszerzalności, reużywalności i
utrzymania w celu wydajnego zarządzania zależnościami pakietów.

%package doc
Summary:	JDepend documentation
Summary(fr.UTF-8):	Documentation pour JDepend
Summary(it.UTF-8):	Documentazione di JDepend
Summary(pl.UTF-8):	Dokumentacja do JDepend
Group:		Documentation
Obsoletes:	jdepend-doc

%description doc
JDepend documentation.

%description doc -l fr.UTF-8
Documentation pour JDepend.

%description doc -l it.UTF-8
Documentazione di JDepend.

%description doc -l pl.UTF-8
Dokumentacja do JDepend.

%package javadoc
Summary:	Online manual for JDepend
Summary(pl.UTF-8):	Dokumentacja online do JDepend
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jdepend-javadoc

%description javadoc
Documentation for JDepend.

%description javadoc -l pl.UTF-8
Dokumentacja do JDepend.

%prep
%setup -qn %{pkgname}-%{version}

%build
%ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a dist/%{pkgname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{pkgname}-%{version}.jar
ln -s %{pkgname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{pkgname}.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname}-%{version}
cp -a build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname}-%{version}
ln -s %{pkgname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{pkgname}-%{version} %{_javadocdir}/%{pkgname}

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%{_javadir}/jdepend*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{pkgname}-%{version}
%ghost %{_javadocdir}/%{pkgname}
