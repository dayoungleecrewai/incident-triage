import os


from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ExaSearchTool






@CrewBase
class ServiceOpsIncidentTriageCrew:
    """ServiceOpsIncidentTriage crew"""

    
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
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def senior_site_reliability_diagnostician(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["senior_site_reliability_diagnostician"],
            
            
            tools=[				ExaSearchTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def remediation_runbook_policy_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["remediation_runbook_policy_analyst"],
            
            
            tools=[				ExaSearchTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
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
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
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
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
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

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


