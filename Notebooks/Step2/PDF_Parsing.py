import requests
from pathlib import Path
from pypdf import PdfReader
from lxml import etree
import re

# Parse PDF with GROBID
def parse_pdf_with_grobid(pdf_file_path):
  
  grobid_url = 'http://localhost:8070/api/processFulltextDocument'
  
  files = {'input': open(pdf_file_path, 'rb')}
  response = requests.post(grobid_url, files=files)

  xml_content = response.content
  root = etree.fromstring(xml_content)

  text_content = root.xpath('//text()')
  parsed_text = ' '.join(text_content)
  
  return parsed_text, root

# Restructure parsed text
def restructure_text(parsed_text):
  
  paragraphs = re.split(r'\n\s*\n', parsed_text)
  formatted_text = '\n\n'.join(paragraphs)

  return formatted_text

# Parse PDF with PyPDF  
def parse_pdf_with_pypdf(pdf_file_path):

  pdf_reader = PdfReader(pdf_file_path)

  content = [f"{pdf_reader.metadata.title}"]
  content.append(f"Number of pages: {len(pdf_reader.pages)}")

  for page in pdf_reader.pages:
    content.append(page.extract_text())
  
  return '\n'.join(content)

def extract_element_text(root, element_path, namespaces):
    element = root.find(element_path, namespaces=namespaces)
    return element.text.strip() if element is not None and element.text is not None else ''

def extract_metadata(root, filename):
    try:
        ns = {"tei": "http://www.tei-c.org/ns/1.0", "xml": "http://www.w3.org/XML/1998/namespace"}

        metadata = {
            'Filename': filename,
            'Title': extract_element_text(root, ".//tei:title[@type='main']", ns),
            'Header': extract_element_text(root, ".//tei:head", ns),
            'Paragraph': extract_element_text(root, ".//tei:p", ns),
            'Idno': extract_element_text(root, ".//tei:idno", ns),
            'Application': extract_element_text(root, ".//tei:desc", ns)
        }

        return metadata

    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML: {str(e)}")
        return None

def save_metadata_to_json(metadata, file_prefix):
    import json
    output_file_path = f"{file_prefix}_metadata.json"
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(metadata, file, indent=2)

def save_metadata_to_xml(metadata, file_prefix):
    output_file_path = f"{file_prefix}_metadata.xml"
    root = etree.Element("metadata")
    for key, value in metadata.items():
        tag_name = key.replace(' ', '_')
        element = etree.SubElement(root, tag_name)
        element.text = value
    tree = etree.ElementTree(root)
    tree.write(output_file_path, encoding="utf-8", xml_declaration=True)

def save_metadata_to_csv(metadata_list, csv_filename):
    import csv
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = set(field for metadata in metadata_list for field in metadata.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for metadata in metadata_list:
            filtered_metadata = {field: metadata.get(field, '') for field in fieldnames}
            writer.writerow(filtered_metadata)

# Process PDF files
pdf_files = ['2024-l1-topics-combined-2.pdf',  
             '2024-l2-topics-combined-2.pdf',
             '2024-l3-topics-combined-2.pdf']

# Dictionary to store all metadata             
all_metadata = []

for pdf_file in pdf_files:

  print(f"Processing {pdf_file}")
  
  # Parse PDFs
  parsed_text, root = parse_pdf_with_grobid(pdf_file)
  restructured_text = restructure_text(parsed_text)
  
  pypdf_text = parse_pdf_with_pypdf(pdf_file)
   
  # Save text outputs
  grobid_output = f"Grobid_RR_{pdf_file.split('-')[0]}_{pdf_file.split('-')[1].split('.')[0]}_combined.txt"
  pypdf_output = f"PyPDF_RR_{pdf_file.replace('-topics-combined-2.pdf', '_combined.txt')}"

  with open(grobid_output, 'w', encoding='utf-8') as f:
    f.write(restructured_text)

  with open(pypdf_output, 'w', encoding='utf-8') as f:
    f.write(pypdf_text)

  # Extract and save metadata
  metadata = extract_metadata(root, pdf_file)
  if metadata:
    all_metadata.append(metadata)
    file_prefix = f"Grobid_RR_{pdf_file.split('-')[0]}_{pdf_file.split('-')[1].split('.')[0]}_combined"
    save_metadata_to_json(metadata, file_prefix)
    save_metadata_to_xml(metadata, file_prefix)

save_metadata_to_csv(all_metadata, 'metadata.csv')