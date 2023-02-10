# Investigation and analysis of malware spreading via MSI package files

[日本語のREADMEはこちらから確認することができます。](./README.md)

## malicious_vbscript.zip

ZIP file containing malicious VBScript (`malicious_vbscript.txt`) extracted from the sample.  
Password is `infected`.

## deobfuscate_vbscript.py

Python script that deobfuscates `malicious_vbscript.txt`.

```
$ python3 ./deobfuscate_vbscript.py ./malicious_vbscript.txt
```
