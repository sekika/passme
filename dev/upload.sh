#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`

# Install the source
echo "Installing the source"
pip3 install -e .. > /dev/null

# Test
sh test.sh

# Check version
LATEST=`pip3 search passme | grep ^passme | awk '{print $2}' | sed -e 's/(//' | sed -e 's/)//'`
echo 'Latest version: '$LATEST
CURRENT=`grep version ../setup.py | sed -e "s/^.*version='//" | sed -e "s/',//"`
echo 'Development version: '$CURRENT
if [ $LATEST = $CURRENT ]; then
  echo 'Change version in ../setup.py to upload.'
  exit
fi

# Make package
echo "Making packages."
cd ..
python3 setup.py sdist
python3 setup.py bdist_wheel

# Upload
echo "Preparing PyPI password with passme"
passme python
twine upload "dist/passme-"$CURRENT*

# Uninstall
pip3 uninstall passme
echo "Upload completed. Installed version uninstalled. Wait for a while and run"
echo "pip3 install passme"

