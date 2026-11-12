#!/usr/bin/env python3
"""Generate an original example loop without recordings or third-party samples.

This generator and its output are dedicated under CC0 1.0 Universal:
https://creativecommons.org/publicdomain/zero/1.0/
Requires Python 3 and ffmpeg (only for regeneration, not playback).
Usage: python3 tools/generate-example-audio.py path/to/generated-ambient-loop.mp3
"""
import argparse
import array
import math
import pathlib
import subprocess
import sys
import tempfile
import wave

SAMPLE_RATE = 44100
DURATION = 8
FREQUENCIES = (220.0, 275.0, 330.0)


def generate(destination):
    destination = pathlib.Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    samples = array.array('h')
    for index in range(SAMPLE_RATE * DURATION):
        t = index / SAMPLE_RATE
        fade = min(1.0, t / 0.5, (DURATION - t) / 0.5)
        tone = sum(math.sin(2 * math.pi * f * t) for f in FREQUENCIES) / len(FREQUENCIES)
        pulse = 0.8 + 0.2 * math.sin(2 * math.pi * t / 4)
        samples.append(round(32767 * 0.22 * fade * pulse * tone))
    if sys.byteorder != 'little':
        samples.byteswap()
    with tempfile.TemporaryDirectory() as temporary:
        source = pathlib.Path(temporary) / 'loop.wav'
        with wave.open(str(source), 'wb') as output:
            output.setparams((1, 2, SAMPLE_RATE, 0, 'NONE', 'not compressed'))
            output.writeframes(samples.tobytes())
        subprocess.run([
            'ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', str(source),
            '-map_metadata', '-1', '-codec:a', 'libmp3lame', '-b:a', '128k',
            '-metadata', 'title=Generated ambient example loop',
            '-metadata', 'comment=Generated from sine waves; no recordings or samples. CC0 1.0 Universal.',
            str(destination),
        ], check=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination')
    generate(parser.parse_args().destination)
