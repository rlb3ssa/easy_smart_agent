from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.text_file_knowledge_source  import TextFileKnowledgeSource
from crewai.knowledge.storage.knowledge_storage import KnowledgeStorage
from typing import List

@CrewBase
class ExampleCrew():
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def example_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['example_agent'],
            memory=True,
            respect_context_window=True,
        )

    @task
    def example_task(self) -> Task:
        return Task(
            config=self.tasks_config['example_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
        )
