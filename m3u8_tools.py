import time
import urllib.error
import m3u8


def check_stream_connection(m3u8_url):
    try:
        playlist = m3u8.load(m3u8_url)
        return True
    except urllib.error.HTTPError:
        raise Exception("Can't connect.")
        return False


def continuous_check_stream_run(m3u8_url, code, arguments, run_on_down, time_between_tries, continue_on_trigger):
    while True:
        if not check_stream_connection(m3u8_url):
            if run_on_down:
                code(arguments)
            if not continue_on_trigger:
                return None
        else:
            if not run_on_down:
                code(arguments)
            if not continue_on_trigger:
                return None

        time.sleep(time_between_tries)

