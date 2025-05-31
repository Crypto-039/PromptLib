from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from pathlib import Path
import yaml
import json

app = Flask(__name__)
CORS(app)

PROMPT_LIBRARIES_DIR = Path("prompt_libraries")
PROMPT_LIBRARIES_DIR.mkdir(exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/libraries', methods=['GET'])
def get_libraries():
    libraries = []
    for file in PROMPT_LIBRARIES_DIR.glob('*.yaml'):
        with open(file, 'r') as f:
            library = yaml.safe_load(f)
            libraries.append({
                'filename': file.name,
                'domain': library['domain']
            })
    return jsonify(libraries)

@app.route('/api/library/<filename>', methods=['GET'])
def get_library(filename):
    file_path = PROMPT_LIBRARIES_DIR / filename
    if not file_path.exists():
        return jsonify({'error': 'Library not found'}), 404
    
    with open(file_path, 'r') as f:
        library = yaml.safe_load(f)
    return jsonify(library)

@app.route('/api/library', methods=['POST'])
def create_library():
    data = request.json
    domain_name = data['domain']['name']
    filename = f"{domain_name.lower().replace(' ', '_')}_prompts.yaml"
    
    with open(PROMPT_LIBRARIES_DIR / filename, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    return jsonify({'message': 'Library created successfully', 'filename': filename})

@app.route('/api/library/<filename>', methods=['DELETE'])
def delete_library(filename):
    file_path = PROMPT_LIBRARIES_DIR / filename
    if not file_path.exists():
        return jsonify({'error': 'Library not found'}), 404
    
    file_path.unlink()
    return jsonify({'message': 'Library deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True) 