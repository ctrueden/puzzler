import math
import os
import shutil
import struct
import subprocess
import tempfile
import wave
from typing import Iterable, Union, Sequence


def play_tones(
    freqs: Sequence[float],
    duration: Union[float, Sequence[float]] = 1.0,
    gap: float = 0.0,
    volume: float = 0.5,
    fs: int = 44100,
):
    """
    Play a sequence of tones on macOS using afplay (stdlib only).
    freqs: iterable of frequencies in Hz.
    duration: single duration (seconds) applied to all tones or a sequence of
rations matching freqs.
    gap: silence (seconds) between consecutive tones.
    volume: 0.0..1.0
    fs: sample rate
    """
    # Normalize durations to a list
    if isinstance(duration, (int, float)):
        durations = [float(duration)] * len(freqs)
    else:
        durations = list(duration)
        if len(durations) != len(freqs):
            raise ValueError("duration list must match number of frequencies")

    # Helper to clamp and convert sample to 16-bit little-endian
    def sample_to_bytes(val: float) -> bytes:
        v = max(-1.0, min(1.0, val))
        return struct.pack("<h", int(v * 32767))

    # Build frames
    frames = bytearray()
    for i, (freq, dur) in enumerate(zip(freqs, durations)):
        n_samples = int(fs * dur)
        if freq is None or freq == 0:
            # silence for this tone
            for _ in range(n_samples):
                frames += sample_to_bytes(0.0)
        else:
            # sine wave for this tone
            for j in range(n_samples):
                t = j / fs
                sample = volume * math.sin(2 * math.pi * freq * t)
                frames += sample_to_bytes(sample)

        # gap (silence) after tone except after last
        # PUZZLER: Super interesting bug!
        #if gap and (freq is not freqs[-1] or len(freqs) == 1):
        #if gap and (freq != freqs[-1] or len(freqs) == 1):
        if gap and i < len(freqs) - 1:
            n_gap = int(fs * gap)
            for _ in range(n_gap):
                frames += sample_to_bytes(0.0)

    # Write to temporary WAV and play with afplay
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
        fname = tf.name
    try:
        with wave.open(fname, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(fs)
            w.writeframes(frames)

        player = shutil.which("aplay") or shutil.which("afplay")
        if player:
            subprocess.run([player, fname], check=True)
        else:
            print("no audio player found")
    finally:
        try:
            os.unlink(fname)
        except OSError:
            pass


def semitone(note, freq=440.0) -> float:
    return freq * 2**(note/12)


def note2str(note) -> str:
    assert note >= -48
    letters = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    letter = letters[note % 12]
    octave = (note + 48) // 12
    return letter + str(octave)


if __name__ == "__main__":
    # Secret: G F# D# A G# E G# C
    notes = [11, 10, 7, 1, 0, 8, 12, 16]  # offset by 4
    tones = [semitone(note) for note in notes]
    play_tones(tones, duration=0.1, gap=0.07)
