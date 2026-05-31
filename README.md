##Segunda Prova
Explicação: Esse código já está com todos os filtros pedidos pela 
professora podendo ser rodado por um menu. 

Tecnologias usada: 

1. Liguagem Usada: Python 
2. Biblioteca Usada: OpenCV(cv2), Numpy(np) e Matplotlib(plt)

Resultados obtidos: 

Fourier:
<img width="996" height="534" alt="fourier" src="https://github.com/user-attachments/assets/6a3e4e82-ce2c-4149-a6e8-838f3819d02f" />
Passa-Baixa: 
 <img width="1211" height="628" alt="Passa-Baixa" src="https://github.com/user-attachments/assets/783a68a6-d9c1-4ff4-a72e-664da25095c9" />
Passa-alta: 
 <img width="1242" height="634" alt="Passa-alta" src="https://github.com/user-attachments/assets/598be0d4-8bbe-4190-b0bd-4c4806102401" />
passa-banda: 
 <img width="1205" height="633" alt="passa-banda" src="https://github.com/user-attachments/assets/4a02a660-8e17-4b30-aab1-3037a6096b64" />
Notch: 
 <img width="1258" height="629" alt="Notch" src="https://github.com/user-attachments/assets/05c1b829-1b61-473d-ac17-d5ef3418dcf5" />

Descrição dos filtros utilizados:  
Fourier: Ele não é um filtro e sim uma transformação matemática que 
move a imagem do domínio dos pixels para o domínico da frequência. 
Decompondo a imagem para componentes de frequências senoidais. 
No espectro centralizado, o centro representa as baixas frequências 
(mudanças suaves, tons constantes) e as extremidades representam as 
altas frequências (detalhes finos, bordas e ruído). 
Passa-Baixa: Filtro que permite a passagem de frequências abaixo de 
uma frequência de corte definida e atenua ou bloqueia as frequências 
mais altas. É representado por um círculo branco (passagem livre) 
sobre um fundo preto no centro do espectro. 
Passa-alta: É o inverso do passa-baixa. Ele bloqueia as baixas 
frequências centrais (região preta no centro) e permite a passagem das 
altas frequências periféricas. 

Passa-Banda: Com esse filtro é permitido apenas a passagem de uma 
faixa (banda) específica de frequências, bloqueando tanto as 
frequências muito baixas (abaixo do raio interno) quanto as muito altas 
(acima do raio externo). É representado visualmente por um anel (um 
"donut" branco).  

Notch: É um filtro altamente seletivo projetado para rejeitar (bloquear) 
frequências específicas localizadas em coordenadas predefinidas do 
espectro, sem alterar o restante das frequências. Na imagem fornecida, 
ele consiste em uma sequência de pontos pretos posicionados 
diagonalmente para remover um ruído periódico específico. 

##Explique o que representa o espectro de Fourier:  

O espectro de Fourier representa a distribuição das frequências 
espaciais contidas na imagem. Cada ponto no espectro indica a 
magnitude e a direção de uma determinada frequência de variação de 
brilho. Centro do espectro concentra a maior parte da energia da 
imagem, correspondendo às baixas frequências das formas gerais e 
possíveis variações lentas de intensidade, falando das bordas e 
direções externas correspondem às altas frequências (transições 
abruptas, bordas, texturas finas e ruídos) e as linhas ou pontos 
brilhantes isolados fora do centro (como os vistos diagonalmente na 
imagem original do Elvis) indicam a presença de padrões repetitivos ou 
ruídos periódicos que afetam a imagem inteira no domínio espacial. 

##Explique quais frequências foram removidas ou preservadas:  
Passa-Baixa: Preservou as baixas frequências (centro) e removeu todas 
as altas frequências (periferia). 

Passa-Alta: Removeu as baixas frequências (centro) e preservou as 
altas frequências (periferia). 

Passa-Banda: Removeu as frequências muito baixas do centro e as 
muito altas da borda externa, preservando apenas as frequências 
intermediárias contidas no raio do anel. 

Notch: Preservou quase a totalidade das frequências da imagem (tanto 
baixas quanto altas), removendo apenas as frequências espaciais 
específicas causadas pelo ruído periódico diagonal, mapeadas como 
pontos pretos no filtro. 

##Explique o impacto visual causado por cada filtro:  

Passa-Baixa: Deixou a imagem mais borrada e suave. Os detalhes do 
rosto, da roupa e as linhas de ruído desapareceram, ficando apenas as 
formas principais. 

Passa-Alta: Removeu grande parte das áreas cinzas da imagem e 
destacou as bordas. Assim, ficaram mais visíveis os contornos do 
cabelo, do microfone, da roupa e das linhas de ruído. 

Passa-Banda: Mostrou apenas os detalhes de tamanho intermediário. O 
resultado destacou alguns contornos e texturas, removendo tanto as 
áreas muito suaves quanto os detalhes muito pequenos. 

Notch: Removeu as linhas diagonais de interferência que apareciam na 
imagem. Com isso, a imagem ficou mais limpa e nítida, mantendo os 
detalhes importantes do cantor e de suas roupas. 

##Compare os resultados entre os filtros:  

Os filtros Passa-Baixa, Passa-Alta e Passa-Banda alteraram bastante a 
imagem original, pois removeram grandes grupos de frequências. O 
Passa-Baixa suavizou a imagem e reduziu os detalhes, o Passa-Alta 
destacou as bordas e contornos, e o Passa-Banda manteve apenas 
uma faixa intermediária de detalhes. 

Já o filtro Notch trabalhou de forma mais precisa. Em vez de remover 
muitas frequências de uma vez, ele eliminou apenas as frequências 
responsáveis pelo ruído das linhas diagonais. Por isso, conseguiu 
limpar a imagem sem prejudicar seus principais detalhes e 
características. 

##Indique qual filtro produziu o melhor resultado e justifique: 

O Filtro Notch apresentou o melhor resultado. 

Justificativa: A imagem original tinha um ruído em forma de linhas 
diagonais repetidas. Outros filtros conseguiram reduzir esse ruído, mas 
também removeram detalhes importantes da imagem. Já o Filtro Notch 
eliminou apenas as frequências responsáveis pelo ruído, deixando a 
imagem mais limpa sem perder a qualidade. Assim, detalhes como a 
roupa, o rosto e as bordas do Elvis foram preservados, tornando o 
resultado mais nítido e próximo da imagem original.
