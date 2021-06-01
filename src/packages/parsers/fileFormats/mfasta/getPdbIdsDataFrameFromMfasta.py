from Bio import SeqIO
import pandas as pd



def getPdbChainsDataFrameFrom(mfasta, columnFlag=str):
    mfastaIterator  = SeqIO.parse(handle=mfasta, format="fasta")

    pdbIdsDict  = dict()
    key         = "pdbChains_%s" % columnFlag
    values      = list()
    for fasta in mfastaIterator:
        pdbId = fasta.description[0:4].lower() + fasta.description[4:]
        values.append(pdbId)
    pdbIdsDict[key] = values
    pdbIdsDataFrame = pd.DataFrame.from_dict(data=pdbIdsDict, 
                                            orient="columns",
                                            dtype=str)
    return pdbIdsDataFrame

# mfasta          = "/home/matias/Projects/2020/RvDb_phyloCodnasHomologues" \
#                 "/outputs/2020-06-23/clustalw/pdbChainIdHomologuesInCodnas" \
#                 "/RV6.fasta"
# pdbIdsDataFrame = getPdbChainsDataFrameFrom(mfasta)
# print()
