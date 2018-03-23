"""Parse log entries for datetimes and calculate the time
   between two shutdown initializations"""
from datetime import datetime
import os, re
import urllib.request
import dateutil.parser as dparser

# prep

tempfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', tempfile)

# code


def read_file():
    """Read in tempfile return list of lines"""
    with open(tempfile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def convert_to_datetime(line):
    """Given a line extract timestamp and convert to datetime"""
    linedate = dparser.parse(line,fuzzy=True)
    return linedate

def time_between_shutdowns(lines):
    """Extract shutdown init events and calculate timedelta between
       first and last one"""
    shutdowns = list()
    for line in lines:
        if 'Shutdown initiated' in line:
            shutdown = convert_to_datetime(line)
            if isinstance(shutdown, datetime):
                shutdowns.append(shutdown)

    timediff = shutdowns[1] - shutdowns[0]
    return timediff
