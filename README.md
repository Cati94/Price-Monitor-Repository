# Price Monitor --- Web Scraper Genérico com Email Diário

Um sistema completo para monitorização de preços em qualquer website
usando **Selenium**, **configurações em JSON**, e **envio automático de
email diário**.

## ✨ Funcionalidades

-   Monitorização de preços totalmente configurável
-   Suporte para qualquer loja e qualquer produto via JSON
-   Selenium com browser headless
-   Envio automático de relatórios por email
-   Automatização diária via cron/Agendador de Tarefas

## 📁 Estrutura

    price-monitor/
    │
    ├── config/
    │   ├── products.json
    │   └── email.json
    │
    ├── src/
    │   ├── monitor.py
    │   ├── selectors.py
    │   └── emailer.py
    │
    ├── run_daily.bat
    └── README.md

## 🚀 Como usar

1.  Edita `products.json` para adicionar produtos + seletores CSS.
2.  Configura o email em `email.json` (recomendo password de app Gmail).
3.  Corre:

```{=html}
<!-- -->
```
    python src/monitor.py

4.  (Opcional) Agenda execução diária.

## 📬 Resultado

Recebes todos os dias um email com: - Nome do produto - Lista de sites -
Preço encontrado - Sites onde o preço falhou
