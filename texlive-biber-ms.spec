%global tl_name biber-ms
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.0~1
Release:	%{tl_revision}.1
Summary:	A BibTeX replacement for users of BibLaTeX (multiscript version)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/biber-ms/base
License:	artistic2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biber-ms.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biber-ms.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biber-ms.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(biber-ms.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the multiscript version of biber (biber-ms) and must be used
with the multiscript version of biblatex-ms

