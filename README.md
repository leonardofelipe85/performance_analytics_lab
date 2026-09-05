# performance_analytics_lab

Laboratório de estudos em ferramentas de análise de dados, pensamento analítico e automações para Marketing de Performance — preparação prática para atuação como analista de dados/growth.

## Sobre

Repositório com scripts em Python (pandas, matplotlib, plotly) aplicados a dados de campanhas de mídia paga (Google Ads/Meta Ads), seguindo a linha de tratamento de dados → cálculo de métricas → diagnóstico analítico.

*Datasets são simulados, criados para fins de estudo e prática — a lógica de análise é a mesma aplicada a dados reais de campanha.*

## Destaque: detecção de falha de tracking via análise de série temporal

Em `01_ferramenta/01_exploracao_inicial.py`, ao isolar uma campanha de remarketing e plotar cliques x conversões por dia, o gráfico revelou ausência de correlação entre as duas métricas — cliques oscilando entre 60 e quase 800/dia, conversões travadas numa faixa baixa e estável. Esse padrão é assinatura típica de falha de tracking (pixel/evento de conversão não disparando), não de queda real de performance — uma distinção que evita a decisão errada de pausar uma campanha que na verdade está performando bem.

## Estrutura

- `01_ferramenta/` — fundamentos: leitura, limpeza e tratamento de dados, cálculo de métricas (ROAS), visualização
- `02_pensamento_analitico/` — (em andamento)
- `03_automacoes/` — (em andamento)

## Stack

Python · pandas · matplotlib · plotly
