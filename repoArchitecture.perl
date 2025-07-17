project-pollen/
│
├── 📁 data/
│   ├── raw/                     # Original unprocessed corpus (.txt, .jsonl)
│   ├── processed/               # Cleaned, deduplicated, filtered text corpus
│   └── metadata/                # Licensing info, provenance, source tags
│
├── 📁 scripts/
│   ├── collect/                 # Web scrapers, crawlers, interview parsers
│   ├── clean/                   # Text normalization, tokenization, filtering
│   └── format/                  # Convert to model-friendly format (e.g., .txt, HuggingFace `Dataset`)
│
├── 📁 model/
│   ├── config/                  # Tokenizer & training configs
│   ├── finetune/                # Training/finetuning code on AAVE corpus
│   └── eval/                    # Bias detection, perplexity, BLEU, human eval
│
├── 📁 notebooks/
│   ├── exploratory_data_analysis.ipynb
│   └── qualitative_eval_examples.ipynb
│
├── 📁 docs/
│   ├── paper.md                 # Draft research paper or whitepaper
│   └── proposal.md             # Initial concept, goals, and impact
│
├── 📁 assets/
│   ├── logo.png                 # Project Pollen logo
│   └── preview.png              # Readme image preview
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
