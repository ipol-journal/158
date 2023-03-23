#!/usr/bin/env python3

import subprocess
import argparse

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("threshold", type=int)
args = ap.parse_args()

#run algo
with open("output.txt", "w") as fd:
    subprocess.run(['otsus', '-t', str(args.threshold), 'input_0.png', 'output.png'], stdout=fd, stderr=fd)
