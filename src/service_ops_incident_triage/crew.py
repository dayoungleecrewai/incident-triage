from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ServiceOpsIncidentTriageCrew:
    """Incident triage crew designed for AMP-managed LLM connections."""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def incident_intake_normalization_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["incident_intake_normalization_specialist"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
        )

    @agent
    def senior_site_reliability_diagnostician(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_site_reliability_diagnostician"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
        )

    @agent
    def remediation_runbook_policy_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["remediation_runbook_policy_analyst"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
        )

    @agent
    def on_call_engineer_approval_gate(self) -> Agent:
        return Agent(
            config=self.agents_config["on_call_engineer_approval_gate"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
        )

    @agent
    def incident_record_audit_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config["incident_record_audit_compiler"],  # type: ignore[index]
            allow_delegation=False,
            inject_date=True,
            verbose=True,
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
        )
