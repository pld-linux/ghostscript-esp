Summary:	PostScript interpreter and renderer
Summary(de):	PostScript-Interpreter und Renderer
Summary(fr):	Interpr�teur et visualisateur PostScript
Summary(pl):	Bezp�atny interpreter PostScriptu
Summary(tr):	PostScript yorumlay�c� ve g�sterici
Name:		ghostscript
Version:	5.50
Release:	1
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Copyright:	GPL
URL:		http://www.cs.wisc.edu/~ghost/
Source0:	ftp://ftp.cs.wisc.edu/ghost/gnu/gs510/%{name}-%{version}.tar.gz
Source1:	jpegsrc.v6b.tar.gz
#Icon:		ghost.gif
Patch0:		%{name}-config.patch
Vendor:		Aladdin Enterprises
BuildRoot:	/tmp/%{name}-%{version}-root
BuildRequires:	zlib-devel, libpng-devel, patch

%description
Ghostscript is a PostScript interpretor. It can render both PostScript
and PDF compliant files to devices which include an X window, many printer
formats (including support for color printers), and popular graphics
file formats.

%description -l de
Ghostscipt ist ein PostScript-Interpretierer. Er kann sowohl PostScript als
auch PDF-konforme Dateien an Ger�te ausgeben, zu denen ein X-Fenster, 
viele Druckerformate (einschlie�lich Support f�r Farbdrucker) und g�ngige
Grafikdateiformate z�hlen.

%description -l fr
Ghostscript est un interpr�teur PostScript. Il peut rendre des fichiers
PostScript ou PDF sur des p�riph�riques dont une fen�tre X,de nombreux
types d'imprimantes (dont un support pour imprimantes couleur), et des
formats de fichiers graphiques populaires.

%description -l pl
Ghostcript jest interpreterem PostScriptu, j�zyku u�ywanego do opisu formatu
dokumentu. Ghostscript potrafi przetworzy� dokument w formacie PostScript
i PDF %{name} szereg postaci wyj�ciowych: drukarki (w��czaj�c kolorowe), okno
X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalar�, X penceresinde g�sterebilir
ve bir�ok yaz�c�n�n (renkli yaz�c�lar dahil) basabilece�i bi�ime getirebilir.

%prep
%setup -q -n gs%{version}
ln -s unix-gcc.mak Makefile
%patch0 -p1 
tar zxf %{SOURCE1}
mv jpeg-6b jpeg

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DA4 -w" prefix=/usr

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/doc
install -d $RPM_BUILD_ROOT/%{_mandir}
install -d $RPM_BUILD_ROOT/%{_bindir}

make install prefix=$RPM_BUILD_ROOT/usr

echo .so gs.1 > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1

ln -sf gs 	$RPM_BUILD_ROOT%{_bindir}/ghostscript

strip 		$RPM_BUILD_ROOT%{_bindir}/gs

gzip -9nf 	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(644,root,root) %{_datadir}/doc/%{name}-%{version}

%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{version}/*.ps
%config %verify(not size md5 mtime) %{_datadir}/%{name}/%{version}/Fontmap

%dir %{_datadir}/%{name}/%{version}/examples
%{_datadir}/%{name}/%{version}/examples/*.ps

%{_mandir}/man1/*
