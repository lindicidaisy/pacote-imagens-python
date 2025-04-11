from image_processor import process_image

# Caminho da imagem original
input_path = "imagens/doguinho.jpg"
output_path = "imagens/doguinho_pb.jpg"

# Processa a imagem
process_image(input_path, output_path)

print(f"Imagem processada com sucesso! Arquivo salvo em: {output_path}")
