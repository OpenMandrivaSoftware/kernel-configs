# MIB header

%if %{mdvver} <= 201100
%define distsuffix mib
%define disttag %{distsuffix}
Vendor: MIB - Mandriva International Backports
%endif

Packager: Nicolo' Costanza <abitrules@yahoo.it>
# end MIB header

%define kernelversion	4
%define patchlevel	1
%define sublevel	1

# Package release
%define mibrel		1.1
%define mibase		1%{disttag}

# kernel Makefile extraversion is substituted by 
# kpatch/kgit/kstable wich are either 0 (empty), rc (kpatch), git (kgit) 
# or stable release (kstable)
%define kpatch		0
# kernel.org -gitX patch (only the number after "git")
%define kgit		0

# kernel base name (also name of srpm)
%define kname 		kernel

# Patch tarball tag
%define ktag		nicco

%define rpmtag		%{disttag}
%if %kpatch
%if %kgit
%define rpmrel		0.%{kpatch}.%{kgit}.%{mibrel}
%else
%define rpmrel		0.%{kpatch}.%{mibrel}
%endif
%else
%define rpmrel		%{mibrel}
%endif

# fakerel and fakever never change, they are used to fool
# rpm/urpmi/smart and ensure the kernels are installed,
# not upgraded so old kernel is not overwritten or removed
%define fakever		1
%define fakerel 	1

# version defines
%define kversion  	%{kernelversion}.%{patchlevel}.%{sublevel}
%define kverrel   	%{kversion}-%{rpmrel}
%define mibfull   	%{kversion}-%{mibase}

# When we are using a pre/rc patch, the tarball is a sublevel -1
%if %kpatch
%if %sublevel
%define tar_ver   	%{kernelversion}.%{patchlevel}
%else
%define tar_ver		%{kernelversion}.%(expr %{patchlevel} - 1)
%endif
%define patch_ver 	%{kversion}-%{kpatch}-%{ktag}%{mibrel}
%else
%define tar_ver   	%{kernelversion}.%{patchlevel}
%define patch_ver 	%{kversion}-%{ktag}%{mibrel}
%endif

# Used for not making too long names for rpms or search paths
%if %kpatch
%if %kgit
%define buildrpmrel     0.%{kpatch}.%{kgit}.%{mibrel}%{rpmtag}
%else
%define buildrpmrel     0.%{kpatch}.%{mibrel}%{rpmtag}
%endif
%else
%define buildrpmrel     %{mibrel}%{rpmtag}
%endif
%define buildrel     	%{kversion}-%{buildrpmrel}

Source5:	kernel.rpmlintrc

# Build defines
%define build_devel 		1
%define build_desktop		1

#
# SRC RPM description
#
Summary: 	Linux kernel built for Mandriva and ROSA
Name:		%{kname}
Version: 	%{kversion}
Release: 	%{rpmrel}
License: 	GPLv2
Group: 	 	System/Kernel and hardware
ExclusiveArch: %{ix86} ppc powerpc x86_64 amd64 sparc sparc64
ExclusiveOS: 	Linux
URL:            http://wiki.mandriva.com/en/Manbo_Core2_kernel
BuildRoot: 	%{_tmppath}/%{kname}-%{kversion}-%{_arch}-build
Autoreqprov: 	no

BuildRequires: 	gcc bc

%if %{mdvver} == 201210
BuildRequires:	kmod-devel
%else
BuildRequires:	module-init-tools
%endif

%description
The kernel package contains the Linux kernel (vmlinuz), the core of your
Mandriva and ROSA Linux operating systems. The kernel handles the basic
functions of the operating system: memory allocation, process allocation,
device input and output, etc.

# mkflavour() name flavour processor
# name: the flavour name in the package name
# flavour: first parameter of CreateKernel()
%define mkflavour(R:)					\
%package -n %{kname}-%{1}-latest			\
Version:	%{kversion}				\
Release:	%{rpmrel}				\
Summary:	Virtual rpm for latest %{kname}-%{1}	\
Group:		System/Kernel and hardware		\
Requires:	kernel-nrj-desktop-%{mibfull}		\
Provides:	%{kname}-latest				\
%ifarch %{ix86}						\
Conflicts:	arch(x86_64)				\
%endif							\
							\
%description -n %{kname}-%{1}-latest			\
This package is a virtual rpm that aims to make sure you always have the \
latest %{kname}-%{1} installed...			\
							\
%common_description_info				\
							\
%if %build_devel					\
%package -n %{kname}-%{1}-devel-latest			\
Version:	%{kversion}				\
Release:	%{rpmrel}				\
Summary:	Virtual rpm for latest %{kname}-%{1}-devel \
Group:		Development/Kernel			\
Requires:	%{kname}-nrj-desktop-devel-%{mibfull}	\
Provides:	%{kname}-devel-latest			\
%ifarch %{ix86}						\
Conflicts:	arch(x86_64)				\
%endif							\
							\
%description -n %{kname}-%{1}-devel-latest		\
This package is a virtual rpm that aims to make sure you always have the \
latest %{kname}-%{1}-devel installed...			\
							\
%common_description_info				\
%endif							\
							\
%files -n %{kname}-%{1}-latest				\
%defattr(-,root,root)					\
							\
%if %build_devel					\
%files -n %{kname}-%{1}-devel-latest			\
%defattr(-,root,root)					\
%endif							

%if %build_desktop
%mkflavour desktop desktop
%endif


%changelog

* Fri Jul 03 2015 Nicolo' Costanza <abitrules@yahoo.it> 4.1.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 4.1.1 - mainline
- add ck/bfs-0462 cpu scheduler for kernel 4.1 
- add TOI for 4.1
- add UKSM for 4.1
+ now the most important nrjQL patches are really working inside ;-)
- thanks to Alfred Chen and Giuseppe Ghibò for the latest QL patches
- ---------------------------------------------------------------------
- Kernel 4.1 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-ql) will be used for development and experimental flavours,
- instead (-one) is born by the -1 & -ql merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Mon Jun 29 2015 Nicolo' Costanza <abitrules@yahoo.it> 4.1.0-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 4.1.0 - mainline
+ it's first version of "nrj/nrjQL" stable 4.1.x, in early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- for your daily PC working, because is still to fix all over!!!
- create_configs scripts have been prepared for the 4.1 series
- defconfigs have been prepared for the 4.1 series
- patches have been added/update for the 4.1 series
- kernel specs have been updated to the 4.1 series
- custom openmandriva/rosa features have been backported from previous
- ---------------------------------------------------------------------
- Kernel 4.1 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-ql) will be used for development and experimental flavours,
- instead (-one) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Thu Jun 25 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.19.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.19.8 (EOL) - stable 
- sync / add new patches
- update BFQ to v7R8
- update TOI to 3.19.8
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.19 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Mon May 11 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.19.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.19.7 - stable
- fix the proper path folder for all x86_64 _perf files
- nrjQL TOI is patched and enabled for x86_64 and arm only, not for i586
- drop few patch
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.19 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Wed May 06 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.19.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.19.6 - stable
- add TOI for kernels 3.19
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.19 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sun Apr 26 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.19.5-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.19.5 - stable
- drop few patches
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.19 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sun Apr 26 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.19.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.19.1 - stable
+ it's first version of "nrj/nrjQL" stable 3.19.x, in early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- for your daily PC working, because is still to fix all over!!!
- all the create_configs scripts have been prepared for the 3.19 series
- all the defconfigs have been prepared for the 3.19 series
- all the patches have been added/update for the 3.19 series
- all the kernel specs have been updated to the 3.19 series
- all custom openmandriva/rosa features have been backported from previous
- ---------------------------------------------------------------------
- Kernel 3.19 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sat Apr 25 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.12-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.12 - this is the current LTS kernel version ;-) 
- change a config key from CONFIG_SATA_SIL=m to CONFIG_SATA_SIL=y
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Thu Apr 09 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.11-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.11 - this is the current LTS kernel version ;-) 
- readd TOI (we need to test a lot with different hardware and configs)
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Mar 27 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.10 - this is the current LTS kernel version ;-) 
- add patch: fifo-nv04-remove-the-loop-from-the-interrupt-handler
- drop a patch that now is already in mainstream:
  0001-drm-radeon-dp-Set-EDP_CONFIGURATION_SET-for-bridge-c.patch
- fix few kernel keys hoping that now lxc-checkconfig may be happy
- fix BR: xmlto is now required only for docs build with a condition,
  to avoid a ton of requested rpms installation when docs is disable
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Mar 20 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.9 - this is the first 3.18 LTS version ;-)
- disable Multiblock Queue I/O, revert to old disk I/O schedulers,
­- for that I've changed to > # CONFIG_SCSI_MQ_DEFAULT is not set
- add two pending patches for the bfs 460 scheduler:
- /patches-QL/bfs460-locked-pluggedio.patch
- /patches-QL/bfs460-smt-should-sched-not-is.patch
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Wed Mar 04 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.8 - stable 
- drop TOI: there are still issues with hybernation/resume in some HW,
- the four patches for TOI support have been moved to /archives
- add 0001-drm-radeon-dp-Set-EDP_CONFIGURATION_SET-for-bridge-c.patch
- a try to fix : https://issues.openmandriva.org/show_bug.cgi?id=1137
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Feb 27 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.7 - stable 
- add support for the reiser4 fs with: reiser4-for-3.18.6.patch
- add TOI for 3.18 plus 3 fix patches: TOI is back!
- drop some patches patches that now are already in mainstream 
- fix a kconflicts for nvidia-long-lived when mdvver >= 201300
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Wed Feb 25 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.6 - stable 
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Mon Feb 02 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.5-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.5 - stable 
- drop some patches patches that now are already in mainstream 
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sat Jan 31 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.4-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.4 - stable 
- add a new key > Fibre Channel over Ethernet (FCoE) (I40E_FCOE) [N/y/?] (NEW)
- currently its first setup value as disabled > # CONFIG_I40E_FCOE is not set
- drop some patches patches that now are already in mainstream 
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Tue Jan 27 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.3-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.3 - stable 
- drop # block fixes patches that now are already in mainstream 
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Jan 23 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.2-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.2 - stable 
- add a patch to fix performance issue:
- x86-vdso-Use-asm-volatile-in-__getcpu.patch
- add a patch for iwlwifi:
- net-wireless-iwlwifi-mvm-fix-Rx-with-both-chains.patch
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Wed Jan 21 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.18.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.18.1 - stable
+ it's first version of "nrj/nrjQL" stable 3.18.x, in early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- for your daily PC working, because is still to fix all over!!!
- all the defconfigs have been prepared for the 3.18 series
- all the patches have been added/update for the 3.18 series
- all the kernel specs have been updated to the 3.18 series
- all custom openmandriva/rosa features have been backported from previous
- ---------------------------------------------------------------------
- Kernel 3.18 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Mon Jan 12 2015 Nicolo' Costanza <abitrules@yahoo.it> 3.17.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.17.8 - stable
- ---------------------------------------------------------------------
- Kernel 3.17 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-QL) will be used for development and experimental flavours,
- instead (-ONE) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sun Dec 28 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.17.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.17.7 - stable
- update BFQ patches from v7r6 to v7r7 to prevent an occasional memory leak
- add AUFS support (there is a new key, currently disabled):
- File-based Hierarchical Storage Management (AUFS_FHSM): set as "disabled"
- add OverlayFS code being merged in upstream 3.18
- a request from POK: CONFIG_SATA_SIL changed from =m to =y
- netlink: Re-add locking to netlink_lookup() and seq walker
  (fixes latency regression)
- input: i8042 - touchpad quirks for Fujitsu Lifebook A(H)544
- ext4: fix oops when loading block bitmap failed
- saa7146: Create a device name before it's used
- drm/i915: Do not store the error pointer for a failed userptr registration
- drm/i915: Do not leak pages when freeing userptr objects
- drm/radeon/dpm: disable ulv support on SI
- drm/radeon: dpm fixes for asrock systems
- lib/scatterlist: fix memory leak with scsi-mq
- revert 'block: all blk-mq requests are tagged'
- scsi: set REQ_QUEUE for the blk-mq case
- revert 'ACPI / EC: Add support to disallow QR_EC to be issued before
  completing previous QR_EC'
- ACPI / EC: Fix regression due to conflicting firmware behavior between
  Samsung and Acer
- rcu: Provide counterpart to rcu_dereference() for non-RCU situations
- add ahci, alsa, i2c support for Intel Sunrise Point PCH / Skylake
- ---------------------------------------------------------------------
- Kernel 3.17 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-QL) will be used for development and experimental flavours,
- instead (-ONE) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sun Dec 14 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.17.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.17.6 - stable
- ---------------------------------------------------------------------
- Kernel 3.17 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-QL) will be used for development and experimental flavours,
- instead (-ONE) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sat Dec 06 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.17.5-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.17.5 - stable
- ---------------------------------------------------------------------
- Kernel 3.17 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-QL) will be used for development and experimental flavours,
- instead (-ONE) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Nov 28 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.17.4-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.17.4 - stable
- drop unofficial ck1/bfs 456
- added official ck2/bfs 458
- ---------------------------------------------------------------------
- Kernel 3.17 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-QL) will be used for development and experimental flavours,
- instead (-ONE) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Thu Nov 20 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.17.3-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.17.3 - stable
- added UKSM 0.1.2.3 ge.2 for kernel 3.17
- added Reiser4 file system for kernel 3.17
- added ix86 & x86_64 build fixes for cooker (201500)
- ---------------------------------------------------------------------
- Kernel 3.17 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-QL) will be used for development and experimental flavours,
- instead (-ONE) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sat Nov 01 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.17.2-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.17.2 - stable
- all the create_configs scripts have been updated to v.2.4
- all netbook flavours have NAMESPACES enabled, as this speedup things
- drop few patches
- ---------------------------------------------------------------------
- Kernel 3.17 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-QL) will be used for development and experimental flavours,
- instead (-ONE) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sun Oct 26 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.17.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.17.1 - stable
+ it's first version of "nrj/nrjQL" stable 3.17.x, in early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- for your daily PC working, because is still to fix all over!!!
- all the defconfigs have been prepared for the 3.17 series
- all the patches have been added/update for the 3.17 series
- all the create_configs scripts have been updated to v.2.3
- all the kernel specs have been updated to the 3.17 series
- all custom openmandriva/rosa features have been backported from previous
- ---------------------------------------------------------------------
- Kernel 3.17 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sat Aug 30 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.15.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.15.10 (EOL) - stable (replacement release)
- update ReiserFS4:
- /patches-NRJ/0004-reiser4-for-3.15.2.patch
- update BFS scheduler to 455, plus fixes, plus HT/SMT Nice 6 and configs:
- /patches-QL/0001_3.15-sched-bfs-455-2.patch
- /patches-QL/0002_ck-3.16-revert-KVM-workaround-due-to-proper-cond_res.patch
- /patches-QL/0003_bfs449-smtnice-6.patch
- ---------------------------------------------------------------------
- Kernel 3.15 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sat Aug 16 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.15.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.15.10 (EOL) - stable
- add drm/radeon: Adding UVD handle basis fps estimation v2
- http://lists.freedesktop.org/archives/dri-devel/2014-August/065766.html
- add ReiserFS4 for kernel 3.15
- /patches-NRJ/0004-reiser4-for-3.15.1.patch
- /patches-NRJ/0005-3.15.1-reiser4-basic-discard-support.patch
- ---------------------------------------------------------------------
- Kernel 3.15 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Aug 08 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.15.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.15.9 - stable
- import ASPM fix patch from kernel 3.17 queue to improve powersave
- to read: http://www.phoronix.com/scan.php?page=news_item&px=MTc0NzE
- audio powersave: reduced idle time from 15 to 10 seconds
- configs for kernel realtime have audio powersave disable
- update TOI (power manager) from release 3.5.7 to 3.5.8  
- fix the broken support for running 16-bit code (X86_16BIT):
- to read: http://cateee.net/lkddb/web-lkddb/X86_16BIT.html
. new keys added to configs for X86_16BIT:
+ CONFIG_X86_16BIT=y
+ CONFIG_X86_ESPFIX32=y
- ---------------------------------------------------------------------
- Kernel 3.15 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Aug 01 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.15.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.15.8 - stable
- drop patch: x86-x86_32-entry-store-badsys-error-code-in-eax.patch
- update TOI (power manager) from release 3.5.6 to 3.5.7 
- audio powersave: reduced idle time from 60 to 15 seconds
- ---------------------------------------------------------------------
- Kernel 3.15 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Tue Jul 29 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.15.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.15.7 - stable
- add patch: x86-x86_32-entry-store-badsys-error-code-in-eax
- drop patch: revert-Bluetooth-Add-a-new-PID_VID-0cf3_e005-for-AR3012
- fix create_configs-QL script for a new TOI request (TOI_INCREMENTAL=n)
- update BFS (task scheduler) from release 448 to 449 
- ---------------------------------------------------------------------
- Kernel 3.15 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sun Jul 20 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.15.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.15.6 - stable
+ it's first version of "nrj/nrjQL" stable 3.15.x, in early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- for your daily PC working, because is still to fix all over!!!
- all the defconfigs have been prepared for the 3.15 series
- all the patches have been added/update for the 3.15 series
- all the create_configs scripts have been updated to v.2.2
- all the kernel specs have been updated to the 3.15 series
- all custom openmandriva/rosa features have been backported from 3.14.13
- ---------------------------------------------------------------------
- Kernel 3.15 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Jul 18 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.14.13-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.14.13 - stable
- update UKSM (nrjQL memory management) from 0.1.2.2 to 0.1.2.3
- x86 configs change: CONFIG_X86_VERBOSE_BOOTUP from "=y" to "=n" 
- to suppress annoying flashing messages while decompressig intrd:
- "Decompressing Linux . . . Parsing ELF . . . done
- Booting the kernel"
- fix from Eugene.S.: add perf-python-ext-link-with-dl.patch
- this patch is needed to fix the proper build of the perf tool
- ---------------------------------------------------------------------
- Kernel 3.14 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Tue Jul 01 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.14.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.14.10 - stable
- patch: tux on ice 3.14.10
- kernel.spec: add a new flavour to complete nrj set: nrj-server
- scripts/create_configs: add a new kernel flavour: nrj-server
- bero: added BuildRequires: pkgconfig(ncurses) 
- ---------------------------------------------------------------------
- Kernel 3.14 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Jun 27 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.14.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.14.9 - stable
- patch: tux on ice 3.14.9
- ---------------------------------------------------------------------
- Kernel 3.14 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Tue Jun 24 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.14.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.14.8 - stable
- few fixes to BR
- ---------------------------------------------------------------------
- Kernel 3.14 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sat Jun 21 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.14.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.14.6 (LTS???) - stable
+ this is first version of "nrj/nrjQL" stable 3.14.x, in its early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- for your daily PC working, because is still to fix all over!!!
- all the defconfigs have been prepared for the 3.14 series
- all the patches have been added/update for the 3.14 series
- all the create_configs scripts have been updated to v.2.1
- all the kernel specs have been updated to the 3.14 series
- modified kernel.spec to support from %mdvver 201200 to 201500
- tpg: fbsplash/fbcondecor feature: /patches-latest/fbcondecor-3.14.patch
- add config key: CONFIG_FB_CON_DECOR=y, changed: FB_TILEBLITTING=n
- pok: /patches-latest/linux-3.15-rc3-ahci-alpm-with-devslp-accounting.patch
- pok: build a cross-kernel-header package for arm, arm64 & mips toolchains
- arm: from CONFIG_SQUASHFS_DECOMP_MULTI=y to CONFIG_SQUASHFS_DECOMP_MULTI_PERCPU=y
- to be fixed: %if %{build_perf} with /traceevent and /traceevent/plugins
- ---------------------------------------------------------------------
- Kernel 3.14 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sat May 17 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.13.11-2.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.13.11 (EOL) - stable
- update BFQ to v7r4: 
  it fixes some oops that may happen with some new NCQ HDD devices,
  it leads other small speed improvements:
  - 0001-block-cgroups-kconfig-build-bits-for-BFQ-v7r4-3.13.patch
  - 0002-block-introduce-the-BFQ-v7r4-I-O-sched-for-3.13.patch
  - 0003-block-bfq-add-Early-Queue-Merge-EQM-to-BFQ-v7r4-for-3.13.0.patch
- two lines commented to know what triggers them show up (by TPG request):
  from: /arch/x86/boot/compressed/misc.c
     // debug_putstr("\nDecompressing Linux... ")
    // debug_putstr("done.\nBooting the kernel.\n")
- ---------------------------------------------------------------------
- Kernel 3.13 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Thu Apr 24 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.13.11-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.13.11 (EOL) - stable
- update patches:
  * tuxonice-for-linux-3.13.11-2014-04-24.patch
  * uksm-0.1.2.2-for-v3.13.ge.9.patch
- update BFQ to v7r3
  * 0001-block-cgroups-kconfig-build-bits-for-BFQ-v7r3-3.13.patch
  * 0002-block-introduce-the-BFQ-v7r3-I-O-sched-for-3.13.patch
  * 0003-block-bfq-add-Early-Queue-Merge-EQM-to-BFQ-v7r3-for-.patch
- suggestion / request received by Per Øyvind Karlsen (POK)
  * CONFIG_ACPI_CUSTOM_DSDT=y
- ---------------------------------------------------------------------
- Kernel 3.13 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Mon Apr 14 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.13.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.13.10 - stable
- on request by Alexander Khryukin: 
  * adding keys requested by Fedya to solve this issue:
  * https://issues.openmandriva.org/show_bug.cgi?id=165
  * http://pastie.org/9079599 > fixed missing features
  * Cgroup sched: missing
  * Cgroup cpu account: missing
  * Cgroup memory controller: missing
- ---------------------------------------------------------------------
- Kernel 3.13 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sun Apr 13 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.13.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.13.10 - rc1
- add: /patches-latest with its script (where are the latest things)
  * criu-no-expert.patch
  * linux-003-no_dev_console.patch
  * linux-004_lower_undefined_mode_timeout.patch
  * linux-006_enable_utf8.patch
  * linux-991.01-ptrace_fix.patch
- ---------------------------------------------------------------------
- Kernel 3.13 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Apr 04 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.13.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.13.9 stable
- add: /patches-queue (for tests) and /patches-geek with HW support:
- * DVB cards, IR receivers, WiFi devices, Game controllers, Laptops  
- add: 6 patches to improve NFS behaviour, fixing ops and start time
- add: the 3 patches for Pegatron device driver (offered by Benatto)
- add: new kernel driver modules are enabled, just below the list:
  * CONFIG_DVB_USB_DVBSKY=m
  * CONFIG_HID_SPINELPLUS=m
  * CONFIG_LIRC_XBOX=m 
  * CONFIG_PEGATRON_LAPTOP=m 
- add: patch to fix a disconnection USB problem with some slow USB HW
- suggested by Marco Benatto and was requested by Colin Close (itchka)
  - website: http://marc.info/?l=linux-usb&m=137714769606183&w=2
  * USB:_Fix_USB_device_disconnects_on_resume.patch
- on request by Fedya
  * adding keys requested by Fedya to solve this issue:
  * https://issues.openmandriva.org/show_bug.cgi?id=165
- fix: Benatto sent a working solution for UKSM 3.13 build error 3.13.9
  * 0001-uksm-0.1.2.2-for-v3.13.patch
  * 0002-uksm_change_compound_head_call.patch
-  visual improvements: boot and console appereance changes:
- add: colored printk feature with the default colors for all .configs
  * we must setup our preferred color palette, different than (=0x07)
- add: font-8x16-iso-latin-1-v3.patch
  * this shows the boot with more readable fonts, with a more dense look
- ---------------------------------------------------------------------
- Kernel 3.13 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Mon Mar 31 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.13.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.13.8 stable
- sync patches
- ---------------------------------------------------------------------
- Kernel 3.13 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Mar 28 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.13.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.13.7 stable
- sync with few nrjQL patches
- sync all the patches for 3.13.8 (rc1)
- add REISER4 (file system) support, with two new patches:
  * 0004-reiser4-for-3.13.6.patch
  * 0005-3.13.1-reiser4-different-transaction-models.patch
- ---------------------------------------------------------------------
- Kernel 3.13 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Mon Mar 10 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.13.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.13.6 stable
+ this is first version of "nrj" stable 3.13.x, in its early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- because is still to fix all over!!!
- all the defconfigs have been prepared for the 3.13 series
- all the patches have been added for the 3.13 series
- all the create_configs scripts have been updated to v.2.1
- all the kernel specs have been updated to the 3.13 series
- ---------------------------------------------------------------------
- Kernel 3.13 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Sun Feb 23 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.12.13-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ kernel 3.12.13 stable
- drop 2 patches, already in mainstream:
  * x86-xen-mmu-fix-NUMA-crash.patch
  * revert-usbcore-set-lpm_capable-field-for-lpm-capable-root-hubs.patch
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Feb 21 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.12.12-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ kernel 3.12.12 stable
- add: libunwind-devel as BR for %mdvver >= 201210 (ROSA 2012.1)
- change ftp://ftp.kernel.org patch format from .bz2 to .xz
- update: tuxonice-for-linux-3.12.12-2014-02-21.patch
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel (-1) (mainline serie), with official kernel sources and addons,
- the rel (-69) will be used for development and experimental flavours,
- instead (-70) is born by the -1 % -69 merge, can generate all flavours
- Yin & Yang (69) release - it's a very complete kernel flavour sets
- ---------------------------------------------------------------------

* Fri Feb 14 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.12.11-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ kernel 3.12.11 stable
- add: H930C-part1.patch, H930C-part2.patch, H930C-part3.patch
- add: kernel-3.11.8-i915-quirk-acer-aspire-v3-772g.patch
- drop: 2 drm patches, already in mainstream
- update: BFQ (disk I/O scheduler) from v7r1 to v7r2
- update: linux-saa716x_PCIe_interface_chipset.patch
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Feb 11 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.12.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ kernel 3.12.10 stable
- update BFQ (disk I/O scheduler) to v7r1
- enable the key: CONFIG_DRM_RADEON_UMS=y
- drop 12 patches, already in mainstream
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Thu Jan 30 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.12.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.12.9 stable
- small fixes and cleanups:
- removed all the remaining warning msgs from create_configs:
- fixed .defconfigs (arm.config, i386.config, x86_64.config)
 - satisfied all build CHK (audit, numa and unwind): 
- BuildRequires: audit-devel numa-devel unwind-devel
- sync & add new patches
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sun Jan 26 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.12.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.12.8 stable
- sync & add new patches
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Mon Jan 13 2014 Nicolo' Costanza <abitrules@yahoo.it> 3.12.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.12.7 stable
- sync and add new patches
- drop 3rdparty heci driver (obsoleted by in-kernel mei driver)
- switch to percpu squashfs multi-decompressor on i586 & x86_64
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Dec 31 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.12.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.12.6 stable
- add fix to properly rebuild the modules for latest VMware products 
- add patch: reiser4-for-3.12.6.patch
- add fix to all kernel.spec for a proper "cooker" rebuild 
- drop a workaround introduced since 3.7.9-1 to fix issues with dkms: 
- # /linux/version.h symlink to /include/generated/uapi/linux/version.h
- hoping there will follow many other kernels developed by me...
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Fri Dec 20 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.12.5-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.12.5 stable
+ this is first version of "nrj" stable 3.12.x, in its early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- because is still to fix all over!!!
-
- hoping there will follow many other kernels developed by me...
-
- all the defconfigs have been prepared for the 3.12 series
- all the patches have been added for the 3.12 series
- all the create_configs scripts have been updated to v.2.0
- all the kernel specs have been updated to the 3.12 series
- ---------------------------------------------------------------------
- Kernel 3.12 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sun Dec 01 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.11.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.11.10 stable
- http://lwn.net/Articles/575269/ > This is EOL for 3.11
- * 44 files changed, 395 insertions(+), 195 deletions(-)
- update: /patches-QL/tuxonice-for-linux-3.11.10-2013-11-30.patch
- small fixes and cleanups
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Thu Nov 28 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.11.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.11.9 stable
- revert latest EFI changes
  * CONFIG_EFIVAR_FS set to m
  * CONFIG_EFI_VARS set to y
- update: /patches-QL/tuxonice-for-linux-3.11.9-2013-11-22.patch
- Imported a commit from Bero: Add Acer Aspire v3-772g i915 quirk
  * https://abf.rosalinux.ru/openmandriva/kernel/commit/d6365d6f707d638ca4cb2c1e244da98dfed04776
- ---------------------------------------------------------------------
- Kernel 3.11 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- --------------------------------------------------------------------

* Sat Nov 16 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.11.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.11.8 stable 
- update: /patches-QL/tuxonice-for-linux-3.11.8-2013-11-15.patch
- Thanks to Eugene Shatokhin we have a modified BFS patch compatible with
- the ondemand speed-up patch, so also nrjQL should perform even better...
- ---------------------------------------------------------------------
- Kernel 3.11 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- --------------------------------------------------------------------

* Sun Nov 10 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.11.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.11.7 stable plus all the patches from the 3.11.8-rc1
- update: /patches-QL/uksm-0.1.2.2-for-v3.11.ge.7.patch
- ---------------------------------------------------------------------
- Kernel 3.11 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- --------------------------------------------------------------------

* Thu Nov 07 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.11.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.11.7 stable
- update: /patches-QL/tuxonice-for-linux-3.11.7-2013-11-07.patch
- add 'on request' by Eugene Shatokhin, few MEI changes to avoid too many error logs wasting space
  * CONFIG_INTEL_MEI from "=y" to "=m"
  * CONFIG_INTEL_MEI_ME from "=y" to "=m"
- add 'on request' by Alexander Burmashev: CONFIG_DRM_LOAD_EDID_FIRMWARE=y
  * with this we should be able to override the wrong EDID of displays with options at kernel boot
  * About EDID override howto, you read here:
  * https://www.osadl.org/monitoring/patches/r2s0/drivers-gpu-drm-allow-to-load-edid-firmware.patch
- add 'on request' by Alexander Kazancev the full configs for UEFI from:
  * https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface#Linux_Kernel_Config_options_for_UEFI
  * add CONFIG_RELOCATABLE=y also for i386.config
  * change CONFIG_EFIVAR_FS from "=m" to "=y"
  * change CONFIG_EFI_VARS from "=y" to "=n"
- add a patch to speed-up nuveau / radeon timers improvments for (from an 3.12 idea),
- it was addded patches-NRJ-only, /scripts/apply_patches-NRJ-only, and a spec modify
  * openSUSE 13.1 RC2 Updates Systemd, Has Speedy Fix:
  * http://www.phoronix.com/scan.php?page=news_item&px=MTQ5OTc
  * Here's Why Radeon Graphics Are Faster On Linux 3.12:
  * http://www.phoronix.com/scan.php?page=article&item=linux_312_performance&num=1
- ---------------------------------------------------------------------
- Kernel 3.11 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- --------------------------------------------------------------------

* Sat Oct 19 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.11.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.11.6 stable
- add 'on request' by 'Bero' aka Bernhard Rosenkränzer:
  * add: linux-3.11.4-saa716x.patch > driver for SAA7160 based DVB cards
  * add: to the /configs/*.config the proper keys for the SAA7160 driver
- add 3.11-haswell-intel_pstate.patch > to support P-state in new Haswell
- add 'on request' by Eugene Shatokhin: if debug > DEBUG_INFO_REDUCED=y
- add /specs folder with 4 kernel.spec, so you can use any other .specs
- drop to cleanups two old and really not used patches:
  * /patches-NRJ/kernel-inittmpfs.patch
  * /patches-NRJ/vhba-3.8-20130427.patch
- update: tuxonice-for-linux-3.11.6-2013-10-19.patch
- fix: missing XEN configs to all the -server flavours with config_xen();
- small fixes and aestetic cleanups to all the create_configs-* /scripts
- ---------------------------------------------------------------------
- Kernel 3.11 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- --------------------------------------------------------------------

* Sun Oct 06 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.11.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ this is first version of "nrj" stable 3.11.1, in its early development
- stage, so, it's only for testing purposes, please, dont use this srpm,
- because is still to fix all over!!!
+ update to 3.11.1 stable
- defconfigs: have been prepared for 3.11 series
- patches: have been updated for the 3.11 series
- specs: some needed updates to nrj, nrjQL, ONE
- ---------------------------------------------------------------------
- Kernel 3.11 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- --------------------------------------------------------------------

* Sat Oct 05 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.15-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.15 stable
- sync: /patches
- modified defconfigs for:
 * # CONFIG_FW_LOADER_USER_HELPER is not set
 * # CONFIG_X86_GOLDFISH is not set
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Oct 01 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.14-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.14 stable
- drop: fbcondecor.patch from /patches-others and /patches-NRJ (one)
- changes in defconfigs:
- drop config for CONFIG_FB_CON_DECOR
- recover to CONFIG_FB_TILEBLITTING=y
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Fri Sep 27 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.13-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.13 stable
- update patch
- * /patches-QL/tuxonice-for-linux-3.10.13-2013-09-27.patch
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Mon Sep 16 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.12-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.12 stable
- add patch
- * linux-fixuClibc.patch
- (it was recommended by Alexander Burmashev: uclibc builds on kernel 3.10
- we have a lot of such stuff in cooker, especially recommended for cooker)
- drop patches from previous 3.0.11 (these are already applied in 3.10.12):
  * net-sched-psched_ratecfg_precompute-improvements.patch
  * net-sched-restore-linklayer-atm-handling.patch
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Sep 10 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.11-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.11 stable
- the compressed folder now is the same (mibrel 69) for -1/-69/-70(one) 
- sync: new /patches:
  * /patches-QL/tuxonice-for-linux-3.10.11-2013-09-10.patch
- drop old 3.10.10 patches (these are already applied in 3.10.11):
  * kernel-workqueue-cond_resched-after-processing-each-work-item.patch
  * jfs-fix-readdir-cookie-incompatibility-with-nfsv4.patch
  * drm-nouveau-mc-fix-race-condition-between-constructor-and-request_irq.patch
  * net-wireless-ath-ath9k-Enable-PLL-fix-only-for-AR9340-AR9330.patch
  * net-mac80211-add-a-flag-to-indicate-CCK-support-for-HT-clients.patch
  * net-sunrpc-Fix-memory-corruption-issue-on-32-bit-highmem-systems.patch
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- the rel -69  is used for development and the experimental flavours,
- the rel -70 is merge of mainline & experimental flavours in ONE srpm
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sun Sep 01 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.10 stable
- BFQ: replaced with fixed version (nr.3 patches 3.10.8+-v6r2/ dated 25 August)
- sync: /patches
- updates: /patches-others /patches-NRJ /patches-QL /patches-RT
- modified all defconfigs, enabled: CONFIG_CHECKPOINT_RESTORE=y
- modified create_configs (all -server flavours: compression from XZ to GZIP)
- fixed Kconflicts for all distro or almost (hoping...)
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Thu Aug 22 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
- replacement 3.10.9 release
- To fix the "hangs on boot issue" signaled: bugs.rosalinux.ru/show_bug.cgi?id=2530
- add: /patches-NRJ/0004-block-Switch-from-BFQ-v6r2-for-3.10.0-to-BFQ-v6r2-fo.patch
- sync: /patches
- update: /patches-QL/tuxonice-for-linux-3.10.9-2013-08-21.patch
- fix conflicts as suggested by Tomasz ﻿Paweł﻿ Gajc: dkms-nvidia-current < 325.15-1
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Wed Aug 21 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.9 stable
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Aug 20 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.8 stable
- sync and update few patches
- the compressed folder has redundant contents to be used for NRJ4/NRJ5:
- the same folder can be used with kernel.spec for new Kernels ONE model
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Thu Aug 15 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.7 stable
- sync patches, drop old stable queue, drm-radeon and zram patches
- fixed the Conflicts: dkms-broadcom-wl < 5.100.82.112-12
- fixed create_configs (ver 1.8) - removed question when -netbook +pae
  * modified from: $values{XEN} = "n"; >>> to >>> $to_add{XEN} = "n";
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Aug 13 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.6 stable
- sync all /patches
- update QL patch: tuxonice-for-linux-3.10.6-2013-08-13.patch
- fixed Conflicts with new proprietary driver version-release
- fixed Provides value for Alsa
- small fix to .spec for %files headers section
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Wed Aug 07 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.5-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.5 stable
- sync all /patches
- sync defconfigs
- enable ndiswrapper
- update QL patch: tuxonice-for-linux-3.10.5-2013-08-04.patch
- revert to power save disable to verify if fixes an issue of audio noise:
- (that issue has been firstly reported by "dago68", then verified by me)
  * CONFIG_SND_HDA_POWER_SAVE_DEFAULT=0
  * CONFIG_SND_AC97_POWER_SAVE_DEFAULT=0
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Thu Aug 01 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.4-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.4 stable
- revert to old /scripts/create_configs-QL behaviour:
  * now -laptop and -netbook are 300 and 250HZ again
- sync /patches
- update patch: tuxonice-for-linux-3.10.4-2013-07-30.patch
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Jul 30 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.10.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.10.1 stable
- all the defconfigs have been prepared for 3.10 series
- all the patches have been updated for the 3.10 series
- update kernel specs
- ---------------------------------------------------------------------
- Kernel 3.10 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Jul 23 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.9.11-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to stable 3.9.11 (EOL)
- update patches:
  * tuxonice-for-linux-3.9.11-2013-07-21.patch
- update defconfigs
- ---------------------------------------------------------------------
- Kernel 3.9 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Wed Jul 17 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.9.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.9.10 stable
- update patches:
  * tuxonice-for-linux-3.9.10-2013-07-14.patch
  * uksm-0.1.2.2-for-v3.9.ge.8.patch
- update defconfigs
- ---------------------------------------------------------------------
- Kernel 3.9 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Fri Jul 05 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.9.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.9.9 stable
- update update: tuxonice-for-linux-3.9-8-2013-06-29.patch
- added patch: net-wireless-bcma-add-support-for-BCM43142.patch
- ---------------------------------------------------------------------
- Kernel 3.9 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Thu Jun 27 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.9.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.9.8 stable
- update patch: tuxonice-for-linux-3.9-7-2013-06-23.patch
- add patch: ath9k_htc > Handle IDLE state transition properly
- removed unused config keys: ATH9K_RATE_CONTROL=y & USB_CHIPIDEA_HOST=y
- ---------------------------------------------------------------------
- Kernel 3.9 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This kernel contains also some other patches to improve the hw support
- ---------------------------------------------------------------------

* Thu Jun 20 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.9.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.9.7 stable
- fixed a shutdown issue reported on nrjQL laptop -netbook and -server 
- now BFQ is the version updated to v6r2, dated 15 June
- replaced 3 patches:
  * 0001-block-cgroups-kconfig-build-bits-for-BFQ-v6r2-3.8.patch
  * 0002-block-introduce-the-BFQ-v6r2-I-O-sched-for-3.8.patch
  * 0003-block-bfq-add-Early-Queue-Merge-EQM-to-BFQ-v6r2-for-3.8.0.patch
- new key since 3.9.7 >>> # CONFIG_ATH9K_LEGACY_RATE_CONTROL is not set
- ---------------------------------------------------------------------
- Kernel 3.9 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This kernel contains also some other patches to improve the hw support
- ---------------------------------------------------------------------

* Fri Jun 14 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.9.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.9.6 stable
- update TOI patch >>> tuxonice-for-linux-3.9-6-2013-06-14.patch
- update all defconfigs: insert the new key values in the proper places
- update kernel.spec about text descriptions for nrj and nrjQL flavours
- small overall cleanups
- ---------------------------------------------------------------------
- Kernel 3.9 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Wed Jun 12 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.9.5-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.9.5 stable
- update TOI patch >>> tuxonice-for-linux-3.9-5-2013-06-08.patch
- ---------------------------------------------------------------------
- Kernel 3.9 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Jun 11 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.9.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.9.1 stable
- all the defconfigs have been prepared for 3.9 series
- all the patches have been updated for the 3.9 series
- update kernel specs
- update kernel scripts
- on mainline nrj kernels we apply again > create_configs-withBFQ
- we've received some good suggestions, and all have been accepted
- 1> suggestions and requests received by Per Øyvind Karlsen (POK)
  * TOI (tuxonice) was only in laptop/netbook, now in all flavours
  * CONFIG_PM_AUTOSLEEP=y 
  * CONFIG_SFI =m
  * CONFIG_BLK_DEV_DRBD=m 
  * # CONFIG_DRBD_FAULT_INJECTION is not set
  * CONFIG_HW_RANDOM_TIMERIOMEM=m 
  * CONFIG_DRM_VIA=m 
  * CONFIG_FB_ATY128_BACKLIGHT=y  
  * CONFIG_USB_RIO500=m 
  * CONFIG_DRM_VMWGFX_FBCON=y
  * CONFIG_SND_PCSP=m 
  * CONFIG_SND_HDA_POWER_SAVE_DEFAULT=10
  * CONFIG_SND_AC97_POWER_SAVE_DEFAULT=10
- 2> suggestions from an advanced user to A.Burmashev
  * CONFIG_TCP_CONG_ADVANCED=y
  * CONFIG_TCP_CONG_BIC=m
  * CONFIG_TCP_CONG_CUBIC=y
  * CONFIG_TCP_CONG_WESTWOOD=m
  * CONFIG_TCP_CONG_HTCP=m
  * CONFIG_TCP_CONG_HSTCP=m
  * CONFIG_TCP_CONG_HYBLA=m
  * CONFIG_TCP_CONG_VEGAS=m
  * CONFIG_TCP_CONG_SCALABLE=m
  * CONFIG_TCP_CONG_LP=m
  * CONFIG_TCP_CONG_VENO=m
  * CONFIG_TCP_CONG_YEAH=m
  * CONFIG_TCP_CONG_ILLINOIS=m
  * CONFIG_DEFAULT_CUBIC=y
  * # CONFIG_DEFAULT_RENO is not set
- ---------------------------------------------------------------------
- Kernel 3.9 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Thu May 09 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.12-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.12 stable 
- * 129 files changed, 641 insertions(+), 320 deletions(-)
- patches dropped, now in upstream
- patches updated to newer versions
- * tuxonice 3.8.12 20130509
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue May 07 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.11-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.11 stable 
- * 49 files changed, 454 insertions(+), 166 deletions(-)
- patches dropped, now in upstream
- patches updated to newer versions
- * aufs3 3.8 20130504
- * tuxonice 3.8.11 20130504
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sat Apr 27 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.10 stable 
- * 58 files changed, 405 insertions(+), 222 deletions(-)
- * 3 files changed, 27 insertions(+), 1 deletion(-)
- patches updated to newer versions dated 20130427:
  * aufs3, fbcondor, ureadahead, toi, vhba, zwap 
- patch add: try removing a boot warning about kernelvariables
  * /patches-extras/kernelvariables.patch
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Wed Apr 17 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.8 stable 
- *  37 files changed, 335 insertions(+), 344 deletions(-)
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Mon Apr 15 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.7 stable 
- * 67 files changed, 507 insertions(+), 341 deletions(-)
- new patches added, enabled and configured with default values
  * /patches-extras/linux-3.8.6-colored-printk.patch
  */patches-extras/zswap-3.8-20130415.patch
  * zswap now is enabled only on x86 arch, not in ARM (using zcache2)
- patches updated to newer versions 20130414:
  * aufs3, toi 
- patches updated to newer versions 20130415:
  * fbcondor, ureadahead, vhba
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sun Apr 07 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.6 stable 
- * (158 files changed, 1341 insertions(+), 658 deletions(-)
- patch add: reiserfs4 ver.3.8 with its configuration as new module
  * add an experimental support to Reiser4 FS: please test this FS!
- patches updated to newer git version 20130406:
  * aufs3, brtfs-lz4, fbcondor, toi, ureadahead, vhba
- Some kernel.spec changes from cooker to make it ARM/ARM64 compatible:
  * Import Bero commit 0e1b905e24 from openmandriva cooker kernel.spec
  * Import Fedya commit 4254d039f6 from openmandriva cooker kernel.spec
- add conflict for dkms-nvidia173 <= 173.14.36
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Thu Mar 28 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.5-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.5 stable 
- * (109 files changed, 778 insertions(+), 683 deletions(-)
- add two new keys to defconfigs:
  * CONFIG_EFI_VARS_PSTORE=y
  * # CONFIG_EFI_VARS_PSTORE_DEFAULT_DISABLE is not set
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sun Mar 24 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.4-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.4 stable (86 fixes all over)
+ NRJ 4, scripts v 1.6: more info on file > create_configs_changelog
+ Import Bero commit 32d3796b8b from openmandriva cooker kernel.spec
- patches updated:
  * AUFS3 to 3.8 20130324
  * TOI to 3.8.3 20130324
- patches added:
  * uksm-0.1.2.2-for-v3.8.ge.3.patch
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Fri Mar 15 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.3-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.3 stable (144 fixes all over)
+ Imported "Build kernel-headers in here" from OpenMandriva kernel
- drop Haswell id fixup: gpu-drm-i915-Fix-Haswell-CRW-PCI-IDs.patch
+ patches new entries are placed in /extras folder:
- kernel-esfq.patch
- kernel-inittmpfs.patch
- btrfs-lz4-3.8-20130314.patch
- ureadahead-3.8-20130314.patch
+ patches updated:
- AUFS3 to 3.8 20130315
- TOI to 3.8.3 20130315
- VHBA 3.8 20130314
+ NRJ 4, scripts v 1.5: 
- nrjQL_server & nrjQL_server_computing: dynticks enabled to save energy
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Mon Mar 11 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.2-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.2 stable (80 fixes all over)
+ Patch added from ZEN:
- Virtual (SCSI) HBA for Virtual CD emulation module
+ update to the patches:
- AUFS3 to 3.8 20130310
- TOI to 3.8.2 20130310
+ some spec cleanup for cooker
+ defconfigs updated for VHBA, enable for x86/x86_64, disable for ARM
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sun Mar 10 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.8.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.8.1 stable 
+ update to nrj v4 - rel 1.4 (09 mar 2013) 
- This version is first attempt to merge stuff with OpenMandriva devel:
- it should build from mdv2010/2011, rosa2012.0/2012.1, and cooker 2013
- ---------------------------------------------------------------------
- Kernel 3.8 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sun Mar 03 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.7.10-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.7.10 stable (79 fixes all over)
- With this version, 3.7 has reached the EOL status (End of Life)
+ update to nrj v4 - rel 1.3 (05 mar 2013) 
- On request of Alexander Khryukin, fixed configs and scripts for ARM:
- fixed configs, removed all warnings, enabled again all arm defconfigs
- defconfigs for kirkwood, versatile, iop32x have BFQ enable by default
- ---------------------------------------------------------------------
- Kernel 3.7 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Wed Feb 20 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.7.9-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.7.9 stable (12 fixes all over)
- update AUFS3 to 3.7.9 20130218
- specific for nrjQL addons:
- update tuxonice 3.7.9 20130218
- add a workaround to fix issue with dkms drivers for recent distros:
- /linux/version.h symlink to /include/generated/uapi/linux/version.h
- ---------------------------------------------------------------------
- Kernel 3.7 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sat Feb 16 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.7.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.7.8 stable (69 fixes all over)
- update AUFS3 to 3.7 20130215
- specific for nrjQL addons:
- update tuxonice 3.7.8 20130215
- updated scripts:
- all nrj flavours use BFQ v6 (disk I/O) enabled by default
- all nrj laptop flavours since now use the full preemption 
- ---------------------------------------------------------------------
- Kernel 3.7 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Wed Feb 13 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.7.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.7.7 stable (34 fixes all over)
- update AUFS3 to 3.7 20130212
- specific for nrjQL addons:
- update BFQ v6 I-O-sched for-3.7
- update tuxonice 3.7.7 20130212
- remove microcode from "requires", now it's in "suggests"
- ---------------------------------------------------------------------
- Kernel 3.7 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Mon Feb 04 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.7.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.7.6 stable (101 fixes all over)
- add "# CONFIG_NETFILTER_XT_TARGET_NOTRACK is not set" to defconfigs
- ---------------------------------------------------------------------
- Kernel 3.7 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- The rel -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours,
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sat Feb 02 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.7.5-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.7.5 stable
- drop two staging patches
- ---------------------------------------------------------------------
- Kernel 3.7 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Sat Feb 02 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.7.1-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.7.1 stable
- update kernel.spec to be complaint with new V4 nrj/nrjQL model 
- update all scripts to be complaint with new V4 nrj/nrjQL model
- merged defconfigs for nrj & nrjQL, source folders and contents have been unified
- merged all changelogs, as now nrj and nrjQL will be developed in perfect sync
- applied all ROSA customizations of defconfigs as requested by Alexander Burmashev
- update AUFS3 to 3.7 20130128
- update 4200_fbcondecor-0.9.6
- add 08-18-brcmsmac-Add-support-for-writing-debug-messages-to-the-trace-buffer.patch
- specific for nrjQL addons:
- update BFQ v5r1 I-O-sched for-3.7
- update ck1 3.7 and bfs426-427
- update tuxonice 3.7.5 20130128
- update uksm 0.1.2.2 for v3.7.ge.1
- ---------------------------------------------------------------------
- Kernel 3.7 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Fri Jan 25 2013 Nicolo' Costanza <abitrules@yahoo.it> 3.7.1-0.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.7.1 stable
- update script with nrj module v.3.1
- update .spec filelists
- update/sync defconfigs
- fix zram oops (upstream)
- add perf bash_completion
- add 3.7 buildfixes for alx, IFWLOG, mach64, ndiswrapper
- rediff disable-mrproper patch
- restore patch preferring ata over ide drivers
- drop compress modules at install time patch
  (obsolete as we compress them at rpm build time)
- ---------------------------------------------------------------------
- Kernel 3.7 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Dec 11 2012 Nicolo' Costanza <abitrules@yahoo.it> 3.6.10-0.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.6.10 stable (29 fixes all over)
- update AUFS3 version to git 20121207
- update T.O.I version to gif 20121207
- add speakup-lower-default-software-speech-rate.patch
- This is a testing version with nrj-desktop BFQ enabled!
- ---------------------------------------------------------------------
- Kernel 3.6 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Fri Nov 30 2012 Nicolo' Costanza <abitrules@yahoo.it> 3.6.8-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.6.8-1 (96 fixes all over)
- add 4200_fbcondecor-0.9.6.patch
- add config key CONFIG_FB_CON_DECOR=y, changed FB_TILEBLITTING=n
- ---------------------------------------------------------------------
- Kernel 3.6 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Tue Nov 20 2012 Nicolo' Costanza <abitrules@yahoo.it> 3.6.7-1.1
- Virtual package for new nrj kernel for properly install and updates.
+ update to 3.6.7-1.1 (89 fixes all over)
- updated all patches for kernel 3.6.7: AUFS3, OverlayFS, TOI
- re-add cpufreq_ondemand_performance_optimise_default_settings.patch
- small modifies and fixes to "create_configs" and "kernel.spec" files
- ---------------------------------------------------------------------
- Kernel 3.6 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Wed Nov 07 2012 Nicolo' Costanza <abitrules@yahoo.it> 3.6.6-2.2
+ update to 3.6.6-2.2
- Virtual package for new nrj kernel for properly install and updates.
- drop cpufreq_ondemand_performance_optimise_default_settings.patch
- to test if removing this patch the p4-clockmod can works again...
- ---------------------------------------------------------------------
- Kernel 3.6 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Mon Nov 05 2012 Nicolo' Costanza <abitrules@yahoo.it> 3.6.6-1.1
+ update to 3.6.6-1.1
- Virtual package for new nrj kernel for properly install and updates.
- drop FX01_fs-ext4-fix-unjournaled-inode-bitmap-modification.patch,
- because that's already inside patch-3.6.6.bz2
- modify configuration for server flavour to DEFAULT_GOV_ONDEMAND=y
- ---------------------------------------------------------------------
- Kernel 3.6 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------

* Fri Nov 02 2012 Nicolo' Costanza <abitrules@yahoo.it> 3.6.5-2.2
+ update to 3.6.5-2.2
- Virtual package for new nrj kernel for properly install and updates.
- drop FX01_fix-serious-progressive-ext4-data-corruption-bug.patch
- add FX01_fs-ext4-fix-unjournaled-inode-bitmap-modification.patch
- ---------------------------------------------------------------------
- Kernel 3.6 for mdv 2010.2, 2011.0, cooker, rosa.lts2012.0, rosa2012.1
- MIB (Mandriva International Backports) - http://mib.pianetalinux.org/
- This is -1 (mainline serie), with official kernel sources and addons,
- instead (-69) will be used for development and experimental flavours
- Yin & Yang (69) release - a very complete but experimental flavours...
- ---------------------------------------------------------------------
