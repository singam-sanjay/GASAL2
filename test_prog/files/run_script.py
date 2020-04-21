#!/usr/bin/python3.6
# ./test_prog.out -p -y local query_batch.fasta target_batch.fasta > golden.log
#!/usr/local/bin/python3.7
# code_name = 'T{}_Q{}'.format(tlen, qlen)
# command_str = './test_prog.out -p -y local {}.txt_Q {}.txt_T > golden_{}.log'.format(code_name, code_name, code_name)

import os

len_ = [100, 500, 1000, 2500, 5000, 7500, 10000]

for i  in range(len(len_)):
  for j in range(i+1):
    tlen = len_[i]
    qlen = len_[j]
    code_name = 'T{}_Q{}'.format(tlen, qlen)
    cmd_str = '../test_prog.out -t -p -y local {}.txt_Q {}.txt_T > golden_{}.log 2> output_{}.log'.format(code_name, code_name, code_name, code_name)
    print('command: {}'.format(cmd_str))
    os.system(cmd_str)
