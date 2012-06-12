#! /usr/bin/python
#
# Echo StreamServer: Echo Query Language Shell
# ============================================================
import sys, os, readline
import atexit

from echo import __version__ as echo_version
from echo import items, StreamServerError
from pprint import pprint

__author__ = 'Andrew Droffner'

# Use GNU Readline and a history file.
# ============================================================
histfile = os.path.join(os.path.expanduser("~"), ".eqlhist")
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)

# Introduction
# ============================================================
sys.stdout.write("""
Echo Query Language Shell (echo.items version %r)

Send an EQL text string to Stream Server and display the results.
EQL> url:http://example.com/index.html

Prompts:
EQL>   "This prompt means execute a search."
COUNT> "This prompt means execute a count."

Shell Commands
COUNT:  Set to COUNT> mode.
SEARCH: Set to SEARCH> mode.
QUIT:   Quit the shell.

""" % echo_version)

# Read-Execute Loop:
# ============================================================
count_flag = False

while True:
    try:
        # Prompt user for EQL text string.
        # Example: "url:http://www-stage.nola.com/festivals/index.ssf/2012/06/testing_3_4_5.html")
        eql_text = raw_input('COUNT> ' if count_flag else 'EQL> ')
        eql_text = eql_text.strip()

        # Skip empty lines.
        if '' == eql_text:
            continue
        # Shell Commands
        if 'count' == eql_text.lower():
            count_flag = True
            continue
        if 'search' == eql_text.lower():
            count_flag = False
            continue
        if 'quit' == eql_text.lower():
            sys.exit()

        # Based on the prompt, execute either a "count" or "search" query.
        if count_flag:
            n = items.count(eql_text)
            sys.stdout.write("\tCOUNT: %d\n" % n)
        else:
            r = items.search(eql_text)
            pprint(r)
    except StreamServerError, e:
        sys.stderr.write("Echo StreamServer: [%s] %s\n" % (e.errorCode, e.errorMessage))
    except (EOFError, KeyboardInterrupt, SystemExit):
        sys.stderr.write("\nQUIT\n\n")
        sys.exit()

