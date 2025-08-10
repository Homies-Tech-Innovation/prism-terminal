import platform
import os
from datetime import datetime
from src.models import SessionEntryRole


class PromptEngine:
    def format_prompt(
        self,
        system_instructions: str,
        session_memory: str,
        new_prompt: str
    ) -> str:
        # Get system context information
        system_context = self._get_system_context()
       
        return f"""
{system_instructions}

--- System Context ---
Operating System: {system_context['os']}
OS Architecture: {system_context['architecture']}
OS version: {system_context['version']}
OS Username: {system_context['username']}
Shell: {system_context['shell']}
Current Directory: {system_context['current_dir']}
Current Date & Time: {system_context['datetime']}

--- Conversation History ---
{session_memory}
{SessionEntryRole.USER}: {new_prompt}
        """

    def _get_system_context(self) -> dict[str, str]:
        """
        Gathers current system information for context.
       
        Returns:
            Dictionary containing system context information
        """
        try:
            # Get OS information
            os_name = platform.system()
            os_version = platform.version()
            architecture = platform.machine()
           
            # Get username
            username = os.getenv('USERNAME') or os.getenv('USER') or 'Unknown'
           
            # Get shell information
            shell = os.getenv('SHELL') or os.getenv('COMSPEC') or 'Unknown'
           
            # Get current directory
            current_dir = os.getcwd()
           
            # Get current date and time
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
            return {
                'os': os_name,
                'architecture': architecture,
                'version': os_version,
                'username': username,
                'shell': shell,
                'current_dir': current_dir,
                'datetime': current_datetime
            }
        except Exception:
            # Fallback values if system information gathering fails
            return {
                'os': 'Unknown',
                'architecture': 'Unknown',
                'version': 'Unknown',
                'username': 'Unknown',
                'shell': 'Unknown',
                'current_dir': 'Unknown',
                'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }


# Create a singleton instance
prompt_engine = PromptEngine()
