import pprint
import ppfactors
import sys
import logging
import multiprocessing


def test_primality(factor):
    try:
        prime = True
        for factor in ppfactors1:
            if i == factor:
                prime = False
                break
            elif i % factor == 0:
                prime = False
                break

        if prime:
            ppfactors1.add(i)
            logging.info(str(i) + " is prime!")
        elif i % 100000 == 0:
            logging.info("i is " + str(i))
            pass
        else:
            logging.debug(str(i) + " is not prime!")
            pass
    except (KeyboardInterrupt):
        print "stopping factors"


logging.basicConfig(
    level=logging.INFO, format=" %(asctime)s - %(levelname)s " "- %(message)s"
)

ppfactors1 = ppfactors.ppfactors
p = multiprocessing.Pool(multiprocessing.cpu_count())

p.map(test_primality, range(1, sys.maxint))

ppfile = open("ppfactors.py", "w")
logging.info("opening file")
ppfile.write("ppfactors = " + pprint.pformat(ppfactors1) + "\n")
logging.info("writing file")
ppfile.close()
logging.info("closing file")

# primality test:

# take integer in xrange(2, positive infinity) 5

#  modulus divide integer by all previous factors 5 % 13

# if modulus == 0 number is not prime
