Name:		texlive-apa6e
Version:	0.3
Release:	1
Summary:	Format manuscripts to APA 6th edition guidelines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apa6e
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is a minimalist class file for formatting manuscripts in
the style described in the American Psychological Association
(APA) 6th edition guidelines. Some day, the established (and
more capable) apa class will perhaps gain support for the 6th
edition of the APA guidelines, in which case users should
probably use it instead. But in the mean time, this class may
be useful.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/apa6e/apa6e.cls
%doc %{_texmfdistdir}/doc/latex/apa6e/README
%doc %{_texmfdistdir}/doc/latex/apa6e/apa6e.pdf
#- source
%doc %{_texmfdistdir}/source/latex/apa6e/apa6e.dtx
%doc %{_texmfdistdir}/source/latex/apa6e/apa6e.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
