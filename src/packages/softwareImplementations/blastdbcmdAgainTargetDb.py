import os

def blastdbcmdAgain(blastDbPath, dbIdListFile, outFolderPath, outFileName):
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
                                                                    outFileName)
    
    os.system(shellCmd)
    return