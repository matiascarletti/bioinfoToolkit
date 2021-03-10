#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Blastp runner again a target database
{License_info}
"""

# Futures
from __future__ import print_function
# […]

# Built-in/Generic Imports
import subprocess
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


def blastp_getHomologuesFrom(blastDbPath=str, 
                            queryFasta=str,
                            outFolderPath=str,
                            outFileName=str,
                            outFileFormat=6, 
                            evalueCutoff=1E-10, 
                            numAlignementsCutoff=1000,
                            queryCoverageCutoff=70, 
                            sortHitsByParam=3,    
                            sortHspsByParam=3):
    """
    Purpose: Run blastp shell command line again a blast Database \
            with evalue and num alignemnts and query coverage cutoffs
            - note: for objetives of get homologues sequences run with \
                    this defaults setting format:
                                sevalueCutoff=1E-10, 
                                numAlignementsCutoff=1000,
                                queryCoverageCutoff=70

            shellCmd: blastp -query $1 -db $2 -evalue $3 -out "$1"_out -outfmt '6 qaccver qlen qstart qend sseqid saccver slen sstart send length nident gaps evalue pident qcovs' -num_alignments $4
            sourceCmd: https://gitlab.com/sbgunq/bioinfo-scripts/-/blob/master/BLAST_runner/run_blast.sh

    Parameters:
    - blastDbPath           a srt for set the blast database path 
    - queryFastaPath        a str for set the query fasta path
    - outFolderPath=str     a str for set out folder path 
    - outBlastName=str      a str for set out file name
    - outFileFormat         a int for set out file format. 6 = Tabular.
    - evalueCutoff          a int for set the evalue cutoff (scientific format). 
    - numAlignementsCutoff  a int for set the number of alignements cutoff. 1000 for get homologues
    - queryCoverageCutoff   a int for set the query coveraget cutoff. 1E-10 for get homologues
    - sortHitsByParam       a int for set the sorting of hits. 4 = Sort by query coverage
    - sortHspsByParam       a int for set the sorting of hsps. 3 = Sort by hsp percent identity

    *** Input query options
    -query <File_In>
    Input file name
    Default = `-'

    *** General search options
    -db <String>
    BLAST database name
        * Incompatible with:  subject, subject_loc
    -out <File_Out>
    Output file name
    Default = `-'
    -evalue <Real>
    Expectation value (E) threshold for saving hits 
    Default = `10'
    -threshold <Real, >=0>
    Minimum word score such that the word is added to the BLAST lookup table

    *** Formatting options
    -outfmt <String>
    alignment view options:
        0 = Pairwise,
        1 = Query-anchored showing identities,
        2 = Query-anchored no identities,
        3 = Flat query-anchored showing identities,
        4 = Flat query-anchored no identities,
        5 = BLAST XML,
        6 = Tabular,
        7 = Tabular with comment lines,
        8 = Seqalign (Text ASN.1),
        9 = Seqalign (Binary ASN.1),
        10 = Comma-separated values,
        11 = BLAST archive (ASN.1),
        12 = Seqalign (JSON),
        13 = Multiple-file BLAST JSON,
        14 = Multiple-file BLAST XML2,
        15 = Single-file BLAST JSON,
        16 = Single-file BLAST XML2,
        18 = Organism Report
    
    Options 6, 7 and 10 can be additionally configured to produce
    a custom format specified by space delimited format specifiers,
    or by a token specified by the delim keyword.
        E.g.: "17 delim=@ qacc sacc score".
    The delim keyword must appear after the numeric output format
    specification.
    The supported format specifiers are:
            qseqid means Query Seq-id
            qgi means Query GI
            qacc means Query accesion
        qaccver means Query accesion.version
            qlen means Query sequence length
            sseqid means Subject Seq-id
        sallseqid means All subject Seq-id(s), separated by a ';'
            sgi means Subject GI
            sallgi means All subject GIs
            sacc means Subject accession
        saccver means Subject accession.version
        sallacc means All subject accessions
            slen means Subject sequence length
            qstart means Start of alignment in query
            qend means End of alignment in query
            sstart means Start of alignment in subject
            send means End of alignment in subject
            qseq means Aligned part of query sequence
            sseq means Aligned part of subject sequence
            evalue means Expect value
        bitscore means Bit score
            score means Raw score
            length means Alignment length
            pident means Percentage of identical matches
            nident means Number of identical matches
        mismatch means Number of mismatches
        positive means Number of positive-scoring matches
        gapopen means Number of gap openings
            gaps means Total number of gaps
            ppos means Percentage of positive-scoring matches
            frames means Query and subject frames separated by a '/'
            qframe means Query frame
            sframe means Subject frame
            btop means Blast traceback operations (BTOP)
            staxid means Subject Taxonomy ID
        ssciname means Subject Scientific Name
        scomname means Subject Common Name
        sblastname means Subject Blast Name
        sskingdom means Subject Super Kingdom
        staxids means unique Subject Taxonomy ID(s), separated by a ';'
                (in numerical order)
        sscinames means unique Subject Scientific Name(s), separated by a ';'
        scomnames means unique Subject Common Name(s), separated by a ';'
        sblastnames means unique Subject Blast Name(s), separated by a ';'
                (in alphabetical order)
        sskingdoms means unique Subject Super Kingdom(s), separated by a ';'
                (in alphabetical order) 
            stitle means Subject Title
        salltitles means All Subject Title(s), separated by a '<>'
        sstrand means Subject Strand
            qcovs means Query Coverage Per Subject
        qcovhsp means Query Coverage Per HSP
            qcovus means Query Coverage Per Unique Subject (blastn only)
    When not provided, the default value is:
    'qaccver saccver pident length mismatch gapopen qstart qend sstart send
    evalue bitscore', which is equivalent to the keyword 'std'
    Default = `0'
    -show_gis
    Show NCBI GIs in deflines?
    -num_descriptions <Integer, >=0>
    -num_descriptions <Integer, >=0>
     Number of database sequences to show one-line descriptions for
    Not applicable for outfmt > 4
    Default = `500'
        * Incompatible with:  max_target_seqs
    -num_alignments <Integer, >=0>
    Number of database sequences to show alignments for
    Default = `250'
        * Incompatible with:  max_target_seqs

    (...)
    -sorthits <Integer, (>=0 and =<4)>
    Sorting option for hits:
    alignment view options:
        0 = Sort by evalue,
        1 = Sort by bit score,
        2 = Sort by total score,
        3 = Sort by percent identity,
        4 = Sort by query coverage
    Not applicable for outfmt > 4
    -sorthsps <Integer, (>=0 and =<4)>
    Sorting option for hps:
        0 = Sort by hsp evalue,
        1 = Sort by hsp score,
        2 = Sort by hsp query start,
        3 = Sort by hsp percent identity,
        4 = Sort by hsp subject start
    Not applicable for outfmt != 0

    (...)
    
    *** Restrict search or results
    (...)
    -qcov_hsp_perc <Real, 0..100>
    Percent query coverage per hsp
    -max_hsps <Integer, >=1>
    Set maximum number of HSPs per subject sequence to save for each query
    -culling_limit <Integer, >=0>
    If the query range of a hit is enveloped by that of at least this many
    higher-scoring hits, delete the hit
        * Incompatible with:  best_hit_overhang, best_hit_score_edge
    -best_hit_overhang <Real, (>0 and <0.5)>
    Best Hit algorithm overhang value (recommended value: 0.1)
        * Incompatible with:  culling_limit
    -best_hit_score_edge <Real, (>0 and <0.5)>
    Best Hit algorithm score edge value (recommended value: 0.1)
        * Incompatible with:  culling_limit
    -subject_besthit
    Turn on best hit per subject sequence

    """
    # make out folder for saving the output
    try:
        os.makedirs(outFolderPath)
    except FileExistsError:
        print("Out folder alredy exist")
    # seting the shell command line
    subprocess.call([
                    "-db", blastDbPath,
                    "-query", queryFasta,
                    "-evalue", str(evalueCutoff),
                    "-out", "%s/%s" % (outFolderPath, outFileName),
                    "-outfmt", str(outFileFormat) + " qaccver qlen qstart qend sseqid saccver slen sstart send length nident gaps evalue pident qcovs",
                    "-num_alignments", str(numAlignementsCutoff),
                    "-qcov_hsp_per", str(queryCoverageCutoff),
                    "-sorthits", str(sortHitsByParam),
                    "-sorthsps", str(sortHspsByParam)
                    ], 
                    shell=False
                    )
    return