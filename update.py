#!/usr/bin/env python

import sys
import os
import requests

output_file = "git-annex.sh"
urlprefix = 'https://amnesia.cbrain.mcgill.ca/SIMON_data/SIMON_BIDS/'
directory = sys.argv[1]

with open(output_file, 'w') as out:
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            
            # assert(os.path.exists(path))
            if os.path.islink(path):
                url = (urlprefix + path).replace('./', '')
                code = requests.head(url, verify=False).status_code
                if code != 200:
                    out.write(f'[ WARNING ]: {url} not found')
                out.write(f'datalad remove {path} ; git annex addurl {url} --file {path}{os.linesep}')
