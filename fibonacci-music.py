"""
See: https://marcthespark.github.io/FibonacciMusicBox/
"""

from typing import Sequence

from play import play_tones, semitone, note2str


def pair_sequence(n: int, y: int, x: int) -> list[tuple[int, int]]:
    """
    Calculate the music box's sequence of coordinate pairs.

    Args:
        n: The Modulo of the music box.
        y: The Y (vertical/row) starting coordinate value.
        x: The X (horizontal/column) starting coordinate value.
    Returns:
        List of coordinate pairs visited by the music box.
        Begins with the initial (y, x) coordinate. Ends when a previously
        visited coordinate is revisited, indicating a cycle has been reached.
    """
    result: list[tuple[int, int]] = [(y, x)]
    visited: set[tuple[int, int]] = {(y, x)}
    total = y + x
    while True:
        y, x = x, y + x
        y %= n
        x %= n
        total += y
        result.append((y, x))
        if (y, x) in visited: break # Cycle!
        visited.add((y, x))

    return result


def note_sequence(pair_sequence: Sequence[tuple[int, int]]) -> list[int]:
    """
    Boils down a coordinate pair sequence into a sequence of notes to play.
    The "note" value is the Y coordinate value of the coordinate pair.

    Args:
        Sequence of coordinate pairs visited.
    Returns:
        List of notes to play.
    """
    return [y for (y, x) in pair_sequence]


def equals_with_offset(n: int, sub: Sequence[int], goal: Sequence[int], offset: int) -> bool | None:
    offsetted = [note + offset for note in goal]
    if any(offsetted) >= n: return None
    return sub == offsetted


def find_subsequence(n: int, full: Sequence[int], goal: Sequence[int], any_key=False) -> tuple[int, int]:
    sublen = len(goal)
    for i in range(len(full) - sublen + 1):
        sub = full[i:i+sublen]
        for offset in range(n):
            eq = equals_with_offset(n, sub, goal, offset)
            if eq is None: break # overflow
            if eq is True: return (i, offset) # match
    return None


def play(note_seq: Sequence[tuple[int]], n: int) -> None:
    pitches = [semitone(i) for i in range(n)]
    tones = [pitches[note] for note in note_seq]
    play_tones(tones, duration=0.1, gap=0.1)


def search_for_notes(notes: Sequence[int], bound=10) -> tuple[int, int, int]:
    hits = []
    for n in range(2, bound):
        print(f"== Searching {n=} ==")
        for y in range(n):
            for x in range(n):
                pair_seq = pair_sequence(n, y, x)
                note_seq = note_sequence(pair_seq)
                if find_subsequence(n, note_seq, notes, any_key=True) is not None:
                    print(f"HIT {n=} {y=} {x=}: {note_seq} in {notes}")
                    hits.append((n, y, x))
                    #play(note_seq, n)
                    #return (n, y, x)
    return hits


if __name__ == "__main__":
    bound = 40
    # Secret: G F# D# A G# E G# C
    note_seq = [11, 10, 7, 1, 0, 8, 12, 16]  # offset by 4
    #note_seq = [0, 2, 4, 5]
    #note_seq = [0, 1, 1, 0]
    print(f"Note sequence: {note_seq}")

    # Note sequence -> letter notation.
    print(f"Music notes: {[note2str(note) for note in note_seq]}")

    # Note sequence -> tone sequence.
    pitches = [semitone(i) for i in range(bound)]
    tones = [pitches[note] for note in note_seq]
    print(f"Tones: {tones}")

    # Play the tones.
    play_tones(tones, duration=0.1, gap=0.08)

    # See if we can find it.
    hits = search_for_notes(note_seq, bound=bound)
    print("== Search complete ==")
    print(f"{hits=}")
