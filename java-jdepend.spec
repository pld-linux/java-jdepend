Summary:	JDepend utility
Summary(pl.UTF-8):	Narzędzie JDepend
Name:		jdepend
Version:	2.9
Release:	3
License:	BSD
Group:		Development/Languages/Java
Source0:	http://www.clarkware.com/software/%{name}-%{version}.zip
# Source0-md5:	4e979c0dda766ba1dd719905ca975c7b
URL:		http://www.clarkware.com/software/JDepend.html
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
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

%description javadoc
Documentation for JDepend.

%description javadoc -l pl.UTF-8
Dokumentacja do JDepend.

%prep
%setup -q

%build
%ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%{_javadir}/jdepend*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
