from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.text_file_knowledge_source  import TextFileKnowledgeSource
from crewai.knowledge.storage.knowledge_storage import KnowledgeStorage
from src.uLawyer.config import embedder
from typing import List

@CrewBase
class EnvolvidoCrew():
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def envolvido_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['envolvido_agent'],
            memory=True,
            respect_context_window=True,
            embedder=embedder.EMBEDDER_DEFAULT,
        )

    @task
    def envolvido_task(self) -> Task:
        return Task(
            config=self.tasks_config['envolvido_task'],
        )

    @crew
    def crew(self) -> Crew:

        case_id = self.inputs.get("case_id")

        text_storage = KnowledgeStorage(
            collection_name="envolvido",
        )

        text_knowledge_source = TextFileKnowledgeSource(
            file_paths=[f"{case_id}.txt"],
            storage=text_storage,
        )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            knowledge_sources=[text_knowledge_source],
        )
