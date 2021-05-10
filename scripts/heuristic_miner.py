import sys
from import_xes import import_xes
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.petri_net import visualizer as pn_visualizer

# TODO parsing command line arguments for heuristic miner parameters and printing of petri net


def run_heuristic_miner(event_log):
    # Heuristic Net
    parameters = {heuristics_miner.Variants.CLASSIC.value.Parameters.MIN_DFG_OCCURRENCES: 50, heuristics_miner.Variants.CLASSIC.value.Parameters.MIN_ACT_COUNT: 50,
                  heuristics_miner.Variants.CLASSIC.value.Parameters.DFG_PRE_CLEANING_NOISE_THRESH: 0.3, heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.8}
    heu_net = heuristics_miner.apply_heu(event_log, parameters)

    gviz = hn_visualizer.apply(heu_net)
    hn_visualizer.view(gviz)

    # Petri Net
    net, im, fm = heuristics_miner.apply(
        event_log, parameters)
    gviz = pn_visualizer.apply(net, im, fm)
    pn_visualizer.view(gviz)


if __name__ == "__main__":
    event_log = import_xes(sys.argv[1])
    run_heuristic_miner(event_log)
