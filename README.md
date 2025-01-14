# Automação Personalizada com PyAutoGUI

Este repositório contém um script criado especificamente para atender às minhas necessidades pessoais de automação de tarefas no computador. Ele utiliza a biblioteca `pyautogui` para simular ações do mouse e teclado, facilitando a abertura de aplicativos e páginas que utilizo frequentemente. Caso deseje replicá-lo em outra máquina, podem ser necessários ajustes para funcionar corretamente, como as coordenadas de clique ou os aplicativos referenciados no código.

---

## 🚀 Funcionalidades

1. Verificação e ajuste para garantir que a automação ocorra na área de trabalho principal.
2. Abertura automática de:
   - Google Chrome em modo tela cheia.
   - Agenda e organização da janela em outra tela.
   - Aplicativos como TickTick e WhatsApp.
   - Página do Notion diretamente em um link específico.

3. Alternância automática entre áreas de trabalho.

---

## 🛠️ Como o Script Funciona

### Explicação do Código

- **Bibliotecas Importadas:**
  - `pyautogui`: Permite o controle do mouse e teclado.
  - `time`: Utilizada para inserir pausas necessárias entre ações.

```python
import pyautogui
import time
```

- **Configuração Inicial:**
  Define um intervalo entre cada ação de `pyautogui` para evitar erros.

```python
pyautogui.PAUSE = 0.5
```

- **Alternância entre Áreas de Trabalho:**
  Garante que o script comece na área de trabalho correta.

```python
pyautogui.hotkey('win', 'ctrl', 'right')
pyautogui.hotkey('win', 'ctrl', 'right')
pyautogui.hotkey('win', 'ctrl', 'left')
```

- **Abertura do Google Chrome:**
  Utiliza coordenadas específicas para clicar no ícone do navegador e maximizar a janela.

```python
pyautogui.click(x=958, y=1060)
pyautogui.hotkey('win', 'up')
```

- **Manipulação da Agenda:**
  Clica em locais específicos e arrasta a janela para outra tela.

```python
time.sleep(0.5)
pyautogui.click(x=332, y=31)
pyautogui.dragTo(x=1920, y=500, duration=0.5)
```

- **Abertura de Aplicativos:**
  Automatiza a busca e abertura do TickTick e WhatsApp.

```python
pyautogui.press('win')
pyautogui.write('TickTick')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('win')
pyautogui.write('WhatsApp')
pyautogui.press('enter')
time.sleep(0.5)
```

- **Abertura do Notion:**
  Utiliza atalhos para abrir o navegador em um link específico e maximizar a janela.

```python
pyautogui.hotkey('alt', 'space')
pyautogui.write('um link qualquer')
pyautogui.press('enter')
pyautogui.hotkey('win', 'up')
```

---

## 📦 Instalação e Configuração

1. **Instale o Python:**
   Certifique-se de que o Python está instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. **Instale a Biblioteca `pyautogui`:**
   Execute o seguinte comando no terminal:

   ```bash
   pip install pyautogui
   ```

3. **Ajuste as Coordenadas:**
   Verifique as coordenadas de clique e arraste utilizando o seguinte comando no Python:

   ```python
   import pyautogui
   print(pyautogui.position())
   ```
   Mova o mouse para os locais desejados e anote as coordenadas exibidas no terminal.

4. **Execute o Script:**
   Salve o código em um arquivo com extensão `.py` e execute-o pelo terminal:

   ```bash
   python seu_script.py
   ```

---

## ⚠️ Observações Importantes

- **Coordenadas Dependentes do Sistema:**
  As coordenadas de clique e arraste são específicas para o meu monitor e layout de aplicativos. Ajuste-as para o seu ambiente.

- **Dependência do Ambiente de Trabalho:**
  Certifique-se de que os aplicativos mencionados estão instalados e configurados como no meu ambiente para evitar erros.

---

## 🤝 Contribuições

Este script foi desenvolvido para uso pessoal e pode não atender diretamente a outros cenários. Se você deseja adaptá-lo ou melhorar suas funcionalidades, fique à vontade para contribuir. Abra uma issue ou envie um pull request!

---

## 📜 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
