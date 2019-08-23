#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jcifs
Version  : 1
Release  : 1
URL      : https://repo.gradle.org/gradle/libs-releases/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17-sources.jar
Source0  : https://repo.gradle.org/gradle/libs-releases/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17-sources.jar
Source1  : https://repo.gradle.org/gradle/libs-releases/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: mvn-jcifs-data = %{version}-%{release}
Requires: mvn-jcifs-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
Tue Oct 18 15:10:23 EDT 2011
jcifs-1.3.17
The jcifs.smb.client.soTimeout property, which controls how long the
client will wait to read data from a server, was broken in the previous
release (1.3.16). Not only was it broken but no SO_TIMEOUT was specified
at all meaning if a server became unresponive, JCIFS could hang for
an uncontrollably long time. This behavior of this property has been
restored.

%package data
Summary: data components for the mvn-jcifs package.
Group: Data

%description data
data components for the mvn-jcifs package.


%package license
Summary: license components for the mvn-jcifs package.
Group: Default

%description license
license components for the mvn-jcifs package.


%prep
%setup -q -n jcifs_1.3.17

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jcifs
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-jcifs/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17-sources.jar
/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17.jar
/usr/share/java/.m2/repository/org/samba/jcifs/jcifs/1.3.17/jcifs-1.3.17.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jcifs/LICENSE.txt
