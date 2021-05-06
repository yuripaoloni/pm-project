import sys
from import_xes import import_xes
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.petrinet import visualizer as pn_visualizer


def run_heuristic_miner(event_log):
    # Heuristic Net
    heu_net = heuristics_miner.apply_heu(event_log)
    gviz = hn_visualizer.apply(heu_net)
    hn_visualizer.view(gviz)

    # Petri Net
    net, im, fm = heuristics_miner.apply(event_log)
    gviz = pn_visualizer.apply(net, im, fm)
    pn_visualizer.view(gviz)


if __name__ == "__main__":
    event_log = import_xes(sys.argv[1])
    run_heuristic_miner(event_log)
