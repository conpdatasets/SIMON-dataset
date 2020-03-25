#!/usr/bin/env bash

URLPRE="https://amnesia.cbrain.mcgill.ca/SIMON_data/SIMON_BIDS/"
FILEPRE="./data_BIDS"
for file in $(awk -F 'SIMON_BIDS/' '{print $2}' all_urls_clean.txt)
do
    echo git-annex addurl --fast ${URLPRE}/${file} --file ${FILEPRE}/${file}
done