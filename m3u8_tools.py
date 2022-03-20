import urllib.error
import m3u8
import requests


def check_stream_connection(m3u8_url):
    try:
        playlist = m3u8.load(m3u8_url)
        return True
    except urllib.error.HTTPError:
        raise Exception("Can't connect.")
        return False


def check_stream_run(m3u8_url, code, arguments, run_on_down):
    if not check_stream_connection(m3u8_url):
        if run_on_down:
            code(arguments)
    else:
        if not run_on_down:
            code(arguments)
