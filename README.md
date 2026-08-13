# Sistema Python PowerUp (versão local para prática)

Réplica funcional do site usado na Aula 1 da Jornada Python, pra você
treinar automação com `pyautogui` igual ao professor fez.

## Como usar

1. Copia essa pasta inteira (`sistema-python-powerup/`) pro seu
   computador, dentro da pasta do seu projeto `pratica-python/aula-01-automacao/`.
2. Abre o `index.html` **dando duplo clique** (ele abre no seu navegador
   padrão, como uma página local — não precisa de servidor).
3. Qualquer e-mail/senha funciona no login, igual na apostila.
4. Depois do login você cai na tela de cadastro de produtos, com o
   formulário e a tabela "Produtos Cadastrados" ao lado — exatamente
   como no mockup do professor.
5. Use o `produtos.csv` (nessa mesma pasta) como sua base de dados pro
   `pd.read_csv`.

## Sobre as posições de clique

Como a apostila explica, as coordenadas de clique são específicas de
CADA monitor/resolução. Use o `pegar_posicao.py` pra pegar as suas:

```
python pegar_posicao.py
```

Rode, e você tem 5 segundos pra posicionar o mouse em cima do campo (ou
botão) que quer descobrir a posição — repita pra cada campo do
formulário: código, marca, tipo, categoria, preço, custo, obs e o botão
Enviar.

## Reiniciar os testes

Os produtos cadastrados ficam salvos no navegador (localStorage). Se
quiser zerar e recomeçar os testes, abre o Console do navegador (F12) na
página `cadastro.html` e roda:

```js
localStorage.removeItem("produtos")
```

Depois recarrega a página.

## Dica pra testar sem esperar rodar 65 produtos

Faz uma cópia do `produtos.csv` só com 5 linhas (`produtos_teste.csv`)
pra validar seu script rápido antes de rodar a base completa.
