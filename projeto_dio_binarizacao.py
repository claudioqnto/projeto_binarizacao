from PIL import Image

#Função para rransformar Imagem Colorida para Níveis de Cinza
def converter_para_cinza(caminho_entrada, caminho_saida):
    try:
        img_colorida = Image.open(caminho_entrada).convert("RGB")
        largura, altura = img_colorida.size
        # Cria uma nova imagem em modo 'L' (tons de cinza de 8 bits)
        img_cinza = Image.new('L', (largura, altura))

        # Itera sobre cada pixel
        for x in range(largura):
            for y in range(altura):
                # pega os valores R, G, B do pixel
                R, G, B = img_colorida.getpixel((x, y))
                #conversão usando média (R+G+B)/3
                # A conversão por luminância: L = 0.299*R + 0.587*G + 0.114*B
                intensidade_cinza = int((R + G + B) / 3)                 
                # Define o pixel na nova imagem
                img_cinza.putpixel((x, y), intensidade_cinza)

        # Salvando a nova imagem em tons de cinza
        img_cinza.save(caminho_saida)
        print(f"Sucesso: Imagem salva em tons de cinza como '{caminho_saida}'")

    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada não encontrado em '{caminho_entrada}'")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


#Função: Transformar Imagem em Cinza para Preto e Branco
def binarizar_imagem(caminho_entrada_cinza, caminho_saida, limiar=128):
    try:
        img_cinza = Image.open(caminho_entrada_cinza).convert("L")
        largura, altura = img_cinza.size
        img_binarizada = Image.new('L', (largura, altura))
#iteração
        for x in range(largura):
            for y in range(altura):
                intensidade = img_cinza.getpixel((x, y))
                if intensidade > limiar:
                    novo_valor = 255 
                else:
                    novo_valor = 0 
                img_binarizada.putpixel((x, y), novo_valor)

        # Salvando a nova imagem preto e brancoi
        img_binarizada.save(caminho_saida)
        print(f"Sucesso: Imagem salva como preto e branco ('{caminho_saida}' com limiar={limiar})")

    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada não encontrado em '{caminho_entrada_cinza}'")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# 1. Defina o caminho da sua imagem colorida
IMAGEM_COLORIDA = 'binarizar.jpg'
# 2. Defina os caminhos de saída
IMAGEM_CINZA = 'imagem_em_cinza.png'
IMAGEM_P_B = 'imagem_binarizada.png'

print("Iniciando a conversão...")

# Passo 1: Converter Colorida para Cinza
converter_para_cinza(IMAGEM_COLORIDA, IMAGEM_CINZA)

# Passo 2: Converter Cinza para Preto e Branco (binarização)
# Você pode experimentar diferentes valores de limiar, como 100, 150, etc.
binarizar_imagem(IMAGEM_CINZA, IMAGEM_P_B, limiar=140)

print("Processamento concluído.")