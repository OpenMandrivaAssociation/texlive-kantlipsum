# revision 24935
# category Package
# catalog-ctan /macros/latex/contrib/kantlipsum
# catalog-date 2011-12-24 01:22:03 +0100
# catalog-license lppl1.3
# catalog-version 0.5
Name:		texlive-kantlipsum
Version:	0.5
Release:	1
Summary:	Generate sentences in Kant's style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kantlipsum
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kantlipsum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kantlipsum.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kantlipsum.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package spits out sentences in Kantian style; the text is
provided by the Kant generator for Python by Mark Pilgrim,
described in the book "Dive into Python". The package is
modelled on lipsum, and may be used for similar purposes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kantlipsum/kantlipsum.sty
%doc %{_texmfdistdir}/doc/latex/kantlipsum/README
%doc %{_texmfdistdir}/doc/latex/kantlipsum/kantlipsum.pdf
#- source
%doc %{_texmfdistdir}/source/latex/kantlipsum/kantlipsum.dtx
%doc %{_texmfdistdir}/source/latex/kantlipsum/kantlipsum.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
