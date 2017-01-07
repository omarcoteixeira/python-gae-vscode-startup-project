""" Python dev startup for vs code."""

import os
import sys

import ptvsd

# Assuming that pdvsd is located in the working folder
sys.path.append(os.getcwd())

# Fee free to change the secret and port number
ptvsd.enable_attach(secret='gae', address=('0.0.0.0', 3000))

# The debug server has started and you can now use VS Code
# to attach to the application for debugging
print "Google App Engine has started, ready to attach the debugger"
