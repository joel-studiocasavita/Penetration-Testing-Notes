
## Tools to install
[penelope shell handler](https://github.com/brightio/penelope)  
rlwrap  
docker

## Configuring python virtual environment
```
# install virtual environment
sudo apt install virtualenv

## starting environment

# for python 3
virtualenv <path to new environment> -b /path/to/python3/bin

# for python 2
virtualenv <path to new envivronment> -b /path/to/python2/bin

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
