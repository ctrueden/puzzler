"""
See: https://marcthespark.github.io/FibonacciMusicBox/
"""

from typing import Sequence

from play import play_tones, semitone, note2str


def pair_sequence(n: int, a: int, b: int) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = [(a, b)]
    visited: set[tuple[int, int]] = {(a, b)}
    total = a + b
    while True:
        a, b = b, a + b
        a %= n
        b %= n
        total += b
        result.append((a, b))
        if (a, b) in visited: break # Cycle!
        visited.add((a, b))

    return result


def note_sequence(pair_sequence: Sequence[tuple[int, int]]) -> list[int]:
    return [a for (a, b) in pair_sequence]


def find_subsequence(full: Sequence, sub: Sequence) -> int:
    sublen = len(sub)
    for i in range(len(full) - sublen + 1):
        if sub == full[i:i+sublen]:
            return i
    return None


def play(note_seq: Sequence[tuple[int]], n: int) -> None:
    pitches = [semitone(i) for i in range(n)]
    tones = [pitches[note] for note in note_seq]
    play_tones(tones, duration=0.1, gap=0.1)


def search_for_notes(notes: Sequence[int], bound=10) -> tuple[int, int, int]:
    for n in range(2, bound):
        print(f"== Searching {n=} ==")
        for a in range(n):
            for b in range(n):
                print(f"{a=} {b=}")
                pair_seq = pair_sequence(n, a, b)
                note_seq = note_sequence(pair_seq)
                print(f"Searching {note_seq} for {notes}...")
                if find_subsequence(note_seq, notes) is not None:
                    print(n, a, b)
                    play(note_seq, n)
                    #return (n, a, b)


if __name__ == "__main__":
    """
    # Calculate pair sequence.
    n = 2
    pair_seq = pair_sequence(n, 0, 1)
    print(f"Pair sequence: {pair_seq}")

    # Pair sequence -> note sequence.
    note_seq = note_sequence(pair_seq)
    print(f"Note sequence: {note_seq}")

    # Note sequence -> letter notation.
    print(f"Music notes: {[note2str(note) for note in note_seq]}")

    # Note sequence -> tone sequence.
    pitches = [semitone(i) for i in range(n)]
    tones = [pitches[note] for note in note_seq]
    print(f"Tones: {tones}")

    # Play the tones.
    play_tones(tones, duration=0.1, gap=0.1)
    """

    # See if we can find it.
    wanted_notes = [0, 1, 1, 0]
    search_for_notes(wanted_notes, bound=3)
