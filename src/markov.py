import numpy as np

class HiddenMarkovModel:
    """
    Stores parameters of a Hidden Markov Model.
    """
    def __init__(
        self,
        states: set,
        observations: set,
        init_prob: dict,
        trans_prob: np.array,
        emm_prob: np.array,
    ) -> None:
        self.states = states
        self.observations = observations
        self.init_prob = init_prob
        self.trans_prob = trans_prob
        self.emis_prob = emis_prob