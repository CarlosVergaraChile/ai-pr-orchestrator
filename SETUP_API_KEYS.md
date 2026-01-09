# API Keys Setup Guide

This guide will help you obtain and configure API keys for all AI providers integrated in the Multi-AI PR Orchestrator system.

## Quick Start

You'll need to create GitHub Actions secrets for each AI provider. Navigate to:
**Settings → Secrets and variables → Actions → New repository secret**

## 1. ChatGPT (OpenAI)

**Secret Name:** `CHATGPT_API_KEY`

### How to Get Your API Key:

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Log in with your account: **carlos.solar.c@gmail.com**
3. Click "Create new secret key"
4. Copy the API key (you can only see it once)
5. Paste it as the secret value

**Capabilities:**
- Code review and analysis
- Branch planning and structure
- Commit message generation
- Test generation and review

**Cost:** $0.01 - $0.04 per 1K tokens (variable based on model)

---

## 2. DeepSeek

**Secret Name:** `DEEPSEEK_API_KEY`

### How to Get Your API Key:

1. Visit [DeepSeek API](https://platform.deepseek.com/api-keys)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste as the secret value

**Capabilities:**
- Code generation and implementation
- Refactoring suggestions
- Performance optimization
- Security vulnerability detection

**Cost:** More cost-effective than GPT-4, excellent for coding tasks

---

## 3. Claude (Anthropic)

**Secret Name:** `CLAUDE_API_KEY`

### How to Get Your API Key:

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Create an account if needed
3. Navigate to API keys section
4. Generate a new API key
5. Copy and add as secret

**Capabilities:**
- High-quality documentation generation
- Architecture and design review
- Complex technical analysis
- Best practices recommendations

**Cost:** Competitive pricing, excellent for detailed analysis

---

## 4. Gemini (Google)

**Secret Name:** `GEMINI_API_KEY`

### How to Get Your API Key:

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API key"
3. Select your project
4. Copy the generated API key
5. Add as GitHub secret

**Capabilities:**
- Multimodal analysis (text and potentially images)
- Workflow optimization suggestions
- Testing strategy development
- Performance analysis

**Cost:** FREE tier available (up to 60 requests/minute)

---

## 5. Mistral AI

**Secret Name:** `MISTRAL_API_KEY`

### How to Get Your API Key:

1. Go to [Mistral AI Platform](https://console.mistral.ai/)
2. Sign up for free
3. Create a new API key
4. Copy the key and paste as secret

**Capabilities:**
- Rapid code implementation
- Quick code reviews
- Debugging assistance
- Fast turnaround on analysis

**Cost:** Free tier and very affordable paid plans

---

## 6. Grok (X.AI)

**Secret Name:** `GROK_API_KEY`

### How to Get Your API Key:

1. Visit [X.AI Grok API](https://x.ai/) (if available)
2. Sign up or log in
3. Access API credentials section
4. Generate an API key
5. Add to GitHub secrets

**Capabilities:**
- Real-time information analysis
- Trend analysis with current data
- Contextual improvements based on latest info
- Current events integration

**Cost:** Check X.AI pricing

---

## Adding Secrets to GitHub

### Step-by-Step Instructions:

1. Go to your repository: **CarlosVergaraChile/ai-pr-orchestrator**
2. Click **Settings** tab
3. In left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Enter the secret name (e.g., `CHATGPT_API_KEY`)
6. Paste the API key in the **Secret** field
7. Click **Add secret**
8. Repeat for all providers

### Verification Checklist:

- [ ] CHATGPT_API_KEY
- [ ] DEEPSEEK_API_KEY  
- [ ] CLAUDE_API_KEY
- [ ] GEMINI_API_KEY
- [ ] MISTRAL_API_KEY
- [ ] GROK_API_KEY

---

## Cost Optimization Strategy

Since you have access to multiple free and paid tiers:

1. **Start with FREE tiers:**
   - Gemini: 60 requests/minute free
   - Mistral: Free tier available
   - OpenAI: Free trial credits

2. **Use based on task:**
   - Heavy analysis → Claude (excellent quality)
   - Code generation → DeepSeek (cost-effective)
   - Quick reviews → Mistral (fast)
   - Advanced insights → Gemini (free tier)
   - Current data → Grok (real-time)

3. **Configure rate limits** in `orchestrator.config.yaml` to prevent excessive API calls

---

## Security Best Practices

✅ **DO:**
- Use repository secrets for sensitive keys
- Regenerate compromised keys immediately
- Limit API key permissions where possible
- Set spending limits on paid accounts

❌ **DON'T:**
- Commit API keys to version control
- Share keys in issues or discussions
- Use the same key across multiple systems
- Store keys in environment variable files committed to git

---

## Testing Your Setup

After adding all secrets, you can test the orchestrator:

1. Create a test PR in your project
2. The GitHub Actions workflow will run
3. Check the Actions tab for execution logs
4. Review the PR comments for AI analysis

If workflow fails, check:
- All required secrets are added
- API keys are valid (not expired)
- Accounts have sufficient credits/quota
- Network connectivity (firewall/VPN issues)

---

## Troubleshooting

### API Key Not Recognized
- Verify the exact secret name matches the workflow file
- Ensure no extra spaces in the key
- Check that the account is not rate-limited

### Workflow Not Running
- Verify repository secrets exist
- Check GitHub Actions are enabled in Settings
- Review Actions tab for error messages

### Inconsistent Results
- Different AI providers may return varied results
- This is expected - intentional diversity for consensus
- Configure `orchestrator.config.yaml` to weight providers

---

## Need Help?

If you encounter issues:
1. Check API provider status pages
2. Verify account quotas and limits
3. Review GitHub Actions logs
4. Consult individual API documentation

**Documentation Links:**
- [OpenAI API Docs](https://platform.openai.com/docs)
- [DeepSeek API Docs](https://deepseek.com/api)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [Google Gemini Docs](https://ai.google.dev)
- [Mistral AI Docs](https://docs.mistral.ai)
- [GitHub Secrets Docs](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
