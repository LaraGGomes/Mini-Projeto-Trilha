# 🎬 Mini-Projeto: JSON de Filmes e Séries

## 📋 Sobre o Projeto

Este mini-projeto consiste em um parser de arquivos JSON que extrai e organiza informações sobre filmes e séries. O programa lê dados estruturados em JSON, processa as informações e gera um relatório visualmente atraente em formato TXT.

## ✨ Funcionalidades

- **Parsing de JSON**: Leitura e interpretação de arquivos JSON contendo dados de filmes e séries
- **Extração de Dados**: Coleta de características como título, ano, gênero, diretor, elenco, etc.
- **Formatação Visual**: Apresentação dos dados em um formato organizado e visualmente agradável
- **Exportação para TXT**: Geração de relatório em arquivo de texto para fácil visualização

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Biblioteca JSON**: Para parsing dos arquivos de entrada
- **Manipulação de Strings**: Para formatação do relatório de saída

## 🚀 Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/laraggomes/mini-projeto-trilha.git
cd mini-projeto-trilha
```
2. Execute o script principal:
```bash
python miniProjeto.py
```
3. Verifique o arquivo de saída gerado:
```bash
cat miniProjeto.txt
```

# 📁 Estrutura do Projeto
```python
mini-projeto-trilha/
├── miniProjeto.py                # Script principal
├── data/                         # Diretório com arquivos JSON de entrada
│   ├── movies_and_series.json    # Dados dos filmes e séries
├── output/                       # Diretório com arquivos de saída
│   └── miniProjeto.txt           # Relatório gerado
└── README.md                     # Este arquivo
```

# 📝 Exemplo de Entrada (JSON)
```json
{
  "titulo": "Inception",
  "ano": 2010,
  "diretor": "Christopher Nolan",
  "genero": ["Ficção Científica", "Ação", "Thriller"],
  "elenco": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
  "duracao": 148,
  "classificacao": 8.8
}
```
# 📞 Contato
Lara Gomes - laragomes471@gmail.com
Link do projeto: https://github.com/laraggomes/mini-projeto-trilha
⭐️ Feito com ❤️ 
