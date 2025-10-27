import bibtexparser
import os
import yaml 

def read_bibtex_file(file_path):
    bib_database = bibtexparser.parse_file(file_path)
    return bib_database.entries

def extract_fields(entries):
    extracted_data = []
    for entry in entries:
        entry_data = {}
        entry_data['entry_type'] = entry.entry_type
        entry_data['cite_key'] = entry.key
        for key in ['title', 'author', 'year', 'journal', 'publisher']:
            formatted = entry.fields_dict[key].value
            entry_data[key] = 'N/A' if formatted==None else formatted
        
        # Add more fields as needed
        extracted_data.append(entry_data)
    return extracted_data

def save_to_yaml_files(extracted_data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for entry in extracted_data:
        cite_key = entry['cite_key']
        file_name = os.path.join(output_dir, f"{cite_key}.yaml")
        print(entry)
        with open(file_name, 'w') as yaml_file:
            yaml.dump(entry, yaml_file, default_flow_style=False)

if __name__ == "__main__":
    file_path = 'research/2023-09-01-project-latidos/latidos_bibliography.bib'  # Replace with your BibTeX file path
    output_dir = 'output_yaml_files'  # Directory to save YAML files
    entries = read_bibtex_file(file_path)
    extracted_data = extract_fields(entries)
    save_to_yaml_files(extracted_data, output_dir)