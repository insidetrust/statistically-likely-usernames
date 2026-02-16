# statistically-likely-usernames
This resource contains wordlists for creating statistically likely usernames for use in username-enumeration, simulated password-attacks and other security testing tasks.

When many users are present in an application or network, I normally approach password-attacks by guessing likely usernames, (rather than focusing on guessing too many passwords). This has several advantages (such as avoiding account lockout for example) and is almost always successful (usually several users have either "Password1", "password" or something equally trivial).

The best approach is a horizontal password attack, trying one password for thousands of possible usernames.

I originally generated my core username lists from US Census data, though more recently I have been using lists I generated from base lists that someone else extracted from 171 million names indexed on Facebook (this has several advantages) Ref: [See original blog post by Ron Bowes](https://blog.skullsecurity.org/2010/return-of-the-facebook-snatchers). The generated lists here have been tested extensively in live attacks against target networks and applications, and this has resulted in a rapid and very high degree of success (during authorised penetration tests).

The initial reason for generating these username lists was that I wanted to know when it was statistically worthwhile to try z.smith, compared to say j.jackson (or any other name) and create the most efficient set of guesses in the shortest possible time, based on common username formats in statistically likely order.

As you can see below, name popularity follows the pareto curve, so it's best to start with jsmith and work down...

![alt text](https://github.com/insidetrust/statistically-likely-usernames/blob/master/popular-names.JPG "Pareto curves are awesome")

## Start here: Awesome Mix volumes

If you're unsure which list to use, or the username format is unknown, **start with these**. They are interleaved combinations of several of the individual lists below, designed to maximise coverage across multiple common username formats in the fewest guesses.

**awesome-mix-vol1.txt** - ~25,800 usernames. Interleaves the most common format lists (john.smith, jsmith, jjs) with service and test accounts, giving broad coverage of the most likely usernames and common default accounts in a single compact list.

**awesome-mix-vol2.txt** - ~49,400 usernames. A continuation of vol1, picking up where it left off with additional interleaved entries across the same and further formats. Run this after vol1 if you want to go deeper.

Because the entries are interleaved rather than concatenated, each guess cycles through a different format — so even a short run covers multiple naming conventions simultaneously. This makes them ideal as a first pass before falling back to individual targeted lists.

## Individual pre-canned lists and base-lists for generating your own in a variety of targeted formats:

### (Formats of the following pre-canned lists should be self-evident from the filename)

jsmith.txt - 50,000 usernames in a very common format.

john.smith.txt - 250,000 usernames in another very common format (more usernames are typically required here due to the higher entropy).

jjs.txt - All 17,576 three-letter combinations, for the most part sorted by most popular initials. This works surprisingly well.

john.smith-at-example.com.txt - 250,000 email addresses in this common format (replace the example.com with a target domain).

top-formats.txt - A mix in a variety of popular formats (around 1 million examples) interleaved and de-duplicated for ease-of-use. Covers more formats than the Awesome Mix volumes but is much larger and slower — use the Awesome Mix lists first and fall back to this for exhaustive coverage.

john.txt - 10,000 forenames.

smith.txt - 10,000 surnames.

johnsmith.txt - Just under 250,000 examples.

jjsmith.txt - 100,000 examples.

smithjj.txt - 100,000 examples.

johnjs.txt - 100,000 examples.

smithj.txt - 50,000 examples.

johns.txt - 50,000 examples.

jsmith2.txt - A popular format which commonly suffers from collisions (hence jsmith2, jsmith3 etc.). 5,000 examples.

smithj2.txt - As above. 5,000 examples.

## Rolling your own

If this isn't sufficient (and it won't be in some cases, expect that!) the base-lists can be manipulated and combined in a wide variety of ways. For example if a pentester uses Foca, or similar, and identifies that the username format of an organisation is `j_smith` and wants 10,000 guesses (with which to try "Password1", or whatever) the base-lists can be modified as follows:

`head -n 10000 facebook-base-lists/j.smith-x100000.txt | tr "\." "_" > usernames.txt`

Alternatively, if the username would be `jwilliams`, but is always truncated to 7 characters, such as `jwillia`:

`head -n 10000 facebook-base-lists/j.smith-x100000.txt | tr -d "." | cut -c1-7 | awk '!x[$0]++' > usernames.txt`

**Important:** when truncating usernames, duplicates can be generated, so it is very important to remove these, especially when used with password attacks where lockout is present. This can be done, whilst keeping statistically likely order, with the `awk '!x[$0]++'` command (as shown above).

Unusual Email address formats can be created as follows for example `smith-j@example.com`:

`head -n 10000 facebook-base-lists/j.smith-x100000.txt | awk -F "." '{ print $2 "-" $1 }' | sed 's/$/@example.com/g' > usernames.txt`

Obviously a wider variety of formats can be combined to generate an enhanced selection of likely popular usernames or email addresses.
