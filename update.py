import re

def update_incorporation_state(html_path: str, xsd_path: str, new_state: str):
    # Load HTML file
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    with open(xsd_path, 'r', encoding='utf-8') as f:
        xsd = f.read()

    updated_html = ""

    #TODO: replace the state

    # Save updated HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(updated_html)
