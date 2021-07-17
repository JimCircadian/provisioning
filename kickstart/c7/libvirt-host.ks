install
cdrom
lang en_GB.UTF-8
keyboard uk
network <<REDACTED>>
rootpw  <<REDACTED>>
firewall --service=ssh
authconfig --enableshadow --passalgo=sha512
selinux --permissive
timezone --utc Europe/London
bootloader --location=mbr --append="crashkernel=auto quiet"

skipx
zerombr
clearpart --all --initlabel


part /boot --fstype xfs --size=1024 --ondisk=sda
part swap --size=4096 --ondisk=sda
part pv.sys --size=131072 --ondisk=sda
part pv.vms --size=1 --grow --ondisk=sdb

volgroup systemVG pv.sys
logvol / --fstype=xfs --name=root --vgname=systemVG  --size=32768
logvol /home --fstype=xfs --name=home --vgname=systemVG --size=8192
logvol /tmp --fstype=xfs --name=tmp --vgname=systemVG  --size=8192
logvol /usr --fstype=xfs --name=usr --vgname=systemVG  --size=16384
logvol /var --fstype=xfs --name=var --vgname=systemVG  --size=8192

volgroup vmsVG pv.vms

repo --name base --baseurl http://mirror.centos.org/centos/7/os/x86_64/
repo --name updates --baseurl http://mirror.centos.org/centos/7/updates/x86_64/
repo --name extras --baseurl http://mirror.centos.org/centos/7/extras/x86_64/

%packages --nobase
@core --nodefaults
-postfix
-sendmail
bind-utils
vim-enhanced
strace
screen

%end

%post
# TODO: Key
yum -y update
reboot
%end
