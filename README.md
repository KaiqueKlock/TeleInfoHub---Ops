# 📡 Operations Hub

Sistema desenvolvido em **Python + Streamlit** para acompanhamento operacional de migrações de telecomunicações.

O projeto nasceu de uma necessidade real durante minha atuação como **Auxiliar de Telecomunicações**, onde era necessário acompanhar simultaneamente mais de uma centena de localidades em processo de migração de links de comunicação.

Ao invés de consultar constantemente planilhas extensas, desenvolvi um dashboard operacional capaz de centralizar as informações mais importantes da operação.

---

# Objetivo

Facilitar o acompanhamento diário das migrações através de uma interface simples, rápida e focada na operação.

O sistema permite visualizar:

- Pendências operacionais
- Agendamentos futuros
- Histórico das últimas movimentações
- Responsável atual
- Localidade
- Identificação do circuito
- Serviço contratado
- Banda
- Indicadores visuais de acompanhamento

---

# Principais Funcionalidades

## 📅 Agenda Operacional

Identifica automaticamente atividades futuras cadastradas no histórico da demanda.

Exemplos reconhecidos:

- Agenda Confirmada
- Vistoria Técnica
- Instalação
- Janela
- Ativação
- Visita Técnica

Cada agenda apresenta:

- Data
- Horário
- Cidade
- Endereço
- Operadora
- ID / Designação
- Serviço
- Banda

---

## 🔴 Pendências Operacionais

Agrupa automaticamente todas as demandas pendentes por operadora.

Exemplo:

```
Claro
├── Campinas
├── Pernambuco
├── Bahia
└── ...
```

---

## 📜 Histórico Inteligente

Cada card apresenta apenas as últimas movimentações relevantes da demanda.

Exemplo:

```
17/07 Agenda Confirmada
15/07 Solicitar novo agendamento
14/07 Atividade confirmada
08/07 Aguardando Operadora
01/07 Vistoria Técnica
```

Isso reduz significativamente a necessidade de abrir a planilha completa.

---

## 🚦 Indicador de Acompanhamento

Cada demanda possui um indicador visual baseado no histórico.

🟢 Atualização recente

🟡 Atenção necessária

🔴 Demanda sem acompanhamento recente

---

## 📍 Informações Operacionais

Cada card apresenta:

- Cidade
- Endereço
- Operadora
- ID / Designação
- Serviço contratado
- Banda
- Empresa responsável
- Últimas atualizações

---

# Arquitetura

O projeto foi organizado utilizando separação por responsabilidades.

```
Operations Hub
│
├── app.py
│
├── models
│   └── Demand
│
├── services
│   ├── ExcelService
│   ├── FilterService
│   ├── AgendaService
│   ├── StatusService
│   ├── IndicatorService
│   └── DemandService
│
├── components
│
├── views
│
├── utils
│
└── data
```

---

# Estrutura dos Services

## ExcelService

Responsável pela leitura da planilha de Follow Up.

---

## FilterService

Realiza filtros de demandas.

Exemplo:

- Pendentes
- Operadora

---

## AgendaService

Procura automaticamente agendas futuras utilizando palavras-chave presentes no histórico da demanda.

---

## StatusService

Manipula o histórico de movimentações.

Responsável por:

- últimos registros
- data da última atualização
- cálculo de dias
- interpretação do histórico

---

## IndicatorService

Traduz as informações do StatusService em indicadores visuais.

---

# Tecnologias

- Python
- Streamlit
- Pandas
- OpenPyXL

---

# Fonte de Dados

O sistema utiliza uma planilha Excel como origem dos dados.

O arquivo não faz parte deste repositório por conter informações internas da empresa.

Cada linha representa uma demanda operacional.

---

# Como executar

Clone o projeto

```bash
git clone ...
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Execute

```bash
streamlit run app.py
```

---

# Roadmap

## Sprint 1

- Leitura da planilha
- Modelo Demand
- Dashboard inicial

---

## Sprint 2

- Cards operacionais
- Agrupamento por operadora
- Informações da localidade

---

## Sprint 3

- Agenda Operacional
- Histórico resumido
- Serviço e Banda

---

## Sprint 4

- Indicador visual
- Refatoração dos Services
- Melhorias de arquitetura

---

# Melhorias Futuras

- Pesquisa avançada
- Dashboard de métricas
- Indicadores por operadora
- Exportação de relatórios
- Integração direta com SharePoint
- Atualização automática da base
- Dashboard executivo
- Histórico de alterações

---

# Motivação

Este projeto foi desenvolvido para resolver um problema real de operação.

Durante períodos de migração simultânea de dezenas de localidades, tornou-se inviável consultar constantemente uma planilha extensa.

O Operations Hub centraliza as informações críticas e reduz significativamente o tempo necessário para localizar pendências, agendas e identificar a próxima ação operacional.

---

# O que aprendi

Durante o desenvolvimento deste projeto pude aplicar diversos conceitos de desenvolvimento de software além da programação em si.

Entre eles:

- Organização por camadas (Models, Services, Components e Views)
- Refatoração contínua
- Separação de responsabilidades (Single Responsibility Principle)
- Manipulação de dados utilizando Pandas
- Construção de interfaces com Streamlit
- Estruturação incremental utilizando Sprints
- Versionamento com Git
- Documentação técnica
- Desenvolvimento orientado ao uso real da ferramenta

---

# Autor

**Kaique Klock**

Projeto desenvolvido para apoio operacional em Telecomunicações utilizando Python e Streamlit.
