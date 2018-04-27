# github-merge-strategies
Show the difference between "Merge," "Squash and Merge," and "Rebase and Merge."

## Diceware Password Generator

usage: diceware.py [-h] [-n NUM_WORDS] [-l] [-a] [-e] [-w WORD_LIST]

optional arguments:
  -h, --help                             show this help message and exit
  -n NUM_WORDS, --num-words NUM_WORDS    Number of words to generate [5]
  -l, --lower                            All lowercase (no capitalization) [false]
  -a, --alpha                            Only alpha characters (no symbols or numbers) [false]
  -e, --leet                             U53 1337 5p34k [false]
  -w WORD_LIST, --word-list WORD_LIST    Word list filename [wordlist.txt

### Samples

diceware.py -n 5 => Karp vulcan=census#Rabid rocket
diceware.py -n 4 => plunk Snore clare:harley
diceware.py -n 7 => Quota Scion.bulky|Abode-berra:80th sw

diceware.py --lower => revel.enamel yang.bet lagoon

diceware.py --alpha => vague Scrim Punky denny Wise

diceware.py --alpha --lower --leet => c1ph3r l01n um ch153l 80und (cipher loin um chisel bound)

*Suggestion:*

```diceware.py --alpha --lower``` let's you choose where to capitalize, punctuate, and, optionally, leet-ize
