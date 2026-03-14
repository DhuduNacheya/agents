#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime

from debate_per.crew import DebatePer


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Need of developers in era of AI LLMs'
    }

    try:
        DebatePer().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

