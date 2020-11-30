# Slido Data Connector SKD Example

This repository contains a simple example of running queries via the
[Slido Data Connector](https://docs.google.com/document/d/19PLz-NZPXOm5YDNXML9P419BRek7QQymExI0gxlxK9o/edit)
(currently in preview) using [AWS SDK](https://aws.amazon.com/sdk-for-python/) in Python 3+.

### Requirements

For the "basic" example (`query.py`) `boto3` is required (tested with version 1.16.25).

You can install it (along its dependencies) by running the following command:

    $ pip install -r requirements.txt

### Running the example

In order to run the example, the following environment variables need to be
set:

    $ export AWS_ACCESS_KEY_ID=<the value you received>
    $ export AWS_SECRET_ACCESS_KEY=<the value you received>
    $ export SLIDO_ACCOUNT_UUID=<the value you received>

Provided all the requirements are installed, the example can be executed by
running

    $ python query.py

### Running the `aws-data-wrangler` example

The [`aws-data-wrangler`](https://aws-data-wrangler.readthedocs.io/en/latest/index.html)
is a library that allows one to interact with AWS Athena in a Pandas-like
manner (i.e. it automatically creates a Pandas DataFrame from the results,
which can then be easily serialized to various other formats).

In order to run the example, the following environment variables need to be
set:

    $ export AWS_ACCESS_KEY_ID=<the value you received>
    $ export AWS_SECRET_ACCESS_KEY=<the value you received>
    $ export SLIDO_ACCOUNT_UUID=<the value you received>

And install the `aws-data-wrangler`-specific requirements:

    $ pip install -r requirements-wrangler.txt

Provided all the requirements are installed, the example can be executed by
running

    $ python wrangler.py
