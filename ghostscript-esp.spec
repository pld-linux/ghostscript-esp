#
# Conditional build:
# _with_svgalib
#
%define		gp_version	4.1.9
Summary:	PostScript & PDF interpreter and renderer
Summary(de):	PostScript & PDF Interpreter und Renderer
Summary(fr):	Interpr�teur et visualisateur PostScript & PDF
Summary(ja):	PostScript ���󥿡��ץ꥿�������顼
Summary(pl):	Bezp�atny interpreter PostScriptu & PDF
Summary(tr):	PostScript & PDF yorumlay�c� ve g�sterici
Name:		ghostscript
Version:	7.03
Release:	2
Vendor:		Aladdin Enterprises <bug-gs@aladdin.com>
License:	Aladdin Free Public License
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	ftp://download.sourceforge.net/pub/sourceforge/ghostscript/%{name}-%{version}.tar.bz2
Source1:	http://www.ozemail.com.au/~geoffk/pdfencrypt/pdf_sec.ps
# we need to link with libjpeg recompiled with our parameters
Source2:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
Source3:	%{name}-find_devs.sh
Source4:	ftp://download.sourceforge.net/pub/sourceforge/gimp-print/gimp-print-%{gp_version}.tar.gz
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-config.patch
Patch1:		%{name}-hpdj_driver.patch
Patch2:		%{name}-cdj880.patch
#Patch3:		%{name}-nosafer.patch
Patch4:		%{name}-missquotes.patch
Patch5:		%{name}-setuid.patch
Patch6:		%{name}-time_h.patch
URL:		http://www.ghostscript.com/
# Required by ghostscript-find_devs.sh
BuildRequires:	awk
BuildRequires:	XFree86-devel
# Required by 'gdevvglb' device.
%ifnarch sparc sparc64 alpha
%{?_with_svgalib:BuildRequires:	svgalib-devel}
%endif
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghostscript is a PostScript interpretor. It can render both PostScript
and PDF compliant files to devices which include an X window, many
printer formats (including support for color printers), and popular
graphics file formats.

%description -l de
Ghostscipt ist ein PostScript-Interpretierer. Er kann sowohl
PostScript als auch PDF-konforme Dateien an Ger�te ausgeben, zu denen
ein X-Fenster, viele Druckerformate (einschlie�lich Support f�r
Farbdrucker) und g�ngige Grafikdateiformate z�hlen.

%description -l fr
Ghostscript est un interpr�teur PostScript. Il peut rendre des
fichiers PostScript ou PDF sur des p�riph�riques dont une fen�tre X,de
nombreux types d'imprimantes (dont un support pour imprimantes
couleur), et des formats de fichiers graphiques populaires.

%description -l ja
Ghostscript �� PostScript ���󥿡��ץ꥿�Ǥ����ݥ��ȥ�����ץȤ� PDF
�������󥰤���X window ��¾�Υץ�󥿥ե����ޥåȤǽ���
���ޤ������Υѥå����������ܸ��б����Ƥ��ޤ���

%description -l pl
Ghostcript jest interpreterem PostScriptu, j�zyku u�ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzy� dokument w formacie
PostScript i PDF na szereg postaci wyj�ciowych: drukarki (w��czaj�c
kolorowe), okno X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalar�, X penceresinde
g�sterebilir ve bir�ok yaz�c�n�n (renkli yaz�c�lar dahil) basabilece�i
bi�ime getirebilir.

%prep
%setup -q -n gs%{version}
ln -s src/unix-gcc.mak Makefile
%patch0 -p1
%patch1 -p1
%patch2 -p1
##%patch3 -p1 
%patch4 -p1
%patch5 -p1
%patch6 -p1
%setup -q -T -D -a 2 -a 4 -n gs%{version}
ln -s jp* jpeg
install %{SOURCE3} .

%build
# prepare gimp-print driver
cd gimp-print-%{gp_version}
#libtoolize --copy --force
#aclocal
#autoconf
%configure2_13 \
	--with-ghost \
	--without-gimp \
	--disable-escputil \
	--disable-libgimpprint
%{__make}
cp src/ghost/*.[ch] ../src/
sed -e 's/stp.dev:/stp.dev :/'< src/ghost/contrib.mak.addon >> ../src/contrib.mak
cd ..

# NOTE: %%{SOURCE3} takes _blacklist_ as arguments, not the list of
# drivers to make!

%{__make} \
	XCFLAGS="%{rpmcflags} -DA4=1 -w" \
	XLDFLAGS="%{rpmldflags}" \
	prefix=%{_prefix} \
	datadir=%{_datadir}/%{name} \
	mandir=%{_mandir} \
	docdir=%{_datadir}/doc/%{name}-%{version} \
	DEVICE_DEVS16="`/bin/sh %{SOURCE3} devs.mak \
%ifarch sparc sparc64 alpha
		vgalib lvga256\
%else
		%{!?_with_svgalib:vgalib lvga256} \
%endif
		`" \
	DEVICE_DEVS17="`/bin/sh %{SOURCE3} contrib.mak \
%ifarch sparc sparc64 alpha
		vgalib lvga256\
%else
		%{!?_with_svgalib:vgalib lvga256} \
%endif
		`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

install lib/{gs_frsd,pdfopt,pdfwrite}.ps $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
	$RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},gsbj,gsdj,gsdj500,gslj,eps2eps}.1

echo ".so gs.1"     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/man1/eps2eps.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsbj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj500.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gslj.1

bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

install -d $RPM_BUILD_ROOT%{_bindir}
# install -d $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.htm
# %doc %{_datadir}/doc/%{name}-%{version}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
# "*.*" will not match "Fontmap". It is OK.
%{_datadir}/%{name}/lib/*.*
%dir %{_datadir}/%{name}/examples
%{_datadir}/%{name}/examples/*
%config %verify(not size md5 mtime) %{_datadir}/%{name}/lib/Fontmap
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(pl) %{_mandir}/pl/man*/*
