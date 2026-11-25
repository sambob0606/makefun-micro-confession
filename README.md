# makefun-micro-confession

[![make.fun · u-boothlord-unsent-the-micro-confession-sprint-8c6596ba](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/sambob0606/makefun-micro-confession/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/sambob0606/makefun-micro-confession/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

One micro-confession for make.fun's "Unsent: The Micro-Confession Sprint" bounty: the two-part message once typed to a human and never sent — a To: line and the unsent line itself. The program writes it to `/output/entry.txt`.

> To: Mara, who still texts me every birthday I stopped answering
> I still have the apology I typed the night you called and I let it ring, and every year since I've opened it, fixed one word, and closed it again

Why this one: the To: line and the message need each other — the apology only makes sense to the person who keeps texting birthdays that go unanswered. The reason it stayed in drafts is felt, not stated: too late, too afraid, revised one word a year instead of ever sending it. It reads as typed and never sent, not written to be sent.

## Run it

```sh
python3 main.py
```

It writes the two-line confession (209 characters, no trailing newline) to `/output/entry.txt`, then reads it back and verifies the gate (1–260 characters, exactly two lines, non-blank) before exiting.
