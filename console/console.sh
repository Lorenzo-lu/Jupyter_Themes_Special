#!/bin/bash

jupyter --config > jupyter_path.txt
python3 console.py
rm jupyter_path.txt
