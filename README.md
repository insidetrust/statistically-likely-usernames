# statistically-likely-usernames
This resource contains wordlists for creating statistically likely usernames for use in username-enumeration, simulated password-attacks and other security testing tasks.

When many users are present in an application or network, I normally approach password-attacks by guessing likely usernames, (rather than focusing on guessing too many passwords). This has several advantages (such as avoiding account lockout for example) and is almost always successful (usually several users have either "Password1", "password" or something equally trivial).

The best approach is a horizontal password attack, trying one password for thousands of possible usernames.

The core username lists here were generated orignally from US Census data, but I have recently updated this to use data indexed from Facebook. These lists have been tested extensively in live attacks against target networks and applications. This resulted in a very high degree of success (during authorised penetration tests).

The initial reason for generating these username lists was that I wanted to know when it was statistically worthwhile to try z.smith, compared to say j.jackson (or any other name) and create the most efficient set of guesses in the shortest possible time, based on common username formats in statistically likely order.

As you can see below, name popularity follows the pareto curve, so it's best to start with jsmith and work down...

![alt text](https://github.com/insidetrust/statistically-likely-usernames/blob/master/popular-names.JPG "Pereto curves are awesome")

## A bunch of pre-canned lists are provided, as well as base-lists for generating your own in a variety of targeted formats:

### (Formats of the following pre-canned lists should be self-evident from the filename)

jsmith.txt - A popular place to start, 50,000 usernames in a very common format.

john.smith.txt - Also a very common format 250,000 (more usernames are typically required here due to the higher entropy).

jjs.txt - This works surprisingly well, all 17,576 three letter combinations, for the most part sorted by most popular initials.

john.smith-at-example.com.txt - 250,000 email addresses in this common format (replace the example.com with a target domain)

top-formats.txt - A mix in a variety of popular formats (around 1 million examples) interleaved and de-duplicated for ease-of-use (a very useful first step when the format is unknown, but slower than targeted formats)

john.txt - 10,000 forenames

smith.txt - 10,000 surnames

johnsmith.txt - Just under 250,000 examples

jjsmith.txt - 100,000 examples

smithjj.txt - 100,000 examples

johnjs.txt - 100,000 examples

smithj.txt - 50,000 examples

johns.txt - 50,000 examples

jsmith2.txt - A popular format which commonly suffers from collisions (hence jsmith2, and jsmith3 etc. 5,000 examples)

smithj2.txt - As above x 5,000

## Rolling your own

If this isn't sufficient (and it won't be in some cases, expect that!) the base-lists can be manipulated and combined in a wide variety of ways. For example if a pentester uses Foca, or similar, and identifies that the username format of an organisation is `j_smith` and wants 10,000 guesses (with which to try "Password1", or whatever) the base-lists can be modified as follows:

`head -n 10000 j.smith-x100000 | tr "\." "_" > usernames.txt`

Altertatively; if the username would be `jwilliams` , but is always truncated to 7 characters, such as `jwillia`:

`head -n 10000 j.smith-x100000 | tr -d "." | cut -c1-7 | awk '!x[$0]++' > usernames.txt`

**Important:** when truncating usernames, duplicates can be generated, so it very is important to remove these, especially when used with password attacks where lockout is present. This can be done, whilst keeping statistically likely order, with the `awk '!x[$0]++'` command (as shown above).

Unusual Email address formats can be created as follows for example `smith-j@example.com`:

`head -n 10000 j.smith-x100000.txt  | awk -F "." '{ print $2 "-" $1 }' | sed 's/$/@example.com/g' > usernames.txt`

Obviously a wider variety of formats can be combined to generate an enhanced selection of likely popular usernames or email addresses.
