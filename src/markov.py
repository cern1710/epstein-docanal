import random

class MarkovModel:
    """
    Markov Model for text generation based on n-gram analysis.
    """
    def __init__(self, n_gram: int=1) -> None:
        self.n_gram = n_gram
        self.model = {}

    def train(self, text: list) -> None:
        for i in range(len(text) - self.n_gram):
            # Create current and next states based on n-gram size
            curr_state = ' '.join(text[i:i + self.n_gram])
            next_state = ' '.join(text[i + self.n_gram:i + 2 * self.n_gram])

            # Update counts for observed state transition
            self.model.setdefault(curr_state, {}).setdefault(next_state, 0)
            self.model[curr_state][next_state] += 1

        # Convert counts to probabilities
        for curr_state, transitions in self.model.items():
            total = sum(transitions.values())
            for state in transitions:
                transitions[state] /= total

    def _generate_text(self, start: str, length: int) -> str:
        if start not in self.model:
            raise ValueError(f"Start state '{start}' not in model.")
        current_state = start
        text = [current_state]
        for _ in range(length):
            # Choose next state based on transition probabilities
            next_states = list(self.model[current_state].keys())
            probabilities = list(self.model[current_state].values())
            next_state = random.choices(next_states, probabilities)[0]

            # Update current state and append text
            text.append(next_state)
            current_state = next_state

        return ' '.join(text)

    def create_sentences(self, start: str, length: int, num_lines: int) -> None:
        for i in range(num_lines):
            story = MarkovModel._generate_text(self, start, length)
            print(f"{i+1}: {story}")