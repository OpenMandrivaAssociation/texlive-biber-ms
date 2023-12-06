Name:		texlive-biber-ms
Version:	66478
Release:	1
Summary:	A BibTeX replacement for users of BibLaTeX (multiscript version)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biber-ms
License:	artistic2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber-ms.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber-ms.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber-ms.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the multiscript version of biber (biber-ms) and must be
used with the multiscript version of biblatex-ms

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/source/bibtex/biber-ms
%doc %{_texmfdistdir}/doc/bibtex/biber-ms

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
