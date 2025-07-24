from src.models import ExitCode

class OutputProcessor:
    MAX_SIZE = 8000
    KEEP_START = 2000
    KEEP_END = 4000
    
    def process_output(self, output: str, exit_code: ExitCode) -> str:
        # If command failed, always return full output (preserve errors)
        if exit_code.exit_code != 0:
            return f"Command failed (exit code {exit_code.exit_code}):\n{output}"
        
        # If output is small enough, return as-is
        if len(output) <= self.MAX_SIZE:
            return output
        
        # Apply intelligent truncation
        start_part = output[:self.KEEP_START]
        end_part = output[-self.KEEP_END:]
        middle_size = len(output) - self.KEEP_START - self.KEEP_END
        
        truncated = (
            f"{start_part}\n"
            f"\n... [truncated {middle_size} characters] ...\n\n"
            f"{end_part}"
        )
        
        return truncated

output_processor = OutputProcessor()