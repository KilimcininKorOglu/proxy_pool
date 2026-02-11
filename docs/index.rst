.. ProxyPool documentation master file, created by
   sphinx-quickstart on Wed Jul  8 16:13:42 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ProxyPool
=====================================

::

   ****************************************************************
   *** ______  ********************* ______ *********** _  ********
   *** | ___ \_ ******************** | ___ \ ********* | | ********
   *** | |_/ / \__ __   __  _ __   _ | |_/ /___ * ___  | | ********
   *** |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | | ********
   *** | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___  ****
   *** \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____/ ****
   ****                       __ / /                          *****
   ************************* /___ / *******************************
   *************************       ********************************
   ****************************************************************

Python Crawler Proxy IP Pool

Installation
-------------

* Download code

.. code-block:: console

    $ git clone git@github.com:jhao104/proxy_pool.git

* Install dependencies

.. code-block:: console

    $ pip install -r requirements.txt

* Update configuration

.. code-block:: python

   HOST = "0.0.0.0"
   PORT = 5000

   DB_CONN = 'redis://@127.0.0.1:8888'

   PROXY_FETCHER = [
       "freeProxy01",
       "freeProxy02",
       # ....
   ]

* Start project

.. code-block:: console

    $ python proxyPool.py schedule
    $ python proxyPool.py server

Usage
______

* API

============     ========    ================       ==============
Api               Method      Description            Params
============     ========    ================       ==============
/                GET         API introduction        None
/get             GET         Return a proxy          Optional: `?type=https` filter https-supporting proxies
/pop             GET         Return and delete       Optional: `?type=https` filter https-supporting proxies
/all             GET         Return all proxies      Optional: `?type=https` filter https-supporting proxies
/count           GET         Return proxy count      None
/delete          GET         Delete specified proxy  `?proxy=host:ip`
============     ========    ================       ==============


* Crawler

.. code-block:: python

   import requests

   def get_proxy():
       return requests.get("http://127.0.0.1:5010/get?type=https").json()

   def delete_proxy(proxy):
       requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

   # your spider code

   def getHtml():
       # ....
       retry_count = 5
       proxy = get_proxy().get("proxy")
       while retry_count > 0:
           try:
               html = requests.get('https://www.example.com', proxies={"http": "http://{}".format(proxy), "https": "https://{}".format(proxy)})
               # Access using proxy
               return html
           except Exception:
               retry_count -= 1
               # Delete proxy from pool
               delete_proxy(proxy)
       return None

Contents
--------

.. toctree::
   :maxdepth: 2

   user/index
   dev/index
   changelog
