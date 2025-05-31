# Prompt Library Builder

A tool for creating optimized domain-specific prompt libraries with customizable parameters and templates.

## Features

- Create domain-specific prompt libraries
- Customize temperature, top_p, and max tokens for each prompt
- Add variable placeholders to your prompts
- Export libraries in YAML format
- Interactive command-line interface
- Rich text formatting and user-friendly prompts

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the prompt builder:
```bash
python prompt_builder.py
```

The tool will guide you through:
1. Defining your domain
2. Setting up prompt parameters (temperature, top_p, max tokens)
3. Creating prompt templates with variable placeholders
4. Saving your prompt library

## Output

The tool creates a YAML file in the `prompt_libraries` directory with your domain-specific prompts. The filename will be based on your domain name (e.g., `medical_diagnosis_prompts.yaml`).

## Example Prompt Library Structure

```yaml
domain:
  name: Medical Diagnosis
  description: Prompts for medical diagnosis assistance
prompts:
  - name: Symptom Analysis
    template: "Given the following symptoms: {symptoms}, provide a preliminary analysis considering {patient_history}"
    variables:
      - name: symptoms
        description: List of current symptoms
      - name: patient_history
        description: Relevant medical history
    parameters:
      temperature: 0.7
      top_p: 0.9
      max_tokens: 2000
```

## Contributing

Feel free to submit issues and enhancement requests! 