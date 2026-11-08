# Referências

Marcação: `[fundamento]` = clássico para entender a base; `[recente]` = 2021–2026, elegível para estado da arte.
Status de leitura: **não lido** = só vi título/resumo em busca na web (2026-11-07); nada abaixo foi lido na íntegra.

## Fundamentos
| Ref | Tag | Uso no projeto | Link | Status |
|---|---|---|---|---|
| Kolisch & Sprecher (1997). PSPLIB — A project scheduling problem library. EJOR 96(1):205–216 | [fundamento] | Define o benchmark (j30/j60/j90/j120, formato `.sm`) | https://www.bohrium.com/paper-details/psplib-a-project-scheduling-problem-library/812412375398350848-12367 | não lido |
| Hartmann (1998). A competitive GA for resource-constrained project scheduling. Naval Research Logistics | [fundamento] | Codificação activity list e operadores | https://www.academia.edu/2325659/A_Competitive_Genetic_Algorithm_for_Resource_Constrained_Project_Scheduling | não lido |
| Myszkowski et al. (2015/2018). iMOPSE benchmark / library MS-RCPSP | [fundamento] | Benchmark da Frente B (36 instâncias, 100 tarefas, 20 recursos, `.def`) | https://annals-csis.org/proceedings/2015/drp/273.html ; https://link.springer.com/article/10.1007/s00500-017-2997-5 | não lido |
| Estabilidade proativo/reativo (KU Leuven) | [fundamento] | Definição de custo de estabilidade (desvio ponderado de datas de início) | https://lirias.kuleuven.be/retrieve/306427 | não lido |

## Candidatas a estado da arte (a triar na busca estruturada)
| Ref | Tag | Relevância | Link | Status |
|---|---|---|---|---|
| Reactive heuristics for disrupted multi-mode RCPSP. ESWA (2021), DOI 10.1016/j.eswa.2020.114132 | [recente] | Reativo, AG+imunológico, rescheduling completo vs. parcial | https://dl.acm.org/doi/abs/10.1016/j.eswa.2020.114132 | não lido |
| Reactive procedure for robust project scheduling under activity disruptions. KSCE J. Civil Eng. (2021) | [recente] | Reativo com AG, disrupção de atividades | https://link.springer.com/article/10.1007/s12205-021-1555-y | não lido |
| Event-based reactive approach for RCPSP with unreliable resources. Computers & Industrial Eng. (2020) | limítrofe | Memético, disrupções de recursos | https://www.sciencedirect.com/science/article/abs/pii/S0360835220306513 | não lido |
| Kybernetes (2024), AG híbrido + VNS, rescheduling sob disrupção de recursos | [recente] | Candidato direto | https://d2pnhgckm19p0r.cloudfront.net/insight/content/doi/10.1108/K-09-2022-1339/full/pdf | não lido |
| Snauwaert & Vanhoucke (2021). AG para MS-RCPSP, skills em amplitude/profundidade. EJOR | [recente] | Frente B | https://repository.vlerick.com/handle/20.500.12127/6652 | não lido |
| Zhu et al. (2021). GP hyper-heuristic multiobjetivo MS-RCPSP. KBS | [recente] | Frente B, avaliado no iMOPSE | https://gpbib.cs.ucl.ac.uk/gp-html/ZHU_2021_KBS.html | não lido |
| Two-phase GA for RCPSP (2025), arXiv 2506.21915 | [recente] | AG recente para RCPSP (comparação de AG base) | https://arxiv.org/pdf/2506.21915 | não lido |

## Ferramentas e dados
- PSPLIB (site oficial, segundo fontes secundárias): om-db.wi.tum.de — **confirmar links de download e contagem de instâncias**. Fontes secundárias: https://cpmpy.readthedocs.io/en/logo/api/tools/datasets/psplib.html ; https://pypi.org/project/psplib ; https://ptal.github.io/scheduling-data.html
- iMOPSE: homepage imopse.ii.pwr.wroc.pl ; IEEE DataPort https://ieee-dataport.org/documents/full-scale-imopse-and-synthesised-dataset
- Candidatos de código de timetabling (não avaliados): https://github.com/PROxZIMA/TimetableScheduler ; https://github.com/msaadx/GeneticAlgorithmTimeTableScheduling ; ScorpionKirk/GeneticAlgorithmUniversityClassScheduler

## Pendências de verificação
- Contagem de instâncias da PSPLIB: fontes divergem (j30/j60 = 480; j120 = 600; j90 = 480). Confirmar no site oficial.
- Nenhuma busca em Scopus/WoS/IEEE ainda: a busca na web retornou quase só trabalhos ≤2021.
