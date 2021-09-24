# Compiling Code  

## C  
### Static 32bit  
`gcc -m32 --static -o <OUTPUT> <INPUT>`  
### Dynamic 32bit  
`gcc -m32 -o <OUTPUT> <INPUT>`  

### Cross compiling
  
```
# install minigw compiler
# sudo apt install gcc-mingw-w64

# compiling

32 bit
$ i686-w64-mingw32-gcc input.c ouput32.exe

64 bit
$ x86_64-w64-mingw32-gcc input.c output32.exe
```
