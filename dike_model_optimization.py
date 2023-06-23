from ema_workbench import (
    Model,
    MultiprocessingEvaluator,
    ScalarOutcome,
    IntegerParameter,
    optimize,
    Scenario,
)
from ema_workbench.em_framework.optimization import EpsilonProgress
from ema_workbench.util import ema_logging

from problem_formulation import get_model_for_problem_formulation
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == "__main__":
    ema_logging.log_to_stderr(ema_logging.INFO)

    model, steps = get_model_for_problem_formulation(2)

    reference_values = {
        "Bmax": 175,
        "Brate": 1.5,
        "pfail": 0.5,
        "discount rate 0": 3.5,
        "discount rate 1": 3.5,
        "discount rate 2": 3.5,
        "ID flood wave shape": 4,
    }
    scen1 = {
        "A.0_ID flood wave shape": 22,
        "A.1_Bmax": 137.546977,
        "A.1_Brate": 10.0,
        "A.1_pfail": 0.396447,
        "A.2_Bmax": 220.586531,
        "A.2_Brate": 10.0,
        "A.2_pfail": 0.738226,
        "A.3_Bmax": 341.19908,
        "A.3_Brate": 10.0,
        "A.3_pfail": 0.932627,
        "A.4_Bmax": 101.448571,
        "A.4_Brate": 10.0,
        "A.4_pfail": 0.608045,
        "A.5_Bmax": 323.663681,
        "A.5_Brate": 1.0,
        "A.5_pfail": 0.979922,
        "discount rate 0": 3.5,
        "discount rate 1": 4.5,
        "discount rate 2": 1.5}

    for key in model.uncertainties:
        name_split = key.name.split("_")

        if len(name_split) == 1:
            scen1.update({key.name: reference_values[key.name]})

        else:
            scen1.update({key.name: reference_values[name_split[1]]})

    ref_scenario = Scenario("reference", **scen1)

    convergence_metrics = [EpsilonProgress()]

    espilon = [1e3] * len(model.outcomes)

    nfe = 200  # proof of principle only, way to low for actual use

    with MultiprocessingEvaluator(model) as evaluator:
        results, convergence = evaluator.optimize(
            nfe=nfe,
            searchover="levers",
            epsilons=espilon,
            convergence=convergence_metrics,
            reference=ref_scenario,
        )

    fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True)
    fig, ax1 = plt.subplots(ncols=1)
    ax1.plot(convergence.epsilon_progress)
    ax1.set_xlabel("nr. of generations")
    ax1.set_ylabel(r"$\epsilon$ progress")
    sns.despine()
