from pdf2image import convert_from_path
import os

poppler_path = r"D:\\Descargas\\poppler-0.68.0\\poppler-0.68.0\\bin"
pdf_patch = r'D:\\Documentos\\alexys\\CERTIFICADOS Y CURSOS ALEXYS.pdf'

pages = convert_from_path(pdf_path= pdf_patch, poppler_path= poppler_path)

saving_folder = r'C:\\Users\\Eleazar Grillet\\Desktop\\Converted_pdf'

c = 1

for page in pages:
    img_name = f"img-{c}.jpeg"
    page.save(os.path.join(saving_folder,img_name), "JPEG")
    c += 1