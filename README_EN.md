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

## IoC

### SHA256 hash of analyzed MSI package file

```
8cc8f32b2f44e84325e5153ec4fd60c31a35884220e7c36b753550356d6a25c8
```

### SHA256 hash of extracted DLL file (`5.dll`) 

```
0150eb84d16f0330b2952c9c722fbf55e47d9697b27de9335de6113556e9b317
```
