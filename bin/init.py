"""Top-level package for FRA."""
# Fraud_Risk_Assessment_Tool/_init.py

from main import main

import os

def init():
        os.system("python -m pip install -r Makefile")
        main()


init()