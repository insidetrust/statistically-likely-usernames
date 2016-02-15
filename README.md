# statistically-likely-usernames
Wordlists for creating statistically likely username lists for use in username enumeration, simulated password attacks and other security testing tasks.

The core username lists were generated orignally from US Census data, and sorted in statistically likely order, such that username lists can be generated quickly to match common organisational patterns. These lists have been tested extensively in live attacks against target sites during authorised penetration tests, with a high degree of success. The initial reason for generating these was that I wanted to know when it was statistically likely to try z.smith, compared to say b.jones.

Forename with first initial of surname e.g. james.m
 - sorted-forename-dot-letter-lowercase.txt

First initial with surname e.g. j.smith
 - sorted-letter-dot-surname-lowercase.txt

Top 1000 most popular surnames
 - last1000.txt

Forenames, both male and female
 - firstfemale.txt
 - firstmale.txt

These lists can be combined in a variety of ways. For example if a pentester uses Foca, or similar and identifies that the username format of an organisation is "j_smith" and wants 10,000 guesses (to try with "Password1", or whatever):

head -n 10000 sorted-letter-dot-surname-lowercase.txt | tr "\." "_" > usernames.txt

Altertatively; if the username is jwilliams , but truncated to 7 characters:

head -n 10000 sorted-letter-dot-surname-lowercase.txt | tr -d "." | cut -c1-7 | awk '!x[$0]++' > usernames.txt

(note, when truncating usernames, duplicates can be created and it is important to remove these, especially when used with password attacks. This can be done with the "awk '!x[$0]++'" command above)

Email addresses can be created as follows, for example smith.j@example.com:

head -n 10000 sorted-letter-dot-surname-lowercase.txt | awk -F "." '{ print $2 "." $1 }' | sed 's/$/@example.com/g' > usernames.txt

Here for example we are creating email addresses from male and female names in the format james.smith@example.com

for first in $(head -q first*male.txt); do for last in $(head last1000.txt); do echo $first.$last@example.com; done; done > usernames.txt

Obviously the above can be combined to generate a selection of popular formats, if the format cannot be enumerated in advance or mixed formats are present.



