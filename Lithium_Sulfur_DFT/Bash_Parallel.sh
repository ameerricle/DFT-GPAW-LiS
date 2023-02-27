#!/bin/bash
#SBATCH --account=rrg-peslherb-ac
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G
#SBATCH --time=0-03:00
#SBATCH --job-name=GPAW-convK

module load gcc/9.3.0 openmpi/4.0.3
source ~/ENV_AN/bin/activate

export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
export GPAW_SETUP_PATH=/scratch/$USER/gpaw-setups-0.9.20000

srun gpaw python /home/anizami/ENV_AN/DFT-GPAW-LiS/Ti_Slab.py
