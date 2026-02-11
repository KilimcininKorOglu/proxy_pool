.. _changelog:

ChangeLog
==========

2.4.2 (2024-01-18)
------------------

1. Proxy format check supports authenticated proxy format `username:password@ip:port`; (2023-03-10)
2. Added proxy source **Docip Proxy**; (2023-05-15)
3. Added proxy source **Binglx Proxy**; (2023-01-18)

2.4.1 (2022-07-17)
------------------

1. Added proxy source **FreeProxyList**; (2022-07-21)
2. Added proxy source **FateZero**; (2022-08-01)
3. Added proxy attribute ``region``; (2022-08-16)

2.4.0 (2021-11-17)
------------------

1. Removed invalid proxy source **Shenji Proxy**; (2021-11-16)
2. Removed invalid proxy source **Jisu Proxy**; (2021-11-16)
3. Removed proxy source **Xila Proxy**; (2021-11-16)
4. Added proxy source **Dieniao IP**; (2021-11-16)
5. Added proxy source **PROXY11**; (2021-11-16)
6. Multi-threaded proxy fetching; (2021-11-17)

2.3.0 (2021-05-27)
------------------

1. Fixed Dockerfile timezone issue; (2021-04-12)
2. Added Proxy attribute ``source`` to mark proxy origin; (2021-04-13)
3. Added Proxy attribute ``https`` to mark https-supporting proxies; (2021-05-27)

2.2.0 (2021-04-08)
------------------

1. Check database connectivity on startup;
2. Added free proxy source **Mipu Proxy**;
3. Added free proxy source **Pzzqz**;
4. Added free proxy source **Shenji Proxy**;
5. Added free proxy source **Jisu Proxy**;
6. Added free proxy source **Xiaohuan Proxy**;

2.1.1 (2021-02-23)
------------------

1. Fix Bug `#493`_, added timezone configuration; (2020-08-12)
2. Fixed **Proxy66** fetching; (2020-11-04)
3. Fixed **Quanwang Proxy** fetching, solved HTML port encryption issue; (2020-11-04)
4. Added **Proxy Box** free source; (2020-11-04)
5. Added ``POOL_SIZE_MIN`` config option, trigger fetching when remaining proxies are less than POOL_SIZE_MIN during runProxyCheck; (2021-02-23)

.. _#493: https://github.com/jhao104/proxy_pool/issues/493

2.1.0 (2020.07)
------------------

1. Added free proxy source **Xila Proxy** (2020-03-30)
2. Fix Bug `#356`_ `#401`_
3. Optimized Docker image size; (2020-06-19)
4. Optimized configuration method;
5. Optimized code structure;
6. No longer store raw_proxy, validate and store directly after fetching;

.. _#401: https://github.com/jhao104/proxy_pool/issues/401
.. _#356: https://github.com/jhao104/proxy_pool/issues/356

2.0.1 (2019.10)
-----------------

1. Added free proxy source **89 Free Proxy**;
#. Added free proxy source **Qiyun Proxy**

2.0.0 (2019.08)
------------------

1. WebApi integrated Gunicorn startup, Windows platform not supported yet;
#. Optimized Proxy scheduler;
#. Extended Proxy attributes;
#. Added CLI tool for easier proxyPool startup

1.14  (2019.07)
-----------------

1. Fixed ``ProxyValidSchedule`` deadlock bug caused by Queue blocking;
#. Modified **Yun Proxy** fetching;
#. Modified **Manong Proxy** fetching;
#. Modified **Proxy66** fetching, introduced ``PyExecJS`` module to crack Jiasule dynamic Cookies encryption;

1.13  (2019.02)
-----------------

1. Use .py file instead of .ini as configuration file;

#. Optimized proxy fetching part;

1.12  (2018.04)
-----------------

1. Optimized proxy format check;

#. Added proxy sources;

#. fix bug `#122`_  `#126`_

.. _#122: https://github.com/jhao104/proxy_pool/issues/122
.. _#126: https://github.com/jhao104/proxy_pool/issues/126

1.11  (2017.08)
-----------------

1. Use multi-threading to validate useful_pool;

1.10  (2016.11)
-----------------

1. First version;

#. Support PY2/PY3;

#. Basic proxy pool functionality;
