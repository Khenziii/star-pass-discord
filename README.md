## STAR-PASS Discord bot

STAR-PASS is an ECI ([European Citizens' Initiative](https://en.wikipedia.org/wiki/European_Citizens%27_Initiative)) aimed at granting EU citizens a choice between national passport covers and shared EU ones. Read more about it [here](https://star-pass.eu).

This repository contains the source code of a Discord bot used in STAR-PASS' official server.

### Features

- automatically posting most recent social media posts to a predefined Discord channel-->
<!-- - tracking the progress of signature collection (there should be a command for this, as well as a channel in which the bot would regularly send messages such as "we've collected 5% of the votes!") TODO: move this comment to an issue -->

### Development environment

Copy and fill out the environment variables:

```shell
$ cp .env.example .env
```

And then run those commands:

```shell
$ python3 -m venv env
$ source env/bin/activate
$ poetry install
```

<!-- ### Self-hosting -->
