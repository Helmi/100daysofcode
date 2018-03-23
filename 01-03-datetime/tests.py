from datetime import datetime, timedelta

from logtimes import read_file, convert_to_datetime, time_between_shutdowns


def test_read_file():
    lines = read_file()
    assert type(lines) == list
    assert len(lines) == 32
    grep = [line for line in lines if
            'Shutdown' in line]
    assert len(grep) == 4


def test_convert_to_datetime():
    line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
    line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
    assert convert_to_datetime(line1) == datetime(2014, 7, 3, 23, 24, 31)
    assert convert_to_datetime(line2) == datetime(2015, 10, 3, 10, 12, 51)
    assert convert_to_datetime(line3) == datetime(2016, 9, 3, 2, 11, 22)


def test_time_between_events():
    lines = read_file()
    diff = time_between_shutdowns(lines)
    assert type(diff) == timedelta
    assert str(diff) == '0:03:31'