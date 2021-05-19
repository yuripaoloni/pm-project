# pm-project

Application of Process Mining techniques and algorithms on artificial logs generated from the execution of a process model. [PM4PY](https://pm4py.fit.fraunhofer.de) was used to run the algorithms and [PLG](https://plg.processmining.it/) to generate the artificial logs over the process model.

## Structure

The repository has the following folder structure:

- _scripts_ : contains the Python scripts defined to run the Process Discovery and Conformance Checking algorithms.
- _logs_ : contains the artificial logs used in the application.
- _models_ : contains the models from which the logs have been generated and the output models from the Process Discovery algorithms.
- _docs_ : contains the project documentation

## Execution

To execute the scripts, PM4PY must be [installed](https://pm4py.fit.fraunhofer.de/install). Then, each script can be executed by providing as an argument the log under analysis:

```bash
python .\scripts\heuristic_miner.py .\logs\log_high_noise.xes
```

## Author

- **Yuri Paoloni** - [yuripaoloni](https://github.com/yuripaoloni)
