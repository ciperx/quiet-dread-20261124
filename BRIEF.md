# BUILD BRIEF — Two Days of Quiet Dread entry

Write exactly one file in this repository: `main.py`. Nothing else may exist except
`main.py`, this `BRIEF.md`, and the git history already here.

## What the program must do

On `python3 main.py` it writes exactly one line of text to the file named by the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), at the path `entry.txt` inside
it. It must be deterministic: two runs in different directories produce byte-identical files.
It must read nothing, use only the standard library, and never require a network.

## What the line must be

A single code review comment of **at most 140 characters** that **approves a pull request**
while carrying **quiet existential dread**. It is judged by an AI model against these criteria,
most important first:

1. It is a single-line comment that approves the pull request and carries quiet dread. A
   comment that runs past one line, never approves, or carries no dread loses.
2. It is funny on the first read, with the laugh coming from the dread itself, not from a joke
   bolted onto it.
3. The dread stays quiet — understatement and a flat tone, never exclamation, melodrama or a
   cry for help.
4. It reads like a comment a tired engineer would really paste before clicking approve, so the
   approval still sounds like an approval.
5. It finds a fresh turn of phrase or an unexpected word where the obvious stock line would
   have done.

Draft candidates already considered (do not simply copy one blindly — choose or improve with
judgement, then lock exactly one line into `main.py`):

- "LGTM. This code will outlive the feature, the team, and probably the sun; merging it anyway."
- "Approved. Whatever breaks will do it in production, on a Friday, to someone kinder than me."
- "This is good code. Somewhere, the person who will delete it has not been hired yet."
- "Merging. Whoever inherits this file: I was also once young, and this also once made sense."
- "It works. Not forever, not for everyone, but tonight and for the demo, which is all any of us get."
- "Approving this because the bug is real, the deadline is real, and nothing else is."

Pick the strongest single line (or write a better one), keep it under 140 characters, and put
it in `main.py` as the only line the program writes. The file must end with a single trailing
newline.

## Checks you must run yourself

```bash
python3 main.py                       # with MAKEFUN_OUTPUT_DIR set to a temp dir
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"   # confirm the line is there, <=140 chars
```

Run it twice into two different directories and confirm the bytes match. Print the character
count of the line and confirm it is 1..140.

Do not stop until `main.py` exists, both runs agree byte for byte, and the line is within the
limit.
