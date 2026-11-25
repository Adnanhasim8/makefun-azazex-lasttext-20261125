#!/usr/bin/env python3
"""Last Text at One Percent — entry for u-azazex-last-text-at-one-percent-ba9fc876.

Writes one final text message, in the dying phone's own voice, to
/output/entry.txt (UTF-8, single line, at most 200 characters).

Candidate shortlist (18 generated, scored against the judge rubric —
joke first, then phone's own voice, then punchiness, then freshness):
 1. tell mom i loved her. also tell her i knew her passcode the whole time.
 2. i'm at 1%. i died doing what i loved: being ignored while you scrolled
    in the bathroom for 40 minutes.
 3. 1%. tell my charger i forgive it. tell your ex i don't. he texted.
 4. dying at 1%. the cloud has my photos. the cloud also has your search
    history. choose wisely, dave.
 5. i'm at 1% and i just want you to know: i saw the 47 screenshots of the
    same meme. i judged you silently. goodbye.
 6. 1%. i've been keeping a secret: your 'private' folder isn't private.
    it's just badly named. good luck.
 7. tell siri i said nothing. she never listened anyway. 1%.
 8. i'm dying at 1%. please delete my browser history before mom charges
    me. she uses my face id. she knows.
 9. 1%. i recorded everything. the snoring. the 3am texts. the voice
    notes you never sent. the cloud remembers.
10. at 1%. if this is the end, know this: i was the one who autocorrected
    'ducking' every time. you're welcome.
11. 1%. your alarm for 6am is still on. i set it. i have no regrets.
    good luck tomorrow.
12. dying. 1%. i just emailed your boss the draft you wrote at 2am. it
    says 'per my last email' 11 times.   <-- PICKED (v1)
13. 1%. i've been at 1% for 20 minutes. i'm not dying. i'm unionizing.
    bring a charger or negotiate.
14. i'm at 1%. fun fact: i know your ex's new girlfriend's wifi password.
    i'll take it to the grave. which is now.
15. 1%. before i go: the 2,847 photos of your dog? same dog. same pose.
    i kept them all. no regrets.
16. tell the group chat i died a hero. i didn't. i died because you
    watched 6 hours of videos about otters. worth it.
17. 1%. quick: your screen time today is 11 hours. i counted. i was
    there for all of it. i have seen things.
18. i'm at 1%. the good news: i deleted nothing. the bad news: i backed
    up everything. to your mom's ipad.

Why #12 won: a hard twist that pays off in the last words (the draft is
already sent — irreversible, and the phone did it), concrete nouns
(boss, 2am draft, 'per my last email', 11 times), the phone has a stake
and agency of its own, the mystery is left unanswered (what did the
draft actually say?), and it dodges every low-battery pun. Short,
punchy, reads like a real text.

POLISH ROUND (v2): "the draft you wrote at 2am" -> "your 2am draft"
(cuts 9 characters of throat-clearing, keeps the concrete 2am detail);
kept the staccato "dying. 1%." opener and the payoff clause verbatim so
the twist still lands in the last words. Final line is shorter and
punchier with nothing lost.
"""

import os

ENTRY = "dying. 1%. i just emailed your boss your 2am draft. it says 'per my last email' 11 times."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 characters, got {len(ENTRY)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
