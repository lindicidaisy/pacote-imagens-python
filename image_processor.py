from PIL import Image

def process_image(input_path, output_path):
    # Abre a imagem original
    img = Image.open(input_path)

    # Converte a imagem para preto e branco
    img_pb = img.convert("L")

    # Salva a nova imagem
    img_pb.save(output_path)
