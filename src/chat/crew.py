from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import BaseTool
from src.chat.tools.custom_tool import PDFCreationTool

# Uncomment the following line to use an example of a custom tool
# from chat.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class PDFCrew():
    """Crew responsável por criar PDFs"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def pdf_creator_agent(self) -> Agent:
        """
        Configura o agente que usará a ferramenta PDFCreationTool para criar PDFs.
        """
        return Agent(
            config=self.agents_config['pdf_creator_agent'],
            tools=[PDFCreationTool()],  # Ferramenta customizada para criar PDFs
            verbose=True,
            allow_delegation=False,
            allow_interruption=True,  # Permite interrupções para reagir rapidamente a mudanças nos produtos dos concorrentes
            allow_fallback=True,
        )

    @task
    def generate_pdf_task(self) -> Task:
        """
        Configura a tarefa de geração de PDFs, que instrui o agente a usar o PDFCreationTool.
        """
        return Task(
            config=self.tasks_config['generate_pdf_task'],
        )

    @crew
    def crew(self) -> Crew:
        """
        Cria o Crew com o agente e a tarefa configurados.
        """
        return Crew(
            agents=self.agents,  # Criado automaticamente pelos decoradores @agent
            tasks=self.tasks,    # Criado automaticamente pelos decoradores @task
            process=Process.sequential,
            verbose=True
        )