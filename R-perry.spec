#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-perry
Version  : 0.3.1
Release  : 10
URL      : https://cran.r-project.org/src/contrib/perry_0.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/perry_0.3.1.tar.gz
Summary  : Resampling-Based Prediction Error Estimation for Regression
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ggplot2
BuildRequires : R-ggplot2
BuildRequires : buildreq-R

%description
error estimation with minimal programming effort and assist users with
    model selection in regression problems.

%prep
%setup -q -c -n perry
cd %{_builddir}/perry

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641072878

%install
export SOURCE_DATE_EPOCH=1641072878
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library perry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library perry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library perry
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc perry || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/perry/DESCRIPTION
/usr/lib64/R/library/perry/INDEX
/usr/lib64/R/library/perry/Meta/Rd.rds
/usr/lib64/R/library/perry/Meta/features.rds
/usr/lib64/R/library/perry/Meta/hsearch.rds
/usr/lib64/R/library/perry/Meta/links.rds
/usr/lib64/R/library/perry/Meta/nsInfo.rds
/usr/lib64/R/library/perry/Meta/package.rds
/usr/lib64/R/library/perry/NAMESPACE
/usr/lib64/R/library/perry/NEWS
/usr/lib64/R/library/perry/R/perry
/usr/lib64/R/library/perry/R/perry.rdb
/usr/lib64/R/library/perry/R/perry.rdx
/usr/lib64/R/library/perry/doc/examples/example-accessors.R
/usr/lib64/R/library/perry/doc/examples/example-aggregate.R
/usr/lib64/R/library/perry/doc/examples/example-perryFit.R
/usr/lib64/R/library/perry/doc/examples/example-perryPlot.R
/usr/lib64/R/library/perry/doc/examples/example-perryReshape.R
/usr/lib64/R/library/perry/doc/examples/example-perrySelect.R
/usr/lib64/R/library/perry/doc/examples/example-perryTuning.R
/usr/lib64/R/library/perry/doc/examples/example-reperry.R
/usr/lib64/R/library/perry/doc/examples/example-setupPerryPlot.R
/usr/lib64/R/library/perry/doc/examples/example-subset.R
/usr/lib64/R/library/perry/doc/examples/example-summary.R
/usr/lib64/R/library/perry/help/AnIndex
/usr/lib64/R/library/perry/help/aliases.rds
/usr/lib64/R/library/perry/help/paths.rds
/usr/lib64/R/library/perry/help/perry.rdb
/usr/lib64/R/library/perry/help/perry.rdx
/usr/lib64/R/library/perry/html/00Index.html
/usr/lib64/R/library/perry/html/R.css
/usr/lib64/R/library/perry/tests/test-perryFit-oneCV.R
/usr/lib64/R/library/perry/tests/test-perryFit-repCV.R
/usr/lib64/R/library/perry/tests/test-perryReshape.R
/usr/lib64/R/library/perry/tests/test-perrySelect.R
/usr/lib64/R/library/perry/tests/test-perryTuning-oneCV.R
/usr/lib64/R/library/perry/tests/test-perryTuning-repCV.R
/usr/lib64/R/library/perry/tests/test-subset.R
