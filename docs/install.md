---
layout: page
title: Install
permalink: /install/
---

# Install Passme

## iOS app

Install the Flutter-based iOS app from the [App Store](https://apps.apple.com/us/app/password-passme/id6830239169). Python is not required on your phone. See [Mobile](../mobile/) for sitekey import and usage instructions.

## JavaScript version

Use the Python / CLI version to generate an HTML file with `passme html`, then open it in a browser. Python is not required on the device opening the HTML file. See [JavaScript](../javascript/) for details.

## Python / CLI version

Install [Python 3](https://wiki.python.org/moin/BeginnersGuide/Download) and install the passme package with [pip](https://pip.pypa.io/en/stable/getting-started/) by

```bash
> python -m pip install passme
```

or to specify Python 3

```bash
> python3 -m pip install passme
```

You can check the [latest version on PyPI](https://pypi.python.org/pypi/passme) and your installed version by running:

```bash
> python -m pip show passme
```

To upgrade to the latest version:

```bash
> python -m pip install --upgrade passme
```

---

[Top page](../)