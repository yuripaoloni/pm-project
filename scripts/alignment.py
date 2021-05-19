import sys
from import_xes import import_xes
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.conformance.alignments.petri_net import algorithm as alignments
from random import randint
from pprint import pprint


def run_alignment(event_log):
    net, initial_marking, final_marking = alpha_miner.apply(
        event_log)

    traces = []
    # Randomly pick 5 traces in the events log
    for _ in range(5):
        value = randint(0, len(event_log))
        print("\nTrace number: {}".format(value))
        print(*event_log[value], end="\n", sep="\n")
        traces.append(event_log[value])

    aligned_traces = alignments.apply_log(
        traces, net, initial_marking, final_marking)

    pprint(aligned_traces)


if __name__ == "__main__":
    event_log = import_xes(sys.argv[1])
    run_alignment(event_log)
