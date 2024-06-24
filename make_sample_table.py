#! /usr/bin/env python
import os
import logging
import pandas as pd
from collections import defaultdict

def get_sample_files(path):
    samples = defaultdict(dict)
    seen = set()
    for dir_name, sub_dirs, files in os.walk(os.path.abspath(path)):
        for fname in files:
            if ".fastq.gz" in fname:
                sample_id = fname.split(".fastq.gz")[0]
                sample_id = sample_id.replace("_R1", "").replace("_R2", "")
                fq_path = os.path.join(dir_name, fname)
                if "_R1" in fname:
                    samples[sample_id]['R1'] = fq_path
                else:
                    samples[sample_id]['R2'] = fq_path
    samples= pd.DataFrame(samples).T
    samples.index.name = 'sample_id'
    samples.to_csv(sys.argv[1] + "config.tsv",sep='\t')
    return samples
if __name__ == '__main__':
    import sys
    get_sample_files(sys.argv[1] +"00_raw")