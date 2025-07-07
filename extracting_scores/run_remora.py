import pod5, sys, os
from remora import io, refine_signal_map
from tqdm import tqdm
import numpy as np

def run_remora(outfile: str, bam_path: str, pod5_path: str, levels_path: str):
    bam_fh = io.ReadIndexedBam(bam_path)
    pod5_dr = pod5.DatasetReader(pod5_path)
    level_table = levels_path

    sig_map_refiner = refine_signal_map.SigMapRefiner(
        kmer_model_filename=level_table,
        do_rough_rescale = True,
        scale_iters = 1,
        algo = "dwell_penalty",
        do_fix_guage = False,
        rough_rescale_method = "theil_sen",
    )

    read_id = list(pod5_dr.read_ids)[0]

    bam_read = bam_fh.get_first_alignment(read_id)
    pod5_read = pod5_dr.get_read(read_id)
    remora_read = io.Read.from_pod5_and_alignment(
        pod5_read, 
        bam_read,
        reverse_signal=False
    )
    remora_read.set_refine_signal_mapping(sig_map_refiner, ref_mapping=False)
    query_to_signal = remora_read.query_to_signal
    with open(outfile, "w") as f:
        np.savetxt(f, query_to_signal)

if __name__=="__main__":
    outfile = sys.argv[1]
    bam_path = sys.argv[2]
    pod5_path = sys.argv[3]
    levels_path = sys.argv[4]
    run_remora(outfile, bam_path, pod5_path, levels_path)