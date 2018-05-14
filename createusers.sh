#1/bin/sh
for i in `more /home/revoscaler/Source/pycondemos/userlist.txt`
do
b="/home/"
basepass="magickey"
c=$b$i
p=$i$basepass
echo $c
echo $i
echo $p
sudo useradd -d $c -m -p $(echo "$p" | openssl passwd -1 -stdin) $i
done
