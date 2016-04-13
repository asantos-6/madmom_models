# encoding: utf-8
"""
Models package.

Please see the LICENSE file for licensing details of this package.

"""

from __future__ import absolute_import, division, print_function

import os
import glob

path = os.path.dirname(__file__)

# beats
BEATS_BLSTM = sorted(glob.glob('%s/beats/2013/beats_blstm_[1-8].pkl' % path))
# downbeats
DOWNBEATS_BLSTM = sorted(glob.glob(
    '%s/downbeats/2016/downbeats_blstm_[1-8].pkl' % path))
# notes
NOTES_BRNN = sorted(glob.glob('%s/notes/2013/notes_brnn.pkl' % path))
# onsets
ONSETS_RNN = sorted(glob.glob('%s/onsets/2013/onsets_rnn_[1-8].pkl' % path))
ONSETS_BRNN = sorted(glob.glob('%s/onsets/2013/onsets_brnn_[1-8].pkl' % path))
ONSETS_BRNN_PP = sorted(glob.glob('%s/onsets/2014/onsets_brnn_pp_[1-8].pkl' %
                                  path))
# patterns
PATTERNS_BALLROOM = sorted(
    glob.glob('%s/patterns/2013/ballroom_pattern_[34]_4.pkl' % path))

# keep namespace clean
del os, glob, path