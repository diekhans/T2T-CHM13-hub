"""configuration file for transMap batch run"""

import os
from transMap.transMapConf import TransMapConf
from transMap.genomeData import ChainType


def getConfig(configPyFile, dataRootDir=None, srcHgDb=None, destHgDb=None,
              annotationType=None, chainType=None):
    version = "V1"

    # increment to prevent reusing batch directories on restart
    batchGen = 2
    asm = "t2tChm13_20200727"
    buildDir = "/hive/users/markd/nanopore/projs/t2t-chm13/build/" + asm
    genomeDir = os.path.join(buildDir, "genome")
    dataRootDir = os.path.join(buildDir, "transMap/tmp")
    conf = TransMapConf(configPyFile,
                        paraHost="hgwdev",
                        dataRootDir=dataRootDir,
                        srcHgDb=srcHgDb,
                        destHgDb=destHgDb,
                        annotationType=annotationType,
                        chainType=chainType,
                        version=version,
                        batchGen=batchGen,
                        destTwoBitPathPat=os.path.join(genomeDir, asm + ".2bit"),
                        destChromSizesPat=os.path.join(genomeDir, asm + ".sizes"))
    return conf
