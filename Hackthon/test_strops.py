'''Microsoft Windows [Version 10.0.26100.3476]
(c) Microsoft Corporation. All rights reserved.

(myenv) C:\Users\265150\Desktop\Python_training>cd myenv

(myenv) C:\Users\265150\Desktop\Python_training\myenv>cd Scripts

(myenv) C:\Users\265150\Desktop\Python_training\myenv\Scripts>activate

(myenv) C:\Users\265150\Desktop\Python_training\myenv\Scripts>cd..

(myenv) C:\Users\265150\Desktop\Python_training\myenv>cd..

(myenv) C:\Users\265150\Desktop\Python_training>cd C:\Users\265150\Desktop\Python_training\hack

(myenv) C:\Users\265150\Desktop\Python_training\hack>pip install .
Processing c:\users\265150\desktop\python_training\hack
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: subhack
  Building wheel for subhack (pyproject.toml) ... done
  Created wheel for subhack: filename=subhack-0.1-py3-none-any.whl size=2226 sha256=307d91617a3a958b7a85651e7f9a34272a3231234082e6e9cfb091cc26cc36ec
  Stored in directory: C:\Users\265150\AppData\Local\Temp\pip-ephem-wheel-cache-tpapqcl4\wheels\8d\c0\3b\aa9d346bb0213323a9fb022dc8f97d622c0e5c6dbb3019dd34
Successfully built subhack
Installing collected packages: subhack
  Attempting uninstall: subhack
    Found existing installation: subhack 0.1
    Uninstalling subhack-0.1:
      Successfully uninstalled subhack-0.1
Successfully installed subhack-0.1

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(myenv) C:\Users\265150\Desktop\Python_training\hack>python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Failed calling sys.__interactivehook__
Traceback (most recent call last):
  File "<frozen site>", line 535, in register_readline
AttributeError: module 'readline' has no attribute 'backend'






>>> import subhack
Enter a word to be searched: mississippi
Enter a substring to be searched in mississippi: ss
2 4
5 7
--------------------------------------------------------------------------------
Enter a word to be reversed: hello
olleh
--------------------------------------------------------------------------------
Enter a sentence with puctuation: Hello! how are you?
Hello how are you
--------------------------------------------------------------------------------
Enter a word to get the count of the word: iam good thank you
4
--------------------------------------------------------------------------------
Enter a sentence to get the count of each character: whats is your name
{'w': 1, 'h': 1, 'a': 2, 't': 1, 's': 2, ' ': 3, 'i': 1, 'y': 1, 'o': 1, 'u': 1, 'r': 1, 'n': 1, 'm': 1, 'e': 1}
--------------------------------------------------------------------------------
Enter a sentence to make it to a title: my name is partha
My Name Is Partha
--------------------------------------------------------------------------------
Enter a sentence to normalize spaces: oh   thats    a    good   name
oh thats a good name
--------------------------------------------------------------------------------
Enter a string for transforming: thank you and whats yours
SRUOY STAHW DNA UOY KNAHT
--------------------------------------------------------------------------------
Enter a string to get the different possible permutations of it: god
['dgo', 'dog', 'gdo', 'god', 'ogd', 'odg']
--------------------------------------------------------------------------------
>>> '''