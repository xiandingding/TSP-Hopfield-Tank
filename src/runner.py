from main import run
from input import read_data
from args_parse import get_args

data = read_data("./input_data/burma14.txt")

args = get_args()

for seed in args.seeds:
    for size_adj in args.size_adjs:
        run(seed, args.steps, size_adj, data, args.freq)
