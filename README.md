# gpu-job-manager
My GPU job manager


Run example:

If you have a server with 4 GPUs, then run with a yaml config file.

`python gjm/gjm.py --ngpu 4 -i local-jobs/test.yaml --logdir ./log`

The first job in queue will run when a running job is just finished.

```
11/19/2019 13:11:54 - INFO - __main__ -   code_dir is set as local-jobs/
11/19/2019 13:11:54 - INFO - __main__ -   Current dir is set as .
11/19/2019 13:11:54 - INFO - __main__ -   Parsing Jobs...
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '3', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '3', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '3', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '5', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '5', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '5', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '7', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '7', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '7', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '9', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '9', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '9', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '11', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '11', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '11', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '13', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '13', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '1', 'cnt': '13', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '3', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '3', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '3', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '5', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '5', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '5', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '7', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '7', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '7', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '9', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '9', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '9', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '11', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '11', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '11', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '13', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '13', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '2', 'cnt': '13', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '3', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '3', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '3', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '5', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '5', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '5', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '7', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '7', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '7', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '9', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '9', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '9', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '11', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '11', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '11', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '13', 'host': 'baidu.com'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '13', 'host': 'localhost'}
11/19/2019 13:11:54 - INFO - __main__ -   {'exp_name': 'exp_name', 'useless': '3', 'cnt': '13', 'host': 'google.com'}
11/19/2019 13:11:54 - INFO - __main__ -   Finding 54 jobs to run...
11/19/2019 13:11:54 - INFO - __main__ -   Start running job: test-1-exp_name-c3-hostbaidu.com on 0-th GPU
11/19/2019 13:11:54 - INFO - __main__ -   Command: ping -c 3 baidu.com
11/19/2019 13:11:54 - INFO - __main__ -   Start running job: test-1-exp_name-c3-hostlocalhost on 1-th GPU
11/19/2019 13:11:54 - INFO - __main__ -   Command: ping -c 3 localhost
11/19/2019 13:11:54 - INFO - __main__ -   Start running job: test-1-exp_name-c3-hostgoogle.com on 2-th GPU
11/19/2019 13:11:54 - INFO - __main__ -   Command: ping -c 3 google.com
11/19/2019 13:11:54 - INFO - __main__ -   Start running job: test-1-exp_name-c5-hostbaidu.com on 3-th GPU
11/19/2019 13:11:54 - INFO - __main__ -   Command: ping -c 5 baidu.com
11/19/2019 13:11:59 - INFO - __main__ -   Start running job: test-1-exp_name-c5-hostlocalhost on 0-th GPU
11/19/2019 13:11:59 - INFO - __main__ -   Command: ping -c 5 localhost
11/19/2019 13:11:59 - INFO - __main__ -   Start running job: test-1-exp_name-c5-hostgoogle.com on 1-th GPU
11/19/2019 13:11:59 - INFO - __main__ -   Command: ping -c 5 google.com
11/19/2019 13:11:59 - INFO - __main__ -   Start running job: test-1-exp_name-c7-hostbaidu.com on 2-th GPU
11/19/2019 13:11:59 - INFO - __main__ -   Command: ping -c 7 baidu.com
11/19/2019 13:11:59 - INFO - __main__ -   Start running job: test-1-exp_name-c7-hostlocalhost on 3-th GPU
11/19/2019 13:11:59 - INFO - __main__ -   Command: ping -c 7 localhost
...
```
