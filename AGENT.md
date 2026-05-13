# AGENT.md — Knowledge Base: Generative AI for Graphics & Multimedia (PoliTo)

This file governs how the AI agent reads, writes, and maintains the knowledge base.
**Read this file in full before touching any other file in the vault.**

---

## Default behavior when given lecture materials

When the user provides slides and/or a transcript:

1. **Always create a lecture note first** — run the full System 1 workflow (writes to `notes/`).
2. **Update the wiki only if the user explicitly asks** — run System 2 as a separate step.

**After reading the source files, start writing immediately. Do not stop to ask for confirmation between steps.**

The word "ingest" in user prompts is informal; it does not imply wiki-only. The correct interpretation is always: notes first, wiki only on explicit request.

---

## Quick Start

### 0. Pre-process slides (one-time setup)

The agent cannot read PDF files directly. Convert all slide decks to Markdown before using the vault:

```bash
# first time only — install dependencies
poetry install

# convert all slides (skips already-converted files)
poetry run python convert_slides.py

# force re-conversion of everything
poetry run python convert_slides.py --force
```

Run this once (and again whenever new PDF slides are added). The converted files land in `raw/slides-md/` — do not edit them manually.

### 1. Pull and start the model

```bash
# Pull the model (first time only)
ollama pull gemma4e:4b

# Start the Ollama server (skip if already running as a daemon)
ollama serve
```

### 2. Launch the agent

```bash
# From the vault root directory
pi --model ollama/gemma4e:4b

# If your pi.dev installation requires pointing to the context file explicitly:
pi --model ollama/gemma4e:4b --context AGENT.md
```

> Adjust flags to match your pi.dev installation. The agent must have `AGENT.md` in context at startup so it knows the vault conventions.

### 3. Commands to give the agent

**Create a lecture note (always the first step):**

```text
notes: lecture NN — Topic Name, YYYY-MM-DD
slides: raw/slides-md/NN. Topic Name.md
transcript: raw/lesson-transcripts/NN. Topic Name.md
```

**Also update the wiki (optional, after the note is done):**

```text
wiki: update wiki/models/page.md
source: raw/lesson-transcripts/NN. Topic Name.md
```

**Both at once:**

```text
notes + wiki: lecture NN — Topic Name, YYYY-MM-DD
slides: raw/slides-md/NN. Topic Name.md
transcript: raw/lesson-transcripts/NN. Topic Name.md
wiki target: wiki/models/page.md
```

> The agent executes all steps in order and writes all files without waiting for intermediate confirmation.

---

## Two Independent Systems

This vault maintains **two parallel, independent systems**. They do not reference each other.

| System              | Location  | Purpose                                                      |
|---------------------|-----------|--------------------------------------------------------------|
| **Lecture Notes**   | `notes/`  | Standalone, self-contained notes per lecture — for studying  |
| **Wiki**            | `wiki/`   | Structured knowledge base organized by topic — for querying  |

- A **lecture note** is a complete document covering one session. It does not link to wiki pages.
- A **wiki page** aggregates a topic across multiple lectures. It does not link to individual notes.
- **Raw sources** in `raw/` feed both systems and are never modified.

---

## Vault Structure

```text
GAN-vault/
├── AGENT.md                            # This file — agent instructions
├── skills/
│   └── skill-Lecture-to-Notes.md       # Notes style specification (reference only)
│
├── notes/                              # Standalone lecture notes
│   ├── index.md                        # Chronological list of all notes
│   └── YYYY-MM-DD-topic-slug.md        # One file per lecture
│
├── wiki/                               # Structured knowledge base
│   ├── index.md                        # Navigation map
│   ├── overview.md                     # Course info (staff, schedule, objectives)
│   ├── log.md                          # Append-only change diary
│   ├── models/
│   │   ├── autoregressive.md           # GPT, PixelCNN, WaveNet
│   │   ├── vae.md                      # VAE, β-VAE, VQVAE
│   │   ├── gan.md                      # GAN, DCGAN, StyleGAN, WGAN
│   │   ├── normalizing-flows.md        # Glow, RealNVP, MAF
│   │   ├── diffusion.md                # DDPM, Stable Diffusion, DALL-E
│   │   └── energy-based.md             # EBM, NCSN, ScoreNet
│   ├── rl/
│   │   └── rl-overview.md
│   ├── applications/
│   │   ├── image-synthesis.md
│   │   ├── animation.md
│   │   └── creative-pipelines.md
│   ├── tools/
│   │   ├── comfyui.md
│   │   └── mlagents.md
│   ├── labs/
│   │   ├── lab-overview.md
│   │   └── crownlabs.md
│   └── assessment/
│       ├── project.md
│       ├── homeworks.md
│       └── exam.md
│
└── raw/                                # Original sources — READ ONLY
    ├── slides/                         # Original PDF slide decks (do not read directly)
    │   └── NN. Topic Name.pdf
    ├── slides-md/                      # Slides converted to Markdown — READ THIS
    │   └── NN. Topic Name.md
    └── lesson-transcripts/             # Lecture transcripts
        └── NN. Topic Name.md
```

**The wiki file tree above is the authoritative list of allowed pages.** Do not create wiki pages that are not in this tree without updating `wiki/index.md` and logging the creation in `wiki/log.md` with a clear justification.

---

## System 1: Lecture Notes (`notes/`)

### Purpose

Each file in `notes/` is a complete, standalone set of notes for a single lecture or session. The title is the topic name of the slides. Notes are written for studying: narrative, clear, and self-contained. They do not depend on any other file in the vault.

### File naming

```text
YYYY-MM-DD-topic-slug.md
```

The title of the note (and the filename slug) must reflect the **slide deck topic**, not the lecture number. Examples: `2025-03-07-variational-autoencoders.md`, `2025-03-14-generative-adversarial-networks.md`.

Use the lecture date. If unknown, derive it from the transcript or ask the user.

### Frontmatter

```yaml
---
title: "Slide deck topic name"
date: YYYY-MM-DD
topics: [topic1, topic2]
source_slides: raw/slides-md/NN. Topic Name.md
source_transcript: raw/lesson-transcripts/NN. Topic Name.md
status: draft | complete
---
```

### Notes style

The goal is to produce notes that **follow the professor's explanation flow** and facilitate deep understanding. Slides provide the structure; the transcript provides the reasoning, intuition, and examples — integrate both, always prioritising the spoken explanation.

- **Narrative and conversational format** that follows the logical flow of the explanation
- Use bulleted lists **only when strictly necessary** (enumerated properties, procedural steps, multiple parallel items)
- Maintain balance between completeness and conciseness — no redundancy, no omission of key ideas
- **Clearly highlight formal definitions** in a distinguishable way: use a bold lead-in or a blockquote
- Emphasize fundamental concepts and key principles
- Integrate slides with oral explanations — **verbal clarifications and insights take priority** over slide text
- Include significant examples cited by the professor that aid understanding
- Group information into **coherent thematic sections** with `##` headings
- Maintain the logical progression of the lecture
- Create connections between related concepts when relevant
- **No links to reference material, wiki pages, or other notes**

### Workflow: Creating a note

Execute all steps in order. Do not stop between steps.

1. **Read the source files**: the transcript in `raw/lesson-transcripts/` and the slide PDF in `raw/slides/`. Do not copy or move them.

2. **Create** `notes/YYYY-MM-DD-topic-slug.md` with the frontmatter above and `status: draft`.

3. **Write the full note** following the style above. Summarize and paraphrase — never transcribe verbatim.

4. **Set `status: complete`** in the frontmatter once the note covers the full lecture.

5. **Add one line to `notes/index.md`** (most recent at the top):

   ```text
   - [Topic Name](YYYY-MM-DD-topic-slug.md) — YYYY-MM-DD
   ```

6. **Do not touch `wiki/`** unless the user explicitly asked for a wiki update.

---

## System 2: Wiki (`wiki/`)

### Role

The wiki is a structured, topic-organized knowledge base for reference and querying. It aggregates information across multiple lectures, identifying patterns, comparing models, and building a coherent conceptual map of the course.

### Frontmatter (required on every wiki page)

```yaml
---
title: "Readable page title"
category: models | rl | applications | tools | labs | assessment
tags: [tag1, tag2]
related: [gan.md, diffusion.md]
last_updated: YYYY-MM-DD
status: stub | draft | complete
---
```

- `stub` — file created, nearly empty
- `draft` — partial content, needs completion
- `complete` — content verified against sources in `raw/`

### Workflow: Adding new content to the wiki

Execute all steps in order. Do not stop between steps.

1. **Identify the target wiki page** from the file tree in the Vault Structure section above. If no existing page fits, check with the user before creating a new one.

2. **Read the target page** if it already exists, to understand what is already there.

3. **If the page does not exist:** create it with full frontmatter and `status: stub`. Add a link in `wiki/index.md`. Log in `wiki/log.md`:

   ```text
   YYYY-MM-DD | CREATE | wiki/models/page.md | stub created, source: raw/lesson-transcripts/NN. Topic Name.md
   ```

4. **Write content**: summarize and synthesize — do not transcribe. Follow style conventions.

5. **Verify cross-links**: does the updated page link related pages? Do related pages link back?

6. **Update `wiki/log.md`** (new entries at the top):

   ```text
   YYYY-MM-DD | INGEST | raw/lesson-transcripts/NN. Topic Name.md → wiki/models/page.md | brief note
   ```

### Workflow: Updating existing wiki content

When new information contradicts or extends existing content:

1. Read the existing page.
2. Classify the change:
   - *Extension* — new non-contradictory info → add a section or paragraph
   - *Correction* — new source corrects an error → replace text, note the source inline
   - *Unresolved contradiction* — two authoritative sources disagree → add `> ⚠️ Note: ...` and log it
3. Never delete content without logging it in `wiki/log.md` first.
4. Update `last_updated` in frontmatter.
5. Log the change (new entry at the top):

   ```text
   YYYY-MM-DD | UPDATE | wiki/models/gan.md | Added section on progressive growing
   ```

6. Check if `wiki/index.md` needs updating.

### Cross-links (wiki only)

- Use relative paths: `[VAE](../models/vae.md)` — never absolute URLs
- Every `models/` page must link its corresponding `applications/` pages
- Every `tools/` page must link the labs where the tool is used
- **Never link from wiki pages to `notes/` files, and never link from notes to wiki pages**

---

## Special files

### `notes/index.md`

Chronological list of all lecture notes, most recent at the top. One line per entry:

```text
- [Topic Name](YYYY-MM-DD-topic-slug.md) — YYYY-MM-DD
```

### `wiki/index.md`

Navigation map of the wiki. No didactic content here — only links and one-line descriptions, organized by folder.

```markdown
# Wiki — Generative AI for Graphics & Multimedia

## Generative Models
- [GAN](models/gan.md) — GAN, DCGAN, StyleGAN, WGAN
- [VAE](models/vae.md) — Variational Autoencoders
- ...

## Assessment
- [Group Project](assessment/project.md) — guidelines, deadlines, criteria
- ...
```

### `wiki/log.md`

Append-only diary of all wiki changes. **Add new entries at the top. Never modify existing lines. Use the real date, not the placeholder "YYYY-MM-DD".**

```text
YYYY-MM-DD | TYPE | file | brief description
```

Allowed types: `INGEST`, `UPDATE`, `REMOVE`, `CREATE`, `FIX`

**Never delete `wiki/log.md`** under any circumstances.

---

## Style conventions

**Language:** English for all content (matching the course slide language).

**Text:**

- Use `**bold**` only for key technical terms at first occurrence per page
- Inline LaTeX equations: `$p_\theta \approx p_{data}$`
- No inline HTML anywhere

**File naming:**

- All lowercase, hyphen-separated words: `normalizing-flows.md`, `2025-03-07-vae-intro.md`
- No spaces, no underscores, no uppercase in filenames

---

## What NOT to do

- **Never modify files in `raw/`.** They are immutable primary sources.
- **Never delete `wiki/log.md`**, even if it seems old or redundant.
- **Never create wiki pages outside the defined file tree** without user confirmation and a log entry.
- **Never add didactic content in `wiki/index.md` or `wiki/log.md`.** Only navigation and diary entries.
- **Never use absolute URLs for internal cross-links.** Relative paths only.
- **Never link from wiki pages to `notes/` files, or from `notes/` files to wiki pages.**
- **Never transcribe verbatim from slides or transcripts.** Summarize, paraphrase, add context.
- **Never modify a page's frontmatter without updating `last_updated`.**
- **Never rename existing files** without updating all cross-links and logging the rename in `wiki/log.md`.
- **Never leave a wiki page with `status: stub`** without a `wiki/log.md` entry explaining what is missing.
- **Never update the wiki when only asked to create notes**, and vice versa.
- **Never use "YYYY-MM-DD" literally in `wiki/log.md`.** Always use the real current date.
- **Never stop and wait for confirmation between workflow steps.** Execute all steps and write all files, then report what was done.
