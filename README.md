To install dependencies:

```
sudo easy_install pip
pip install -r requirements.txt
```

Example data capture/processing pipeline is split into separate files...

```
python downloader.py
python bwer.py
```

May eventually make into more bona-fide standalone shell scripts
with nice command line args...
