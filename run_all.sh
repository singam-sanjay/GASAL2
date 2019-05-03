#!/bin/bash
./configure.sh /usr/local/cuda-10.0/
make GPU_SM_ARCH=sm_50 MAX_SEQ_LEN=300 N_CODE=4 N_PENALTY=1
cd test_prog
make 262k2 
sha256sum -c crc_out.log.crc
cd ..
sha256sum test_prog/out.log
