from src.models import RouteDecision
from src import settings

class InputRouter():
    COMMAND_PREFIX = settings.COMMAND_PREFIX
    PROMPT_PREFIX = settings.PROMPT_PREFIX
    KNOWN_COMMANDS = settings.KNOWN_COMMANDS
    Q_WORDS = settings.Q_WORDS

    def route_input(self, user_input: str) -> RouteDecision:
        command_confidence = 0.0
        prompt_confidence = 0.0
        processed_input = user_input.lower().strip()
        
        # Command Prefix Detection 
        if user_input.startswith(self.COMMAND_PREFIX):
            return RouteDecision(prediction="command")

        # Prompt Prefix Detection 
        if user_input.startswith(self.PROMPT_PREFIX):
            return RouteDecision(prediction="prompt")
        
        # Command Dictionary Matching
        first_word = processed_input.split(maxsplit=1)[0]
        if first_word in self.KNOWN_COMMANDS:
            command_confidence += 0.7
        else:
            prompt_confidence += 0.2

        # Question Pattern Detection
        if any(q_word in processed_input for q_word in self.Q_WORDS):
            prompt_confidence += 0.5
        else:
            command_confidence += 0.2
        
        # Sentence Length Analysis
        input_len = len(processed_input)
        if input_len<10:
            command_confidence += 0.2
        elif input_len>25:
            prompt_confidence += 0.3
        
        if prompt_confidence>=command_confidence:
            return RouteDecision(prediction='prompt')
        else:
            return RouteDecision(prediction='command')
        
input_router = InputRouter()