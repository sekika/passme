Install passme
=======================

Install Python 3
---------------

Install Python 3.4 or higher by either of the following.

* Download and install from `Python official page <https://www.python.org/>`_.
* If you are using `Ubuntu or Debian of Windows subsystem on Linux <https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux>`_, just run "sudo apt install python3"
* If you are using `Homebrew <https://brew.sh/>`_ on macOS, just run "brew install python3"

Install pip
---------------

Just run

.. code-block:: bash

 > python3 -m ensurepip

then pip is installed if it is not installed on your system.

On Windows subsystems on Linux, pip distributed with apt package may not properly work (it does not properly execute the entry points). Therefore, if python3-pip is already installed by apt, remove it with

.. code-block:: bash

 > sudo apt remove python3-pip

and then install pip properly by

.. code-block:: bash

 > sudo apt install wget
 > wget https://bootstrap.pypa.io/get-pip.py
 > sudo python3 get-pip.py

Install passme
---------------

.. code-block:: bash

 > pip3 install passme

or, on Windows subsystem on Linux,

.. code-block:: bash

 > sudo pip install passme

Check the `latest version <https://pypi.python.org/pypi/passme>`_ and installed version by

.. code-block:: bash

 > pip3 search passme

Upgrade to the latest version by

.. code-block:: bash

 > pip3 install -U passme

----

Toppage_

.. _Toppage: README.rst
