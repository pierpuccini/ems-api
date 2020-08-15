---
description: How to install Ems-api and Ems-ui onto your windows machine
---

# Installation & Usage

## View Properly at

[https://pierpuccini.gitbook.io/ems-api/](https://pierpuccini.gitbook.io/ems-api/)

## Pre requisites & Installation for Ems-api 

#### Ems-api

> Note: DigSilents Powerfactory can **only** be run on a Windows machine. If you happen to be on a Unix based system, there are various virtualization tools in order to get windows setup. In the Help section you'll find some helpful tips with debugging on your unix machine while running the service in Windows.

* Windows 10
* DigSilent 15.1.7 _This can be checked by in the menu bar going to Help&gt;About PowerFactory... And at the top you'll find the PowerFactory version._
* Python 3.3.2 _This can be checked this by running_ `python` _in your terminal._ 
  * if you don't have this version installed, you can get it from your:
    * **INSTALLATION\_DIRECTORY**\DIgSILENT\PowerFactory 15.1\python\python-3.3.2
    * Directly from python.org: [https://www.python.org/ftp/python/3.3.2/python-3.3.2.msi](https://www.python.org/ftp/python/3.3.2/python-3.3.2.msi)
* Pip and setuptools **Note:** Since python 3.3.2 is no longer suported, Pip and setuptools can no longer be downloaded by tradicional methods _e.g._ get-pip.py. In order to get pip and setup tools, please follow the steps from: [https://stackoverflow.com/questions/56798617/how-to-install-pip-for-python-3-3-on-windows](https://stackoverflow.com/questions/56798617/how-to-install-pip-for-python-3-3-on-windows)
* For Flask and dependencies run:

```
pip install Flask Flask-Jsonpify Flask-RESTful
```

{% hint style="warning" %}
If your **INSTALLATION\_DIRECTORY** for PowerFactory is different than **C:\Program Files \(x86\)** please correct that path in _resources&gt;powerfactory.py_ on line 7.
{% endhint %}

## Run the app

In order to run the app, navigate via CMD to its installation directory and do the following

```bash
venv\Scripts\activate
set FLASK_APP=app.py
flask run
```

Now open up the provided url and port and feel free to use the api at your will.

{% hint style="info" %}
In order to change the host and port add `-h HOST -p PORT`
{% endhint %}





