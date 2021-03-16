from pathlib import Path
import sys
import keyboard
import time
import fire
import json

def print_key(pretty):
    def go(key):
        kwargs = {}
        if pretty:
            kwargs = {
                'indent': 4,
                'sort_keys': True
            }

        print(json.dumps(
            key.__dict__ | { 'repr': repr(key) },
            **kwargs
        ))

        sys.stdout.flush()

    return go

def record_kps(pretty=False):
    keyboard.hook(print_key(pretty=pretty))

    # Wait in a more efficient manner
    while True:
        time.sleep(1)

def cli():
    fire.Fire({
        'record': record_kps,
        'test': lambda: keyboard.press_and_release(35)
    })
