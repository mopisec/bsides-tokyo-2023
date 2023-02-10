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

## IoC

### 講演で解析したMSIパッケージファイルのSHA256ハッシュ値

```
8cc8f32b2f44e84325e5153ec4fd60c31a35884220e7c36b753550356d6a25c8
```

### 抽出したDLLファイル (`5.dll`) のSHA256ハッシュ値

```
0150eb84d16f0330b2952c9c722fbf55e47d9697b27de9335de6113556e9b317
```
