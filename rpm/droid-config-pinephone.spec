# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device pinephone
%define vendor pine

%define vendor_pretty Pine64
%define device_pretty PinePhone

# Community HW adaptations need this
%define community_adaptation 1

# Sailfish OS is considered to-scale, if in app grid you get 4-in-a-row icons
# and 2x2 or 3x3 covers when up-to-4 or 5-or-more apps are open respectively.
# For 4-5.5" device screen sizes of 16:9 ratio, use this formula (hold portrait):
# pixel_ratio = 4.5/DiagonalDisplaySizeInches * HorizontalDisplayResolution/540
# Other screen sizes and ratios will require more trial-and-error.
%define pixel_ratio 1.0

%define native_build 1

%include droid-configs-device/droid-configs.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

#pre-install script to add users and groups that would be create by DHD
#this is temporary until the sailfish-setup package is available
%pre
useradd -rf nfc || :
useradd -rf radio || :
groupadd -rf system || :
usermod -a -G system nemo || :
groupadd -rf media || :
usermod -a -G media nemo || :
exit 0