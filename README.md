# Slido Data Connector SKD Example

This repository contains a simple example of running queries via the
[Slido Data Connector](https://docs.google.com/document/d/19PLz-NZPXOm5YDNXML9P419BRek7QQymExI0gxlxK9o/edit)
(currently in preview) using [AWS SDK](https://aws.amazon.com/sdk-for-python/) in Python.

### Requirements

is `boto3` (tested with version 1.16.25).

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

