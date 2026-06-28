import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ExaSearchTool






@CrewBase
class ServiceOpsIncidentTriageCrew:
    """ServiceOpsIncidentTriage crew"""

    def _llm_from_connection(self) -> LLM:
        """
        Build LLM config from connection-style environment settings.
        In AMP, prefer configuring model connection values (MODEL, optional
        base URL/key) instead of relying on OPENAI_API_KEY directly.
        """
        model = os.getenv("MODEL") or os.getenv("OPENAI_MODEL_NAME") or "gpt-4o-mini"
        base_url = os.getenv("MODEL_BASE_URL") or os.getenv("LITELLM_BASE_URL")
        api_key = (
            os.getenv("MODEL_API_KEY")
            or os.getenv("LITELLM_API_KEY")
            or os.getenv("API_KEY")
        )

        llm_kwargs = {"model": model}
        if base_url:
            llm_kwargs["base_url"] = base_url
        if api_key:
            llm_kwargs["api_key"] = api_key

        return LLM(**llm_kwargs)

    @agent
    def incident_intake_normalization_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["incident_intake_normalization_specialist"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=self._llm_from_connection(),
        )

    @agent
    def senior_site_reliability_diagnostician(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_site_reliability_diagnostician"],
            tools=[ExaSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=self._llm_from_connection(),
        )

    @agent
    def remediation_runbook_policy_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["remediation_runbook_policy_analyst"],
            tools=[ExaSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=self._llm_from_connection(),
        )

    @agent
    def on_call_engineer_approval_gate(self) -> Agent:
        return Agent(
            config=self.agents_config["on_call_engineer_approval_gate"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=self._llm_from_connection(),
        )

    @agent
    def incident_record_audit_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config["incident_record_audit_compiler"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=self._llm_from_connection(),
        )

    @task
    def parse_incident_task(self) -> Task:
        return Task(
            config=self.tasks_config["parse_incident_task"],
            markdown=False,
        )

    @task
    def diagnose_incident_task(self) -> Task:
        return Task(
            config=self.tasks_config["diagnose_incident_task"],
            markdown=False,
        )

    @task
    def policy_check_remediation_task(self) -> Task:
        return Task(
            config=self.tasks_config["policy_check_remediation_task"],
            markdown=False,
        )

    @task
    def human_approval_task(self) -> Task:
        return Task(
            config=self.tasks_config["human_approval_task"],
            markdown=False,
        )

    @task
    def generate_incident_record_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_incident_record_task"],
            markdown=False,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ServiceOpsIncidentTriage crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=self._llm_from_connection(),
        )
