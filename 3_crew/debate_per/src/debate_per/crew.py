from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class DebatePer():
    """DebatePer crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def debater(self) -> Agent:
        return Agent(
            config=self.agents_config['debater'], # type: ignore[index]
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'], # type: ignore[index]
            verbose=True
        )

    @task
    def debate_task(self) -> Task:
        return Task(
            config=self.tasks_config['debate_task'], # type: ignore[index]
        )

    @task
    def counter_debate_task(self) -> Task:
        return Task(
            config=self.tasks_config['counter_debater_task']
        )

    @task
    def judege_task(self) -> Task:
        return Task(
            config=self.tasks_config['decide']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DebatePer crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
