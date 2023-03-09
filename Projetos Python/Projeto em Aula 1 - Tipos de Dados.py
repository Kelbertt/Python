Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10
10
>>> type(10)
<class 'int'>
>>> type('tudo bem')
<class 'str'>
>>> 
>>> 
>>> 5/2
2.5
>>> type(5/2)
<class 'float'>
>>> 
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 10%3
1
>>> 
>>> peso = 78
>>> altura = 1.8
>>> 
>>> peso
78
>>> altura
1.8
>>> type(altura)
<class 'float'>
>>> type(peso)
<class 'int'>
>>> 
>>> IMC = Peso / (altura **2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    IMC = Peso / (altura **2)
NameError: name 'Peso' is not defined
>>> IMC = peso / (altura **2)
>>> IMC
24.074074074074073
>>> 
>>> 
>>> 
>>> IMCINTEIRO = int(IMC)
>>> IMCINTEIRO
24
>>> 
>>> 
>>> 
>>> texto = "Bom dia, Tudo bem?"
>>> 
>>> len(texto)
18
>>> 