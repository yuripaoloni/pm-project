import sys
from import_xes import import_xes
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petrinet import visualizer as pn_visualizer


def run_alpha_miner(event_log):
    # Petri Net
    net, initial_marking, final_marking = alpha_miner.apply(event_log)
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    pn_visualizer.view(gviz)


if __name__ == "__main__":
    event_log = import_xes(sys.argv[1])
    run_alpha_miner(event_log)
