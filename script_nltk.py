# Asegúrate de haber instalado las bibliotecas requeridas usando los comandos pip install antes de ejecutar el script.
# pip install PyPDF2
# pip install wordcloud
# pip install matplotlib
# pip install collections
# pip install nltk

import PyPDF2
from nltk import sent_tokenize, word_tokenize, FreqDist
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def analyze_pdf(pdf_path, num_words):
    # Leer el contenido del PDF
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ' '.join(page.extract_text() for page in pdf_reader.pages)
    
    # Tokenizar en oraciones y palabras
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    # Eliminar puntuación y convertir a minúsculas
    words = [word.lower() for word in words if word not in string.punctuation]
    
    # Función personalizada para omitir varias palabras específicas
    def should_omit(word):
        omit_words = ['s', 'S','C', 'i', 'l','así', '1', 's /','S/','S /','s/','’', 'c', 'sido', 'dos', 'lp']  # Reemplaza con las palabras que deseas omitir
        return word in omit_words
    
    # Eliminar palabras vacías (stop words) y varias palabras específicas
    stop_words = set(stopwords.words('spanish'))
    words = [word for word in words if word not in stop_words and not should_omit(word)]
    
    # Calcular la frecuencia de las palabras
    word_freq = FreqDist(words)
    
    # Obtener las palabras más frecuentes
    top_words = word_freq.most_common(num_words)
    
    # Generar la nube de palabras
    wordcloud = WordCloud(background_color="white", margin=10, width=800, height=600).generate_from_frequencies(dict(top_words))
    
    # Mostrar la nube de palabras
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Ruta al archivo PDF
pdf_path = "discursos_peru_pdf/C/C.PDF"

# Número de palabras más frecuentes a mostrar en la nube de palabras
num_words = 30

# Analizar el PDF y generar la nube de palabras con el número de palabras especificado
analyze_pdf(pdf_path, num_words)
