# 🤖 Multi-AI PR Orchestrator

An intelligent system for automating pull request analysis, code review, and project management using multiple AI providers working in concert.

## Features

- **Multi-AI Integration**: Leverages ChatGPT, DeepSeek, Claude, Gemini, Mistral, and Grok
- **Automated PR Analysis**: Intelligent code reviews across multiple perspectives
- **Automatic Branch Creation**: Smart branch naming and organization
- **Aggregated Insights**: Consolidated recommendations from all AI providers
- **GitHub Actions Integration**: Seamless CI/CD workflow integration
- **Configurable Strategies**: Choose between balanced, performance-focused, or quality-focused approaches
- **Rate Limiting**: Built-in protection for API rate limits
- **Provider Fallback**: Automatic failover if a provider is unavailable

## Supported AI Providers

| Provider | Model | Capabilities |
|----------|-------|______________|
| ChatGPT | gpt-4-turbo | Code review, branch planning, commit messages, test generation |
| DeepSeek | deepseek-coder | Code generation, refactoring, performance analysis, security |
| Claude | claude-3-opus | Documentation, architecture review, technical analysis |
| Gemini | gemini-2.0-flash | Multimodal analysis, workflow optimization, testing |
| Mistral | mistral-large | Rapid coding, quick reviews, debugging |
| Grok | grok-2 | Real-time analysis, trend analysis, contextual improvements |

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CarlosVergaraChile/ai-pr-orchestrator.git
cd ai-pr-orchestrator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables for each AI provider:
```bash
export CHATGPT_API_KEY="your-key"
export DEEPSEEK_API_KEY="your-key"
export CLAUDE_API_KEY="your-key"
export GEMINI_API_KEY="your-key"
export MISTRAL_API_KEY="your-key"
export GROK_API_KEY="your-key"
```

## Configuration

Edit `orchestrator.config.yaml` to configure:

- AI provider endpoints and models
- Workflow automation settings
- Project-specific strategies
- Rate limiting per provider
- Logging and metrics

## GitHub Actions Setup

The system automatically triggers on:
- Pull request creation/update
- Code pushes
- Manual workflow dispatch

### Adding Repository Secrets

Add your API keys as repository secrets:
1. Go to Settings → Secrets and variables → Actions
2. Add secrets for each provider:
   - `CHATGPT_API_KEY`
   - `DEEPSEEK_API_KEY`
   - `CLAUDE_API_KEY`
   - `GEMINI_API_KEY`
   - `MISTRAL_API_KEY`
   - `GROK_API_KEY`

## Usage

### Manual PR Analysis
```python
from scripts.orchestrator import Orchestrator

orchestrator = Orchestrator()
pr_data = {"number": 123, "title": "Feature", "body": "Description"}
results = await orchestrator.orchestrate_pr_review(pr_data)
```

### Automated Workflow
Simply push to a repository with this action configured:
```yaml
- uses: CarlosVergaraChile/ai-pr-orchestrator@v1
```

## Project Structure

```
.
├── orchestrator.config.yaml          # Main configuration
├── .github/
│   └── workflows/
│       └── multi-ai-orchestrator.yml  # GitHub Actions workflow
├── scripts/
│   ├── orchestrator.py               # Core orchestrator
│   ├── ai-providers/                 # Individual provider implementations
│   ├── aggregator.py                 # Results aggregation
│   └── create-summary.py             # Summary generation
└── README.md
```

## How It Works

1. **PR Trigger**: When a PR is created/updated, the workflow triggers
2. **Analysis**: Each enabled AI provider analyzes the PR independently
3. **Aggregation**: Results are combined and analyzed for consensus
4. **Summary**: A comprehensive review comment is posted on the PR
5. **Actions**: Automatic labels and assignments based on findings

## Cost Optimization

- Use free tier APIs when possible (Gemini with free plan, Mistral community version)
- Configure rate limits to avoid unnecessary API calls
- Enable provider fallback to skip unavailable services
- Use project-specific strategies to focus analysis

## Integration with Dashboard Proyectos 2026

This orchestrator integrates with your GitHub Projects dashboard to:
- Automatically create project items from PRs
- Update project status based on review results
- Sync insights back to the project board

## License

MIT License - See LICENSE file for details

## Support

For issues and feature requests, please open an issue in the repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Created for**: Automated project management with intelligent AI assistance
