@echo off

set MVPA_TESTS_LABILE=no 
set MVPA_TESTS_LOWMEM=yes 
set MVPA_SEED=1

set MVPA_MATPLOTLIB_BACKEND=agg

%PYTHON% -m nose -s -v mvpa2
