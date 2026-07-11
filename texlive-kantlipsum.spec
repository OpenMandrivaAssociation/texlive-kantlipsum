%global tl_name kantlipsum
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8c
Release:	%{tl_revision}.1
Summary:	Generate sentences in Kants style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kantlipsum
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kantlipsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kantlipsum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kantlipsum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package spits out sentences in Kantian style; the text is provided
by the Kant generator for Python by Mark Pilgrim, described in the book
"Dive into Python". The package is modelled on lipsum, and may be used
for similar purposes.

