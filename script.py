import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import PyPDF2
import docx
import os

# Descargar datos necesarios para NLTK
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

# Función para extraer texto de un archivo txt
def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Función para extraer texto de un archivo pdf
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
        return text

# Función para extraer texto de un archivo docx
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text

# Función para identificar entidades nombradas
def identify_named_entities(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    ner_chunks = ne_chunk(pos_tags)
    named_entities = []
    for chunk in ner_chunks:
        if isinstance(chunk, Tree):
            entity_name = ' '.join(c[0] for c in chunk)
            entity_type = chunk.label()
            named_entities.append((entity_name, entity_type))
    return named_entities

# Función para determinar el tipo de archivo y extraer el texto
def extract_text(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.txt':
        return extract_text_from_txt(file_path)
    elif file_extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension.lower() == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")

# Ejemplo de uso
if __name__ == "__main__":
    file_path = 'fime.txt'  
    text = extract_text(file_path)
    named_entities = identify_named_entities(text)
    for entity_name, entity_type in named_entities:
        print(f"Entity: {entity_name}, Type: {entity_type}")
