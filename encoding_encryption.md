# Encoding / Cipher Examples  

#### Base64 
```
VGhlIFF1aWNrIEJyb3duIEZveCBKdW1wcyBPdmVyIFRoZSBMYXp5IERvZw==
```
###### Decoder  

`echo HASH | base64 -d`  

---

#### Json Web Token
`eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiRm94IiwiSXNzdWVyIjoidGhlIEludGVybmV0IiwiVXNlcm5hbWUiOiJUaGUgcXVpY2sgYnJvd24gRm94IiwiZXhwIjo0MDk2ODMyNzM0LCJpYXQiOjE2MzUzODMxMzR9.QfRSWM8HUepboAp4FmC4s3kThG8ATnB73b4HkY2w9Xg`

All json web tokens have the 'ey' prefix.

###### Decoder 
https://token.dev/

---


#### XOR Cipher (key based) 
```Zfk._{gme.L|ay`.Hav.D{c~}.Axk|.Zfk.Botw.Jai```
###### Brute forcing an xor cipher  
https://www.dcode.fr/xor-cipher

---


#### Vigenere Cipher (key based)
`Dlc Aygmo Zbsux Jmh Nswtq Yzcb Xfo Pyjc Byk`
###### Brute forcing a Vigenere key
https://www.dcode.fr/vigenere-cipher

#### AES Encryption  

`2Fno5Z9DMX1FlvoAC6utBL+Qk5sLMm8Zxrxrhs7datmcLES2F1dLZb9bwbOWfZO9`  

Base64 values that do not decode to strings may be AES encrypted strings.  
 
##### Padding Oracle Attack  

AES strings encrypted using Cipher Block Chaining (CBC) are vulnerable to decryption if the website provides different messages depending on whether the cipher padding is good or bad.  For example, sending a server request with a cookie containing an encrypted authentication string would result in an HTTP 200 code.  However, sending a server request after adding or removing values on the cookie string will result in an HTTP 500 or some other code/error message. 

`padbuster URL ENCODED TEXT BIT SIZE -cookies COOKIE VALUES -encoding ENCODING TYPE` 

Additional Information: https://pentesterlab.com/exercises/padding_oracle/course

