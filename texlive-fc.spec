# revision 32796
# category Package
# catalog-ctan /fonts/jknappen/fc
# catalog-date 2012-05-29 13:27:24 +0200
# catalog-license gpl2
# catalog-version 1.4
Name:		texlive-fc
Version:	1.4
Release:	7
Summary:	Fonts for African languages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/jknappen/fc
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts are provided as Metafont source, in the familiar
arrangement of lots of (autogenerated) preamble files and a
modest set of glyph specifications. (A similar arrangement
appears in the ec and lh font bundles.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcbx.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcbxi.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcbxsl.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcbxu.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fccsc.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fci.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcitt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcr.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcsibx.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcsitt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcsl.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcss.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcssbx.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcssi.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcsstt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fctt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/b-fcu.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/c-fcsstt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcaccent.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbx9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxi9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxsl9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcbxu9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccoding.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccsc9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fccscspu.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fci9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcilig.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitalic.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitligt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitlpct.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcitt9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcmacros.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcpunct.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcr9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcrlig.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcroligt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcroman.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcrompct.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcscligt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsfligt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsibx9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsitt9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsl9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcss9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssbx9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcssi9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcsstt9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fctt9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcttligt.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu10.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu11.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu12.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu14.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu17.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu20.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu25.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu5.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu6.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu7.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu8.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/fcu9.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/itala.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italbcd.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/itale.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italfgh.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italij.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italklm.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italn.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italo.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italpqr.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italst.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italuvw.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/italxyz.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowera.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowerbcd.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowere.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowerfgh.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowerij.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowerklm.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowern.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowero.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowerpqr.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowerst.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/loweruvw.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/lowerxyz.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/uppera.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/upperbcd.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/uppere.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/upperfgh.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/upperij.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/upperklm.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/uppern.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/uppero.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/upperpqr.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/upperst.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/upperuvw.mf
%{_texmfdistdir}/fonts/source/jknappen/fc/upperxyz.mf
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbx9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxi9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxsl9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcbxu9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fccsc9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fci9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcitt9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcr9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsibx9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsitt9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsl9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcss9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssbx9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcssi9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcsstt9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fctt9.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu10.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu11.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu12.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu14.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu17.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu20.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu25.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu5.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu6.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu7.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu8.tfm
%{_texmfdistdir}/fonts/tfm/jknappen/fc/fcu9.tfm
%{_texmfdistdir}/tex/latex/fc/fclfont.sty
%{_texmfdistdir}/tex/latex/fc/fcuse.sty
%{_texmfdistdir}/tex/latex/fc/t4cmr.fd
%{_texmfdistdir}/tex/latex/fc/t4cmss.fd
%{_texmfdistdir}/tex/latex/fc/t4cmtt.fd
%{_texmfdistdir}/tex/latex/fc/t4enc.def
%{_texmfdistdir}/tex/latex/fc/t4fcr.fd
%{_texmfdistdir}/tex/latex/fc/t4phonet.sty
%doc %{_texmfdistdir}/doc/fonts/fc/fc.bug
%doc %{_texmfdistdir}/doc/fonts/fc/fc.rme
%doc %{_texmfdistdir}/doc/fonts/fc/fclfont.sty_old
%doc %{_texmfdistdir}/doc/fonts/fc/fctugbot.tex
%doc %{_texmfdistdir}/doc/fonts/fc/fontdef.fc_old
%doc %{_texmfdistdir}/doc/fonts/fc/licence.gnu

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
