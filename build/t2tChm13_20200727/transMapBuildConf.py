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
    dataRootDir = os.path.join(buildDir, "transMap/tmp")
    conf = TransMapConf(configPyFile,
                        dataRootDir=dataRootDir,
                        srcHgDb=srcHgDb,
                        destHgDb=destHgDb,
                        annotationType=annotationType,
                        chainType=chainType,
                        version=version,
                        batchGen=batchGen,
                        destTwoBitPathPat=os.path.join(dataDir, "genome/" + asm + ".2bit"),
                        destChromSizesPat=os.path.join(dataDir, "genome/" + asm + ".sizes"),
    return conf
