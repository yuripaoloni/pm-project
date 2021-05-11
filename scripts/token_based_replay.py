import sys
from import_xes import import_xes
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from random import seed, randint
from pprint import pprint


def run_token_replay(event_log):
    net, initial_marking, final_marking = alpha_miner.apply(
        event_log)

    traces = []

    # Randomly pick 5 traces in the events log
    seed(1)
    for _ in range(5):
        value = randint(0, len(event_log))
        traces.append(event_log[value])

    replayed_traces = token_replay.apply(
        traces, net, initial_marking, final_marking)

    pprint(replayed_traces)


if __name__ == "__main__":
    event_log = import_xes(sys.argv[1])
    run_token_replay(event_log)
