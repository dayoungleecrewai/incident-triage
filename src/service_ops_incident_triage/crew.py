import os
from typing import List

from crewai import Agent, Crew, LLM, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ServiceOpsIncidentTriageCrew:
    """Incident triage crew designed for AMP-managed LLM connections."""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def _amp_llm(self) -> LLM:
        """
        Resolve model configuration from AMP/connection environment variables.
        No OpenAI default fallback is used.
        """
        model = (
            os.getenv("MODEL")
            or os.getenv("LITELLM_MODEL")
            or os.getenv("CREWAI_MODEL")
        )
        if not model:
            raise ValueError(
                "No model connection found. Set MODEL (or LITELLM_MODEL/CREWAI_MODEL) in AMP deployment configuration."
            )

        llm_kwargs = {"model": model}
        base_url = os.getenv("MODEL_BASE_URL") or os.getenv("LITELLM_BASE_URL")
        api_key = (
            os.getenv("MODEL_API_KEY")
            or os.getenv("LITELLM_API_KEY")
            or os.getenv("API_KEY")
        )
        if base_url:
            llm_kwargs["base_url"] = base_url
        if api_key:
            llm_kwargs["api_key"] = api_key

        return LLM(**llm_kwargs)

    @agent
    def incident_intake_normalization_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["incident_intake_normalization_specialist"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
            llm=self._amp_llm(),
        )

    @agent
    def senior_site_reliability_diagnostician(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_site_reliability_diagnostician"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
            llm=self._amp_llm(),
        )

    @agent
    def remediation_runbook_policy_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["remediation_runbook_policy_analyst"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
            llm=self._amp_llm(),
        )

    @agent
    def on_call_engineer_approval_gate(self) -> Agent:
        return Agent(
            config=self.agents_config["on_call_engineer_approval_gate"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
            llm=self._amp_llm(),
        )

    @agent
    def incident_record_audit_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config["incident_record_audit_compiler"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
            llm=self._amp_llm(),
        )

    @task
    def parse_incident_task(self) -> Task:
        return Task(
            config=self.tasks_config["parse_incident_task"],  # type: ignore[index]
        )

    @task
    def diagnose_incident_task(self) -> Task:
        return Task(
            config=self.tasks_config["diagnose_incident_task"],  # type: ignore[index]
        )

    @task
    def policy_check_remediation_task(self) -> Task:
        return Task(
            config=self.tasks_config["policy_check_remediation_task"],  # type: ignore[index]
        )

    @task
    def human_approval_task(self) -> Task:
        return Task(
            config=self.tasks_config["human_approval_task"],  # type: ignore[index]
        )

    @task
    def generate_incident_record_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_incident_record_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Create the incident triage crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            chat_llm=self._amp_llm(),
        )
