"""
Live-coded Puzzler version of the Fibonacci music box problem!

Given a "song", figure out what Fibonacci music box can play that song *if it exists*.
- Find n, (row, col)
- Finding one solution is sufficient.

Questions:

- How are pitches decided?
  - Pitch is based on the ROW of each dot (COL has no effect)
  - For now, assume chromatic scale (half-steps, 12 per octave)

- What are the bounds?
  - 2 <= n <= 100
  - (row, col) = 0 <= row < 100, 0 <= col < 100

- Are there multiple octaves?
  - Yes, pitch starts at some arbitrary value, increasing by half-steps to the top
  - E.g. if n=100, C0 is bottom, 12*8=96, 99=D#8(ish)

- What does "same song" mean?
  - Octave is included

- What does "play that song" mean?
  - Those notes appear in that order without interruption.
  - No notes in between.
  - Other notes before and after the "song" are OK.

Posit: You can't always do it.
  - I agree :-)
"""

from typing import Sequence

SONG = list[int]

# Solution:
# Song begins with a note. Determines the first row.

# Get rid of length.
# Return all songs of size box_size**2
# See if song is a subsequence of any of the songs
# Smarter: stop when we see a cycle. But Eric rejects this as too much work.

# How much lead-up do we need to care about?
# There can be a "prefix" to the song we're trying to generate.
# The first "note" of a song can be one of n dots.
# The *previous* note can be one of n^2 dots, or nothing.
# - But we don't need to *check* all n^2 dots; we only care about *row* of previous dot

# What if we are fine with any "key"? I.e. global offset?
# (1, 3, 5, 6) -> e.g. (2, 4, 6, 7) or (4, 6, 8, 9) are fine
#
# How much more difficult/complex does this make our algorithm?
# - ED: "Maybe it's not that hard to just do this?"
#
# Possible solutions:
# 1. Check for all "variant" songs -- i.e. same song in each possible key
#    O(n^4) -> O(n^5)
# 2. Change is_subsequence to check all variants -- adds n checks instead of 1.
# 3. We want the differences between notes
#    Convert our target song: (1, 3, 5, 6) -> (+1, +2, +2, +1)
#    Make "generate_song" return the differences/gaps, not the sequence itself.
#    This is a *normalization* procedure to eliminate key skew.
#    Complexity remains unchanged?
#    But we need to use all n^2 starting points now.
#    BUT! Do we?
#    - POSIT: Each "triple" (row of previous pair, plus current pair) is part of a unique cycle?

def generate_song(box_size: int, first_row: int, first_col: int) -> SONG:
    # TODO: When song diverges from target song, just stop.
    song = []
    row = first_row
    col = first_col
    visited: set = set()
    while True:
        song.append(row)
        row, col = (row+col) % box_size, row
        if (row, col) in visited:
            break
        visited.add((row, col))
    return song

def generate_songs(box_size: int, first_note: int) -> list[SONG]:
    songs: list[SONG] = []
    note = first_note
    for col in range(box_size):
        song: SONG = generate_song(box_size, first_row=first_note, first_col=col)
        songs.append(song)
    return songs

def is_subsequence(goal: Sequence[int], full: Sequence[int]) -> bool:
    goal_string = "," + ",".join(map(str, goal)) + ","  # <-- This is terrible.
    full_string = "," + ",".join(map(str, full)) + ","
    return goal_string in full_string


# TIME COMPLEXITY of this "dumb" solution?
# (We know it's "bad")
# n is box_size
# Generating each song: O(n^2)
# Generating all songs: n per song, O(n^3) total
# Checking for subsequence: each string is length n^2*log(n) -- O(n^2 * log(n))
# Check for subsequence in all n songs (n columns): O(n^3 * log(n))
# Both steps: O(n^3) + O(n^3 * log(n)) -> O(n^3 * log(n))
# Varying n: we must repeat all of the above for each value of n: O(n^4 * log(n))

# "Song" is a list of notes.
# "Note" is a number: the number of the row to play it.
song: SONG = [1, 1, 0]  # We know this one exists.

# Generate every possible song.
for box_size in range(2, 101):
    print(f"== CHECKING {box_size=}")
    songs = generate_songs(box_size, song[0])
    #print(songs)
    # See if any match.
    print(any(is_subsequence(song, note_seq) for note_seq in songs))
