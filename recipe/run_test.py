import os
import sys
import matplotlib

matplotlib.use('Agg')
os.environ.update({
  'MVPA_TESTS_LABILE': 'no',
  'MVPA_TESTS_LOWMEM': 'yes',
})

import mvpa2

mvpa2.test(verbosity=2, exit_=True)
