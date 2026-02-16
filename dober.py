#!/usr/bin/env python3
"""
DOBer - Date of Birth list generator.

Generates date-of-birth strings in statistically likely order, based on the
assumption that user ages in a target application follow a roughly normal
distribution around a given average age.

Dates radiate outward from the average age, alternating older and younger,
so the most statistically likely dates appear first. Useful for password
attacks where users incorporate their date of birth into passwords.

Ben Williams, 2016 (updated 2026)
"""

import argparse
import sys
from datetime import datetime, timedelta
from itertools import cycle, islice
from typing import Iterator


def roundrobin(*iterables: Iterator) -> Iterator:
    """Yield items from each iterable in turn, until all are exhausted.

    roundrobin('ABC', 'D', 'EF') --> A D E B F C
    Recipe credited to George Sakkis.
    """
    pending = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for n in nexts:
                yield n()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


def generate_dobs(average_age: int, min_age: int, max_age: int, fmt: str) -> Iterator[str]:
    """Generate date-of-birth strings radiating outward from the average age."""
    today = datetime.now()
    base = today - timedelta(days=average_age * 365)

    older = (base - timedelta(days=x) for x in range(1, (max_age - average_age) * 365))
    younger = (base + timedelta(days=x) for x in range(0, (average_age - min_age) * 365))

    for dt in roundrobin(older, younger):
        yield dt.strftime(fmt)


def main():
    parser = argparse.ArgumentParser(
        description="Generate date-of-birth lists in statistically likely order.",
        epilog=(
            "Examples:\n"
            '  python dober.py --format "%%d%%m%%y"\n'
            '  python dober.py --min 21 --max 26 --average 23 --format "%%b-%%d-%%Y" -o dobs.txt\n'
            "  python dober.py --format \"%%Y%%m%%d\" | head -n 1000\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--format",
        default="%d-%m-%y",
        help="strftime format string for dates (default: %%d-%%m-%%y)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file (default: print to stdout)",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=65,
        help="Maximum age (default: 65)",
    )
    parser.add_argument(
        "--min",
        type=int,
        default=18,
        help="Minimum age (default: 18)",
    )
    parser.add_argument(
        "--average",
        type=int,
        default=40,
        help="Average age (default: 40)",
    )

    args = parser.parse_args()

    if args.min >= args.average or args.average >= args.max:
        parser.error("must satisfy: min < average < max")

    dobs = generate_dobs(args.average, args.min, args.max, args.format)

    if args.output:
        with open(args.output, "w") as f:
            for dob in dobs:
                f.write(f"{dob}\n")
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        for dob in dobs:
            print(dob)


if __name__ == "__main__":
    main()
