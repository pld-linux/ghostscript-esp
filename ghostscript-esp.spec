#
# Conditional build:
%bcond_without	cups		# without CUPS support
%bcond_with	svga		# with svgalib display support (vgalib and lvga256 devices)
%bcond_without	omni		# without omni support
#
%define gnu_ver 8.15
Summary:	PostScript & PDF interpreter and renderer
Summary(de):	PostScript & PDF Interpreter und Renderer
Summary(fr):	Interpr�teur et visualisateur PostScript & PDF
Summary(ja):	PostScript ���󥿡��ץ꥿�������顼
Summary(pl):	Bezp�atny interpreter i renderer PostScriptu i PDF
Summary(tr):	PostScript & PDF yorumlay�c� ve g�sterici
Name:		ghostscript-esp
Version:	%{gnu_ver}.3
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://ftp.easysw.com/pub/ghostscript/%{version}/espgs-%{version}-source.tar.bz2
# Source0-md5:	4ec87a3da20c1b433ffbe0ffe3675fcd
# we need to link with libjpeg recompiled with our parameters
Source2:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
# Source2-md5:	dbd5f3b47ed13132f04c685d608a7547
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/ghostscript-non-english-man-pages.tar.bz2
# Source5-md5:	9b5953aa0cc155f4364f20036b848585
Patch1:		%{name}-setuid.patch
Patch2:		%{name}-time_h.patch
Patch3:		%{name}-gdevcd8-fixes.patch
URL:		http://www.cups.org/ghostscript.php
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	docbook-style-dsssl
BuildRequires:	glib2-devel
BuildRequires:	xorg-lib-libX11-devel
# for gsx
#BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
# Required by 'gdevvglb' device.
%{?with_svga:BuildRequires:	svgalib-devel}
# for documentation regeneration
BuildRequires:	tetex
BuildRequires:	tetex-dvips
Provides:	ghostscript = %{version}-%{release}
Obsoletes:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghostscript is a PostScript interpreter. It can render both PostScript
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
Ghostcript jest interpreterem PostScriptu, j�zyka u�ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzy� dokument w formacie
PostScript i PDF na szereg postaci wyj�ciowych: drukarki (w��czaj�c
kolorowe), okno X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalar�, X penceresinde
g�sterebilir ve bir�ok yaz�c�n�n (renkli yaz�c�lar dahil) basabilece�i
bi�ime getirebilir.

%package gtk
Summary:	Ghostscript with GTK+ console
Summary(pl):	Ghostscript z konsol� GTK+
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Provides:	ghostscript-gtk = %{version}-%{release}
Obsoletes:	ghostscript-gtk

%description gtk
Ghostscript with GTK+ console.

%description gtk -l pl
Ghostscript z konsol� GTK+.

%package devel
Summary:	libgs header files
Summary(pl):	Pliki nag��wkowe libgs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	ghostscript-devel = %{version}-%{release}
Obsoletes:	ghostscript-devel

%description devel
Header files for libgs - ghostscript shared library.

%description devel -l pl
Pliki nag��wkowe libgs - wsp�dzielonej biblioteki ghostscript.

%package ijs-devel
Summary:	IJS development files
Summary(pl):	Pliki dla programist�w IJS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	ghostscript-ijs-devel = %{version}-%{release}
Obsoletes:	ghostscript-ijs-devel

%description ijs-devel
IJS development files.

%description ijs-devel -l pl
Pliki do tworzenia program�w z u�yciem biblioteki IJS.

%package ijs-static
Summary:	Static libijs library
Summary(pl):	Statyczna biblioteka IJS
Group:		Development/Libraries
Requires:	%{name}-ijs-devel = %{version}-%{release}
Provides:	ghostscript-ijs-static = %{version}-%{release}
Obsoletes:	ghostscript-ijs-static

%description ijs-static
Static libijs library.

%description ijs-static -l pl
Statyczna wersja biblioteki IJS.

%package -n cups-filter-pstoraster
Summary:	CUPS filter for support non-postscript printers
Summary(pl):	Filtr CUPS-a obs�uguj�cy drukarki niepostscriptowe
Group:		Applications/Printing
Requires:	cups >= 1:1.1.16
Requires:	ghostscript >= %{version}-%{release}
Conflicts:	ghostscript-afpl

%description -n cups-filter-pstoraster
CUPS filter for support non-postscript printers.

%description -n cups-filter-pstoraster -l pl
Filtr CUPS-a obs�uguj�cy drukarki niepostscriptowe.

%package -n cups-driver-pxl
Summary:	CUPS PXL driver
Summary(pl):	Sterownik CUPS dla drukarek PXL
Group:		Applications/Printing
Requires:	cups >= 1:1.1.16

%description -n cups-driver-pxl
CUPS PXL driver.

%description -n cups-driver-pxl -l pl
Sterownik CUPS dla drukarek PXL.

%prep
%setup -q -n espgs-%{version} -a2
%patch1 -p1
%patch2 -p1
%patch3 -p1
ln -sf jp* jpeg

%build
rm -rf autom4te.cache
cp -f %{_datadir}/automake/config.sub .
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -DA4"
export CFLAGS
%configure \
	--with-drivers=ALL%{?with_svga:,vgalib,lvga256} \
	--with-fontpath="%{_datadir}/fonts:%{_datadir}/fonts/Type1" \
	--with-ijs \
	--with-jbig2dec \
	--without-gimp-print \
	%{!?with_cups:--disable-cups} \
	--with%{!?with_omni:out}-omni \
	--with-x
cd ijs
rm -f install-sh missing && install %{_datadir}/automake/{install-sh,missing} .
%configure \
	--enable-shared \
	--enable-static
cd ..

%{__make} \
	docdir=%{_docdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/ghostscript/lib,%{_libdir},%{_includedir}}

%{__make} install \
	install_prefix=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	docdir=%{_docdir}/%{name}-%{version} \
	gsdir=%{_datadir}/ghostscript

cd ijs
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	pkgconfigdatadir=$RPM_BUILD_ROOT%{_pkgconfigdir}
cd ..

install lib/{gs_frsd,pdfopt,pdfwrite}.ps $RPM_BUILD_ROOT%{_datadir}/ghostscript/lib

#install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/ghostscript/lib
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

#mv -f $RPM_BUILD_ROOT%{_bindir}/{gsc,gs}
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/gsc
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

#install -d $RPM_BUILD_ROOT%{_includedir}/ps
#install src/{iapi,errors}.h $RPM_BUILD_ROOT%{_includedir}/ps

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/[bdeflpsux]*
%attr(755,root,root) %{_bindir}/gs
%attr(755,root,root) %{_bindir}/wftopfa
%attr(755,root,root) %{_bindir}/gs[!x]*
%attr(755,root,root) %{_bindir}/ijs_client_example
%attr(755,root,root) %{_libdir}/libijs-*.so
%dir %{_datadir}/ghostscript
%dir %{_datadir}/ghostscript/lib
%{_datadir}/ghostscript/lib/*.*
%dir %{_datadir}/ghostscript/%{gnu_ver}
%{_datadir}/ghostscript/%{gnu_ver}/Resource
%dir %{_datadir}/ghostscript/%{gnu_ver}/lib
%{_datadir}/ghostscript/%{gnu_ver}/lib/*.*
%{_datadir}/ghostscript/%{gnu_ver}/lib/[cfx]*map
%{_datadir}/ghostscript/%{gnu_ver}/lib/FAP*map
%{_datadir}/ghostscript/%{gnu_ver}/lib/*config
%config %verify(not md5 mtime size) %{_datadir}/ghostscript/%{gnu_ver}/lib/Fontmap
%{_datadir}/ghostscript/%{gnu_ver}/examples
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(de) %{_mandir}/de/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(pl) %{_mandir}/pl/man*/*

#%files gtk
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/gsx

#%files devel
#%defattr(644,root,root,755)
#%%{_includedir}/ps
#%%{_libdir}/libgs.so

%files ijs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijs-config
%{_includedir}/ijs
%attr(755,root,root) %{_libdir}/libijs.so
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc

%files ijs-static
%defattr(644,root,root,755)
%{_libdir}/libijs.a

%if %{with cups}
%files -n cups-filter-pstoraster
%defattr(644,root,root,755)
%(cups-config --serverroot)/*
%attr(755,root,root) %(cups-config --serverbin)/filter/*

%files -n cups-driver-pxl
%defattr(644,root,root,755)
%attr(755,root,root) %(cups-config --datadir)/model/*.ppd
%endif
