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
Requires(pre):	texlive-tlpkg
Requires:	texlive(biber-ms.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the multiscript version of biber (biber-ms) and must be used
with the multiscript version of biblatex-ms

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/source/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/biber-ms
%dir %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber-ms
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/biber-ms/biber-ms.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber-ms/Changes
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber-ms/README.biber-ms-linux
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber-ms/README.biber-ms-macos
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber-ms/README.biber-ms-windows
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber-ms/README.md
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber-ms/biblatex-biber-ms.tar.gz
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber-ms/utf8-macro-map.html
