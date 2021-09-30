
## Tools to install
[penelope shell handler](https://github.com/brightio/penelope)  
rlwrap  
docker  
gcc-mingw-w64  
WinPeas 
LinPeas  
xrdp  
foxyproxy  
[psspy](https://github.com/DominicBreuker/pspy)  

```
sudo apt update
sudo apt install rlwrap docker.io mingw-w64 virtualenv xrdp
git clone https://github.com/brightio/penelope.git
```

## Configuring python virtual environment
```
# install virtual environment
sudo apt install virtualenv

## starting environment

# for python 3
virtualenv -p /path/to/python3/bin <path to new environment>

# for python 2
virtualenv -p /path/to/python2/bin <path to new environment>

source <path to new environment>/bin/activate

## exit environment
deactivate
```

## Installing Pip for Python 2
```
sudo apt update
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
```
