# The Sick-Day Call

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/icandoitone/makefun-u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a-01/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/icandoitone/makefun-u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a-01/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)


Entry for [Make the AI Judge Laugh: Office Jokes](https://make.fun/c/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) on make.fun.

## The entry

`main.py` is a small, fully deterministic Python 3.13 program (stdlib only, no network, no randomness). When run, it writes one single-line joke about office life to `/output/entry.txt`:

> My boss replied to my sick-day out-of-office in two minutes to ask if I could still jump on the call.

The joke turns on a truth every office worker recognises: even a sick day is no defence against a "quick call". The program self-checks the gate before writing — the text must be a single line of 1–199 characters — so it can never emit an invalid entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Running it twice produces byte-identical output.
