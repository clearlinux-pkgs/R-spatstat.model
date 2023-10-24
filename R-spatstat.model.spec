#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-spatstat.model
Version  : 3.2.8
Release  : 12
URL      : https://cran.r-project.org/src/contrib/spatstat.model_3.2-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.model_3.2-8.tar.gz
Summary  : Parametric Statistical Modelling and Inference for the
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
mainly spatial point patterns, in the 'spatstat' family of packages.
	     (Excludes analysis of spatial data on a linear network,
	     which is covered by the separate package 'spatstat.linnet'.)
	     Supports parametric modelling, formal statistical inference, and model validation.
	     Parametric models include Poisson point processes, Cox point processes, Neyman-Scott cluster processes, Gibbs point processes and determinantal point processes. Models can be fitted to data using maximum likelihood, maximum pseudolikelihood, maximum composite likelihood and the method of minimum contrast. Fitted models can be simulated and predicted. Formal inference includes hypothesis tests (quadrat counting tests, Cressie-Read tests, Clark-Evans test, Berman test, Diggle-Cressie-Loosmore-Ford test, scan test, studentised permutation test, segregation test, ANOVA tests of fitted models, adjusted composite likelihood ratio test, envelope tests, Dao-Genton test, balanced independent two-stage test), confidence intervals for parameters, and prediction intervals for point counts. Model validation techniques include leverage, influence, partial residuals, added variable plots, diagnostic plots, pseudoscore residual plots, model compensators and Q-Q plots.

%package lib
Summary: lib components for the R-spatstat.model package.
Group: Libraries

%description lib
lib components for the R-spatstat.model package.


%prep
%setup -q -n spatstat.model
pushd ..
cp -a spatstat.model buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698169233

%install
export SOURCE_DATE_EPOCH=1698169233
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
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

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
