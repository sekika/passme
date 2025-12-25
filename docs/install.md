---
layout: page
title: Install
permalink: /install/
---

# Install passme

### Install Python 3

Install Python 3.6 or higher using one of the following methods:

*   Download and install from the [Python official page](https://www.python.org/).
*   If you are using [Ubuntu or Debian on Windows Subsystem for Linux (WSL)](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux), run: `sudo apt install python3`
*   If you are using [Homebrew](https://brew.sh/) on macOS, run: `brew install python3`

### Install pip

Run the following command:

```bash
> python3 -m ensurepip
```

This will install `pip` if it is not already installed on your system.

### Install passme

Install the package via pip:

```bash
> pip3 install passme
```

You can check the [latest version on PyPI](https://pypi.python.org/pypi/passme) and your installed version by running:

```bash
> pip3 search passme
```

To upgrade to the latest version:

```bash
> pip3 install -U passme
```

---

[Top page](../)