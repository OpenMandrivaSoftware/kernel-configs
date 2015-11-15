========================================================
Files:
/configs/arm.config 
/configs/i386.config
/configs//x86_64.config
========================================================


3.7.1 orig
==========
# Linux/x86_64 3.7.1-69.mib Kernel Configuration

3.7.10 orig
==========
# Linux/x86_64 3.7.10-69.mib Kernel Configuration



3.7.1 orig - (not in ARM)
==========
# CONFIG_HZ_100 is not set
# CONFIG_HZ_250 is not set
# CONFIG_HZ_300 is not set
CONFIG_HZ_1000=y
CONFIG_HZ=1000

3.7.10 mod - (not in ARM)
==========
# CONFIG_HZ_100 is not set
# CONFIG_HZ_250 is not set
# CONFIG_HZ_250_NODEFAULT is not set
# CONFIG_HZ_300 is not set
CONFIG_HZ_1000=y
# CONFIG_HZ_1500 is not set
# CONFIG_HZ_2000 is not set
# CONFIG_HZ_3000 is not set
# CONFIG_HZ_4000 is not set
# CONFIG_HZ_5000 is not set
# CONFIG_HZ_7500 is not set
# CONFIG_HZ_10000 is not set
CONFIG_HZ=1000



3.7.1 orig - (not in ARM)
==========
#
# CPU Frequency scaling
#
CONFIG_CPU_FREQ=y
CONFIG_CPU_FREQ_TABLE=y
CONFIG_CPU_FREQ_STAT=m
CONFIG_CPU_FREQ_STAT_DETAILS=y
CONFIG_CPU_FREQ_DEFAULT_GOV_PERFORMANCE=y
# CONFIG_CPU_FREQ_DEFAULT_GOV_POWERSAVE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_USERSPACE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_ONDEMAND is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_CONSERVATIVE is not set
CONFIG_CPU_FREQ_GOV_PERFORMANCE=y
CONFIG_CPU_FREQ_GOV_POWERSAVE=m
CONFIG_CPU_FREQ_GOV_USERSPACE=y
CONFIG_CPU_FREQ_GOV_ONDEMAND=m
CONFIG_CPU_FREQ_GOV_CONSERVATIVE=m

3.7.10 mod - (not in ARM)
==========
#
# CPU Frequency scaling
#
CONFIG_CPU_FREQ=y
CONFIG_CPU_FREQ_TABLE=m
CONFIG_CPU_FREQ_STAT=m
CONFIG_CPU_FREQ_STAT_DETAILS=y
CONFIG_CPU_FREQ_DEFAULT_GOV_ONDEMAND=y
# CONFIG_CPU_FREQ_DEFAULT_GOV_PERFORMANCE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_POWERSAVE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_USERSPACE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_CONSERVATIVE is not set
CONFIG_CPU_FREQ_GOV_PERFORMANCE=y
CONFIG_CPU_FREQ_GOV_POWERSAVE=y
CONFIG_CPU_FREQ_GOV_USERSPACE=y
CONFIG_CPU_FREQ_GOV_ONDEMAND=y
CONFIG_CPU_FREQ_GOV_CONSERVATIVE=y

3.8.1 orig - (not in ARM)
==========
#
# CPU Frequency scaling
#
CONFIG_CPU_FREQ=y
CONFIG_CPU_FREQ_TABLE=y
CONFIG_CPU_FREQ_GOV_COMMON=y
CONFIG_CPU_FREQ_STAT=m
CONFIG_CPU_FREQ_STAT_DETAILS=y
CONFIG_CPU_FREQ_DEFAULT_GOV_PERFORMANCE=y
# CONFIG_CPU_FREQ_DEFAULT_GOV_POWERSAVE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_USERSPACE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_ONDEMAND is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_CONSERVATIVE is not set
CONFIG_CPU_FREQ_GOV_PERFORMANCE=y
CONFIG_CPU_FREQ_GOV_POWERSAVE=m
CONFIG_CPU_FREQ_GOV_USERSPACE=y
CONFIG_CPU_FREQ_GOV_ONDEMAND=m
CONFIG_CPU_FREQ_GOV_CONSERVATIVE=m

3.9.1 mod - (not in ARM)
==========
#
# CPU Frequency scaling
#
CONFIG_CPU_FREQ=y
CONFIG_CPU_FREQ_TABLE=y
CONFIG_CPU_FREQ_GOV_COMMON=y
CONFIG_CPU_FREQ_STAT=m
CONFIG_CPU_FREQ_STAT_DETAILS=y
CONFIG_CPU_FREQ_DEFAULT_GOV_ONDEMAND=y
# CONFIG_CPU_FREQ_DEFAULT_GOV_PERFORMANCE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_POWERSAVE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_USERSPACE is not set
# CONFIG_CPU_FREQ_DEFAULT_GOV_CONSERVATIVE is not set
CONFIG_CPU_FREQ_GOV_PERFORMANCE=y
CONFIG_CPU_FREQ_GOV_POWERSAVE=y
CONFIG_CPU_FREQ_GOV_USERSPACE=y
CONFIG_CPU_FREQ_GOV_ONDEMAND=y
CONFIG_CPU_FREQ_GOV_CONSERVATIVE=y



3.7.1 orig
==========
CONFIG_NETFILTER_XT_TARGET_NFQUEUE=m
CONFIG_NETFILTER_XT_TARGET_RATEEST=m

3.7.10 mod
==========
CONFIG_NETFILTER_XT_TARGET_NFQUEUE=m
# CONFIG_NETFILTER_XT_TARGET_NOTRACK is not set
CONFIG_NETFILTER_XT_TARGET_RATEEST=m



3.7.1 orig
==========
CONFIG_FB_TILEBLITTING=y

3.7.10 mod
==========
CONFIG_FB_TILEBLITTING=n



3.7.1 orig - (not in ARM)
==========
# CONFIG_LOGO is not set

3.7.10 mod - (not in ARM)
==========
CONFIG_LOGO=y
CONFIG_LOGO_LINUX_MONO=y
CONFIG_LOGO_LINUX_VGA16=y
CONFIG_LOGO_LINUX_CLUT224=y
CONFIG_LOGO_MDK_CLUT224=y



3.7.1 orig - (not in ARM)
==========
CONFIG_NLS_CODEPAGE_437=m

3.7.10 mod - (not in ARM)
==========
CONFIG_NLS_CODEPAGE_437=y

3.9.1 mod - (also in ARM)
==========
CONFIG_NLS_CODEPAGE_437=y




- 1> suggestions and requests received by Per Øyvind Karlsen (POK)
  * TOI (tuxonice) was only in laptop/netbook, now in all flavours
  * CONFIG_PM_AUTOSLEEP=y 
  * CONFIG_SFI=y
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

CONFIG_TCP_CONG_ADVANCED=y
CONFIG_TCP_CONG_BIC=m
CONFIG_TCP_CONG_CUBIC=y
CONFIG_TCP_CONG_WESTWOOD=m
CONFIG_TCP_CONG_HTCP=m
CONFIG_TCP_CONG_HSTCP=m
CONFIG_TCP_CONG_HYBLA=m
CONFIG_TCP_CONG_VEGAS=m
CONFIG_TCP_CONG_SCALABLE=m
CONFIG_TCP_CONG_LP=m
CONFIG_TCP_CONG_VENO=m
CONFIG_TCP_CONG_YEAH=m
CONFIG_TCP_CONG_ILLINOIS=m
CONFIG_DEFAULT_TCP_CONG="cubic"
CONFIG_DEFAULT_CUBIC=y
# CONFIG_DEFAULT_RENO is not set


# suggestions and requests received by POK
CONFIG_PM_AUTOSLEEP=y 
CONFIG_SFI =m
CONFIG_BLK_DEV_DRBD=m 
CONFIG_HW_RANDOM_TIMERIOMEM=m 
CONFIG_DRM_VIA=m 
CONFIG_FB_ATY128_BACKLIGHT=y  
CONFIG_USB_RIO500=m 
CONFIG_DRM_VMWGFX_FBCON=y
CONFIG_SND_PCSP=m 
CONFIG_SND_HDA_POWER_SAVE_DEFAULT=10
CONFIG_SND_AC97_POWER_SAVE_DEFAULT=10

  DRBD Distributed Replicated Block Device support (BLK_DEV_DRBD) [M/n/y/?] m
  DRBD fault injection (DRBD_FAULT_INJECTION) [N/y/?] (NEW) Y (Y is ok for you?)

WARNING:
DRBD was/is dibabled by default in all -LAPTOP flavours: what to do?



Request by POK

from
CONFIG_DRM_RADEON_UMS is not set
to
CONFIG_DRM_RADEON_UMS=y


HECI must be removed???
#
# Unofficial 3rd party kernel additions
#
CONFIG_HECI=m




BUILD:   Doing 'make -j2' parallel build

Auto-detecting system features:
...                     backtrace: [ on  ]
...                         dwarf: [ on  ]
...                fortify-source: [ on  ]
...                         glibc: [ on  ]
...                          gtk2: [ on  ]
...                  gtk2-infobar: [ on  ]
...                      libaudit: [ on  ]
...                        libbfd: [ on  ]
...                        libelf: [ on  ]
...             libelf-getphdrnum: [ on  ]
...                   libelf-mmap: [ on  ]
...                       libnuma: [ on  ]
...                       libperl: [ OFF ]
...                     libpython: [ on  ]
...             libpython-version: [ on  ]
...                      libslang: [ on  ]
...                     libunwind: [ on  ]
...                       on-exit: [ on  ]
...                stackprotector: [ on  ]
...            stackprotector-all: [ on  ]
...                       timerfd: [ on  ]

make  -C Documentation  install-man
make[2]: Nothing to be done for `install-man'.
+ make -C tools/power/cpupower DESTDIR=/home/utente/rpmbuild/BUILDROOT/kernel-3.13.6-69-rosa.lts2012.0.x86_64-buildroot libdir=/usr/lib64 mandir=/usr/share/man CPUFREQ_BENCH=false install
make: Entering directory `/home/utente/rpmbuild/BUILD/kernel-x86_64/linux-3.13/tools/power/cpupower'




[18:55]	niccco	we have kernel 3.13.6
[18:55]	niccco	http://mib.pianetalinux.org/forum/viewtopic.php?f=38&t=4371
[18:55]	niccco	none problems found...
[18:56]	benatto	trying to compiling it by hands on two different machines I'm getting: ld: warning: Disabling --icf due to -r
[18:56]	benatto	ld: warning: arch/x86/realmode/rm/header.o: missing .note.GNU-stack section implies executable stack
[18:56]	benatto	for several files and no .ko modules weere generated
[18:57]	benatto	on my fedora 20.1 it's working fine, didn't tried on 2014.0 yet
[18:57]	bero	That means it's using gold...
[18:57]	bero	Fedupra doesn't use gold at all, so that's why you wouldn't see it there
[18:57]	bero	On OMV we're using gold by default, but the kernel should be switching to bfd because of some magic in the spec file
[18:58]	benatto	got it, what do you mean by using "gold"? What should be de difference?
[19:04]	_TPG	Xu_R: i've noticed that you marked blocker a lot of packages which are in contrib or other repo than main
[19:04]	Xu_R	_TPG: I'm marking blocker based on the reports and how long they've been there. If they're in contrib, then downgrade them and just put that they're in contrib.
[19:05]	Xu_R	still has another ~40 bugs to triage
[19:05]	bero	benatto: http://en.wikipedia.org/wiki/Gold_(linker)
[19:05]	bero	benatto: Difference is it's a completely different linker
[19:06]	benatto	bero: got it. What's strange I've compiled some oldest kernel version with not problems on 2013 before...not sure since which family this starts to happen
[19:06]	_TPG	Xu_R: if you have time please test this one https://issues.openmandriva.org/show_bug.cgi?id=561
[19:07]	Xu_R	_TPG: Yeah, will test.
[19:07]	benatto	bero: how do I revert to bfd?
[19:08]	bero	benatto: Usually add -fuse-ld=bfd to the compiler flags, if Makefiles are terribly broken, something along the lines of mkdir /tmp/crap ; ln -s /usr/bin/ld.bfd /tmp/crap/ld ; export PATH=/tmp/crap:$PATH will do the trick as well
[19:09]	benatto	bero: ouch, will try. To kernel's make file is never a good idea....thanks
[19:09]	benatto	btw, sorry for be away from community for the last weeks...so much stuff at work to do...
[19:09]	bero	benatto: No problem, I was gone last week too (Linaro event)





utente ~ $ su -
Password: 
localhost ~ # urpmi /home/utente/rpmbuild/RPMS/x86_64/kernel-nrjQL-desktop-devel-3.13.6-69rosa.lts-1-1-rosa.lts2012.0.x86_64.rpm /home/utente/rpmbuild/RPMS/x86_64/kernel-nrjQL-desktop-3.13.6-69rosa.lts-1-1-rosa.lts2012.0.x86_64.rpm


installazione di kernel-nrjQL-desktop-devel-3.13.6-69rosa.lts-1-1-rosa.lts2012.0.x86_64.rpm kernel-nrjQL-desktop-3.13.6-69rosa.lts-1-1-rosa.lts2012.0.x86_64.rpm da /home/utente/rpmbuild/RPMS/x86_64
In preparazione...               ####################################################################################
      1/2: kernel-nrjQL-desktop-devel-3.13.6-69rosa.lts
                                 ####################################################################################
      2/2: kernel-nrjQL-desktop-3.13.6-69rosa.lts
                                 ####################################################################################
I: *** Including module: dash ***
I: *** Including module: i18n ***
I: *** Including module: rpmversion ***
I: *** Including module: network ***
I: Possible missing firmware "ct2fw-3.2.1.1.bin" for kernel module "bna.ko"
I: Possible missing firmware "ctfw-3.2.1.1.bin" for kernel module "bna.ko"
I: Possible missing firmware "bnx2x/bnx2x-e2-7.8.17.0.fw" for kernel module "bnx2x.ko"
I: Possible missing firmware "bnx2x/bnx2x-e1h-7.8.17.0.fw" for kernel module "bnx2x.ko"
I: Possible missing firmware "bnx2x/bnx2x-e1-7.8.17.0.fw" for kernel module "bnx2x.ko"
I: Possible missing firmware "cxgb4/t5fw.bin" for kernel module "cxgb4.ko"
I: Possible missing firmware "rtl_nic/rtl8168g-3.fw" for kernel module "r8169.ko"
I: Possible missing firmware "rtl_nic/rtl8168g-2.fw" for kernel module "r8169.ko"
I: Possible missing firmware "rtl_nic/rtl8106e-2.fw" for kernel module "r8169.ko"
I: Possible missing firmware "rtl_nic/rtl8106e-1.fw" for kernel module "r8169.ko"
I: Possible missing firmware "rtl_nic/rtl8411-2.fw" for kernel module "r8169.ko"
I: *** Including module: ifcfg ***
I: *** Including module: plymouth ***
I: Omitting driver /kernel/drivers/gpu/drm/radeon/radeon
I: Omitting driver /kernel/drivers/gpu/drm/nouveau/nouveau
I: *** Including module: btrfs ***
I: *** Including module: crypt ***
I: *** Including module: dm ***
I: Skipping udev rule: 64-device-mapper.rules
I: *** Including module: dmsquash-live ***
I: *** Including module: kernel-modules ***
I: Possible missing firmware "ct2fw-3.2.1.1.bin" for kernel module "bfa.ko"
I: Possible missing firmware "ctfw-3.2.1.1.bin" for kernel module "bfa.ko"
I: Possible missing firmware "cbfw-3.2.1.1.bin" for kernel module "bfa.ko"
I: Possible missing firmware "cxgb4/t5fw.bin" for kernel module "csiostor.ko"
I: Possible missing firmware "aic94xx-seq.fw" for kernel module "aic94xx.ko"
I: Omitting driver kernel/fs/nfs
I: Omitting driver kernel/fs/nfs/nfsv4
I: Omitting driver kernel/fs/nfs/nfsv3
I: Omitting driver kernel/fs/nfs/nfsv2
I: Omitting driver kernel/fs/nfs/nfs
I: Omitting driver kernel/fs/nfsd
I: Omitting driver kernel/fs/nfsd/nfsd
I: Omitting driver kernel/fs/nfs_common
I: Omitting driver kernel/fs/nfs_common/nfs_acl
I: Omitting driver kernel/fs/lockd
I: Omitting driver kernel/fs/lockd/lockd
I: *** Including module: lvm ***
I: Skipping udev rule: 64-device-mapper.rules
I: *** Including module: mdraid ***
I: *** Including module: fcoe ***
I: *** Including module: nfs ***
I: *** Including module: resume ***
I: *** Including module: rootfs-block ***
I: *** Including module: terminfo ***
I: *** Including module: udev-rules ***
I: Skipping udev rule: 50-udev.rules
I: Skipping udev rule: 95-late.rules
I: *** Including module: usrmount ***
I: *** Including module: base ***
I: *** Including module: fs-lib ***
I: *** Including module: shutdown ***
I: Skipping program kexec as it cannot be found and is flagged to be optional
I: *** Including modules done ***
I: Wrote /boot/initrd-3.13.6-nrjQL-desktop-69rosa.lts.img:
I: -rw-r--r-- 1 root root 29687688 mar 10 21:49 /boot/initrd-3.13.6-nrjQL-desktop-69rosa.lts.img
Can't call method "get_resolution" on an undefined value at -e line 1.

vhba (1.2.1-4.20100822.1): Installing module.
.........(bad exit status: 10)
  Build failed.  Installation skipped.
warning: existing POPT configuration file "/usr/lib/rpm/rpmpopt:/usr/lib/rpm/%{_target}/rpmpopt:/etc/rpm/rpmpopt.*:/etc/rpm/rpmpopt:/etc/rpm/%{_target}/rpmpopt:~/.rpmpopt" considered INSECURE -- not loaded
Dovresti riavviare il computer per kernel-nrjQL-desktop-3.13.6-69rosa.lts
localhost ~ # 











========================================================
Files:
/scripts/create_configs and /scrips/create_configsQL
========================================================


3.7.1 (removed "1GB" & "4GB" defines, now "4GB" must be replaced with "none")
===========================
sub config_x86_highmem {
    my ($mem) = @_;

    if ($mem eq "1GB" ) {
	$values{HIGHMEM} = "n";
	$values{HIGHMEM4G} = "n" ;
	$values{HIGHMEM64G} = "n";
	$values{NOHIGHMEM} = "y" ;
	$values{HIGHPTE} = "n";
	$values{VMSPLIT_3G} = "y";
	$values{VMSPLIT_3G_OPT} = "n";
	$values{VMSPLIT_2G} = "n";
	$values{VMSPLIT_1G} = "n";
    } elsif ($mem eq "4GB" ) {
	$values{HIGHMEM} = "y";
	$values{NOHIGHMEM} = "n" ;
	$values{HIGHMEM4G} = "y" ;
	$values{HIGHMEM64G} = "n" ;
	$values{HIGHPTE} = "n";
	$values{VMSPLIT_3G} = "y";
	$values{VMSPLIT_3G_OPT} = "n";
	$values{VMSPLIT_2G} = "n";
	$values{VMSPLIT_1G} = "n";
    } elsif ($mem eq "64GB") {
	$values{HIGHMEM} = "y";
	$values{NOHIGHMEM} = "n" ;
	$values{HIGHMEM4G} = "n" ;
	$values{HIGHMEM64G} = "y" ;
	$values{HIGHPTE} = "n";
	$values{VMSPLIT_3G} = "y";
	$values{VMSPLIT_3G_OPT} = "n";
	$values{VMSPLIT_2G} = "n";
	$values{VMSPLIT_1G} = "n";
        $to_add{I2O_EXT_ADAPTEC_DMA64} = "y";
    }
}

3.8.1
===========================
sub config_x86_highmem {
    my ($mem) = @_;

    if ($mem eq "64GB" ) {
	$values{HIGHMEM4G} = "n" ;
	$values{HIGHMEM64G} = "y" ;
        $to_add{I2O_EXT_ADAPTEC_DMA64} = "y";
    }
}




3.7.1 orig ("4GB" replaced with "none")
==========
my @configs = (
     [ qw(i686 smp 4GB nrjQL-desktop) ],
     [ qw(i686 smp 4GB nrjQL-realtime) ],
     [ qw(i686 smp 4GB nrjQL-laptop) ],
     [ qw(i686 smp 4GB nrjQL-netbook) ],
     [ qw(i686 smp 64GB nrjQL-server) ],
     [ qw(i686 smp 64GB nrjQL-server-computing) ],
     [ qw(i686 smp 64GB nrjQL-server-games) ],
     [ qw(i686 smp 64GB nrjQL-desktop-pae) ],
     [ qw(i686 smp 64GB nrjQL-realtime-pae) ],
     [ qw(i686 smp 64GB nrjQL-laptop-pae) ],
     [ qw(i686 smp 64GB nrjQL-netbook-pae) ],
     [ qw(mcore2 smp 4GB nrjQL-desktop-core2) ],
     [ qw(mcore2 smp 64GB nrjQL-desktop-core2-pae) ],

     [ qw(x86_64 smp none nrjQL-desktop) ],
     [ qw(x86_64 smp none nrjQL-realtime) ],
     [ qw(x86_64 smp none nrjQL-laptop) ],
     [ qw(x86_64 smp none nrjQL-netbook) ],
     [ qw(x86_64 smp none nrjQL-server) ],
     [ qw(x86_64 smp none nrjQL-server-computing) ],
     [ qw(x86_64 smp none nrjQL-server-games) ],

     [ qw(arm up none kirkwood) ],
     [ qw(arm up none versatile) ],
     [ qw(arm up none iop32x) ],
);

3.8.1 mod ("4GB" replaced with "none")
==========
my @configs = (
     [ qw(i686 smp none nrjQL-desktop) ],
     [ qw(i686 smp none nrjQL-realtime) ],
     [ qw(i686 smp none nrjQL-laptop) ],
     [ qw(i686 smp none nrjQL-netbook) ],
     [ qw(i686 smp 64GB nrjQL-server) ],
     [ qw(i686 smp 64GB nrjQL-server-computing) ],
     [ qw(i686 smp 64GB nrjQL-server-games) ],
     [ qw(i686 smp 64GB nrjQL-desktop-pae) ],
     [ qw(i686 smp 64GB nrjQL-realtime-pae) ],
     [ qw(i686 smp 64GB nrjQL-laptop-pae) ],
     [ qw(i686 smp 64GB nrjQL-netbook-pae) ],
     [ qw(mcore2 smp none nrjQL-desktop-core2) ],
     [ qw(mcore2 smp 64GB nrjQL-desktop-core2-pae) ],

     [ qw(x86_64 smp none nrjQL-desktop) ],
     [ qw(x86_64 smp none nrjQL-realtime) ],
     [ qw(x86_64 smp none nrjQL-laptop) ],
     [ qw(x86_64 smp none nrjQL-netbook) ],
     [ qw(x86_64 smp none nrjQL-server) ],
     [ qw(x86_64 smp none nrjQL-server-computing) ],
     [ qw(x86_64 smp none nrjQL-server-games) ],

     [ qw(arm up none kirkwood) ],
     [ qw(arm up none versatile) ],
     [ qw(arm up none iop32x) ],
);



3.7.10 orig
==========

	  $to_add{MFD_TC6393XB} = "n";
	  $to_add{IRQ_DOMAIN_DEBUG} = "n";

3.8.1 mod
==========

	  $to_add{MFD_TC6393XB} = "n";
	  $to_add{IRQ_DOMAIN_DEBUG} = "n";
	  $to_add{NTP_PPS} = "n";




========================================================
Files: from mga
/kernel.spec
========================================================


3.7.1
===========
%define requires2	dracut >= 017-9
%define requires3	kmod >= 7-6

3.8.1 -done-
===========
%define requires2	dracut >= 025-5
%define requires3	kmod >= 7-7



3.7.1
===========
%define kprovides 	%{kname} = %{kverrel}, kernel = %{tar_ver}, alsa = 1.0.24
%define kprovides_server drbd-api = 88

3.8.1 -done-
===========
%define kprovides1 	%{kname} = %{kverrel}
%define kprovides2 	kernel = %{tar_ver}
%define kprovides3 	alsa = 1.0.26
%define kprovides_server drbd-api = 88



3.7.1
===========
%define	kobsoletes	dkms-r8192se <= 0019.1207.2010-2, dkms-lzma <= 4.43-32, dkms-psb <= 4.41.1-7

3.8.1 -done-
===========
%define	kobsoletes1	dkms-r8192se <= 0019.1207.2010-2
%define	kobsoletes2	dkms-lzma <= 4.43-32
%define	kobsoletes3	dkms-psb <= 4.41.1-7
# conflict dkms packages that dont support kernel-3.8
%define kconflicts1	dkms-broadcom-wl < 5.100.82.112-6
%define kconflicts1	dkms-fglrx < 9.010.8-5
%define kconflicts2	dkms-nvidia-current < 310.19-2
%define kconflicts3	dkms-nvidia304 < 304.64-4
%define kconflicts4	dkms-nvidia173 < 173.14.36-4
# (tmb) nvidia96xx does not support this kernel or x11-server-1.13
%define kconflicts5	dkms-nvidia96xx <= 96.43.23
%define kconflicts6	dmms-xtables-addons < 2.1-2



3.7.1 rosa/openmdv (we must check carefully)
==========
BuildRequires: 		gcc kmod >= 7-6
# for perf, cpufreq and other tools
BuildRequires:		elfutils-devel
BuildRequires:		zlib-devel
BuildRequires:		binutils-devel
BuildRequires:		newt-devel
BuildRequires:		python-devel
BuildRequires:		perl(ExtUtils::Embed)
BuildRequires:		pciutils-devel
BuildRequires:		asciidoc
BuildRequires:		xmlto
BuildRequires:		gettext
BuildRequires:		docbook-style-xsl
BuildRequires:		pkgconfig(gtk+-2.0)
BuildRequires:		flex
BuildRequires:		bison

%ifarch %{arm}
BuildRequires:		uboot-mkimage
%endif


3.8.1 mga -done- (partial not kmod version)
==========
BuildRequires: 		gcc kmod >= 7-7
# for cpupower
%if %{build_cpupower}
BuildRequires:		pciutils-devel
%endif
# for perf
%if %{build_perf}
BuildRequires:		audit-devel
BuildRequires:		binutils-devel
BuildRequires:		elfutils-devel
BuildRequires:		gtk2-devel
BuildRequires:		libunwind-devel
BuildRequires:		newt-devel
BuildRequires:		python-devel
BuildRequires:		zlib-devel
BuildRequires:		asciidoc
BuildRequires:		bison
BuildRequires:		flex
BuildRequires:		xmlto
%endif
%ifarch %{arm}
BuildRequires:		uboot-mkimage
%endif



3.7.1
==========
Provides:	%kprovides				\

3.8.1 -done-
==========
Provides:	%kprovides1 %kprovides2 %kprovides3	\



3.7.1
==========
Obsoletes:	%kobsoletes				\

3.8.1 -done-
==========
Obsoletes:	%kobsoletes1 %kobsoletes2 %kobsoletes3	\
Conflicts:	%kconflicts1 %kconflicts2 %kconflicts3	\
Conflicts:	%kconflicts4 %kconflicts5 %kconflicts6	\



3.7.1
==========
%if %build_debug					\
%package -n	%{kname}-%{1}-%{buildrel}-debug		\
Version:	%{fakever}				\
Release:	%{fakerel}				\
Summary:	Files with debug info for %{kname}-%{1}-%{buildrel} \
Group:		Development/Debug			\
Provides:	kernel-debug = %{kverrel} 		\
%ifarch %{ix86}						\
Conflicts:	arch(x86_64)				\
%endif							\
%description -n %{kname}-%{1}-%{buildrel}-debug		\
This package contains the files with debug info to aid in debug tasks \
when using %{kname}-%{1}-%{buildrel}.			\

3.8.1 -done-
==========
%if %build_debug					\
%package -n	%{kname}-%{1}-%{buildrel}-debuginfo	\
Version:	%{fakever}				\
Release:	%{fakerel}				\
Summary:	Files with debuginfo for %{kname}-%{1}-%{buildrel} \
Group:		Development/Debug			\
Provides:	kernel-debug = %{kverrel} 		\
%ifarch %{ix86}						\
Conflicts:	arch(x86_64)				\
%endif							\
%description -n %{kname}-%{1}-%{buildrel}-debuginfo	\
This package contains the files with debuginfo to aid in debug tasks \
when using %{kname}-%{1}-%{buildrel}.			\



3.7.1
==========
%if %build_debug					\
%files -n %{kname}-%{1}-%{buildrel}-debug -f kernel_debug_files.%{1} \
%endif

3.8.1 -done-
==========
%if %build_debug					\
%files -n %{kname}-%{1}-%{buildrel}-debuginfo -f kernel_debug_files.%{1} \
%endif



3.7.1 (removed all starting from  > %post -n %{kname}-source-%{buildrel})
========== -done-
==================
%description -n %{kname}-source-%{buildrel}
The %{kname}-source package contains the source code files for the Mageia
kernel. Theese source files are only needed if you want to build your
own custom kernel that is better tuned to your particular hardware.

If you only want the files needed to build 3rdparty (nVidia, Ati, dkms-*,...)
drivers against, install the *-devel-* rpm that is matching your kernel.

%post -n %{kname}-source-%{buildrel}
for i in /lib/modules/%{kversion}-{desktop586,desktop,server}-%{buildrpmrel}; do
        if [ -d $i ]; then
		if [ ! -L $i/build -a ! -L $i/source ]; then
			ln -sf /usr/src/linux-%{kversion}-%{buildrpmrel} $i/build
			ln -sf /usr/src/linux-%{kversion}-%{buildrpmrel} $i/source
		fi
        fi
done
cd /usr/src
rm -f linux
ln -snf linux-%{kversion}-%{buildrpmrel} linux

%preun -n %{kname}-source-%{buildrel}
for i in /lib/modules/%{kversion}-{desktop586,desktop,server}-%{buildrpmrel}/{build,source}; do
	if [ -L $i ]; then
		if [ "$(readlink $i)" = "/usr/src/linux-%{kversion}-%{buildrpmrel}" ]; then
			rm -f $i
		fi
	fi
done
if [ -L /usr/src/linux ]; then
	if [ "$(readlink /usr/src/linux)" = "linux-%{kversion}-%{buildrpmrel}" ]; then
		rm -f /usr/src/linux
	fi
fi
exit 0

3.8.1 (removed all starting from  > %post -n %{kname}-source-%{buildrel})
========== -done-
==================
%description -n %{kname}-source-%{buildrel}
The %{kname}-source package contains the source code files for the Mageia
kernel. Theese source files are only needed if you want to build your
own custom kernel that is better tuned to your particular hardware.

If you only want the files needed to build 3rdparty (nVidia, Ati, dkms-*,...)
drivers against, install the *-devel-* rpm that is matching your kernel.



3.7.1 (removed all starting from  > %if %build_source upto > %endif)
========== -done-
%endif
%if %build_source
# create kernel-source symlinks only if matching -devel- rpm is not installed
if [ -d /usr/src/linux-%{kversion}-%{buildrpmrel} -a ! -d /usr/src/linux-%{kversion}-$kernel_flavour-%{buildrpmrel} ]; then
	rm -f /lib/modules/%{kversion}-$kernel_flavour-%{buildrpmrel}/{build,source}
	ln -sf /usr/src/linux-%{kversion}-%{buildrpmrel} /lib/modules/%{kversion}-$kernel_flavour-%{buildrpmrel}/build
	ln -sf /usr/src/linux-%{kversion}-%{buildrpmrel} /lib/modules/%{kversion}-$kernel_flavour-%{buildrpmrel}/source
fi
%endif
EOF

3.8.1 (removed all starting from  > %if %build_source upto > %endif)
========== -done-
%endif
EOF



3.7.1 
==========
%make -C tools/perf -s V=1 HAVE_CPLUS_DEMANGLE=1 prefix=%{_prefix} all
%make -C tools/perf -s V=1 prefix=%{_prefix} man

3.8.1 -done
==========
%make -C tools/perf -s HAVE_CPLUS_DEMANGLE=1 prefix=%{_prefix} all
%make -C tools/perf -s prefix=%{_prefix} man





3.8.1 
==========
%changelog

* Sat Mar 02 2013 tmb <tmb> 3.8.1-1.mga3
+ Revision: 401081
- drm/i915: Fix Haswell/CRW PCI IDs
- update to 3.8.2-rc1
- drop merged patches

* Thu Feb 28 2013 tmb <tmb> 3.8.0-3.mga3
+ Revision: 400575
- sync up with current -stable queue (154 additional fixes all over)
- require fixed dracut

* Fri Feb 22 2013 tmb <tmb> 3.8.0-2.mga3
+ Revision: 399983
- disable 'mac80211: improve latency and throughput while software scanning' for now
- perf hists: Fix period symbol_conf.field_sep display
- perf tools: Fix build with bison 2.3 and older
- x86-32, mm: Remove reference to alloc_remap()
- x86-32, mm: Remove reference to resume_map_numa_kva()
- x86-32, mm: Rip out x86_32 NUMA remapping code
- x86, efi: Make noefi really disable EFI runtime serivces
- btrfs: access superblock via pagecache in scan_one_device
- btrfs: fix crash in log replay with qgroups enabled
- update ndiswrapper to 1.58

* Tue Feb 19 2013 tmb <tmb> 3.8.0-1.mga3
+ Revision: 399296
- update to 3.8 final
- drop merged patches
- add Intel Wellsburg PCH support to ahci, ata_piix, i2c, lpc, sound

* Fri Feb 08 2013 tmb <tmb> 3.8.0-0.rc7.1.mga3
+ Revision: 397185
- r8169: revert: 'enable ALDPS for power saving' as it breaks some hw (#8622)
- r8169: revert: 'enable internal ASPM and clock request settings' as it
  increases boot time
- update to 3.8-rc7

* Fri Feb 08 2013 tmb <tmb> 3.8.0-0.rc6.2.mga3
+ Revision: 397028
- drm/ttm: fix fence locking in ttm_buffer_object_transfer
- mac80211: improve latency and throughput while software scanning
- brcmsmac: double time for timeout
- ath9k: fix DMA idle but MAC is still stuck processing events
- rtlwifi: fix scheduling while atomic bug
- add support for Cypress PS2 Trackpads
- update to rc6-git as of: Wed Feb 6 12:11:10 2013 -0500

* Wed Feb 06 2013 tmb <tmb> 3.8.0-0.rc6.1.mga3
+ Revision: 394927
- disable perf build as it breaks on BS
- add more updates from upstream git
- add support for booting without initrd
  * https://wiki.mageia.org/en/Feature:BootSansRamdisk
  * works on ahci controllers, with ext4 and btrfs filesystems
  * theese options are now builtin: CONFIG_SCSI_MOD, CONFIG_SCSI,
    CONFIG_BLK_DEV_SD, CONFIG_ATA, CONFIG_SATA_AHCI, CONFIG_EXT4_FS,
    CONFIG_JBD2, CONFIG_BTRFS_FS, CONFIG_CRYPTO_CRC32C, CONFIG_CRC16,
    CONFIG_CRC_T10DIF, CONFIG_LIBCRC32C, CONFIG_ZLIB_DEFLATE
- update to 3.8-rc6-git
- fix perf build

* Sun Jan 27 2013 tmb <tmb> 3.8.0-0.rc5.1.mga3
+ Revision: 392632
- update to 3.8-rc5

* Fri Jan 18 2013 tmb <tmb> 3.8.0-0.rc4.1.mga3
+ Revision: 389476
- update to 3.8-rc4

* Wed Jan 16 2013 tmb <tmb> 3.8.0-0.rc3.2.mga3
+ Revision: 388788
- iwlwifi: audit single frames from AGG queue in RS
- drop __devinit/exit from heci, ndiswrapper, alx, shuttle-wmi
- update to 3.8-rc3-git as of 2013-01-16
- drop build, source symlinking of source package to kernel tree as it
  makes dkms build unusable modules
- rename -debug packages to -debuginfo
- specfile cleanups
- add more dkms conflicts
- conflict dkms packages that does not support kernel-3.8 to help upgrade ordering

* Thu Jan 10 2013 tmb <tmb> 3.8.0-0.rc3.1.mga3
+ Revision: 344645
- disable broken perf build for now
- update defconfigs
- rediff patches to apply cleanly
- drop merged zram patches
- update to 3.8-rc3
- update to 3.8-rc2-git as of 2013-01-04



%changelog
- update defconfigs
- rediff patches to apply cleanly
- specfile cleanups
- add more dkms conflicts
- conflict dkms packages that does not support kernel-3.8 to help upgrade ordering
- rename -debug packages to -debuginfo
- drop build, source symlinking of source package to kernel tree as it
  makes dkms build unusable modules
- iwlwifi: audit single frames from AGG queue in RS
- drop __devinit/exit from heci, ndiswrapper, alx, shuttle-wmi

- add support for booting without initrd
  * https://wiki.mageia.org/en/Feature:BootSansRamdisk
  * works on ahci controllers, with ext4 and btrfs filesystems
  * theese options are now builtin: CONFIG_SCSI_MOD, CONFIG_SCSI,
    CONFIG_BLK_DEV_SD, CONFIG_ATA, CONFIG_SATA_AHCI, CONFIG_EXT4_FS,
    CONFIG_JBD2, CONFIG_BTRFS_FS, CONFIG_CRYPTO_CRC32C, CONFIG_CRC16,
    CONFIG_CRC_T10DIF, CONFIG_LIBCRC32C, CONFIG_ZLIB_DEFLATE

- drm/ttm: fix fence locking in ttm_buffer_object_transfer
- mac80211: improve latency and throughput while software scanning
- brcmsmac: double time for timeout
- ath9k: fix DMA idle but MAC is still stuck processing events
- rtlwifi: fix scheduling while atomic bug
- add support for Cypress PS2 Trackpads

- r8169: revert: 'enable ALDPS for power saving' as it breaks some hw (#8622)
- r8169: revert: 'enable internal ASPM and clock request settings' as it
  increases boot time

- add Intel Wellsburg PCH support to ahci, ata_piix, i2c, lpc, sound

- disable 'mac80211: improve latency and throughput while software scanning' for now
- perf hists: Fix period symbol_conf.field_sep display
- perf tools: Fix build with bison 2.3 and older
- x86-32, mm: Remove reference to alloc_remap()
- x86-32, mm: Remove reference to resume_map_numa_kva()
- x86-32, mm: Rip out x86_32 NUMA remapping code
- x86, efi: Make noefi really disable EFI runtime services
- btrfs: access superblock via pagecache in scan_one_device
- btrfs: fix crash in log replay with qgroups enabled
- update ndiswrapper to 1.58

- require fixed dracut

- drm/i915: Fix Haswell/CRW PCI IDs



========================================================
Files: from ROSA to OpenMandriva changes
/kernel.spec
========================================================

%changelog
* Fri Feb 08 2013 Per Øyvind Karlsen peroyvind@mandriva.org> 3.7.6-70
- use %%{disttag} rather than dead %%{distsuffix}
- disable default --build-id=sha1 implictly set by linker, for places
  otherwise in build which actually do use --build-id, it will be passed
  later and reenable it without problems

%if %{mdvver} <= 201100
%define distsuffix mib
Vendor: MIB - Mandriva International Backports
%endif

%define rpmtag		%{distsuffix}


%{disttag} replace %{rpmtag}


> from which distro disttag is present to replace distsuffix?
> - mdv2010.2
$ rpm --eval %disttag
%disttag
> - mdv2011.0
$ rpm --eval %disttag
mdv
> - rosa2012.1
$ rpm --eval %disttag
rosa

So I guess you can add something like this to spec:

%if %{mdvver} < 201100
%define disttag %{distsuffix}
%endif



3.7 rosa
======================
%define kmake %make CC="$CC"
%else
%define kmake %make
%endif
# there are places where parallel make don't work
%define smake make


3.7 OpenMandriva
=====================
%define kmake %make CC="$CC" LD="$LD" LDFLAGS="$LDFLAGS"
%else
%define kmake %make LD="$LD" LDFLAGS="$LDFLAGS"
%endif
# there are places where parallel make don't work
%define smake make LD="$LD" LDFLAGS="$LDFLAGS"


3.7 ROSA
=====================
%if %{mdvver} >= 201210
%define requires1	bootloader-utils >= 1.15-8
%define requires2	dracut >= 017-16
%define requires3	kmod >= 7-6
%define requires4	sysfsutils >=  2.1.0-12
%define requires5	kernel-firmware >=  20120219-1
%endif

3.7 OpenMandriva -done-
=====================
%define requires2   dracut >= 017-16
%define requires3   kmod >= 7-6
%define requires4   sysfsutils >=  2.1.0-12
%define requires5   kernel-firmware >=  20120219-1
%define requires6   microcode


3.7 ROSA
=====================
%{expand:%%{?kprovides_%{1}:Provides: %{kprovides_%{1}}}} \
Provides:	%{kname}-%{1}				\
Requires(pre):	%requires1 %requires2 %requires3 %requires4 \

3.7 OpenMandriva -done- (for nrj_desktop & nrjQL_desktop)
=====================
%{expand:%%{?kprovides_%{1}:Provides: %{kprovides_%{1}}}} \
Provides:   %{kname}-%{1}               \
%if %{build_nrjQL_desktop}              \
Provides:   kernel-desktop              \
%endif                                  \
Requires(pre):  %requires2 %requires3 %requires4 \


3.7 ROSA
=====================
%if %{mdvver} >= 201200
Obsoletes:	cpufreq cpufrequtils
%endif

3.7 OpenMandriva -done-
=====================
Obsoletes:  cpufreq cpufrequtils




3.7 ROSA
=====================
%build
# Common target directories

3.7 OpenMandriva
=====================
%build
# Make sure we don't use gold
export LD="%{_target_platform}-ld.bfd"
export LDFLAGS="--hash-style=sysv --build-id=none"

# Common target directories




3.7 ROSA
=====================
# perf
%make -C tools/perf -s V=1 HAVE_CPLUS_DEMANGLE=1 prefix=%{_prefix} all
%make -C tools/perf -s V=1 prefix=%{_prefix} man
%endif

%if %{build_cpupower}
# cpupower
# make sure version-gen.sh is executable.
chmod +x tools/power/cpupower/utils/version-gen.sh
%make -C tools/power/cpupower CPUFREQ_BENCH=false
%endif

3.7 OpenMandriva
=====================
# perf
%make -C tools/perf -s V=1 HAVE_CPLUS_DEMANGLE=1 prefix=%{_prefix} LDFLAGS="%optflags" all
%make -C tools/perf -s V=1 prefix=%{_prefix} LDFLAGS="%optflags" man
%endif

%if %{build_cpupower}
# cpupower
# make sure version-gen.sh is executable.
chmod +x tools/power/cpupower/utils/version-gen.sh
%kmake -C tools/power/cpupower CPUFREQ_BENCH=false LDFLAGS="%optflags"
%endif


3.7 ROSA
=====================
%if %{build_cpupower}
make -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false install

3.7 OpenMandriva
=====================
%if %{build_cpupower}
%make -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false LDFLAGS="%optflags" install




3.7 ROSA
=====================
%description -n cpupower-devel
This package contains the development files for cpupower.
%endif

#
# End packages - here begins build stage
#

3.7 OpenMandriva (add kernel-headers)
=====================
%description -n cpupower-devel
This package contains the development files for cpupower.
%endif

%package headers
Version:    %kversion
Release:    %rpmrel
Summary:    Linux kernel header files mostly used by your C library
Group:      System/Kernel and hardware
Epoch:      1
%rename linux-userspace-headers

%description headers
C header files from the Linux kernel. The header files define
structures and constants that are needed for building most
standard programs, notably the C library.

This package is not suitable for building kernel modules, you
should use the 'kernel-devel' package instead.

%files headers
%_includedir/*
# Don't conflict with cpupower-devel
%exclude %_includedir/cpufreq.h

#
# End packages - here begins build stage
#



3.7 ROSA
=====================
# modules
    install -d %{temp_modules}/$KernelVer
    %smake INSTALL_MOD_PATH=%{temp_root} KERNELRELEASE=$KernelVer modules_install

    # remove /lib/firmware, we use a separate kernel-firmware
    rm -rf %{temp_root}/lib/firmware

3.7 OpenMandriva (add kernel-headers)
=====================
# modules
    install -d %{temp_modules}/$KernelVer
    %smake INSTALL_MOD_PATH=%{temp_root} KERNELRELEASE=$KernelVer modules_install

    # headers
    %make INSTALL_HDR_PATH=%{temp_root}%_includedir KERNELRELEASE=$KernelVer headers_install

    # remove /lib/firmware, we use a separate kernel-firmware
    rm -rf %{temp_root}/lib/firmware




new commit
https://abf.rosalinux.ru/openmandriva/kernel/commit/b832c4b195cf325844005ca6799423a29f54f8f6

	# headers
	%make INSTALL_HDR_PATH=%{temp_root}%_includedir KERNELRELEASE=$KernelVer headers_install
	%make INSTALL_HDR_PATH=%{temp_root}%_prefix KERNELRELEASE=$KernelVer headers_install


new commit
https://abf.rosalinux.ru/openmandriva/kernel/commit/32d3796b8b3cfa514b0216068661d7c7793a7279


### This is for full SRC RPM
Source0: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/linux-%{tar_ver}.tar.xz
Source1: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/linux-%{tar_ver}.tar.sign

Source0: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/linux-%{tar_ver}.tar.xz
Source1: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/linux-%{tar_ver}.tar.sign


	
%if %kpatch
%if %sublevel
Patch2:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/stable-review/patch-%{kversion}-%{kpatch}.bz2
Source11:	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/stable-review/patch-%{kversion}-%{kpatch}.sign
	
Patch2:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/stable-review/patch-%{kversion}-%{kpatch}.bz2
Source11:	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/stable-review/patch-%{kversion}-%{kpatch}.sign
%else
Patch1:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/testing/patch-%{kernelversion}.%{patchlevel}-%{kpatch}.bz2
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/testing/patch-%{kernelversion}.%{patchlevel}-%{kpatch}.sign
	
Patch1:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/testing/patch-%{kernelversion}.%{patchlevel}-%{kpatch}.bz2
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/testing/patch-%{kernelversion}.%{patchlevel}-%{kpatch}.sign	
%endif	
%endif
%if %kgit
Patch2:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/snapshots/patch-%{kernelversion}.%{patchlevel}-%{kpatch}-git%{kgit}.bz2
Source11: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/snapshots/patch-%{kernelversion}.%{patchlevel}-%{kpatch}-git%{kgit}.sign
	
Patch2:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/snapshots/patch-%{kernelversion}.%{patchlevel}-%{kpatch}-git%{kgit}.bz2
Source11: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/snapshots/patch-%{kernelversion}.%{patchlevel}-%{kpatch}-git%{kgit}.sign
%endif
%if %sublevel
%if %kpatch
%define prev_sublevel %(expr %{sublevel} - 1)
%if %prev_sublevel
Patch1:   	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/patch-%{kernelversion}.%{patchlevel}.%{prev_sublevel}.bz2		
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/patch-%{kernelversion}.%{patchlevel}.%{prev_sublevel}.sign

Patch1:   	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/patch-%{kernelversion}.%{patchlevel}.%{prev_sublevel}.bz2
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/patch-%{kernelversion}.%{patchlevel}.%{prev_sublevel}.sign
%endif
%else
Patch1:   	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/patch-%{kversion}.bz2
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.%{patchlevel}/patch-%{kversion}.sign
	
Patch1:   	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/patch-%{kversion}.bz2
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/patch-%{kversion}.sign
%endif
%endif

then

%if %kpatch
%if %sublevel
Patch2:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/stable-review/patch-%{kversion}-%{kpatch}.bz2
Source11:	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/stable-review/patch-%{kversion}-%{kpatch}.sign
%else
Patch1:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/testing/patch-%{kernelversion}.%{patchlevel}-%{kpatch}.bz2
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/testing/patch-%{kernelversion}.%{patchlevel}-%{kpatch}.sign	
%endif	
%endif
%if %kgit
Patch2:		ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/snapshots/patch-%{kernelversion}.%{patchlevel}-%{kpatch}-git%{kgit}.bz2
Source11: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/snapshots/patch-%{kernelversion}.%{patchlevel}-%{kpatch}-git%{kgit}.sign
%endif
%if %sublevel
%if %kpatch
%define prev_sublevel %(expr %{sublevel} - 1)
%if %prev_sublevel
Patch1:   	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/patch-%{kernelversion}.%{patchlevel}.%{prev_sublevel}.bz2
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/patch-%{kernelversion}.%{patchlevel}.%{prev_sublevel}.sign
%endif
%else
Patch1:   	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/patch-%{kversion}.bz2
Source10: 	ftp://ftp.kernel.org/pub/linux/kernel/v%{kernelversion}.x/patch-%{kversion}.sign
%endif
%endif



3.12
=========================
* TPM Hardware Support
*
TPM Hardware Support (TCG_TPM) [M/n/y/?] m
  TPM Interface Specification 1.2 Interface (TCG_TIS) [M/n/?] m
  TPM Interface Specification 1.2 Interface (I2C - Infineon) (TCG_TIS_I2C_INFINEON) [M/n/?] m
  National Semiconductor TPM Interface (TCG_NSC) [M/n/?] m
  Atmel TPM Interface (TCG_ATMEL) [M/n/?] m
  Infineon Technologies TPM Interface (TCG_INFINEON) [M/n/?] m
  STMicroelectronics ST33 I2C TPM (TCG_ST33_I2C) [M/n/?] m
  XEN TPM Interface (TCG_XEN) [N/m/?] (NEW) n

  DRBD Distributed Replicated Block Device support (BLK_DEV_DRBD) [M/n/y/?] m
    DRBD fault injection (DRBD_FAULT_INJECTION) [N/y/?] (NEW) 



HOSTLD  scripts/kconfig/conf
pushd /home/utente/rpmbuild/BUILD/kernel-x86_64/linux-3.12/3rdparty ; perl ./mkbuild.pl ; popd
~/rpmbuild/BUILD/kernel-x86_64/linux-3.12/3rdparty ~/rpmbuild/BUILD/kernel-x86_64/linux-3.12
~/rpmbuild/BUILD/kernel-x86_64/linux-3.12
scripts/kconfig/conf --oldconfig Kconfig
#
# configuration written to .config
#
scripts/kconfig/conf --oldconfig Kconfig
#
# configuration written to .config
#
scripts/kconfig/conf --oldconfig Kconfig
#
# configuration written to .config
#
scripts/kconfig/conf --oldconfig Kconfig
*
* Restart config...
*
*
* TPM Hardware Support
*
TPM Hardware Support (TCG_TPM) [M/n/y/?] m
  TPM Interface Specification 1.2 Interface (TCG_TIS) [M/n/?] m
  TPM Interface Specification 1.2 Interface (I2C - Infineon) (TCG_TIS_I2C_INFINEON) [M/n/?] m
  National Semiconductor TPM Interface (TCG_NSC) [M/n/?] m
  Atmel TPM Interface (TCG_ATMEL) [M/n/?] m
  Infineon Technologies TPM Interface (TCG_INFINEON) [M/n/?] m
  STMicroelectronics ST33 I2C TPM (TCG_ST33_I2C) [M/n/?] m
  XEN TPM Interface (TCG_XEN) [N/m/?] (NEW) 

defconfig-server
we should add >
CONFIG_TCG_XEN=m




when is making ARM configs, there are some warnings
===========================================================

scripts/kconfig/conf --oldconfig Kconfig
#
# configuration written to .config
#
scripts/kconfig/conf --oldconfig Kconfig
.config:5136:warning: override: reassigning to symbol FRAMEBUFFER_CONSOLE
.config:5139:warning: override: reassigning to symbol EFI_PARTITION
#
# configuration written to .config
#
scripts/kconfig/conf --oldconfig Kconfig
.config:5167:warning: override: reassigning to symbol FRAMEBUFFER_CONSOLE
.config:5170:warning: override: reassigning to symbol EFI_PARTITION
#
# configuration written to .config
#
scripts/kconfig/conf --oldconfig Kconfig
.config:5145:warning: override: reassigning to symbol FRAMEBUFFER_CONSOLE
.config:5148:warning: override: reassigning to symbol EFI_PARTITION
#




