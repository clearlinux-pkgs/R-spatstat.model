#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spatstat.model
Version  : 3.0.2
Release  : 2
URL      : https://cran.r-project.org/src/contrib/spatstat.model_3.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.model_3.0-2.tar.gz
Summary  : Parametric Statistical Modelling for the 'spatstat' Family
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.model-lib = %{version}-%{release}
Requires: R-abind
Requires: R-goftest
Requires: R-spatstat.data
Requires: R-spatstat.explore
Requires: R-spatstat.geom
Requires: R-spatstat.random
Requires: R-spatstat.sparse
Requires: R-spatstat.utils
Requires: R-tensor
BuildRequires : R-abind
BuildRequires : R-goftest
BuildRequires : R-spatstat.data
BuildRequires : R-spatstat.explore
BuildRequires : R-spatstat.geom
BuildRequires : R-spatstat.random
BuildRequires : R-spatstat.sparse
BuildRequires : R-spatstat.utils
BuildRequires : R-tensor
BuildRequires : buildreq-R

%description
spatial data, mainly spatial point patterns,
	     in the 'spatstat' family of packages.
	     (Excludes analysis of spatial data on a linear network,
	     which is covered by the separate package 'spatstat.linnet'.)
	     Methods include quadrat counts, K-functions and their simulation envelopes, nearest neighbour distance and empty space statistics, Fry plots, pair correlation function, kernel smoothed intensity, relative risk estimation with cross-validated bandwidth selection, mark correlation functions, segregation indices, mark dependence diagnostics, and kernel estimates of covariate effects. Formal hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and tests for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov, ANOVA) are also supported.

%package lib
Summary: lib components for the R-spatstat.model package.
Group: Libraries

%description lib
lib components for the R-spatstat.model package.


%prep
%setup -q -n spatstat.model
cd %{_builddir}/spatstat.model

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668014770

%install
export SOURCE_DATE_EPOCH=1668014770
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.model/CITATION
/usr/lib64/R/library/spatstat.model/DESCRIPTION
/usr/lib64/R/library/spatstat.model/INDEX
/usr/lib64/R/library/spatstat.model/Meta/Rd.rds
/usr/lib64/R/library/spatstat.model/Meta/features.rds
/usr/lib64/R/library/spatstat.model/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.model/Meta/links.rds
/usr/lib64/R/library/spatstat.model/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.model/Meta/package.rds
/usr/lib64/R/library/spatstat.model/NAMESPACE
/usr/lib64/R/library/spatstat.model/NEWS
/usr/lib64/R/library/spatstat.model/R/spatstat.model
/usr/lib64/R/library/spatstat.model/R/spatstat.model.rdb
/usr/lib64/R/library/spatstat.model/R/spatstat.model.rdx
/usr/lib64/R/library/spatstat.model/R/sysdata.rdb
/usr/lib64/R/library/spatstat.model/R/sysdata.rdx
/usr/lib64/R/library/spatstat.model/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.model/help/AnIndex
/usr/lib64/R/library/spatstat.model/help/aliases.rds
/usr/lib64/R/library/spatstat.model/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.model/help/paths.rds
/usr/lib64/R/library/spatstat.model/help/spatstat.model.rdb
/usr/lib64/R/library/spatstat.model/help/spatstat.model.rdx
/usr/lib64/R/library/spatstat.model/html/00Index.html
/usr/lib64/R/library/spatstat.model/html/R.css
/usr/lib64/R/library/spatstat.model/tests/testsAtoC.R
/usr/lib64/R/library/spatstat.model/tests/testsD.R
/usr/lib64/R/library/spatstat.model/tests/testsEtoF.R
/usr/lib64/R/library/spatstat.model/tests/testsGtoJ.R
/usr/lib64/R/library/spatstat.model/tests/testsK.R
/usr/lib64/R/library/spatstat.model/tests/testsL.R
/usr/lib64/R/library/spatstat.model/tests/testsM.R
/usr/lib64/R/library/spatstat.model/tests/testsNtoO.R
/usr/lib64/R/library/spatstat.model/tests/testsP1.R
/usr/lib64/R/library/spatstat.model/tests/testsP2.R
/usr/lib64/R/library/spatstat.model/tests/testsQ.R
/usr/lib64/R/library/spatstat.model/tests/testsR1.R
/usr/lib64/R/library/spatstat.model/tests/testsR2.R
/usr/lib64/R/library/spatstat.model/tests/testsS.R
/usr/lib64/R/library/spatstat.model/tests/testsT.R
/usr/lib64/R/library/spatstat.model/tests/testsUtoZ.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.model/libs/spatstat.model.so
/usr/lib64/R/library/spatstat.model/libs/spatstat.model.so.avx2
/usr/lib64/R/library/spatstat.model/libs/spatstat.model.so.avx512
