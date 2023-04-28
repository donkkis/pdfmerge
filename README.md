# Dead simple PDF merging

I was annoyed by the lack of a dead-simple pdf merge tool and/or the hoops I'd need to jump through to install one on my corporate laptop. So I decided to make one that just works!

## Building the tool on linux

Just ```pip install -r requirements.txt``` followed by ```pyinstaller src/merge.py```. The executable
```merge``` will then appear under ```dist/merge```. Throw that into a directory which is on your ```PATH```
and you'll have system-wide pdf merging readily available where ever the need might arise!
