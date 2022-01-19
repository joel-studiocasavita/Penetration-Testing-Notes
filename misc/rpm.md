## Extracting RPM files

```
# install the cpio and rpm2cpio packages
sudo apt install cpio rpm2cpio

# extract all files from the rpm.
rpm2cpio <rpm file> | cpio -idmv
```
