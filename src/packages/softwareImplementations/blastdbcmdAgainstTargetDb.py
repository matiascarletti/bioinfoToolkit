#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Blastdbcmd runner again a target database
{License_info}
"""

# Futures
from __future__ import print_function
# […]

# Built-in/Generic Imports
import os
# […]

# Libs
# […]

# Own modules
# […]

__author__ = 'Matías Carletti'
__copyright__ = 'Copyright 2021, bioinfoToolkit'
__credits__ = ['{credit_list}']
__license__ = '{license}'
__version__ = '{mayor}.{minor}.{rel}'
__maintainer__ = '{maintainer}'
__email__ = 'matias.carletti@gmail.com'
__status__ = '{dev_status}'


def blastdbcmd_getMfastaFrom(blastDbPath, 
                            dbIdListFile, 
                            outFolderPath, 
                            outMfastaName):
    """
    Purpose: Run blastdbcmd shell command line again a target blast database
            shellCmd: blastdbcmd -db $2 -entry $(cat "$1"_ids) > "$1"_seqs.fa
            sourceCmd: https://gitlab.com/sbgunq/bioinfo-scripts/-/blob/master/BLAST_runner/run_blast.sh
    Parameters:
    - blastDbPath   a str path to target blast database
    - dbIdListFile  a str path to database Id list in comma separated values format 
    - outFolderPath a str path to out folder for saving the output
    - outFileName   a str name of out file in fasta format
    """
    # make out folder for saving the output
    try:
        os.makedirs(outFolderPath)
    except FileExistsError:
        print("Out folder already exist")    
    # seting the shell command line
    shellCmd = "blastdbcmd -db %s -entry $(cat %s) > %s/%s.fasta" % (blastDbPath, 
                                                                    dbIdListFile, 
                                                                    outFolderPath, 
                                                                    outMfastaName)
    
    os.system(shellCmd)
    return