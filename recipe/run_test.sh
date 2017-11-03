#!/bin/bash

set -eu
export MVPA_TESTS_LABILE=no 
export MVPA_TESTS_LOWMEM=yes 
export MVPA_SEED=1

export MVPA_MATPLOTLIB_BACKEND=agg 

python -m nose -s -v mvpa2
