DISCRIPTION:
------
A data scraber of fetcher using --youtube data api v3--.<br>
It can be served for extracting data about youtube videos and channels also.<br>
You can use it as a backend code, of a web site that shows details about videos channels and soo.<br>
In my case, I used it for statistical reasons in data science.<br>

PLEASE BE FREE AND WELCOMED TO CONTRIBUTE.<br>
ALLAH Y3AWNEK. ;) ;)

THE HIRARCHY:
-------
```
    Yfetch/
├── README.md
├── config.py
├── mainlib.py
├── managedata.py
├── __init__.py
├── items
│   ├── channel.py
│   ├── video.py
│   └── __init__.py
└── test
    ├── test.py
    ├── videoData.txt
    ├── output.py
    ├── samples.txt
    └── __init__.py
```
    
HOW TO READ THE SOURCE CODE:
---------------
1. config.py
2. managedata
3. items.channel
4. items.video
5. mainlib
6. fitch into the test file,
   >output.py, samples :: are just data that you can use to understand why.
   execute test.py for seeing how does the code works.


TOOLS:
---
* Language
	* Python
*  Version
	* 3.5
* Libraries
	* requets
	* json
	* urllib

DO NOT FORGET:
-------
* GET YOUR OWN API KEY :: Youtube Data API V3.
* CONFIGURE THE DIRECTORY WHERE YOU WANT TO STORE THE DATA.


HOW TO GET AN API KEY:
----------
* [Tutorial En](https://www.youtube.com/watch?v=pP4zvduVAqo)

AUTHOR:
----
* HERHAR Fares
* DZ, Algeria
* https://github.com/HerharFares
