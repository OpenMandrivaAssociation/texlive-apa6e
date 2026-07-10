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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a minimalist class file for formatting manuscripts in the style
described in the American Psychological Association (APA) 6th edition
guidelines. The apa6 class provides better coverage of the requirements.

