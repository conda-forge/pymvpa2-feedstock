import os
import sys
import matplotlib

matplotlib.use('Agg')
os.environ.update({
  'MVPA_TESTS_LABILE': 'no',   
  'MVPA_TESTS_LOWMEM': 'yes',  # stay friendly
  'MVPA_SEED': '1',            # not a time to "sweep"
})

import mvpa2

mvpa2.test(verbosity=3, exit_=True)
