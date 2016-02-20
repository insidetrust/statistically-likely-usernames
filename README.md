# statistically-likely-usernames
This resource contains wordlists for creating statistically likely usernames for use in username-enumeration, simulated password-attacks and other security testing tasks.

When many users are present in an application or network, I normally approach password-attacks by guessing likely usernames, (rather than focusing on guessing too many passwords). This has several advantages (such as avoiding account lockout for example) and is almost always successful (usually several users have either "Password1", "password" or something equally trivial).

The core username lists here were generated orignally from US Census data, and sorted in statistically likely order, such that username lists can be generated quickly to match common organisational patterns. These lists have been tested extensively in live attacks against target networks and applications. This resulted in a very high degree of success (during authorised penetration tests). The initial reason for generating these was that I wanted to know when it was statistically worthwhile to try z.smith, compared to say j.jackson (or any other name) and create the most efficient set of guesses in the shortest possible time, based on popular formats.

The following base wordlists are provided:

Forename with first initial of surname e.g. `james.m`
 - sorted-forename-dot-letter-lowercase.txt

First initial with surname e.g. `j.smith`
 - sorted-letter-dot-surname-lowercase.txt

Top 1000 most popular surnames
 - last1000.txt

Forenames, both male and female
 - firstfemale.txt
 - firstmale.txt

These lists can then be manipulated and combined in a variety of ways. For example if a pentester uses Foca, or similar, and identifies that the username format of an organisation is `j_smith` and wants 10,000 guesses (with which to try "Password1", or whatever):

`head -n 10000 sorted-letter-dot-surname-lowercase.txt | tr "\." "_" > usernames.txt`

Altertatively; if the username would be `jwilliams` , but is always truncated to 7 characters, such as `jwillia`:

`head -n 10000 sorted-letter-dot-surname-lowercase.txt | tr -d "." | cut -c1-7 | awk '!x[$0]++' > usernames.txt`

**Important:** when truncating usernames, duplicates can be generated, so it very is important to remove these, especially when used with password attacks where lockout is present. This can be done, whilst keeping statistically likely order, with the `awk '!x[$0]++'` command (as shown above).

Email addresses can be created as follows, for example `smith.j@example.com`:

`head -n 10000 sorted-letter-dot-surname-lowercase.txt | awk -F "." '{ print $2 "." $1 }' | sed 's/$/@example.com/g' > usernames.txt`

Here for example we are creating email addresses from male and female names in the format `james.smith@example.com`

`for first in $(head -q first*male.txt); do for last in $(head last1000.txt); do echo $first.$last@example.com; done; done > usernames.txt`

Obviously a variety of formats can be combined to generate a selection of likely popular usernames or email address formats (especially useful if the format cannot be enumerated in advance, or mixed formats are present).



