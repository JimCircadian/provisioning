#version=DEVEL
# Use graphical install
text

# Keyboard layouts
keyboard --xlayouts='gb'
# System language
lang en_GB.UTF-8

# Network information
network  --hostname=TODO

# Use CDROM installation media
cdrom

%packages
@^server-product-environment

%end

# Run the Setup Agent on first boot
firstboot --enable

ignoredisk --only-use=sda
part /boot --fstype="xfs" --ondisk=sda --size=1024
part pv.1 --fstype="lvmpv" --ondisk=sda --size=65535 --encrypted --luks-version=luks2
volgroup fedora2 --pesize=4096 pv.1
logvol /home --fstype="xfs" --size=1 --grow --name=home2 --vgname=fedora2
logvol / --fstype="xfs" --size=32768 --name=root2 --vgname=fedora2

timesource --ntp-disable
# System timezone
timezone Europe/London --utc

# Root password
rootpw --iscrypted TODO
user --groups=wheel --name=TODO --password=TODO --iscrypted --uid=TODO --gecom="TODO" --gid=TODO

