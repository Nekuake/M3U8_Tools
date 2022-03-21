# M3U8 Tools
Various functions for checking or handling m3u8 playlists. Ongoing project.

## check_stream_connection(m3u8_url)
Requests the m3u8 playlist and returns True if successful, False if error.

## continuous_check_stream_run(m3u8_url, code, arguments, run_on_down, time_between_tries, continue_on_trigger)

Requests the m3u8 playlist and executes the code with the arguments depending if "run_on_down" is True or False. Code must be a command, so using a dictionary is recommended. More information about how here: https://stackoverflow.com/a/23177341
For example, this function can be useful if you want to trigger a CanaryToken or webhook as soon as a stream is down. 

