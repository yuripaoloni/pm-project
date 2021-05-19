import sys
from import_xes import import_xes
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from random import randint
from pprint import pprint


def run_token_replay(event_log):
    net, initial_marking, final_marking = heuristics_miner.apply(
        event_log)

    traces = []

    # Randomly pick 5 traces in the events log
    for _ in range(5):
        value = randint(0, len(event_log))
        print("\nTrace number: {}".format(value))
        print(*event_log[value], end="\n", sep="\n")
        traces.append(event_log[value])

    replayed_traces = token_replay.apply(
        traces, net, initial_marking, final_marking)

    pprint(replayed_traces)


if __name__ == "__main__":
    event_log = import_xes(sys.argv[1])
    run_token_replay(event_log)
