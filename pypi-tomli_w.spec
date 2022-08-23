#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tomli_w
Version  : 1.0.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/49/05/6bf21838623186b91aedbda06248ad18f03487dc56fbc20e4db384abde6c/tomli_w-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/05/6bf21838623186b91aedbda06248ad18f03487dc56fbc20e4db384abde6c/tomli_w-1.0.0.tar.gz
Summary  : A lil' TOML writer
Group    : Development/Tools
License  : MIT
Requires: pypi-tomli_w-license = %{version}-%{release}
Requires: pypi-tomli_w-python = %{version}-%{release}
Requires: pypi-tomli_w-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
[![Build Status](https://github.com/hukkin/tomli-w/workflows/Tests/badge.svg?branch=master)](https://github.com/hukkin/tomli-w/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)
[![codecov.io](https://codecov.io/gh/hukkin/tomli-w/branch/master/graph/badge.svg)](https://codecov.io/gh/hukkin/tomli-w)
[![PyPI version](https://img.shields.io/pypi/v/tomli-w)](https://pypi.org/project/tomli-w)

%package license
Summary: license components for the pypi-tomli_w package.
Group: Default

%description license
license components for the pypi-tomli_w package.


%package python
Summary: python components for the pypi-tomli_w package.
Group: Default
Requires: pypi-tomli_w-python3 = %{version}-%{release}

%description python
python components for the pypi-tomli_w package.


%package python3
Summary: python3 components for the pypi-tomli_w package.
Group: Default
Requires: python3-core
Provides: pypi(tomli_w)

%description python3
python3 components for the pypi-tomli_w package.


%prep
%setup -q -n tomli_w-1.0.0
cd %{_builddir}/tomli_w-1.0.0
pushd ..
cp -a tomli_w-1.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656368320
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tomli_w
cp %{_builddir}/tomli_w-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tomli_w/9da6ca26337a886fb3e8d30efd4aeda623dc9ade
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tomli_w/9da6ca26337a886fb3e8d30efd4aeda623dc9ade

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
