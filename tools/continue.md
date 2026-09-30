<div align="center">
  <h1>Continue</h1>
  <h4>Open Source Coding Agent</h4>
</div>

## Introduction to Continue

Continue integrates a Large Language Model (LLM) assistant directly into your VSCode environment. This tool allows you to ask contextual questions, generate code, perform refactoring, and deeply understand complex codebases, significantly boosting your development efficiency.

## Prerequisites
* Install [VSCode](https://code.visualstudio.com/download)
* Install [Ollama](https://ollama.com/download)

## Installation Guide - VSCode

### Step 1: Install the Extension
Open VSCode, navigate to the Extensions view, and search for "Continue" to install the official extension.

> [!NOTE]
> The final version should be `v2.0.0` since they were acquired by Cursor in 2026.

### Step 2: Configure the Extension
After installation, open the Continue settings (usually accessible via the VSCode sidebar) to configure your LLM backend.

> [!NOTE]
> This can also be on the bottom right of the VSCode editor.

### Step 3: Example Configuration: config.yaml
Here is a minimal example of what your configuration file ([`.continue/local-config.yaml`](../.continue/agents/local-config.yaml)) might look like. Remember to replace placeholders with your actual API keys and model details.

> [!NOTE]
> `contextLength` will depend on how beefy your GPU is along with the VRAM included. This example below uses an RTX 5060 8GB. If you have more VRAM like in the 90 class Nvidia cards you can bump these to 32K or even 64K context length.

> [!NOTE]
> Just because you have more VRAM like an Intel Arc B580 12GB, it does not mean you can run all the bells and whistles! It is advised to use smaller models in this case.

```yml
name: Local - AI
version: 0.0.1
schema: v1

models:
  - name: <NAME>
    provider: ollama
    model: <MODEL>
    apiBase: http://localhost:11434
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    defaultCompletionOptions:
      contextLength: 16384
```

## Extra
* Continue can also be used in Jetbrains IDEs or simply via the CLI