#!/usr/bin/env python

import sys
import tempfile
import re
import envoy

try:
    config_file = sys.argv[1]
except IndexError:
    print 'usage: %s <config file>'
    exit(1)

logs = tempfile.mkdtemp()

r = envoy.run('tsung -l {logs} -w 1 -f {config} start'.format(logs=logs, config=config_file))

if r.status_code != 0:
    print 'Error running Tsung:'
    print r.std_out
    exit(r.status_code)

print 'Tsung finished!'
log_dir = re.search('"Log directory is: ([^"]+)"', r.std_out).group(1)

print 'Tsung logs are in %s' % log_dir

r = envoy.run('ln -sf {log_dir} ./logs'.format(log_dir=log_dir))
