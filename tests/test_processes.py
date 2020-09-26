#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Process operations functions.

Testing common Process operations. Starting with www.faunadb.com.

> psutil.net_if_addrs()
{'Ethernet 2': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='52-54-00-E7-4D-46', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.10.200', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::a9e0:ec0b:1d03:2ce3', netmask=None, broadcast=None, ptp=None)], 'Tailscale': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='100.73.35.119', netmask='255.255.255.255', broadcast=None, ptp=None)], 'Loopback Pseudo-Interface 1': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='::1', netmask=None, broadcast=None, ptp=None)]}
>>>

False
>>> dir(psutil)
['ABOVE_NORMAL_PRIORITY_CLASS', 'AF_LINK', 'AIX', 'AccessDenied',
'BELOW_NORMAL_PRIORITY_CLASS', 'BSD', 'CONN_CLOSE', 'CONN_CLOSE_WAIT',
'CONN_CLOSING', 'CONN_DELETE_TCB', 'CONN_ESTABLISHED',
'CONN_FIN_WAIT1', 'CONN_FIN_WAIT2', 'CONN_LAST_ACK', 'CONN_LISTEN',
'CONN_NONE', 'CONN_SYN_RECV', 'CONN_SYN_SENT', 'CONN_TIME_WAIT', 'Error', 'FREEBSD',
 'HIGH_PRIORITY_CLASS', 'IDLE_PRIORITY_CLASS', 'IOPRIO_HIGH', 'IOPRIO_LOW', 'IOPRIO_NORMAL',
 'IOPRIO_VERYLOW', 'LINUX', 'MACOS', 'NETBSD', 'NIC_DUPLEX_FULL', 'NIC_DUPLEX_HALF',
 'NIC_DUPLEX_UNKNOWN', 'NORMAL_PRIORITY_CLASS', 'NoSuchProcess',
  'OPENBSD', 'OSX', 'POSIX', 'POWER_TIME_UNKNOWN', 'POWER_TIME_UNLIMITED',
  'PermissionError', 'Popen', 'Process', 'ProcessLookupError', 'REALTIME_PRIORITY_CLASS',
  'STATUS_DEAD', 'STATUS_DISK_SLEEP', 'STATUS_IDLE', 'STATUS_LOCKED', 'STATUS_PARKED',
  'STATUS_RUNNING', 'STATUS_SLEEPING', 'STATUS_STOPPED', 'STATUS_TRACING_STOP',
  'STATUS_WAITING', 'STATUS_WAKING', 'STATUS_ZOMBIE', 'SUNOS', 'TimeoutExpired',
  'WINDOWS', 'ZombieProcess', '_LOWEST_PID', '_PY3', '_SENTINEL', '_TOTAL_PHYMEM',
  '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__',
  '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__',
  '_as_dict_attrnames', '_assert_pid_not_reused', '_common', '_compat', '_cpu_busy_time',
   '_cpu_times_deltas', '_cpu_tot_time', '_last_cpu_times', '_last_cpu_times_2',
   '_last_per_cpu_times', '_last_per_cpu_times_2', '_lock', '_pmap', '_ppid_map',
    '_pprint_secs', '_psplatform', '_psutil_windows', '_pswindows', '_timer',
     '_wrap_numbers', 'boot_time', 'collections', 'contextlib', 'cpu_count',
      'cpu_freq', 'cpu_percent', 'cpu_stats', 'cpu_times', 'cpu_times_percent',
       'datetime', 'disk_io_counters', 'disk_partitions', 'disk_usage', 'functools',
       'getloadavg', 'long', 'net_connections', 'net_if_addrs', 'net_if_stats',
        'net_io_counters', 'os', 'pid_exists', 'pids', 'process_iter', 'pwd',
        'sensors_battery', 'signal', 'subprocess', 'swap_memory', 'sys', 'test',
        'threading', 'time', 'users',
'version_info', 'virtual_memory', 'wait_procs', 'win_service_get', 'win_service_iter']
>>>



"""

import logging
from broccolini.processes import ProcessOperations

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestProcessOperations:
    """Test Process OperationsFunctions."""

    @staticmethod
    def test_view_running_processes():
        """Test view running processes."""
        result = ProcessOperations().view_running_processes(
            # input_data='greg',
        )
        expected = "ystem"
        expected_type = list
        # assert expected == result[0][0]
        assert expected in result[0][0]
        assert isinstance(result, expected_type)
        logging.debug(result)
        print(result)

    @staticmethod
    def test_view_running_processes2():
        """Test view running processes."""
        result = ProcessOperations().view_running_processes_updated()

        expected_type = str
        assert isinstance(result, expected_type)
