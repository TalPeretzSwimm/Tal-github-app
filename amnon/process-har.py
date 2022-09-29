#!/usr/bin/env python3

import sys
import json
from pathlib import Path
from argparse import ArgumentParser
from datetime import datetime


class NamedDict(dict):
    def __getattr__(self, attr):
        return self[attr]


def main():
    parser = ArgumentParser()
    parser.add_argument('harfile')
    parser.add_argument('--microseconds', action='store_true')
    parser.add_argument('--by-url', action='store_true')
    parser.add_argument('--separator', action='store_true')
    args = parser.parse_args()
    try:
        run(args)
    except Exception as e:
        print('ERROR: ', e)
        return 2
    return 0


def run(args):
    time_format = '%H:%M:%S.%f' if args.microseconds else '%H:%M:%S'
    with Path(args.harfile).expanduser().open() as f:
        data = json.load(f, object_pairs_hook=NamedDict)
    generator = ((entry, datetime.fromisoformat(entry.startedDateTime)) for entry in data.log.entries)
    if args.by_url:
        generator = sorted(generator, key=lambda item: (item[0].request.url, item[1]))
    prev_url = None
    for entry, date in generator:
        if args.separator and entry.request.url != prev_url:
            if prev_url is not None:
                print('---')
            prev_url = entry.request.url
        display_url = entry.request.url.replace('%2F', '/').replace('?', ' ? ').replace('&', ' & ')
        print(date.strftime(time_format), f'{entry.request.method:7}', display_url)


class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"

    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"

    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"

    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


if __name__ == '__main__':
    sys.exit(main())
