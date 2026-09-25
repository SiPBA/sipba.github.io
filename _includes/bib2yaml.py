import os
import shutil
import datetime
import yaml
import bibtexparser

def clean_text(text):
    """Limpia llaves y caracteres de escape del texto de BibTeX."""
    if not text:
        return ""
    return text.replace('{', '').replace('}', '').replace('\\', '').strip()

def convert_bib_to_yaml(bib_file, yaml_file):
    # 1. Sistema de Backup
    if os.path.exists(yaml_file):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{yaml_file}.{timestamp}.bak"
        shutil.copy2(yaml_file, backup_file)
        print(f"[*] Backup creado exitosamente: {backup_file}")

    # 2. Leer archivo BibTeX
    with open(bib_file, 'r', encoding='utf-8') as f:
        bib_database = bibtexparser.load(f)

    publications = []

    # 3. Mapear cada entrada al nuevo formato
    for entry in bib_database.entries:
        pub = {}
        
        # Mapeo directo de IDs
        pub['ENTRYTYPE'] = entry.get('ENTRYTYPE', '')
        pub['ID'] = entry.get('ID', '')
        
        # Procesar autores (convertir ' and ' a lista)
        if 'author' in entry:
            authors_list = [clean_text(a) for a in entry['author'].split(' and ')]
            pub['author'] = authors_list
            
        # DOI
        if 'doi' in entry:
            pub['doi'] = clean_text(entry['doi'])
            
        # Container-title (Prioriza journal, luego booktitle)
        if 'journal' in entry:
            pub['container-title'] = clean_text(entry['journal'])
        elif 'booktitle' in entry:
            pub['container-title'] = clean_text(entry['booktitle'])
            
        # Note y Categories
        if 'note' in entry:
            pub['note'] = clean_text(entry['note'])
            
        # Páginas (arreglar los dobles guiones de BibTeX)
        if 'pages' in entry:
            pub['pages'] = clean_text(entry['pages']).replace('--', ' - ')
            
        pub['publication_stage'] = clean_text(entry.get('publication_stage', 'Final'))
        pub['categories'] = []
        
        if 'source' in entry:
            pub['source'] = clean_text(entry['source'])
            
        pub['title'] = clean_text(entry.get('title', ''))
        
        # --- CORRECCIÓN DEL CAMPO TYPE ---
        # 1º: Miramos si existe el campo explícito 'type' en el BibTeX
        explicit_type = entry.get('type', '')
        if explicit_type:
            # Capitalizamos la primera letra por estética si viene en minúsculas,
            # pero respetamos el texto (ej. "Conference paper")
            cleaned_type = clean_text(explicit_type)
            pub['type'] = cleaned_type.capitalize() if cleaned_type.islower() else cleaned_type
        else:
            # 2º: Si no hay campo type, lo deducimos del ENTRYTYPE
            entry_type = pub['ENTRYTYPE'].lower()
            if entry_type == 'article':
                pub['type'] = 'Article'
            elif entry_type in ['inproceedings', 'conference']:
                pub['type'] = 'Conference paper'
            elif entry_type in ['book', 'incollection']:
                pub['type'] = 'Book chapter'
            else:
                pub['type'] = pub['ENTRYTYPE'].capitalize()
        # ---------------------------------

        # Path (URLs)
        if 'url' in entry:
            pub['path'] = clean_text(entry['url'])
        elif 'doi' in entry:
            pub['path'] = f"https://doi.org/{clean_text(entry['doi'])}"
            
        # Volumen, número y año
        if 'volume' in entry:
            pub['volume'] = str(clean_text(entry['volume']))
        if 'number' in entry:
            pub['number'] = str(clean_text(entry['number']))
        if 'year' in entry:
            pub['year'] = str(clean_text(entry['year']))
            
        publications.append(pub)

    # 4. Guardar en YAML con el formato correcto
    class CustomDumper(yaml.Dumper):
        # Esta clase evita que YAML indente las listas con un espacio extra
        def increase_indent(self, flow=False, indentless=False):
            return super(CustomDumper, self).increase_indent(flow, False)

    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(
            publications, 
            f, 
            Dumper=CustomDumper,
            default_flow_style=False, 
            sort_keys=False, 
            allow_unicode=True
        )
        
    print(f"[*] Conversión completada. Archivo guardado en: {yaml_file}")

if __name__ == "__main__":
    # Nombres de tus archivos
    archivo_entrada = "PUBLICATIONS.bib"
    archivo_salida = "publications.yml"
    
    convert_bib_to_yaml(archivo_entrada, archivo_salida)

