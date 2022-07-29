import os
from datetime import timedelta

LICENSE_FILE_NAMES = [
    "LICENSE.md",
    "LICENSE",
    "LICENSE.txt",
    "LICENSE.rst",
    "LICENCE.mit",
    "LICENSE-MIT",
    "LICENSE-APACHE",
    "LICENCE.md",
    "COPYING",
    "COPYING.txt",
    "COPYING.md",
    "COPYING.rst",
    "license",
    "license.txt",
    "license.md",
    "license.rst",
    "license.mit",
    "licence.md",
    "copying",
    "copying.txt",
    "copying.md",
    "copying.rst",
    "License.md",
]

BRANCH_NAMES = [
    "master", "main", "latest"
]

SECONDS_BEFORE_EXPIRATION = int(os.environ.get('SECONDS_BEFORE_EXPIRATION', 0))
MINUTES_BEFORE_EXPIRATION = int(os.environ.get('MINUTES_BEFORE_EXPIRATION', 0))
HOURS_BEFORE_EXPIRATION = int(os.environ.get('HOURS_BEFORE_EXPIRATION', 0))
DAYS_BEFORE_EXPIRATION = int(os.environ.get('DAYS_BEFORE_EXPIRATION', 0))
WEEKS_BEFORE_EXPIRATION = int(os.environ.get('WEEKS_BEFORE_EXPIRATION', 1))

DELTA_BEFORE_EXPIRATION = timedelta(
    seconds=SECONDS_BEFORE_EXPIRATION,
    minutes=MINUTES_BEFORE_EXPIRATION,
    hours=HOURS_BEFORE_EXPIRATION,
    days=DAYS_BEFORE_EXPIRATION,
    weeks=WEEKS_BEFORE_EXPIRATION
)

NPM_LICENSE_STORAGE = os.environ.get('NPM_LICENSE_STORAGE',
                                     'https://raw.githubusercontent.com')
