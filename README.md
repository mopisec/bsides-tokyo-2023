# MSIパッケージファイルを介して感染を広げるマルウェアの調査および解析

## malicious_vbscript.zip

解析した検体から取得したVBScript（`malicious_vbscript.txt`）を含んだZIPファイル。  
パスワード: `infected`

## deobf_msi_vbscript.py

`malicious_vbscript.txt` に施された難読化を解除するPythonスクリプト。

```
$ python3 ./deobf_msi_vbscript.py ./malicious_vbscript.txt
```
