from flask import Flask

app = Flask(__name__)

instance_metadata = {
    'instance-id': 'i-0bb7fbc3154f0ca53',
    'ami-launch-index': '0',
    'public-hostname': 'ec2-44-204-240-148.compute-1.amazonaws.com',
    'public-ipv4': '44.204.240.148',
    'local-hostname': 'ip-172-31-85-167.ec2.internal',
    'local-ipv4': '172.31.85.167',
}

def generate_metadata_table(metadata):
    table_html = '<table border="1">'
    table_html += '<tr><th>Metadata Key</th><th>Value</th></tr>'
    for key, value in metadata.items():
        table_html += f'<tr><td>{key}</td><td>{value}</td></tr>'
    table_html += '</table>'
    return table_html

@app.route('/')
def display_instance_metadata():
    metadata_table = generate_metadata_table(instance_metadata)
    html_content = f'<h1>Instance Metadata</h1>{metadata_table}'
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
