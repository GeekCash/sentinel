# GeekCash Sentinel

An all-powerful toolset for GeekCash.

[![Build Status](https://travis-ci.org/geekcash/sentinel.svg?branch=master)](https://travis-ci.org/geekcash/sentinel)

Sentinel is an autonomous agent for persisting, processing and automating GeekCash governance objects and tasks, and for expanded functions in the upcoming GeekCash V13 release (Evolution).

Sentinel is implemented as a Python application that binds to a local version 12 geekcashd instance on each GeekCash Masternode.

This guide covers installing Sentinel onto an existing Masternode in Ubuntu 14.04 / 16.04.

## Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local GeekCash daemon running is at least version 1.0.1.2 (1000102)

    $ geekcash-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/geekcash/sentinel.git && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### 4. Test the sentinel

At this point, running

    $ venv/bin/python bin/sentinel.py

should return nothing but silence.  This is how you know it's working.

With all tests passing and crontab setup, Sentinel will stay in sync with geekcashd and the installation is complete

## Configuration

An alternative (non-default) path to the `geekcash.conf` file can be specified in `sentinel.conf`:

    geekcash_conf=/path/to/geekcash.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

## Contributing

Please follow the [GeekCash guidelines for contributing](https://github.com/geekcash/geekcash/blob/master/CONTRIBUTING.md).

Specifically:

* [Contributor Workflow](https://github.com/geekcash/geekcash/blob/master/CONTRIBUTING.md#contributor-workflow)

    To contribute a patch, the workflow is as follows:

    * Fork repository
    * Create topic branch
    * Commit patches

    In general commits should be atomic and diffs should be easy to read. For this reason do not mix any formatting fixes or code moves with actual code changes.

    Commit messages should be verbose by default, consisting of a short subject line (50 chars max), a blank line and detailed explanatory text as separate paragraph(s); unless the title alone is self-explanatory (like "Corrected typo in main.cpp") then a single title line is sufficient. Commit messages should be helpful to people reading your code in the future, so explain the reasoning for your decisions. Further explanation [here](http://chris.beams.io/posts/git-commit/).

### License

Released under the MIT license, under the same terms as GeekCash itself. See [LICENSE](LICENSE) for more info.
