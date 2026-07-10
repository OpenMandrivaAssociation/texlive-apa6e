%global tl_name apa6e
%global tl_revision 23350

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Format manuscripts to APA 6th edition guidelines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apa6e
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a minimalist class file for formatting manuscripts in the style
described in the American Psychological Association (APA) 6th edition
guidelines. The apa6 class provides better coverage of the requirements.

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
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/apa6e
%dir %{_datadir}/texmf-dist/source/latex/apa6e
%dir %{_datadir}/texmf-dist/tex/latex/apa6e
%doc %{_datadir}/texmf-dist/doc/latex/apa6e/README
%doc %{_datadir}/texmf-dist/doc/latex/apa6e/apa6e.pdf
%doc %{_datadir}/texmf-dist/source/latex/apa6e/apa6e.dtx
%doc %{_datadir}/texmf-dist/source/latex/apa6e/apa6e.ins
%{_datadir}/texmf-dist/tex/latex/apa6e/apa6e.cls
