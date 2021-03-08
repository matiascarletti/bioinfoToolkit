import os
import subprocess

def cdhit_getSequenceClustersFrom(mfastaFilePath,
                                outFolderPath,
                                outFileName,
                                seqIdenCutoff=0.90,
                                lenghtDiffCutoff=0.95,
                                lenghtDiffAaCutoff=10,
                                covLongAlnCutoff=int,
                                covLongAaAlnCutoff=int,
                                covShortAlnCutoff=int,
                                covShortAaAlnCutoff=int,
                                covAlnCutoff=int
                                ):
    """
    Purpose: Run cdhit shell command line again a multifasta pdb Database \
            with sequence identity and sequence lenght cutoffs
            - note: for objetives of get Conformational Diversity clusters run with \
                    this defaults setting format:
                                seqIdenCutoff=0.90,
                                lenghtDiffCutoff=0.95,
                                lenghtDiffAaCutoff=10,

            shellCmd: cdhit -i "$1"_seqs.fa -o "$1"_seqs_cdhit.fa -c $7 -s -S -aL -AL -as -AS -A
            sourceCmd: https://gitlab.com/sbgunq/bioinfo-scripts/-/blob/master/BLAST_runner/run_blast.sh

    Parameters:
    - mfastaFilePath    a str path to target blast database
    - outFolderPath     a str path to out folder for saving the output
    - outFileName       a str name of out file in fasta format

    
    -i	input filename in fasta format, required, can be in .gz format
    -o	output filename, required
    # Para controlar el corte en la secuencia de identidad
    -c	sequence identity threshold, default 0.9
    	this is the default cd-hit's "global sequence identity" calculated as:
 	    number of identical amino acids or bases in alignment
 	    divided by the full length of the shorter sequence
    # Para controlar las diferencias en el el largo de las secuencias
    -s	length difference cutoff, default 0.0
        if set to 0.9, the shorter sequences need to be
        at least 90% length of the representative of the cluster
    -S	length difference cutoff in amino acid, default 999999
        if set to 60, the length difference between the shorter sequences
        and the representative of the cluster can not be bigger than 60
    # Para controlar el coverage del alineamiento en la secuenicia más larga, en la más corta o en ambas    
    -aL	alignment coverage for the longer sequence, default 0.0
        if set to 0.9, the alignment must covers 90% of the sequence
    -AL	alignment coverage control for the longer sequence, default 99999999
        if set to 60, and the length of the sequence is 400,
        then the alignment must be >= 340 (400-60) residues
    -aS	alignment coverage for the shorter sequence, default 0.0
        if set to 0.9, the alignment must covers 90% of the sequence
    -AS	alignment coverage control for the shorter sequence, default 99999999
        if set to 60, and the length of the sequence is 400,
        then the alignment must be >= 340 (400-60) residues
    -A	minimal alignment coverage control for the both sequences, default 0
        alignment must cover >= this value for both sequences 
    """
    subprocess.call(["cdhit",
                    "-i", mfastaFilePath,
                    "-o", "%s/%s" % (outFolderPath, outFileName),
                    "-c", seqIdenCutoff,
                    "-s", lenghtDiffCutoff,
                    "-S", lenghtDiffAaCutoff,
                    "-aL", covLongAlnCutoff,
                    "-AL", covLongAlnAaCutoff,
                    "-aS", covShortAlnCutoff,
                    "-AS", covShortAaAlnCutoff,
                    "-A", covAlnCutoff,
                    ],
                    shell=True)
    return