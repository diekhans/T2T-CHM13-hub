import twobitreader
import os.path as osp
from pycbio.sys import fileOps
bindir = osp.abspath(osp.dirname(__file__))

def loadChromNames(twoBit):
    tbr = twobitreader.TwoBitFile(twoBit)
    try:
        return tuple(sorted(tbr.sequence_sizes().keys()))
    finally:
        tbr.close()

def findGenomeDir(assembly):
    asmDir = osp.join(bindir, "../../build", assembly)
    if not osp.exists(asmDir):
        raise Exception("assembly build directory not found: " + asmDir)
    return osp.join(asmDir, "genome")

def findGenomeTwoBit(assembly):
    return osp.join(findGenomeDir(assembly), assembly + ".2bit")
