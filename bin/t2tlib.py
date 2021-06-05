import twobitreader
import os.path as osp
bindir = osp.abspath(osp.dirname(__file__))

def loadChromInfo(twoBit):
    """map of chrom names to sizes"""
    tbr = twobitreader.TwoBitFile(twoBit)
    try:
        return dict(tbr.sequence_sizes())
    finally:
        tbr.close()

def loadChromNames(twoBit):
    return tuple(sorted(loadChromInfo(twoBit)))

def findGenomeDir(assembly):
    asmDir = osp.join(bindir, "../../build/dev", assembly)
    if not osp.exists(asmDir):
        raise Exception("assembly build directory not found for {}: {}".format(assembly, asmDir))
    return osp.join(asmDir, "genome")

def findGenomeTwoBit(assembly):
    return osp.join(findGenomeDir(assembly), assembly + ".2bit")
