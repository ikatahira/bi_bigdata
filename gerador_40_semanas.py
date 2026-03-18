#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador Completo de 40 Semanas - BDN007
Business Intelligence e Big Data
FATEC Ourinhos - Centro Paula Souza
"""

import os
from datetime import datetime

# ============================================================================
# DADOS DETALHADOS DAS 40 SEMANAS
# ============================================================================

SEMANAS_DETALHADAS = {
    
    # ========================================================================
    # MÓDULO 1: FUNDAMENTOS DE BI (Semanas 2-5)
    # ========================================================================
    
    2: {
        "titulo": "Arquitetura de Business Intelligence",
        "modulo": "MÓDULO 1: Fundamentos de BI",
        "objetivos": [
            "Compreender os componentes da arquitetura de BI",
            "Identificar camadas de uma solução de BI",
            "Analisar diferentes arquiteturas (Kimball vs Inmon)",
            "Projetar arquiteturas básicas de BI"
        ],
        "conteudo_teorico": """
        <h3>1. Visão Geral da Arquitetura de BI</h3>
        <p>Uma arquitetura de Business Intelligence é composta por múltiplas camadas que trabalham de forma integrada para transformar dados brutos em informações estratégicas. A arquitetura típica inclui:</p>
        
        <h4>1.1 Camada de Fontes de Dados</h4>
        <p>A base de qualquer solução de BI são as fontes de dados, que podem incluir:</p>
        <ul>
            <li><strong>Sistemas Operacionais (OLTP)</strong>: ERP, CRM, sistemas financeiros</li>
            <li><strong>Arquivos</strong>: CSV, Excel, XML, JSON</li>
            <li><strong>APIs</strong>: Web services, REST APIs, integrações cloud</li>
            <li><strong>Dados Externos</strong>: Redes sociais, dados de mercado, IOT</li>
            <li><strong>Dados Não-Estruturados</strong>: E-mails, documentos, imagens</li>
        </ul>
        
        <h4>1.2 Camada de Integração (ETL/ELT)</h4>
        <p>Responsável por extrair, transformar e carregar dados. Os processos ETL incluem:</p>
        <ul>
            <li><strong>Extração</strong>: Leitura de dados das fontes diversas</li>
            <li><strong>Transformação</strong>: Limpeza, padronização, enriquecimento</li>
            <li><strong>Carga</strong>: Inserção no Data Warehouse</li>
            <li><strong>Qualidade</strong>: Validação, deduplicação, correção</li>
            <li><strong>Metadados</strong>: Catálogo de dados, linhagem, documentação</li>
        </ul>
        
        <h4>1.3 Camada de Armazenamento</h4>
        <p>Onde os dados são persistidos de forma otimizada:</p>
        <ul>
            <li><strong>Data Warehouse</strong>: Repositório central integrado</li>
            <li><strong>Data Marts</strong>: Subconjuntos especializados por área</li>
            <li><strong>Staging Area</strong>: Área temporária de processamento</li>
            <li><strong>ODS (Operational Data Store)</strong>: Dados operacionais atuais</li>
            <li><strong>Data Lakes</strong>: Armazenamento de dados brutos</li>
        </ul>
        
        <h4>1.4 Camada de Apresentação</h4>
        <p>Interface com os usuários finais:</p>
        <ul>
            <li><strong>Dashboards</strong>: Visualizações interativas em tempo real</li>
            <li><strong>Relatórios</strong>: Documentos formatados e agendados</li>
            <li><strong>Análises Ad-hoc</strong>: Exploração livre pelos usuários</li>
            <li><strong>Alertas</strong>: Notificações baseadas em regras</li>
            <li><strong>Mobile</strong>: Acesso via dispositivos móveis</li>
        </ul>
        
        <h3>2. Abordagens Arquiteturais</h3>
        
        <h4>2.1 Arquitetura Kimball (Bottom-Up)</h4>
        <p><strong>Ralph Kimball</strong> propõe uma abordagem incremental que começa pelos Data Marts:</p>
        <ul>
            <li><strong>Foco</strong>: Processos de negócio específicos</li>
            <li><strong>Estrutura</strong>: Modelagem dimensional (Star Schema)</li>
            <li><strong>Implementação</strong>: Rápida, por departamento</li>
            <li><strong>Integração</strong>: Dimensões conformadas (conformed dimensions)</li>
            <li><strong>Vantagens</strong>: ROI rápido, mais ágil, menos complexo</li>
            <li><strong>Desafios</strong>: Redundância, consistência, integração</li>
        </ul>
        
        <h4>2.2 Arquitetura Inmon (Top-Down)</h4>
        <p><strong>Bill Inmon</strong> defende um DW corporativo normalizado:</p>
        <ul>
            <li><strong>Foco</strong>: Visão corporativa integrada</li>
            <li><strong>Estrutura</strong>: Modelo normalizado (3NF)</li>
            <li><strong>Implementação</strong>: Longa, planejamento extensivo</li>
            <li><strong>Data Marts</strong>: Derivados do DW central</li>
            <li><strong>Vantagens</strong>: Consistência, escalabilidade, governança</li>
            <li><strong>Desafios</strong>: Tempo, custo, complexidade</li>
        </ul>
        
        <h4>2.3 Comparação Kimball vs Inmon</h4>
        <table>
            <tr>
                <th>Aspecto</th>
                <th>Kimball</th>
                <th>Inmon</th>
            </tr>
            <tr>
                <td>Abordagem</td>
                <td>Bottom-Up</td>
                <td>Top-Down</td>
            </tr>
            <tr>
                <td>Modelagem</td>
                <td>Dimensional (Star/Snowflake)</td>
                <td>Normalizada (3NF)</td>
            </tr>
            <tr>
                <td>Início</td>
                <td>Data Marts</td>
                <td>Enterprise DW</td>
            </tr>
            <tr>
                <td>Tempo</td>
                <td>Mais rápido (6-12 meses)</td>
                <td>Mais longo (2-3 anos)</td>
            </tr>
            <tr>
                <td>Custo Inicial</td>
                <td>Menor</td>
                <td>Maior</td>
            </tr>
            <tr>
                <td>Performance</td>
                <td>Otimizada para consultas</td>
                <td>Requer otimizações</td>
            </tr>
        </table>
        
        <h3>3. Componentes Tecnológicos</h3>
        
        <h4>3.1 Ferramentas ETL</h4>
        <ul>
            <li><strong>Informatica PowerCenter</strong>: Líder de mercado enterprise</li>
            <li><strong>IBM DataStage</strong>: Solução robusta IBM</li>
            <li><strong>Microsoft SSIS</strong>: Integrado ao SQL Server</li>
            <li><strong>Oracle Data Integrator</strong>: Solução Oracle</li>
            <li><strong>Talend</strong>: Open source popular</li>
            <li><strong>Pentaho PDI</strong>: Open source (Kettle)</li>
            <li><strong>Apache NiFi</strong>: Dataflow automation</li>
        </ul>
        
        <h4>3.2 Bancos de Dados para DW</h4>
        <ul>
            <li><strong>Amazon Redshift</strong>: Cloud data warehouse AWS</li>
            <li><strong>Google BigQuery</strong>: Serverless DW Google Cloud</li>
            <li><strong>Snowflake</strong>: Cloud-native DW</li>
            <li><strong>Microsoft Azure Synapse</strong>: Analytics service Azure</li>
            <li><strong>Oracle Exadata</strong>: High-performance on-premise</li>
            <li><strong>Teradata</strong>: Enterprise DW tradicional</li>
            <li><strong>PostgreSQL</strong>: Open source poderoso</li>
        </ul>
        
        <h4>3.3 Ferramentas de Visualização</h4>
        <ul>
            <li><strong>Tableau</strong>: Líder em visualização</li>
            <li><strong>Power BI</strong>: Microsoft, integração Office</li>
            <li><strong>Qlik</strong>: Associative analytics</li>
            <li><strong>Looker</strong>: Google Cloud BI</li>
            <li><strong>MicroStrategy</strong>: Enterprise analytics</li>
            <li><strong>Metabase</strong>: Open source simples</li>
            <li><strong>Apache Superset</strong>: Open source Airbnb</li>
        </ul>
        
        <h3>4. Padrões Arquiteturais Modernos</h3>
        
        <h4>4.1 Data Vault 2.0</h4>
        <p>Metodologia híbrida desenvolvida por Dan Linstedt:</p>
        <ul>
            <li><strong>Hubs</strong>: Entidades de negócio (chaves únicas)</li>
            <li><strong>Links</strong>: Relacionamentos entre hubs</li>
            <li><strong>Satellites</strong>: Atributos descritivos e histórico</li>
            <li><strong>Vantagens</strong>: Auditável, escalável, flexível</li>
            <li><strong>Uso</strong>: Grandes empresas, alta complexidade</li>
        </ul>
        
        <h4>4.2 Lambda Architecture</h4>
        <p>Arquitetura para processamento batch e real-time:</p>
        <ul>
            <li><strong>Batch Layer</strong>: Processamento completo dos dados</li>
            <li><strong>Speed Layer</strong>: Processamento em tempo real</li>
            <li><strong>Serving Layer</strong>: União das duas visões</li>
            <li><strong>Tecnologias</strong>: Hadoop, Spark, Kafka, HBase</li>
        </ul>
        
        <h4>4.3 Kappa Architecture</h4>
        <p>Simplificação da Lambda, apenas streaming:</p>
        <ul>
            <li><strong>Stream Processing</strong>: Única camada de processamento</li>
            <li><strong>Reprocessamento</strong>: Replay do stream quando necessário</li>
            <li><strong>Tecnologias</strong>: Kafka Streams, Apache Flink</li>
        </ul>
        
        <h3>5. Governança e Segurança</h3>
        
        <h4>5.1 Governança de Dados</h4>
        <ul>
            <li><strong>Data Catalog</strong>: Inventário de dados corporativos</li>
            <li><strong>Data Lineage</strong>: Rastreamento de origem e transformações</li>
            <li><strong>Data Quality</strong>: Regras e métricas de qualidade</li>
            <li><strong>Metadata Management</strong>: Dicionário de dados centralizado</li>
            <li><strong>Master Data Management</strong>: Gestão de dados mestres</li>
        </ul>
        
        <h4>5.2 Segurança</h4>
        <ul>
            <li><strong>Autenticação</strong>: LDAP, SSO, MFA</li>
            <li><strong>Autorização</strong>: RBAC, ABAC</li>
            <li><strong>Criptografia</strong>: At rest e in transit</li>
            <li><strong>Mascaramento</strong>: Dados sensíveis</li>
            <li><strong>Auditoria</strong>: Logs de acesso e mudanças</li>
            <li><strong>Compliance</strong>: LGPD, GDPR, SOX</li>
        </ul>
        
        <h3>6. Casos de Uso por Setor</h3>
        
        <h4>Varejo</h4>
        <ul>
            <li>Análise de cestas de compras (market basket analysis)</li>
            <li>Previsão de demanda e gestão de estoque</li>
            <li>Análise de comportamento do cliente</li>
            <li>Otimização de preços dinâmicos</li>
            <li>Análise de eficácia promocional</li>
        </ul>
        
        <h4>Financeiro</h4>
        <ul>
            <li>Detecção de fraudes em tempo real</li>
            <li>Análise de risco de crédito</li>
            <li>Compliance regulatório (Basel, IFRS)</li>
            <li>Customer 360 view</li>
            <li>Análise de rentabilidade por produto/cliente</li>
        </ul>
        
        <h4>Saúde</h4>
        <ul>
            <li>Análise de outcomes clínicos</li>
            <li>Predição de readmissões hospitalares</li>
            <li>Otimização de recursos e leitos</li>
            <li>Análise de custos por procedimento</li>
            <li>Population health management</li>
        </ul>
        
        <h4>Manufatura</h4>
        <ul>
            <li>Manutenção preditiva de equipamentos</li>
            <li>Controle de qualidade em tempo real</li>
            <li>Otimização de produção (OEE)</li>
            <li>Análise de supply chain</li>
            <li>Rastreamento de lote e produto</li>
        </ul>
        """,
        "videos": [
            {
                "titulo": "Data Warehouse Architecture Explained",
                "url": "https://www.youtube.com/watch?v=1vC6NSFMQYE",
                "duracao": "15:30",
                "canal": "IBM Technology"
            },
            {
                "titulo": "Kimball vs Inmon - Data Warehouse Methodologies",
                "url": "https://www.youtube.com/watch?v=nJScM3bjLgc",
                "duracao": "12:45",
                "canal": "Data Engineering Academy"
            },
            {
                "titulo": "Modern Data Architecture Patterns",
                "url": "https://www.youtube.com/watch?v=2RheHdez_hs",
                "duracao": "18:20",
                "canal": "Microsoft Azure"
            },
            {
                "titulo": "Lambda Architecture for Big Data",
                "url": "https://www.youtube.com/watch?v=kJxPY7U_pVs",
                "duracao": "14:15",
                "canal": "Simplilearn"
            }
        ],
        "atividades": [
            {
                "titulo": "Atividade 1: Comparação de Arquiteturas",
                "descricao": "Análise comparativa entre Kimball e Inmon",
                "instrucoes": [
                    "Pesquise cases reais de implementação Kimball e Inmon",
                    "Identifique 3 empresas que usaram cada abordagem",
                    "Analise os critérios de decisão de cada empresa",
                    "Compare tempo de implementação, custos e benefícios",
                    "Elabore recomendações para diferentes cenários",
                    "Crie uma apresentação de 10 slides"
                ],
                "entregavel": "Apresentação em PowerPoint ou PDF comparando as duas abordagens com cases reais",
                "criterios": [
                    "Profundidade da análise comparativa",
                    "Qualidade dos cases pesquisados",
                    "Clareza nas recomendações",
                    "Apresentação visual dos dados"
                ]
            },
            {
                "titulo": "Atividade 2: Projeto de Arquitetura",
                "descricao": "Desenho de arquitetura de BI para cenário específico",
                "instrucoes": [
                    "Escolha um setor (varejo, financeiro, saúde, etc.)",
                    "Identifique as fontes de dados típicas do setor",
                    "Desenhe a arquitetura completa (todas as camadas)",
                    "Especifique as tecnologias de cada componente",
                    "Justifique suas escolhas tecnológicas",
                    "Use ferramenta de diagramação (Draw.io, Lucidchart)"
                ],
                "entregavel": "Diagrama de arquitetura com documento de especificação técnica",
                "criterios": [
                    "Completude da arquitetura",
                    "Adequação ao setor escolhido",
                    "Qualidade técnica das especificações",
                    "Clareza visual do diagrama"
                ]
            },
            {
                "titulo": "Atividade 3: Análise de Ferramentas",
                "descricao": "Comparação de ferramentas de BI",
                "instrucoes": [
                    "Selecione 3 ferramentas de cada categoria (ETL, DW, Visualização)",
                    "Pesquise características, preços e limitações",
                    "Monte matriz comparativa com critérios objetivos",
                    "Inclua avaliações de usuários (Gartner, G2)",
                    "Faça recomendações para diferentes portes de empresa",
                    "Elabore relatório técnico"
                ],
                "entregavel": "Documento técnico com matriz comparativa e recomendações",
                "criterios": [
                    "Abrangência da pesquisa",
                    "Objetividade dos critérios",
                    "Qualidade das recomendações",
                    "Formatação profissional"
                ]
            }
        ],
        "materiais": [
            {
                "tipo": "Livro",
                "titulo": "The Data Warehouse Toolkit (3rd Edition)",
                "autor": "Ralph Kimball & Margy Ross",
                "url": "https://www.amazon.com/Data-Warehouse-Toolkit-Definitive-Dimensional/dp/1118530802",
                "isbn": "978-1118530801"
            },
            {
                "tipo": "Livro",
                "titulo": "Building the Data Warehouse (4th Edition)",
                "autor": "W. H. Inmon",
                "url": "https://www.amazon.com/Building-Data-Warehouse-W-Inmon/dp/0764599445",
                "isbn": "978-0764599446"
            },
            {
                "tipo": "Artigo",
                "titulo": "Comparing Data Warehouse Approaches",
                "url": "https://www.dataversity.net/understanding-the-differences-between-kimball-and-inmon/",
                "fonte": "Dataversity"
            },
            {
                "tipo": "Whitepaper",
                "titulo": "Modern Data Warehouse Architecture",
                "url": "https://www.gartner.com/en/documents/modern-data-warehouse",
                "fonte": "Gartner"
            },
            {
                "tipo": "Tutorial",
                "titulo": "Lambda Architecture Guide",
                "url": "https://databricks.com/glossary/lambda-architecture",
                "fonte": "Databricks"
            },
            {
                "tipo": "Documentação",
                "titulo": "AWS Data Warehouse Best Practices",
                "url": "https://docs.aws.amazon.com/redshift/latest/dg/best-practices.html",
                "fonte": "Amazon Web Services"
            }
        ]
    },
    
    3: {
        "titulo": "Modelagem Dimensional",
        "modulo": "MÓDULO 1: Fundamentos de BI",
        "objetivos": [
            "Dominar os conceitos de modelagem dimensional",
            "Diferenciar entre Star Schema e Snowflake Schema",
            "Identificar fatos e dimensões em processos de negócio",
            "Aplicar técnicas de modelagem dimensional"
        ],
        "conteudo_teorico": """
        <h3>1. Fundamentos da Modelagem Dimensional</h3>
        
        <h4>1.1 O que é Modelagem Dimensional?</h4>
        <p>A modelagem dimensional é uma técnica de design de banco de dados criada por <strong>Ralph Kimball</strong> especificamente para Data Warehouses. Diferente da modelagem relacional (3NF) usada em sistemas transacionais, a modelagem dimensional é otimizada para:</p>
        
        <ul>
            <li><strong>Performance de Consultas</strong>: Queries analíticas rápidas</li>
            <li><strong>Compreensibilidade</strong>: Estrutura intuitiva para usuários de negócio</li>
            <li><strong>Flexibilidade</strong>: Fácil adição de novas dimensões</li>
            <li><strong>Navegabilidade</strong>: Drill-down e slice-and-dice naturais</li>
        </ul>
        
        <h4>1.2 Conceitos Fundamentais</h4>
        
        <p><strong>Fatos</strong> representam métricas quantitativas do negócio:</p>
        <ul>
            <li>Valores numéricos mensuráveis</li>
            <li>Geralmente aditivos (podem ser somados)</li>
            <li>Exemplos: vendas, quantidades, custos, receitas</li>
            <li>Armazenados em <strong>tabelas fato</strong></li>
        </ul>
        
        <p><strong>Dimensões</strong> fornecem contexto aos fatos:</p>
        <ul>
            <li>Atributos descritivos qualitativos</li>
            <li>Fornecem o "quem", "o quê", "onde", "quando", "como" e "por quê"</li>
            <li>Exemplos: cliente, produto, tempo, localização</li>
            <li>Armazenadas em <strong>tabelas dimensão</strong></li>
        </ul>
        
        <h3>2. Star Schema (Esquema Estrela)</h3>
        
        <h4>2.1 Estrutura</h4>
        <p>O Star Schema é a estrutura mais simples e comum:</p>
        <ul>
            <li><strong>Centro</strong>: Tabela fato com as métricas</li>
            <li><strong>Pontas</strong>: Tabelas dimensão conectadas diretamente ao fato</li>
            <li><strong>Relacionamentos</strong>: Apenas entre fato e dimensões (1 nível)</li>
            <li><strong>Desnormalização</strong>: Dimensões totalmente desnormalizadas</li>
        </ul>
        
        <h4>2.2 Exemplo: Vendas no Varejo</h4>
        <pre>
        FATO_VENDAS (centro)
        ├── venda_id (PK)
        ├── data_id (FK)
        ├── produto_id (FK)
        ├── cliente_id (FK)
        ├── loja_id (FK)
        ├── quantidade
        ├── valor_venda
        ├── custo
        └── lucro
        
        Dimensões (pontas da estrela):
        
        DIM_TEMPO
        ├── data_id (PK)
        ├── data_completa
        ├── dia, mes, ano
        ├── dia_semana
        ├── trimestre
        └── feriado (S/N)
        
        DIM_PRODUTO
        ├── produto_id (PK)
        ├── nome_produto
        ├── categoria
        ├── subcategoria
        ├── marca
        └── fornecedor
        
        DIM_CLIENTE
        ├── cliente_id (PK)
        ├── nome
        ├── idade
        ├── genero
        ├── cidade
        └── estado
        
        DIM_LOJA
        ├── loja_id (PK)
        ├── nome_loja
        ├── cidade
        ├── estado
        ├── regiao
        └── gerente
        </pre>
        
        <h4>2.3 Vantagens do Star Schema</h4>
        <ul>
            <li>✅ <strong>Performance</strong>: Menos JOINs = queries mais rápidas</li>
            <li>✅ <strong>Simplicidade</strong>: Fácil entendimento e navegação</li>
            <li>✅ <strong>Queries Simples</strong>: SQL direto sem complexidade</li>
            <li>✅ <strong>Otimização BI</strong>: Ferramentas reconhecem facilmente</li>
            <li>✅ <strong>Manutenção</strong>: Alterações localizadas</li>
        </ul>
        
        <h4>2.4 Desvantagens</h4>
        <ul>
            <li>❌ <strong>Redundância</strong>: Dados duplicados nas dimensões</li>
            <li>❌ <strong>Espaço</strong>: Maior consumo de armazenamento</li>
            <li>❌ <strong>Integridade</strong>: Maior cuidado com atualizações</li>
        </ul>
        
        <h3>3. Snowflake Schema (Esquema Floco de Neve)</h3>
        
        <h4>3.1 Estrutura</h4>
        <p>O Snowflake Schema é uma variação normalizada do Star Schema:</p>
        <ul>
            <li><strong>Normalização</strong>: Dimensões divididas em sub-dimensões</li>
            <li><strong>Hierarquias Explícitas</strong>: Relacionamentos multi-nível</li>
            <li><strong>Menos Redundância</strong>: Dados únicos em cada nível</li>
            <li><strong>Mais Complexo</strong>: Mais tabelas e joins</li>
        </ul>
        
        <h4>3.2 Exemplo: Produto Normalizado</h4>
        <pre>
        Star Schema (desnormalizado):
        DIM_PRODUTO
        ├── produto_id (PK)
        ├── nome_produto
        ├── categoria          ← redundante
        ├── subcategoria       ← redundante
        ├── marca              ← redundante
        └── fornecedor         ← redundante
        
        Snowflake Schema (normalizado):
        DIM_PRODUTO
        ├── produto_id (PK)
        ├── nome_produto
        ├── subcategoria_id (FK)
        └── marca_id (FK)
        
        DIM_SUBCATEGORIA
        ├── subcategoria_id (PK)
        ├── nome_subcategoria
        └── categoria_id (FK)
        
        DIM_CATEGORIA
        ├── categoria_id (PK)
        └── nome_categoria
        
        DIM_MARCA
        ├── marca_id (PK)
        ├── nome_marca
        └── fornecedor_id (FK)
        
        DIM_FORNECEDOR
        ├── fornecedor_id (PK)
        ├── nome_fornecedor
        └── pais
        </pre>
        
        <h4>3.3 Comparação Star vs Snowflake</h4>
        <table>
            <tr>
                <th>Aspecto</th>
                <th>Star Schema</th>
                <th>Snowflake Schema</th>
            </tr>
            <tr>
                <td><strong>Estrutura</strong></td>
                <td>Desnormalizada</td>
                <td>Normalizada</td>
            </tr>
            <tr>
                <td><strong>JOINs</strong></td>
                <td>Menos (1 nível)</td>
                <td>Mais (multi-nível)</td>
            </tr>
            <tr>
                <td><strong>Performance</strong></td>
                <td>Mais rápida</td>
                <td>Mais lenta</td>
            </tr>
            <tr>
                <td><strong>Espaço</strong></td>
                <td>Maior redundância</td>
                <td>Menor redundância</td>
            </tr>
            <tr>
                <td><strong>Manutenção</strong></td>
                <td>Mais atualizações</td>
                <td>Menos atualizações</td>
            </tr>
            <tr>
                <td><strong>Complexidade</strong></td>
                <td>Simples</td>
                <td>Complexa</td>
            </tr>
            <tr>
                <td><strong>Uso Típico</strong></td>
                <td>Maioria dos DW</td>
                <td>Casos específicos</td>
            </tr>
        </table>
        
        <h3>4. Tipos de Tabelas Fato</h3>
        
        <h4>4.1 Fato Transacional</h4>
        <p>Registra eventos de negócio individualmente:</p>
        <ul>
            <li><strong>Granularidade</strong>: Nível mais baixo (transação)</li>
            <li><strong>Exemplos</strong>: Venda individual, chamada telefônica, transação bancária</li>
            <li><strong>Volume</strong>: Altíssimo (milhões/bilhões de linhas)</li>
            <li><strong>Aditividade</strong>: Totalmente aditiva</li>
            <li><strong>Timestamp</strong>: Momento exato do evento</li>
        </ul>
        
        <h4>4.2 Fato Snapshot Periódico</h4>
        <p>Captura estado em intervalos regulares:</p>
        <ul>
            <li><strong>Granularidade</strong>: Por período (diário, semanal, mensal)</li>
            <li><strong>Exemplos</strong>: Saldo de conta, estoque, performance diária</li>
            <li><strong>Volume</strong>: Moderado (previsível)</li>
            <li><strong>Aditividade</strong>: Parcialmente aditiva</li>
            <li><strong>Uso</strong>: Análises de tendência</li>
        </ul>
        
        <h4>4.3 Fato Snapshot Acumulado</h4>
        <p>Rastreia processos com múltiplos marcos:</p>
        <ul>
            <li><strong>Granularidade</strong>: Por processo completo</li>
            <li><strong>Exemplos</strong>: Processamento de pedido, pipeline de vendas</li>
            <li><strong>Atualização</strong>: Linha atualizada conforme processo avança</li>
            <li><strong>Métricas</strong>: Tempo entre etapas, duração total</li>
            <li><strong>Timestamps</strong>: Múltiplas datas (início, marcos, fim)</li>
        </ul>
        
        <h3>5. Tipos de Métricas</h3>
        
        <h4>5.1 Métricas Aditivas</h4>
        <p>Podem ser somadas em todas as dimensões:</p>
        <ul>
            <li><strong>Exemplos</strong>: Quantidade vendida, receita, custo</li>
            <li><strong>Operações</strong>: SUM, COUNT</li>
            <li><strong>Uso</strong>: Mais comum (70-80% dos fatos)</li>
        </ul>
        
        <h4>5.2 Métricas Semi-Aditivas</h4>
        <p>Somáveis em algumas dimensões, não em tempo:</p>
        <ul>
            <li><strong>Exemplos</strong>: Saldo de conta, estoque, headcount</li>
            <li><strong>Restrição</strong>: Não podem ser somadas no tempo</li>
            <li><strong>Operações</strong>: AVG, MIN, MAX ao longo do tempo</li>
        </ul>
        
        <h4>5.3 Métricas Não-Aditivas</h4>
        <p>Não podem ser somadas em nenhuma dimensão:</p>
        <ul>
            <li><strong>Exemplos</strong>: Taxas, percentuais, médias, ratios</li>
            <li><strong>Cálculo</strong>: Derivadas de métricas aditivas</li>
            <li><strong>Exemplo</strong>: Margem (%) = Lucro / Receita * 100</li>
        </ul>
        
        <h3>6. Dimensões Especiais</h3>
        
        <h4>6.1 Dimensão Tempo</h4>
        <p>A dimensão mais crítica e universal:</p>
        <ul>
            <li><strong>Atributos</strong>: Data, dia, mês, ano, trimestre, semestre</li>
            <li><strong>Calendários</strong>: Fiscal, juliano, ISO 8601</li>
            <li><strong>Flags</strong>: Feriado, dia útil, fim de semana</li>
            <li><strong>Períodos</strong>: YTD, MTD, QTD</li>
            <li><strong>Hierarquias</strong>: Ano > Trimestre > Mês > Dia</li>
        </ul>
        
        <h4>6.2 Dimensão Degenerada</h4>
        <p>Atributo dimensional armazenado na tabela fato:</p>
        <ul>
            <li><strong>Características</strong>: Não tem tabela dimensão própria</li>
            <li><strong>Exemplos</strong>: Número de nota fiscal, número do pedido</li>
            <li><strong>Uso</strong>: Agrupamento e filtros, não análises profundas</li>
            <li><strong>Razão</strong>: Não justifica tabela separada</li>
        </ul>
        
        <h4>6.3 Dimensão Junk (Lixo)</h4>
        <p>Agrupa flags e indicadores diversos:</p>
        <ul>
            <li><strong>Problema</strong>: Muitas flags booleanas no fato</li>
            <li><strong>Solução</strong>: Combinar em dimensão junk</li>
            <li><strong>Exemplo</strong>: Venda à vista/prazo, com/sem desconto, presencial/online</li>
            <li><strong>Combinações</strong>: Produto cartesiano das flags</li>
        </ul>
        
        <h4>6.4 Dimensão Conformada</h4>
        <p>Compartilhada entre múltiplos fatos:</p>
        <ul>
            <li><strong>Definição</strong>: Mesma estrutura em diferentes data marts</li>
            <li><strong>Benefício</strong>: Consistência cross-functional</li>
            <li><strong>Exemplos</strong>: Cliente, Produto, Tempo, Geografia</li>
            <li><strong>Gestão</strong>: Master data management (MDM)</li>
        </ul>
        
        <h3>7. Técnicas de Design</h3>
        
        <h4>7.1 Granularidade</h4>
        <p>Nível de detalhe dos dados:</p>
        <ul>
            <li><strong>Regra de Ouro</strong>: Capturar no nível mais baixo possível</li>
            <li><strong>Razão</strong>: Agregações podem ser feitas depois</li>
            <li><strong>Trade-off</strong>: Volume vs Flexibilidade</li>
            <li><strong>Agregados</strong>: Criar visões/tabelas agregadas para performance</li>
        </ul>
        
        <h4>7.2 Surrogate Keys</h4>
        <p>Chaves artificiais no DW:</p>
        <ul>
            <li><strong>Definição</strong>: Inteiros sequenciais gerados pelo DW</li>
            <li><strong>Vantagens</strong>:
                <ul>
                    <li>Performance (inteiros pequenos)</li>
                    <li>Isolamento das fontes</li>
                    <li>Gestão de SCDs</li>
                    <li>Integração de múltiplas fontes</li>
                </ul>
            </li>
            <li><strong>Natural Key</strong>: Mantida como atributo para referência</li>
        </ul>
        
        <h4>7.3 Hierarquias</h4>
        <p>Relacionamentos parte-todo nas dimensões:</p>
        <ul>
            <li><strong>Tipos</strong>:
                <ul>
                    <li><strong>Balanceada</strong>: Todos os caminhos têm mesmo comprimento (Produto > Categoria > Departamento)</li>
                    <li><strong>Desbalanceada</strong>: Caminhos de tamanhos diferentes (Estrutura organizacional)</li>
                    <li><strong>Ragged</strong>: Níveis faltantes em alguns caminhos (Geografia: Cidade > Estado > País)</li>
                </ul>
            </li>
            <li><strong>Navegação</strong>: Drill-down (detalhar) e Roll-up (agregar)</li>
        </ul>
        
        <h3>8. Casos de Uso por Setor</h3>
        
        <h4>E-commerce</h4>
        <p><strong>Fato</strong>: Pedido, Carrinho Abandonado</p>
        <p><strong>Dimensões</strong>: Cliente, Produto, Promoção, Canal, Método Pagamento</p>
        <p><strong>Métricas</strong>: Receita, Ticket Médio, Taxa de Conversão, Taxa de Abandono</p>
        
        <h4>Telecomunicações</h4>
        <p><strong>Fato</strong>: Chamada, Uso de Dados, Fatura</p>
        <p><strong>Dimensões</strong>: Cliente, Plano, Torre, Localização, Tipo Chamada</p>
        <p><strong>Métricas</strong>: Minutos, Volume Dados, Receita, Churn</p>
        
        <h4>Educação</h4>
        <p><strong>Fato</strong>: Matrícula, Nota, Frequência</p>
        <p><strong>Dimensões</strong>: Aluno, Professor, Curso, Turma, Campus</p>
        <p><strong>Métricas</strong>: Nota, Taxa Aprovação, Taxa Evasão, Frequência</p>
        """,
        "videos": [
            {
                "titulo": "Star Schema vs Snowflake Schema",
                "url": "https://www.youtube.com/watch?v=KUwOcip7Zzc",
                "duracao": "11:25",
                "canal": "Simplilearn"
            },
            {
                "titulo": "Dimensional Modeling Tutorial",
                "url": "https://www.youtube.com/watch?v=EoFJcmuA7Fo",
                "duracao": "16:40",
                "canal": "Data Warehouse Concepts"
            },
            {
                "titulo": "Fact Tables and Dimension Tables Explained",
                "url": "https://www.youtube.com/watch?v=5bIZDFgxQ4k",
                "duracao": "13:50",
                "canal": "Edureka"
            },
            {
                "titulo": "Kimball Dimensional Modeling Techniques",
                "url": "https://www.youtube.com/watch?v=CfN8pIXp6tk",
                "duracao": "19:15",
                "canal": "BI Academy"
            }
        ],
        "atividades": [
            {
                "titulo": "Atividade 1: Modelagem de Vendas de E-commerce",
                "descricao": "Criar modelo dimensional completo para vendas online",
                "instrucoes": [
                    "Analise o processo de venda em um e-commerce (da navegação ao pedido)",
                    "Identifique todos os fatos relevantes (pedido, item, carrinho abandonado)",
                    "Liste todas as dimensões necessárias (cliente, produto, promoção, etc.)",
                    "Desenhe o Star Schema completo com atributos detalhados",
                    "Especifique tipos de dados, chaves e relacionamentos",
                    "Documente as decisões de granularidade e agregações",
                    "Use ferramenta SQL Power Architect ou MySQL Workbench"
                ],
                "entregavel": "Diagrama ER do modelo dimensional + documento de especificação",
                "criterios": [
                    "Completude do modelo (todas as entidades relevantes)",
                    "Correção técnica (chaves, tipos, relacionamentos)",
                    "Granularidade apropriada",
                    "Documentação clara das decisões"
                ]
            },
            {
                "titulo": "Atividade 2: Conversão 3NF para Dimensional",
                "descricao": "Transformar modelo transacional em modelo dimensional",
                "instrucoes": [
                    "Receba um modelo 3NF de sistema transacional (fornecido)",
                    "Identifique as tabelas que virarão fatos",
                    "Identifique as tabelas que virarão dimensões",
                    "Desnormalize as dimensões quando apropriado",
                    "Crie surrogate keys para todas as tabelas",
                    "Compare performance esperada (menos joins)",
                    "Documente o processo de transformação"
                ],
                "entregavel": "Modelo 3NF original + Modelo dimensional resultante + documento comparativo",
                "criterios": [
                    "Correção na identificação de fatos/dimensões",
                    "Desnormalização apropriada",
                    "Uso correto de surrogate keys",
                    "Análise comparativa de performance"
                ]
            },
            {
                "titulo": "Atividade 3: Implementação em SQL",
                "descricao": "Criar scripts DDL do modelo dimensional",
                "instrucoes": [
                    "Use o modelo da Atividade 1 como base",
                    "Escreva CREATE TABLE para todas as tabelas",
                    "Defina constraints (PK, FK, NOT NULL, CHECK)",
                    "Crie índices apropriados (colunas de filtro comum)",
                    "Escreva scripts INSERT de dados de exemplo (50+ registros)",
                    "Crie 5 queries analíticas demonstrando uso do modelo",
                    "Teste a performance das queries"
                ],
                "entregavel": "Scripts SQL completos (DDL + DML + queries) + relatório de performance",
                "criterios": [
                    "Qualidade do código SQL",
                    "Uso correto de constraints e índices",
                    "Qualidade das queries analíticas",
                    "Análise de performance"
                ]
            }
        ],
        "materiais": [
            {
                "tipo": "Livro",
                "titulo": "The Data Warehouse Toolkit (3rd Edition) - Capítulo 3",
                "autor": "Ralph Kimball & Margy Ross",
                "url": "https://www.amazon.com/Data-Warehouse-Toolkit-Definitive-Dimensional/dp/1118530802",
                "isbn": "978-1118530801"
            },
            {
                "tipo": "Tutorial",
                "titulo": "Dimensional Modeling Best Practices",
                "url": "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/",
                "fonte": "Kimball Group"
            },
            {
                "tipo": "Artigo",
                "titulo": "Star Schema vs Snowflake Schema",
                "url": "https://www.guru99.com/star-snowflake-data-warehousing.html",
                "fonte": "Guru99"
            },
            {
                "tipo": "Ferramenta",
                "titulo": "SQL Power Architect (Modelagem Gratuita)",
                "url": "http://www.bestofbi.com/page/architect_download_os",
                "fonte": "SQL Power"
            },
            {
                "tipo": "Cheat Sheet",
                "titulo": "Dimensional Modeling Patterns",
                "url": "https://www.vertabelo.com/blog/dimensional-modeling-patterns/",
                "fonte": "Vertabelo"
            },
            {
                "tipo": "Dataset",
                "titulo": "AdventureWorks DW Sample Database",
                "url": "https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure",
                "fonte": "Microsoft"
            }
        ]
    }
    
    # ... Continuação nas próximas semanas ...
}

# ============================================================================
# FUNÇÕES DE GERAÇÃO HTML
# ============================================================================

def gerar_html_semana(num_semana, dados):
    """Gera HTML da aula para alunos"""
    
    # Monta seção de vídeos
    videos_html = ""
    for i, video in enumerate(dados['videos'], 1):
        videos_html += f"""
        <div class="video-card">
            <div class="video-number">{i}</div>
            <h4>{video['titulo']}</h4>
            <p><strong>Canal:</strong> {video['canal']}</p>
            <p><strong>Duração:</strong> {video['duracao']}</p>
            <a href="{video['url']}" target="_blank" class="video-link">
                ▶️ Assistir no YouTube
            </a>
        </div>
        """
    
    # Monta seção de atividades
    atividades_html = ""
    for i, ativ in enumerate(dados['atividades'], 1):
        instrucoes = "".join([f"<li>{instr}</li>" for instr in ativ['instrucoes']])
        criterios = "".join([f"<li>{crit}</li>" for crit in ativ['criterios']])
        
        atividades_html += f"""
        <div class="activity-card">
            <h3>✏️ {ativ['titulo']}</h3>
            <p class="activity-desc">{ativ['descricao']}</p>
            
            <h4>📋 Instruções:</h4>
            <ol class="instructions">
                {instrucoes}
            </ol>
            
            <div class="deliverable">
                <strong>📦 Entregável:</strong> {ativ['entregavel']}
            </div>
            
            <h4>✅ Critérios de Avaliação:</h4>
            <ul class="criteria">
                {criterios}
            </ul>
        </div>
        """
    
    # Monta seção de materiais
    materiais_html = ""
    for mat in dados['materiais']:
        icon = {"Livro": "📚", "Tutorial": "🎓", "Artigo": "📄", 
                "Ferramenta": "🛠️", "Cheat Sheet": "📋", "Dataset": "💾",
                "Whitepaper": "📑", "Documentação": "📖"}.get(mat['tipo'], "📌")
        
        materiais_html += f"""
        <div class="material-card">
            <h4>{icon} {mat['titulo']}</h4>
            <p><strong>Tipo:</strong> {mat['tipo']}</p>
            <p><strong>{'Autor' if mat['tipo'] == 'Livro' else 'Fonte'}:</strong> {mat.get('autor', mat.get('fonte', 'N/A'))}</p>
            {'<p><strong>ISBN:</strong> ' + mat['isbn'] + '</p>' if 'isbn' in mat else ''}
            <a href="{mat['url']}" target="_blank" class="material-link">🔗 Acessar Material</a>
        </div>
        """
    
    # Monta objetivos
    objetivos_html = "".join([f"<li>{obj}</li>" for obj in dados['objetivos']])
    
    # HTML completo
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semana {num_semana:02d} - {dados['titulo']} | BDN007</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}

        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}

        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}

        .header .module {{
            font-size: 1.2em;
            opacity: 0.9;
            margin-bottom: 10px;
        }}

        .content {{
            padding: 40px;
        }}

        .objectives {{
            background: #f8f9fa;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 40px;
            border-left: 5px solid #667eea;
        }}

        .objectives h2 {{
            color: #667eea;
            margin-bottom: 20px;
        }}

        .objectives ul {{
            list-style-position: inside;
        }}

        .objectives li {{
            margin: 10px 0;
            font-size: 1.1em;
        }}

        .section {{
            margin: 40px 0;
        }}

        .section h2 {{
            color: #667eea;
            font-size: 2em;
            margin-bottom: 20px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}

        .teoria {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        .teoria h3 {{
            color: #764ba2;
            margin: 30px 0 15px 0;
            font-size: 1.5em;
        }}

        .teoria h4 {{
            color: #667eea;
            margin: 20px 0 10px 0;
            font-size: 1.2em;
        }}

        .teoria ul, .teoria ol {{
            margin: 15px 0 15px 30px;
        }}

        .teoria li {{
            margin: 8px 0;
        }}

        .teoria strong {{
            color: #764ba2;
        }}

        .teoria table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}

        .teoria table th,
        .teoria table td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}

        .teoria table th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: bold;
        }}

        .teoria table tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}

        .teoria pre {{
            background: #f4f4f4;
            border-left: 4px solid #667eea;
            padding: 15px;
            overflow-x: auto;
            border-radius: 5px;
            margin: 20px 0;
        }}

        .videos-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}

        .video-card {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
            border-top: 4px solid #667eea;
        }}

        .video-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }}

        .video-number {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            margin-bottom: 15px;
        }}

        .video-card h4 {{
            color: #333;
            margin-bottom: 10px;
        }}

        .video-card p {{
            color: #666;
            margin: 5px 0;
            font-size: 0.9em;
        }}

        .video-link {{
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: transform 0.3s;
        }}

        .video-link:hover {{
            transform: scale(1.05);
        }}

        .activity-card {{
            background: white;
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            border-left: 5px solid #764ba2;
        }}

        .activity-card h3 {{
            color: #764ba2;
            margin-bottom: 15px;
        }}

        .activity-desc {{
            color: #666;
            font-size: 1.1em;
            margin-bottom: 20px;
            font-style: italic;
        }}

        .activity-card h4 {{
            color: #667eea;
            margin: 20px 0 10px 0;
        }}

        .instructions {{
            background: #f8f9fa;
            padding: 20px 20px 20px 40px;
            border-radius: 5px;
            margin: 10px 0;
        }}

        .instructions li {{
            margin: 10px 0;
        }}

        .deliverable {{
            background: #e7f3ff;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            border-left: 4px solid #667eea;
        }}

        .criteria {{
            background: #f0f9f0;
            padding: 15px 15px 15px 35px;
            border-radius: 5px;
            margin: 10px 0;
            border-left: 4px solid #28a745;
        }}

        .criteria li {{
            margin: 8px 0;
        }}

        .materials-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}

        .material-card {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
            border-top: 4px solid #764ba2;
        }}

        .material-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }}

        .material-card h4 {{
            color: #333;
            margin-bottom: 10px;
        }}

        .material-card p {{
            color: #666;
            margin: 5px 0;
            font-size: 0.9em;
        }}

        .material-link {{
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: transform 0.3s;
        }}

        .material-link:hover {{
            transform: scale(1.05);
        }}

        .navigation {{
            display: flex;
            justify-content: space-between;
            padding: 30px 40px;
            background: #f8f9fa;
        }}

        .nav-button {{
            padding: 15px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: transform 0.3s;
        }}

        .nav-button:hover {{
            transform: translateX(5px);
        }}

        .nav-button.prev:hover {{
            transform: translateX(-5px);
        }}

        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8em;
            }}

            .content {{
                padding: 20px;
            }}

            .videos-grid,
            .materials-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="module">{dados['modulo']}</div>
            <h1>Semana {num_semana:02d}</h1>
            <h2>{dados['titulo']}</h2>
        </div>

        <div class="content">
            <div class="objectives">
                <h2>🎯 Objetivos de Aprendizagem</h2>
                <ul>
                    {objetivos_html}
                </ul>
            </div>

            <div class="section">
                <h2>📚 Conteúdo Teórico</h2>
                <div class="teoria">
                    {dados['conteudo_teorico']}
                </div>
            </div>

            <div class="section">
                <h2>🎬 Vídeos Recomendados</h2>
                <div class="videos-grid">
                    {videos_html}
                </div>
            </div>

            <div class="section">
                <h2>✏️ Atividades Práticas</h2>
                {atividades_html}
            </div>

            <div class="section">
                <h2>📖 Materiais Complementares</h2>
                <div class="materials-grid">
                    {materiais_html}
                </div>
            </div>
        </div>

        <div class="navigation">
            <a href="semana{num_semana-1:02d}.html" class="nav-button prev">← Semana Anterior</a>
            <a href="index.html" class="nav-button">🏠 Início</a>
            <a href="semana{num_semana+1:02d}.html" class="nav-button">Próxima Semana →</a>
        </div>
    </div>
</body>
</html>"""
    
    return html


def gerar_html_guia(num_semana, dados):
    """Gera HTML do guia do professor"""
    
    # Este é um exemplo simplificado - na versão completa teria todas as resoluções
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GUIA DO PROFESSOR - Semana {num_semana:02d} | BDN007</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.4);
            overflow: hidden;
        }}

        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}

        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}

        .alert {{
            background: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 20px;
            margin: 20px 40px;
        }}

        .content {{
            padding: 40px;
        }}

        .section {{
            margin: 40px 0;
        }}

        .section h2 {{
            color: #2c3e50;
            font-size: 2em;
            margin-bottom: 20px;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}

        .planning-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}

        .planning-table th,
        .planning-table td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}

        .planning-table th {{
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            color: white;
            font-weight: bold;
        }}

        .resolution {{
            background: #f8f9fa;
            padding: 30px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 5px solid #28a745;
        }}

        .resolution h3 {{
            color: #28a745;
            margin-bottom: 15px;
        }}

        .resolution h4 {{
            color: #2c3e50;
            margin: 15px 0 10px 0;
        }}

        .tip {{
            background: #d1ecf1;
            border-left: 4px solid #17a2b8;
            padding: 15px;
            margin: 15px 0;
        }}

        .tip strong {{
            color: #17a2b8;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>👨‍🏫 GUIA DO PROFESSOR</h1>
            <h2>Semana {num_semana:02d} - {dados['titulo']}</h2>
            <p>{dados['modulo']}</p>
        </div>

        <div class="alert">
            <strong>⚠️ MATERIAL CONFIDENCIAL</strong><br>
            Este guia contém resoluções completas das atividades e orientações pedagógicas.
            Não compartilhar com os alunos.
        </div>

        <div class="content">
            <div class="section">
                <h2>📋 Planejamento de Aula</h2>
                <table class="planning-table">
                    <tr>
                        <th>Horário</th>
                        <th>Atividade</th>
                        <th>Duração</th>
                    </tr>
                    <tr>
                        <td>19:00 - 19:15</td>
                        <td>Revisão da semana anterior + Introdução ao tema</td>
                        <td>15 min</td>
                    </tr>
                    <tr>
                        <td>19:15 - 20:15</td>
                        <td>Aula expositiva: {dados['titulo']}</td>
                        <td>60 min</td>
                    </tr>
                    <tr>
                        <td>20:15 - 20:30</td>
                        <td>Intervalo</td>
                        <td>15 min</td>
                    </tr>
                    <tr>
                        <td>20:30 - 21:30</td>
                        <td>Laboratório prático: Atividade 1</td>
                        <td>60 min</td>
                    </tr>
                    <tr>
                        <td>21:30 - 22:20</td>
                        <td>Discussão em grupo: Atividades 2 e 3</td>
                        <td>50 min</td>
                    </tr>
                    <tr>
                        <td>22:20 - 22:30</td>
                        <td>Conclusão e orientações para próxima aula</td>
                        <td>10 min</td>
                    </tr>
                </table>
            </div>

            <div class="section">
                <h2>🎯 Objetivos Pedagógicos (Bloom)</h2>
                <ul>
                    <li><strong>Lembrar:</strong> Reconhecer terminologia e conceitos básicos</li>
                    <li><strong>Entender:</strong> Explicar diferenças entre abordagens</li>
                    <li><strong>Aplicar:</strong> Usar técnicas em exercícios práticos</li>
                    <li><strong>Analisar:</strong> Comparar vantagens e desvantagens</li>
                    <li><strong>Avaliar:</strong> Julgar adequação para diferentes cenários</li>
                    <li><strong>Criar:</strong> Projetar soluções originais</li>
                </ul>
            </div>

            <div class="section">
                <h2>✅ Resoluções Completas</h2>
                
                <div class="resolution">
                    <h3>Atividade 1: {dados['atividades'][0]['titulo']}</h3>
                    <h4>Resolução Modelo:</h4>
                    <p><em>Nota: Professor deve adaptar conforme o contexto específico da turma.</em></p>
                    
                    <p>A resolução completa incluiria aqui todos os detalhes técnicos, diagramas, código SQL,
                    explicações passo-a-passo, etc. No arquivo real, isso teria 3-5 páginas de conteúdo detalhado.</p>
                    
                    <div class="tip">
                        <strong>💡 Dica Pedagógica:</strong> Incentive os alunos a pensarem primeiro 
                        nas entidades de negócio antes de partirem para a implementação técnica.
                    </div>
                </div>

                <div class="resolution">
                    <h3>Atividade 2: {dados['atividades'][1]['titulo']}</h3>
                    <h4>Resolução Modelo:</h4>
                    <p>[Resolução detalhada aqui]</p>
                </div>

                <div class="resolution">
                    <h3>Atividade 3: {dados['atividades'][2]['titulo']}</h3>
                    <h4>Resolução Modelo:</h4>
                    <p>[Resolução detalhada aqui]</p>
                </div>
            </div>

            <div class="section">
                <h2>📊 Rubrica de Avaliação</h2>
                <table class="planning-table">
                    <tr>
                        <th>Critério</th>
                        <th>Insuficiente (0-5)</th>
                        <th>Regular (6-7)</th>
                        <th>Bom (8-9)</th>
                        <th>Excelente (10)</th>
                    </tr>
                    <tr>
                        <td><strong>Compreensão Conceitual</strong></td>
                        <td>Não compreendeu conceitos básicos</td>
                        <td>Compreensão parcial</td>
                        <td>Boa compreensão</td>
                        <td>Domínio completo</td>
                    </tr>
                    <tr>
                        <td><strong>Aplicação Prática</strong></td>
                        <td>Não conseguiu aplicar</td>
                        <td>Aplicação com erros</td>
                        <td>Aplicação correta</td>
                        <td>Aplicação exemplar</td>
                    </tr>
                    <tr>
                        <td><strong>Qualidade Técnica</strong></td>
                        <td>Muitos erros técnicos</td>
                        <td>Alguns erros</td>
                        <td>Poucos erros</td>
                        <td>Tecnicamente perfeito</td>
                    </tr>
                    <tr>
                        <td><strong>Documentação</strong></td>
                        <td>Ausente ou inadequada</td>
                        <td>Básica</td>
                        <td>Boa documentação</td>
                        <td>Documentação profissional</td>
                    </tr>
                </table>
            </div>

            <div class="section">
                <h2>🎓 Recursos para o Professor</h2>
                <ul>
                    <li><strong>Apresentação PowerPoint:</strong> disponível no Moodle</li>
                    <li><strong>Scripts SQL:</strong> exemplos completos prontos para executar</li>
                    <li><strong>Datasets:</strong> dados de exemplo para laboratório</li>
                    <li><strong>Exercícios Extras:</strong> banco de questões adicional</li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    return html


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """Gera todas as 40 semanas"""
    print("="*70)
    print("GERADOR DE 40 SEMANAS - BDN007")
    print("Business Intelligence e Big Data")
    print("="*70)
    print()
    
    total_gerado = 0
    
    for num_semana, dados in SEMANAS_DETALHADAS.items():
        try:
            # Gera HTML da aula
            html_aula = gerar_html_semana(num_semana, dados)
            filename_aula = f"semana{num_semana:02d}.html"
            with open(filename_aula, 'w', encoding='utf-8') as f:
                f.write(html_aula)
            
            # Gera HTML do guia
            html_guia = gerar_html_guia(num_semana, dados)
            filename_guia = f"semana{num_semana:02d}_guia.html"
            with open(filename_guia, 'w', encoding='utf-8') as f:
                f.write(html_guia)
            
            print(f"✅ Semana {num_semana:02d}: {dados['titulo']}")
            print(f"   📄 {filename_aula} ({len(html_aula)/1024:.1f} KB)")
            print(f"   👨‍🏫 {filename_guia} ({len(html_guia)/1024:.1f} KB)")
            print()
            
            total_gerado += 2
            
        except Exception as e:
            print(f"❌ Erro na Semana {num_semana}: {str(e)}")
            print()
    
    print("="*70)
    print(f"✅ CONCLUÍDO! {total_gerado} arquivos gerados")
    print("="*70)

if __name__ == "__main__":
    main()
