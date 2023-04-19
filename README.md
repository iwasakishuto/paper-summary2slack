# Paper Summary to Slack

<a href="https://github.com/iwasakishuto/paper-summary2slack"><img src="https://github.com/iwasakishuto/paper-summary2slack/blob/main/img/architecture.png?raw=true" alt="Architecture"></a>
<a href="https://github.com/iwasakishuto/paper-summary2slack"><img src="https://badge.fury.io/gh/iwasakishuto%2Fpaper-summary2slack.svg" alt="GitHub Version"></a>
<a href="https://github.com/iwasakishuto/paper-summary2slack/blob/main/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000" alt="License"></a>
<br/>
<a href="https://github.com/iwasakishuto/paper-summary2slack/blob/master/.github/workflows/arxiv2slack.yml"><img src="https://github.com/iwasakishuto/paper-summary2slack/workflows/arxiv%20summary%20to%20slack/badge.svg" alt="Answer UTokyo Health Management Report Form"></a>

Github Actions を用いて、日々、論文の要約を Slack に流す。

## How to use?

The program can be executed by the following two methods, but the former is recommended.

### 1. Automatic Execution with Github Actions (recommended)

1. 🚀 Join GitHub.
2. 🍴 Fork this Repository.
3. ✅ Enable Github Actions in YOUR FORKED REPOSITORY.
4. ✏️ Register necessary information in GitHub Secrets.
   - `OPENAI_API_KEY`
   - `SLACK_API_TOKEN`
   - `SLACK_CHANNEL`

### 2. Install in your Local Env

You can also install it in your own environment and run it as appropriate.
