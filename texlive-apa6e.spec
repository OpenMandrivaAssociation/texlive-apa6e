Name:		texlive-apa6e
Version:	23350
Release:	1
Summary:	Format manuscripts to APA 6th edition guidelines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apa6e
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.r23350.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.doc.r23350.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6e.source.r23350.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a minimalist class file for formatting manuscripts in
the style described in the American Psychological Association
(APA) 6th edition guidelines. Some day, the established (and
more capable) apa class will perhaps gain support for the 6th
edition of the APA guidelines, in which case users should
probably use it instead. But in the mean time, this class may
be useful.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
