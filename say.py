#import cowsay
import sys
from sayings import goodbye

# if len(sys.argv) == 2:
#     cowsay.trex("Hello, " + sys.argv[1])

if len(sys.argv) == 2:
    goodbye(sys.argv[1])