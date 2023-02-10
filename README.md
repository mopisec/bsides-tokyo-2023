# MSIパッケージファイルを介して感染を広げるマルウェアの調査および解析

[English version of README can be found here.](./README_EN.md)

## malicious_vbscript.zip

解析した検体から抽出したVBScript（`malicious_vbscript.txt`）を含んだZIPファイル。  
パスワード: `infected`

## deobfuscate_vbscript.py

`malicious_vbscript.txt` に施された難読化を解除するPythonスクリプト。

```
$ python3 ./deobfuscate_vbscript.py ./malicious_vbscript.txt
```
