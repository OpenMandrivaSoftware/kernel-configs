************************************
           Kernel 4.1.3 
************************************

from >>>

4.1.1 orig - (not in ARM)
==========
# CONFIG_HZ_100 is not set
# CONFIG_HZ_250 is not set
# CONFIG_HZ_300 is not set
CONFIG_HZ_1000=y
CONFIG_HZ=1000

to >>>

4.1.1 mod - (not in ARM)
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


from >>>

# CONFIG_TCP_CONG_ADVANCED is not set
CONFIG_TCP_CONG_CUBIC=y
CONFIG_DEFAULT_TCP_CONG="cubic"
# CONFIG_TCP_MD5SIG is not set

to >>>

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
CONFIG_TCP_CONG_DCTCP=m
CONFIG_DEFAULT_CUBIC=y
# CONFIG_DEFAULT_RENO is not set

-

POK requests 
===============================
- suggestions and requests received by Per Øyvind Karlsen (POK)

from
 # CONFIG_PM_AUTOSLEEP is not set
 # CONFIG_PM_WAKELOCKS is not set
to
 CONFIG_PM_AUTOSLEEP=y
 CONFIG_PM_WAKELOCKS=y
 CONFIG_PM_WAKELOCKS_LIMIT=100
 CONFIG_PM_WAKELOCKS_GC=y

from
 # CONFIG_SFI is not set
to
 CONFIG_SFI=y

from
 CONFIG_BLK_DEV_DRBD is not set
to
 CONFIG_BLK_DEV_DRBD=m 
 # CONFIG_DRBD_FAULT_INJECTION is not set

from
 # CONFIG_HW_RANDOM_TIMERIOMEM is not set
to
 CONFIG_HW_RANDOM_TIMERIOMEM=m 

from
 # CONFIG_DRM_VIA is not set
to
 CONFIG_DRM_VIA=m 

from
 # CONFIG_USB_RIO500 is not set
to
 CONFIG_USB_RIO500=m 

from 
 # CONFIG_DRM_VMWGFX_FBCON is not set
to
 CONFIG_DRM_VMWGFX_FBCON=y

from
 CONFIG_SND_PCSP is not set
to
 CONFIG_SND_PCSP=m 

from
 # CONFIG_ACPI_CUSTOM_DSDT is not set
to
 CONFIG_ACPI_CUSTOM_DSDT=y

from
 CONFIG_SATA_SIL=m
to
 CONFIG_SATA_SIL=y


Audio Powersave : 
request not enabled for the reason that in some HW can indroduce noise in audio

 CONFIG_SND_HDA_POWER_SAVE_DEFAULT=10
 CONFIG_SND_AC97_POWER_SAVE_DEFAULT=10

I've tested this for some time, but were reported some issue, audio hicups, ecc.
so, the current config is as DISABLE POWERSAVE

 CONFIG_SND_HDA_POWER_SAVE_DEFAULT=0
 CONFIG_SND_AC97_POWER_SAVE_DEFAULT=0


EDID enable > DONE! (apart ARM whith none CONFIG_DRM_LOAD_EDID_FIRMWARE=y)
===============================
- add 'on request' by Alexander Burmashev: CONFIG_DRM_LOAD_EDID_FIRMWARE=y
  * with this we should be able to override the wrong EDID of displays with options at kernel boot
  * About EDID override howto, you read here:
  * https://www.osadl.org/monitoring/patches/r2s0/drivers-gpu-drm-allow-to-load-edid-firmware.patch

from
 # CONFIG_DRM_LOAD_EDID_FIRMWARE is not set
 # CONFIG_FIRMWARE_EDID is not set
to
 CONFIG_DRM_LOAD_EDID_FIRMWARE=y
 CONFIG_FIRMWARE_EDID=y



ARM create_configs_QL and others configs
.config:102:warning: override: reassigning to symbol GENERIC_CLOCKEVENTS
removed > GENERIC_CLOCKEVENTS

during the configs I saw:
-------------------------
scripts/kconfig/conf  --oldconfig Kconfig
#
# configuration written to .config
#
scripts/kconfig/conf  --oldconfig Kconfig
.config:361:warning: override: ARCH_VERSATILE changes choice state
#
# configuration written to .config
#
scripts/kconfig/conf  --oldconfig Kconfig
.config:102:warning: override: reassigning to symbol GENERIC_CLOCKEVENTS
.config:103:warning: override: reassigning to symbol GENERIC_CLOCKEVENTS
.config:104:warning: override: reassigning to symbol GENERIC_CLOCKEVENTS
.config:105:warning: override: reassigning to symbol GENERIC_CLOCKEVENTS
.config:321:warning: override: ARCH_IOP32X changes choice state
#
# configuration written to .config
#
+ LC_ALL=C

=================================
  if ( $name eq "iop32x" ) {
          $values{GENERIC_TIME} = "n";
        # $values{GENERIC_CLOCKEVENTS} = "n";
          $values{ARCH_IOP32X} = "y";



******************************************
******************************************
OLD STUFF: TO RECHECK (to verify for kernel 4.1.4 time)

1> UEFI keys are all ok?
2> CPU Frequency scaling
3> PAE mode and other fixes from Eugene Shakotin tree
create_configs and cpupower 

******************************************
******************************************

UEFI: Alex Kazancev suggested to verify and adopt the full archilunux configs for UEFI:
https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface#Linux_Kernel_Config_options_for_UEFI

nr. 8 keys to check: DONE!
==========================
1> CONFIG_RELOCATABLE=y
2> CONFIG_EFI=y
3> CONFIG_EFI_STUB=y
4> CONFIG_FB_EFI=y
5> CONFIG_FRAMEBUFFER_CONSOLE=y
6> CONFIG_EFIVAR_FS=y (we have =m, is that right?)
7> CONFIG_EFI_VARS=n (we have =y, is that right?
8> CONFIG_EFI_PARTITION=y
============================



After verifying:
==========================================================
Kernel 3.10.17 & 3.11.6 have the same UEFI keys &  values:
there are differences with ths suggestions from archilinux
we must verify if their suggestions are good also for us
==========================================================

1>
ARM > none
386 > # CONFIG_RELOCATABLE is not set >>> TO BE ASKED to Burma!
x64 > CONFIG_RELOCATABLE=y

2>
ARM > none
386 > CONFIG_EFI=y
x64 > CONFIG_EFI=y

3>
ARM > none
386 > CONFIG_EFI_STUB=y
x64 > CONFIG_EFI_STUB=y

4>
ARM > none
386 > CONFIG_FB_EFI=y
x64 > CONFIG_FB_EFI=y

5>
ARM > CONFIG_FRAMEBUFFER_CONSOLE=y >>> TO BE ASKED to Burma/Fedya!
386 > CONFIG_FRAMEBUFFER_CONSOLE=y
x64 > CONFIG_FRAMEBUFFER_CONSOLE=y

6>
ARM > CONFIG_EFIVAR_FS=m
386 > CONFIG_EFIVAR_FS=m
x64 > CONFIG_EFIVAR_FS=m

7>
CONFIG_EFI_VARS=n, we have different configs, we have this "y", archilinux say to put to "n"
if we dont support > old efivars sysfs interface - /sys/firmware/efi/vars, this can be done
#
# EFI (Extensible Firmware Interface) Support
#
CONFIG_EFI_VARS=y
CONFIG_EFI_VARS_PSTORE=y
CONFIG_EFI_VARS_PSTORE_DEFAULT_DISABLE=y

8>
ARM > CONFIG_EFI_PARTITION=y
386 > CONFIG_EFI_PARTITION=y
x64 > CONFIG_EFI_PARTITION=y >>> TO BE ASKED to Burma/Fedya!



3.xx.1 orig - (not in ARM)
==========
#
# CPU Frequency scaling
#
CONFIG_CPU_FREQ=y
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

3.18.1 mod - (not in ARM) : NOT DONE!
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
CONFIG_CPU_FREQ_GOV_POWERSAVE=m
CONFIG_CPU_FREQ_GOV_USERSPACE=y
CONFIG_CPU_FREQ_GOV_ONDEMAND=y
CONFIG_CPU_FREQ_GOV_CONSERVATIVE=m


