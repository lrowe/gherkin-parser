"""
Main command. Reads a feature file from stdin, outputs it as parsed JSON.
"""

import codecs
import json
import six
import sys

from gherkin_parser import parse_file

stdin = sys.stdin if six.PY2 else sys.stdin.buffer
with codecs.getreader('utf8')(stdin) as fp:
    print(json.dumps(parse_file(fp), indent=4))
