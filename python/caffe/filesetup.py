"""Creates the text label files needed for training from a directory of suitably-named jpgs.
"""

import os
import sys
import glob

if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage: %s <wordnet labels file> <image folder> <output text file>' % \
        os.path.basename(sys.argv[0])
  else:
      wordnet_id_indexes = {}
      for index, id in enumerate(open(sys.argv[1]).readlines()):
          wordnet_id_indexes[id] = index

      output = open(sys.argv[3], 'wb')

      for file in glob.iglob(sys.argv[2] + '/*.jpg'):
          id, rest = os.path.basename(file).split('_', 2)
          index = wordnet_id_indexes[id]
          output.write('%s %d\n' % (file, index))

      output.close