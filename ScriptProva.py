# Bibliotecas utilizadas
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Arquivo que será processado
ARQUIVO_IMAGEM = "ProvaSegundaParte\elvis.png"


# Faz a leitura da imagem em escala de cinza
def obter_imagem():
    foto_cinza = cv2.imread(ARQUIVO_IMAGEM, 0)

    if foto_cinza is None:
        raise FileNotFoundError(
            f"Imagem não encontrada: {ARQUIVO_IMAGEM}"
        )

    return foto_cinza


# Calcula a transformada de Fourier centralizada
def calcular_fourier(imagem):
    frequencias = np.fft.fft2(imagem)
    return np.fft.fftshift(frequencias)


# Converte frequências para espectro visual
def gerar_espectro(frequencias):
    return 20 * np.log(np.abs(frequencias) + 1)


# Exibe resultado padrão dos filtros
def exibir_filtro(imagem, espectro, mascara,
                  resultado, nome_filtro):

    plt.figure(figsize=(10, 7))

    plt.subplot(221)
    plt.imshow(imagem, cmap="gray")
    plt.title("Imagem Original")
    plt.axis("off")

    plt.subplot(222)
    plt.imshow(espectro, cmap="gray")
    plt.title("Espectro")
    plt.axis("off")

    plt.subplot(223)
    plt.imshow(mascara, cmap="gray")
    plt.title(nome_filtro)
    plt.axis("off")

    plt.subplot(224)
    plt.imshow(resultado, cmap="gray")
    plt.title("Resultado")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


# Apenas mostra a transformada de Fourier
def visualizar_fourier():

    foto = obter_imagem()

    frequencias = calcular_fourier(foto)

    espectro = gerar_espectro(frequencias)

    plt.figure(figsize=(10, 5))

    plt.subplot(121)
    plt.imshow(foto, cmap="gray")
    plt.title("Imagem")

    plt.subplot(122)
    plt.imshow(espectro, cmap="gray")
    plt.title("Transformada de Fourier")

    plt.tight_layout()
    plt.show()


# Mantém somente frequências baixas
def aplicar_passa_baixa():

    foto = obter_imagem()

    frequencias = calcular_fourier(foto)

    altura, largura = foto.shape

    meio_y = altura // 2
    meio_x = largura // 2

    mascara = np.zeros((altura, largura), np.uint8)

    alcance = 30

    y, x = np.ogrid[:altura, :largura]

    mascara[
        ((y - meio_y) ** 2 +
         (x - meio_x) ** 2)
        <= alcance**2
    ] = 1

    frequencias_filtradas = frequencias * mascara

    imagem_final = np.abs(
        np.fft.ifft2(
            np.fft.ifftshift(
                frequencias_filtradas
            )
        )
    )

    exibir_filtro(
        foto,
        gerar_espectro(frequencias),
        mascara,
        imagem_final,
        "Passa-Baixa"
    )


# Mantém somente frequências altas
def aplicar_passa_alta():

    foto = obter_imagem()

    frequencias = calcular_fourier(foto)

    altura, largura = foto.shape

    meio_y = altura // 2
    meio_x = largura // 2

    mascara = np.ones((altura, largura), np.uint8)

    alcance = 30

    y, x = np.ogrid[:altura, :largura]

    mascara[
        ((y - meio_y) ** 2 +
         (x - meio_x) ** 2)
        <= alcance**2
    ] = 0

    frequencias_filtradas = frequencias * mascara

    imagem_final = np.abs(
        np.fft.ifft2(
            np.fft.ifftshift(
                frequencias_filtradas
            )
        )
    )

    exibir_filtro(
        foto,
        gerar_espectro(frequencias),
        mascara,
        imagem_final,
        "Passa-Alta"
    )


# Mantém apenas uma faixa intermediária
def aplicar_passa_banda():

    foto = obter_imagem()

    frequencias = calcular_fourier(foto)

    altura, largura = foto.shape

    meio_y = altura // 2
    meio_x = largura // 2

    mascara = np.zeros((altura, largura), np.uint8)

    raio_min = 20
    raio_max = 60

    y, x = np.ogrid[:altura, :largura]

    distancia = (
        (y - meio_y) ** 2 +
        (x - meio_x) ** 2
    )

    mascara[
        (distancia > raio_min**2)
        &
        (distancia < raio_max**2)
    ] = 1

    frequencias_filtradas = frequencias * mascara

    imagem_final = np.abs(
        np.fft.ifft2(
            np.fft.ifftshift(
                frequencias_filtradas
            )
        )
    )

    exibir_filtro(
        foto,
        gerar_espectro(frequencias),
        mascara,
        imagem_final,
        "Passa-Banda"
    )


# Remove ruído periódico usando filtro Notch
def aplicar_notch():

    foto = obter_imagem()

    altura, largura = foto.shape

    eixo_x = np.arange(largura)
    eixo_y = np.arange(altura)

    grade_x, grade_y = np.meshgrid(
        eixo_x,
        eixo_y
    )

    ruido = (
        50
        * np.sin(
            2 * np.pi * 0.15 *
            (grade_x + grade_y)
        )
    )

    foto_ruidosa = np.clip(
        foto + ruido,
        0,
        255
    ).astype(np.uint8)

    frequencias = calcular_fourier(
        foto_ruidosa
    )

    mascara = np.ones(
        (altura, largura),
        np.uint8
    )

    meio_y = altura // 2
    meio_x = largura // 2

    coordenadas = [
        (meio_y - 80, meio_x - 80),
        (meio_y - 60, meio_x - 60),
        (meio_y - 40, meio_x - 40),
        (meio_y - 20, meio_x - 20),
        (meio_y + 20, meio_x + 20),
        (meio_y + 40, meio_x + 40),
        (meio_y + 60, meio_x + 60),
        (meio_y + 80, meio_x + 80)
    ]

    y, x = np.ogrid[:altura, :largura]

    for py, px in coordenadas:
        mascara[
            ((y - py) ** 2 +
             (x - px) ** 2)
            <= 8**2
        ] = 0

    frequencias_filtradas = (
        frequencias * mascara
    )

    imagem_final = np.abs(
        np.fft.ifft2(
            np.fft.ifftshift(
                frequencias_filtradas
            )
        )
    )

    exibir_filtro(
        foto_ruidosa,
        gerar_espectro(frequencias),
        mascara,
        imagem_final,
        "Filtro Notch"
    )


# Menu principal do sistema
if __name__ == "__main__":

    print("\n===== PROCESSAMENTO DE IMAGENS =====")

    while True:
        print("1 - Visualizar Fourier")
        print("2 - Passa-Baixa")
        print("3 - Passa-Alta")
        print("4 - Passa-Banda")
        print("5 - Notch")
        print("6 - Sair")

        escolha = input("\nSelecione uma opção: ")
        
        match escolha:

            case "1":
                visualizar_fourier()

            case "2":
                aplicar_passa_baixa()

            case "3":
                aplicar_passa_alta()

            case "4":
                aplicar_passa_banda()

            case "5":
                aplicar_notch()

            case "6":
                print("Saindo do programa finalizado")
                break

            case _:
                print("Opção inválida.")