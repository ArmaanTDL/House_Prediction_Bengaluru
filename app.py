from flask import Flask, render_template, jsonify
import subprocess
import os
import pandas as pd

app = Flask(__name__)

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    # Check if data files exist
    data_status = {
        'properties_2016': os.path.exists(os.path.join(WORKING_DIR, 'data/properties_2016.csv')),
        'train_2016': os.path.exists(os.path.join(WORKING_DIR, 'data/train_2016_v2.csv')),
    }
    return render_template('index.html', data_status=data_status)

@app.route('/run')
def run_prediction():
    try:
        # Run stack.py using the venv python
        python_path = os.path.join(WORKING_DIR, 'venv/bin/python3')
        if not os.path.exists(python_path):
            python_path = 'python3' # Fallback
            
        result = subprocess.run(
            [python_path, 'stack.py'],
            capture_output=True,
            text=True,
            cwd=WORKING_DIR
        )
        
        output = result.stdout
        if result.stderr:
            output += "\nErrors:\n" + result.stderr
            
        # Get snippet of results if available
        results_path = os.path.join(WORKING_DIR, 'submission/final_stack.csv')
        results_data = ""
        if os.path.exists(results_path):
            df = pd.read_csv(results_path)
            results_data = df.head().to_html(classes='table table-dark table-hover', index=False)
            
        return jsonify({
            'success': result.returncode == 0,
            'output': output,
            'results_html': results_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'output': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
