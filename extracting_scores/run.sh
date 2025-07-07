#!/bin/bash

# Before running the script:
# 1. Change the settings in `remora/extracting_scores/run_remora.py`
# 2. Change the PATH variable in `remora/src/remora/refine_signal_map_core.pyx`
# 3. Change the output file path below

# I'll run it with the following settings: 
# 1. algo = 'Viterbi'; do_rough_rescale = False
# 2. algo = 'dwell_penalty'; do_rough_rescale = False
# 3. algo = 'dwell_penalty'; do_rough_rescale = True

BASEDIR="PATH/TO/remora"

pip install -e $BASEDIR

python "${BASEDIR}/extracting_scores/run_remora.py" \
    "${BASEDIR}/extracting_scores/dwell_penalty_true_alignment.txt" \
    "${BASEDIR}/extracting_scores/test_data/subset.bam" \
    "${BASEDIR}/extracting_scores/test_data/subset.pod5" \
    "${BASEDIR}/extracting_scores/test_data/levels.txt"

