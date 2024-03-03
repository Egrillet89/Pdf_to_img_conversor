from pdf2image import convert_from_path
import os

poppler_path = r"RUTA DE INSTALACION DE POOPLER"
pdf_patch = r'RUTA DE ARCHIVO PDF'

pages = convert_from_path(pdf_path= pdf_patch, poppler_path= poppler_path)

saving_folder = r'RUTA DONDE DESEA GUARDAR IMG CONVERTIDA'

c = 1

for page in pages:
    img_name = f"img-{c}.jpeg"
    page.save(os.path.join(saving_folder,img_name), "JPEG")
    c += 1