import questionary
import yaml
from rich.console import Console
from rich.panel import Panel
from pathlib import Path
import json

console = Console()

class PromptLibraryBuilder:
    def __init__(self):
        self.prompts = {}
        
    def get_domain_info(self):
        domain_name = questionary.text(
            "What domain is this prompt library for? (e.g., 'Medical Diagnosis', 'Legal Writing'):"
        ).ask()
        
        domain_description = questionary.text(
            "Please provide a brief description of this domain:"
        ).ask()
        
        return domain_name, domain_description
    
    def get_prompt_parameters(self):
        temperature = questionary.float(
            "What temperature would you like to use? (0.0-1.0, lower = more focused higher = more creative):",
            min_value=0.0,
            max_value=1.0,
            default=0.7
        ).ask()
        
        top_p = questionary.float(
            "What top_p value would you like to use? (0.0-1.0):",
            min_value=0.0,
            max_value=1.0,
            default=0.9
        ).ask()
        
        max_tokens = questionary.text(
            "What should be the maximum token length? (Press enter for default: 2000)"
        ).ask() or "2000"
        
        return {
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": int(max_tokens)
        }
    
    def get_prompt_template(self):
        template = questionary.text(
            "Enter your prompt template (use {variables} for placeholders):"
        ).ask()
        
        variables = []
        while questionary.confirm(
            "Would you like to add a variable placeholder?",
            default=True
        ).ask():
            var_name = questionary.text("Enter variable name:").ask()
            var_description = questionary.text(
                f"Enter description for {var_name}:"
            ).ask()
            variables.append({
                "name": var_name,
                "description": var_description
            })
        
        return template, variables
    
    def create_prompt_library(self):
        console.print(Panel.fit(
            "Welcome to the Prompt Library Builder!\n"
            "This tool will help you create optimized domain-specific prompt templates.",
            title="🚀 Prompt Library Builder",
            border_style="blue"
        ))
        
        domain_name, domain_description = self.get_domain_info()
        parameters = self.get_prompt_parameters()
        
        prompts = []
        while questionary.confirm(
            "Would you like to add a prompt template?",
            default=True
        ).ask():
            prompt_name = questionary.text(
                "Enter a name for this prompt template:"
            ).ask()
            
            template, variables = self.get_prompt_template()
            
            prompts.append({
                "name": prompt_name,
                "template": template,
                "variables": variables,
                "parameters": parameters.copy()
            })
        
        library = {
            "domain": {
                "name": domain_name,
                "description": domain_description
            },
            "prompts": prompts
        }
        
        # Save to file
        output_dir = Path("prompt_libraries")
        output_dir.mkdir(exist_ok=True)
        
        filename = f"{domain_name.lower().replace(' ', '_')}_prompts.yaml"
        with open(output_dir / filename, 'w') as f:
            yaml.dump(library, f, default_flow_style=False, sort_keys=False)
        
        console.print(f"\n✨ Prompt library saved to: {filename}", style="green")
        console.print("\nLibrary contents:", style="blue")
        console.print(yaml.dump(library, sort_keys=False), style="yellow")