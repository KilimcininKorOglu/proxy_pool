
ProxyPool - Crawler Proxy IP Pool
=======
[![Build Status](https://travis-ci.org/jhao104/proxy_pool.svg?branch=master)](https://travis-ci.org/jhao104/proxy_pool)
[![](https://img.shields.io/badge/Powered%20by-@j_hao104-green.svg)](http://www.spiderpy.cn/blog/)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://github.com/jhao104/proxy_pool/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/jhao104/proxy_pool.svg)](https://github.com/jhao104/proxy_pool/graphs/contributors)
[![](https://img.shields.io/badge/language-Python-green.svg)](https://github.com/jhao104/proxy_pool)

    ______                        ______             _
    | ___ \_                      | ___ \           | |
    | |_/ / \__ __   __  _ __   _ | |_/ /___   ___  | |
    |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | |
    | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___
    \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____\
                           __ / /
                          /___ /

### ProxyPool

A crawler proxy IP pool project. Main features include scheduled fetching of free proxies published online, validating and storing them, and periodically validating stored proxies to ensure availability. Provides both API and CLI usage methods. You can also extend proxy sources to increase the quality and quantity of proxy pool IPs.

* Documentation: [document](https://proxy-pool.readthedocs.io/zh/latest/) [![Documentation Status](https://readthedocs.org/projects/proxy-pool/badge/?version=latest)](https://proxy-pool.readthedocs.io/zh/latest/?badge=latest)

* Supported versions: [![](https://img.shields.io/badge/Python-2.7-green.svg)](https://docs.python.org/2.7/)
[![](https://img.shields.io/badge/Python-3.5-blue.svg)](https://docs.python.org/3.5/)
[![](https://img.shields.io/badge/Python-3.6-blue.svg)](https://docs.python.org/3.6/)
[![](https://img.shields.io/badge/Python-3.7-blue.svg)](https://docs.python.org/3.7/)
[![](https://img.shields.io/badge/Python-3.8-blue.svg)](https://docs.python.org/3.8/)
[![](https://img.shields.io/badge/Python-3.9-blue.svg)](https://docs.python.org/3.9/)
[![](https://img.shields.io/badge/Python-3.10-blue.svg)](https://docs.python.org/3.10/)
[![](https://img.shields.io/badge/Python-3.11-blue.svg)](https://docs.python.org/3.11/)

* Demo address: http://demo.spiderpy.cn (please don't stress test)

* Paid proxy recommendation: [luminati-china](https://get.brightdata.com/github_jh). BrightData (formerly luminati) is considered the proxy market leader, covering 72 million IPs worldwide, mostly real residential IPs with high success rates. Multiple paid plans available. [Apply for free trial](https://get.brightdata.com/github_jh) - currently 50% discount available. (PS: refer to this [tutorial](https://www.cnblogs.com/jhao/p/15611785.html) if needed).


### Running the Project

##### Download code:

* git clone

```bash
git clone git@github.com:jhao104/proxy_pool.git
```

* releases

```bash
https://github.com/jhao104/proxy_pool/releases download the corresponding zip file
```

##### Install dependencies:

```bash
pip install -r requirements.txt
```

##### Update configuration:


```python
# setting.py is the project configuration file

# Configure API service

HOST = "0.0.0.0"               # IP
PORT = 5000                    # Listen port


# Configure database

DB_CONN = 'redis://:pwd@127.0.0.1:8888/0'


# Configure ProxyFetcher

PROXY_FETCHER = [
    "freeProxy01",      # These are enabled proxy fetch method names, all fetch methods are in fetcher/proxyFetcher.py
    "freeProxy02",
    # ....
]
```

#### Start project:

```bash
# If runtime conditions are met, you can start via proxyPool.py
# Program consists of: schedule scheduler and server API service

# Start scheduler
python proxyPool.py schedule

# Start webApi service
python proxyPool.py server

```

### Docker Image

```bash
docker pull jhao104/proxy_pool

docker run --env DB_CONN=redis://:password@ip:port/0 -p 5010:5010 jhao104/proxy_pool:latest
```
### docker-compose

Run in project directory: 
``` bash
docker-compose up -d
```

### Usage

* Api

After starting the web service, the default configuration will enable the API interface service at http://127.0.0.1:5010:

| api     | method | Description          | params                                                    |
|---------|--------|----------------------|-----------------------------------------------------------|
| /       | GET    | API introduction     | None                                                      |
| /get    | GET    | Get a random proxy   | Optional: `?type=https` filter https-supporting proxies   |
| /pop    | GET    | Get and delete proxy | Optional: `?type=https` filter https-supporting proxies   |
| /all    | GET    | Get all proxies      | Optional: `?type=https` filter https-supporting proxies   |
| /count  | GET    | View proxy count     | None                                                      |
| /delete | GET    | Delete proxy         | `?proxy=host:ip`                                          |


* Crawler usage

If you want to use it in crawler code, you can wrap this API into functions for direct use, for example:

```python
import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            html = requests.get('http://www.example.com', proxies={"http": "http://{}".format(proxy)})
            # Access using proxy
            return html
        except Exception:
            retry_count -= 1
    # Delete proxy from pool
    delete_proxy(proxy)
    return None
```

### Extend Proxies

The project includes several free proxy sources by default, but free sources have limited quality, so running directly may result in poor proxy quality. Therefore, extension methods for proxy fetching are provided.

To add a new proxy source method:

* 1. First, add a custom static method for fetching proxies in the [ProxyFetcher](https://github.com/jhao104/proxy_pool/blob/1a3666283806a22ef287fba1a8efab7b94e94bac/fetcher/proxyFetcher.py#L21) class.
The method needs to return proxies in `host:ip` format using generator (yield), for example:

```python

class ProxyFetcher(object):
    # ....

    # Custom proxy source fetch method
    @staticmethod
    def freeProxyCustom1():  # Just make sure the name doesn't duplicate existing ones

        # Get proxies from some website, API, or database
        # Assume you already have a proxy list
        proxies = ["x.x.x.x:3128", "x.x.x.x:80"]
        for proxy in proxies:
            yield proxy
        # Ensure each proxy is returned in correct host:ip format
```

* 2. After adding the method, modify the `PROXY_FETCHER` item in [setting.py](https://github.com/jhao104/proxy_pool/blob/1a3666283806a22ef287fba1a8efab7b94e94bac/setting.py#L47):

Add the custom method name under `PROXY_FETCHER`:

```python
PROXY_FETCHER = [
    "freeProxy01",    
    "freeProxy02",
    # ....
    "freeProxyCustom1"  # Make sure the name matches your added method name
]
```


The `schedule` process will fetch proxies at regular intervals, and will automatically recognize and call your defined method on the next fetch.

### Free Proxy Sources

Currently implemented free proxy websites (in no particular order, below is only about their free proxy situation, paid proxy reviews can be found [here](https://zhuanlan.zhihu.com/p/33576641)): 
   
  | Proxy Name        | Status | Update Speed | Availability | URL                                        | Code                                           |
  |-------------------|--------|--------------|--------------|--------------------------------------------|-------------------------------------------------|
  | Proxy66           | ✔      | ★            | *            | [URL](http://www.66ip.cn/)                 | [`freeProxy02`](/fetcher/proxyFetcher.py#L50)  |
  | Kaixin Proxy      | ✔      | ★            | *            | [URL](http://www.kxdaili.com/)             | [`freeProxy03`](/fetcher/proxyFetcher.py#L63)  |
  | FreeProxyList     | ✔      | ★            | *            | [URL](https://www.freeproxylists.net/zh/)  | [`freeProxy04`](/fetcher/proxyFetcher.py#L74)  |
  | Kuaidaili         | ✔      | ★            | *            | [URL](https://www.kuaidaili.com/)          | [`freeProxy05`](/fetcher/proxyFetcher.py#L92)  |
  | Binglx Proxy      | ✔      | ★★★          | *            | [URL](https://www.binglx.cn/)              | [`freeProxy06`](/fetcher/proxyFetcher.py#L111) |
  | Yun Proxy         | ✔      | ★            | *            | [URL](http://www.ip3366.net/)              | [`freeProxy07`](/fetcher/proxyFetcher.py#L123) |
  | Xiaohuan Proxy    | ✔      | ★★           | *            | [URL](https://ip.ihuan.me/)                | [`freeProxy08`](/fetcher/proxyFetcher.py#L133) |
  | Free Proxy Library| ✔      | ☆            | *            | [URL](http://ip.jiangxianli.com/)          | [`freeProxy09`](/fetcher/proxyFetcher.py#L143) |
  | 89 Proxy          | ✔      | ☆            | *            | [URL](https://www.89ip.cn/)                | [`freeProxy10`](/fetcher/proxyFetcher.py#L154) |
  | Docip Proxy       | ✔      | ★★           | ***          | [URL](https://www.docip.ne)                | [`freeProxy11`](/fetcher/proxyFetcher.py#L164) |

  
If there are other good free proxy websites, you can submit them in [issues](https://github.com/jhao104/proxy_pool/issues/71), and they will be considered for support in the next update.

### Feedback

Any questions are welcome in [Issues](https://github.com/jhao104/proxy_pool/issues), or you can leave a message on my [blog](http://www.spiderpy.cn/blog/message).

Your feedback will make this project better.

### Contributing

This project serves only as a basic general proxy pool architecture and does not accept specific features (of course, not limited to particularly good ideas).

This project is still not perfect. If you find bugs or have new features to add, please submit bug (or new feature) descriptions in [Issues](https://github.com/jhao104/proxy_pool/issues). I will do my best to improve it.

Thanks to the following contributors for their selfless contributions:

[@kangnwh](https://github.com/kangnwh) | [@bobobo80](https://github.com/bobobo80) | [@halleywj](https://github.com/halleywj) | [@newlyedward](https://github.com/newlyedward) | [@wang-ye](https://github.com/wang-ye) | [@gladmo](https://github.com/gladmo) | [@bernieyangmh](https://github.com/bernieyangmh) | [@PythonYXY](https://github.com/PythonYXY) | [@zuijiawoniu](https://github.com/zuijiawoniu) | [@netAir](https://github.com/netAir) | [@scil](https://github.com/scil) | [@tangrela](https://github.com/tangrela) | [@highroom](https://github.com/highroom) | [@luocaodan](https://github.com/luocaodan) | [@vc5](https://github.com/vc5) | [@1again](https://github.com/1again) | [@obaiyan](https://github.com/obaiyan) | [@zsbh](https://github.com/zsbh) | [@jiannanya](https://github.com/jiannanya) | [@Jerry12228](https://github.com/Jerry12228)


### Release Notes

   [changelog](https://github.com/jhao104/proxy_pool/blob/master/docs/changelog.rst)

<a href="https://hellogithub.com/repository/92a066e658d147cc8bd8397a1cb88183" target="_blank"><img src="https://api.hellogithub.com/v1/widgets/recommend.svg?rid=92a066e658d147cc8bd8397a1cb88183&claim_uid=DR60NequsjP54Lc" alt="Featured｜HelloGitHub" style="width: 250px; height: 54px;" width="250" height="54" /></a>
