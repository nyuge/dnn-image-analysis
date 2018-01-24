#!/bin/sh
WGET_REFERENCE_URL="http://btsd.ethz.ch/shareddata/"
DATA_RAW_DIRPATH="$(cd $(dirname $0); pwd)/../../data/raw"

wget -A zip -r --wait 1 $WGET_REFERENCE_URL -P $DATA_RAW_DIRPATH
exit 0
