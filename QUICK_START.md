# 🚀 Quick Start Guide

## What is Multi-AI PR Orchestrator?

This system automatically analyzes pull requests using 6 different AI providers simultaneously (ChatGPT, DeepSeek, Claude, Gemini, Mistral, Grok), combining their insights for comprehensive code review.

## Get Started in 5 Minutes

### Step 1: Add Your API Keys (3 min)

1. Go to: [CarlosVergaraChile/ai-pr-orchestrator Settings](https://github.com/CarlosVergaraChile/ai-pr-orchestrator/settings/secrets/actions)
2. Click **New repository secret**
3. Add each API key with these names:
   - `CHATGPT_API_KEY` → Your OpenAI key
   - `DEEPSEEK_API_KEY` → Your DeepSeek key
   - `CLAUDE_API_KEY` → Your Anthropic key
   - `GEMINI_API_KEY` → Your Google key
   - `MISTRAL_API_KEY` → Your Mistral key
   - `GROK_API_KEY` → Your X.AI key

👉 **See [SETUP_API_KEYS.md](SETUP_API_KEYS.md) for detailed instructions**

### Step 2: Enable the Workflow (1 min)

The GitHub Actions workflow is already configured in `.github/workflows/multi-ai-orchestrator.yml`

It automatically runs when:
- A PR is created
- A PR is updated
- Code is pushed

### Step 3: Create a Test PR (1 min)

1. Create a test branch: `git checkout -b test-ai-review`
2. Make a small code change
3. Push and create a Pull Request
4. Watch the magic happen! 🎉

---

## How It Works

```
Pull Request Created
        ↓
GitHub Actions Triggered
        ↓
All 6 AI Providers Analyze in Parallel
        ↓
ChatGPT  DeepSeek  Claude  Gemini  Mistral  Grok
        ↓           ↓        ↓       ↓       ↓
Results Aggregated & Analyzed
        ↓
Comprehensive Comment Posted on PR
        ↓
Automatic Labels Applied (ai-generated, needs-review)
```

---

## What You Get

Each PR automatically gets analysis for:

✅ **Code Quality** - Complexity, best practices, maintainability
✅ **Security** - Vulnerabilities, unsafe patterns, credentials leak detection
✅ **Performance** - Optimization opportunities, inefficient code
✅ **Documentation** - Missing comments, unclear variable names
✅ **Testing** - Test coverage gaps, missing edge cases
✅ **Architecture** - Design patterns, modularity, coupling

---

## Repository Files Explained

| File | Purpose |
|------|----------|
| `README.md` | Complete feature documentation |
| `SETUP_API_KEYS.md` | API key acquisition & setup guide |
| `orchestrator.config.yaml` | Configuration for all AI providers |
| `.github/workflows/multi-ai-orchestrator.yml` | GitHub Actions workflow |
| `scripts/orchestrator.py` | Core Python orchestrator code |

---

## Cost Optimization Tips

💰 **Start Free:**
- Gemini: FREE tier (60 req/min)
- Mistral: FREE tier available
- OpenAI: $5 free trial credits

💰 **Then Scale:**
- Configure rate limits in `orchestrator.config.yaml`
- Disable expensive providers for routine reviews
- Use specific provider for specific tasks

---

## Integrate with Your Projects

### To use with other repositories:

1. Create a personal GitHub Actions secret in your account
2. Reference it in your workflow
3. Add the orchestrator workflow to your target repo

---

## Dashboard Integration

This orchestrator is linked to your **Dashboard Proyectos 2026** (Item #28).

Use it to manage AI-assisted reviews across all your projects!

---

## Troubleshooting

**Q: Workflow not running?**
- Check GitHub Actions are enabled
- Verify repository secrets exist
- Check Actions tab for error logs

**Q: No PR comments appearing?**
- Check Actions workflow ran successfully
- Verify API keys are valid
- Check account quotas (some providers have rate limits)

**Q: Getting inconsistent results?**
- This is normal - different AIs have different perspectives
- This diversity is a feature, not a bug!
- Use `orchestrator.config.yaml` to weight providers

---

## Next Steps

1. ✅ Add your API keys (see SETUP_API_KEYS.md)
2. ✅ Create a test PR to verify it works
3. ✅ Enable in your main projects
4. ✅ Customize `orchestrator.config.yaml` for your workflow
5. ✅ Monitor costs and adjust rate limits as needed

---

## Documentation

- 📖 [Full README](README.md) - Complete feature guide
- 🔑 [API Keys Setup](SETUP_API_KEYS.md) - How to get API keys
- ⚙️ [Configuration](orchestrator.config.yaml) - Tweak providers & settings
- 🔄 [GitHub Actions](../.github/workflows/multi-ai-orchestrator.yml) - Workflow details

---

## Support

For issues:
1. Check the documentation files above
2. Review [GitHub Actions logs](https://github.com/CarlosVergaraChile/ai-pr-orchestrator/actions)
3. Check individual API provider status pages
4. Verify account credentials and quotas

---

**Ready to supercharge your code reviews? Let's go!** 🚀
