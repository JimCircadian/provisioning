text

# Keyboard layouts
keyboard --xlayouts='gb'
# System language
lang en_GB.UTF-8

url --mirrorlist https://mirrors.fedoraproject.org/mirrorlist?repo=fedora-34&arch=x86_64

# Network information
network  --hostname=TODO

# Run the Setup Agent on first boot
firstboot --enable

ignoredisk --only-use=sda
clearpart --none --initlabel
part /boot --fstype="xfs" --ondisk=sda --size=1024
part pv.272 --fstype="lvmpv" --ondisk=sda --size=163850 --encrypted --luks-version=luks2
part biosboot --fstype="biosboot" --ondisk=sda --size=1
volgroup fedora --pesize=4096 pv.272
logvol /home --fstype="xfs" --size=102400 --name=home --vgname=fedora
logvol / --fstype="xfs" --size=61440 --name=root --vgname=fedora

timesource --ntp-disable
# System timezone
timezone Europe/London --utc

# Root password
rootpw --iscrypted TODO
user --groups=wheel --name=TODO --password=TODO --iscrypted --uid=TODO --gecos="TODO" --gid=TODO

%packages --retries 5 --timeout 20
@core
@^server-product-environment
libvirt
qemu-kvm
qemu-img
virt-manager
%end

firewall --enabled --ssh
services --enabled libvirtd

%post

%end

reboot
