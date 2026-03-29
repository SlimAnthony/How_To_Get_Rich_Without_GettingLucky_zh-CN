# CLAUDE.md

## Project Overview

This repository is a Chinese translation project of Naval Ravikant's podcast series **"How to Get Rich Without Getting Lucky"** — a ~3.5-hour podcast (published 2019) expanding on Naval's viral 2018 Twitter thread of the same name.

- **Original source**: [nav.al/rich](https://nav.al/rich)
- **Translator**: Independent volunteer translator (started August 2019)
- **License**: CC BY-NC 4.0 (non-commercial use)
- **Language**: Bilingual — Chinese (Simplified) translation with original English passages preserved

---

## Repository Structure

```
/
├── README.md                          # Project introduction (Chinese)
├── CLAUDE.md                          # This file
└── NN Title_English UUID.md           # Chapter files (01–51)
```

### Chapter File Naming Convention

Every chapter file follows this exact pattern:

```
{NN} {English Title} {UUID}.md
```

- `NN` — Zero-padded chapter number (e.g., `01`, `13`, `51`)
- `English Title` — Truncated English title matching the original podcast
- `UUID` — Notion-style UUID (32 hex chars), artifact of the Notion-to-Markdown export

Example: `13 Arm Yourself With Specific Knowledge ae17e92786e3450580f6adf947751f4a.md`

There are **51 chapters total** (chapters 01–51), with chapter 51 being a bonus episode.

---

## Chapter File Structure

Each `.md` file has a consistent frontmatter block (informal, not YAML) followed by the translation body:

```markdown
# NN.English Title

Created time: <date>
Number: <chapter number>
Tags: <optional tags>
Translation Process: <Done | In Progress | To Do>  ← not always present
Telegra.ph URL: <optional mirror link>
URL: <nav.al canonical URL>
原载于: <original publication date YYYY/MM/DD>
[音频文件](<libsyn audio URL>)  ← or plain text "音频文件: <URL>"

# Chinese Title

<bilingual content: Chinese translation with original English quotes>

相关/See Also:
[NN. Related Chapter Title](relative link to chapter file)
```

Key fields:
- **Translation Process**: Tracks status — `Done`, `In Progress`, or `To Do`. Chapter 51 is marked `To Do`.
- **音频文件** (audio file): Link to the Libsyn CDN MP3 for that episode.
- **相关/See Also**: Internal cross-references using relative Markdown links to sibling `.md` files.

---

## Content Conventions

### Bilingual Format
Content interleaves English source phrases with Chinese translations. The typical pattern:

```markdown
English original sentence or phrase
对应的中文译文（有时会有补充说明）
```

Block quotes, section headers, and emphasis follow the original podcast structure.

### Internal Links
Cross-references between chapters use relative paths with the full filename including UUID:

```markdown
[36. There Are No Get Rich Quick Schemes](36%20There%20Are%20No%20Get%20Rich%20Quick%20Schemes%20da1af8d053d1474a8d666dd71c6e411c.md)
```

Spaces in filenames are URL-encoded as `%20` in links.

### Section Headers
Chinese section titles use `##` and `###` headers. Bold emphasis (`**text**`) is used for key concepts, mirroring the original emphasis.

---

## Translation Workflow

1. **Source material**: Naval's podcast episodes at nav.al/rich, audio from Libsyn CDN.
2. **Chapter metadata**: Frontmatter records creation time, chapter number, source URL, original publication date, and audio link.
3. **Translation status**: The `Translation Process` field tracks progress. Check this field before editing — only modify chapters or fill in `To Do` chapters after reviewing the original audio/transcript.
4. **Publishing mirror**: Completed translations may have a `Telegra.ph URL` pointing to a published mirror.

---

## Development Branch

Active development happens on: `claude/add-claude-documentation-uNKz4`

The default branch is `master`.

---

## Key Conventions for AI Assistants

1. **Do not alter the UUID suffix** in filenames — these are stable identifiers from the original Notion export.
2. **Preserve bilingual structure** — keep English source fragments alongside Chinese translations; do not remove the English.
3. **Maintain frontmatter fields** — when editing a chapter, keep all existing metadata fields intact.
4. **Respect internal links** — if a file is renamed, update all `相关/See Also` cross-references in other files.
5. **Translation fidelity over fluency** — the project prioritizes accurate representation of Naval's ideas; do not paraphrase or editorialize.
6. **License compliance** — this is CC BY-NC 4.0; do not add commercial content or remove attribution.
7. **Chapter 51 is incomplete** (`Translation Process: To Do`) — treat it as a stub.

---

## Chapter Index Summary

| # | English Title | Status |
|---|---------------|--------|
| 01 | Seek Wealth, Not Money or Status | Done |
| 02 | Make Abundance for the World | Done |
| 03 | Free Markets Are Intrinsic to Humans | Done |
| 04 | Making Money Isn't About Luck | Done |
| 05 | Make Luck Your Destiny | Done |
| 06 | You Won't Get Rich Renting Out Your Time | Done |
| 07 | Live Below Your Means for Freedom | Done |
| 08 | Give Society What It Doesn't Know How to Get | Done |
| 09 | The Internet Has Massively Broadened Career Possibilities | Done |
| 10 | Play Long-term Games With Long-term People | Done |
| 11 | Pick Partners With Intelligence, Energy and Integrity | Done |
| 12 | Partner With Rational Optimists | Done |
| 13 | Arm Yourself With Specific Knowledge | Done |
| 14 | Specific Knowledge Is Highly Creative or Technical | Done |
| 15 | Learn to Sell, Learn to Build | Done |
| 16 | Read What You Love Until You Love to Read | Done |
| 17 | The Foundations Are Math and Logic | Done |
| 18 | There's No Actual Skill Called "Business" | Done |
| 19 | Embrace Accountability to Get Leverage | Done |
| 20 | Take Accountability to Earn Equity | Done |
| 21 | Labor and Capital Are Old Leverage | Done |
| 22 | Product and Media are New Leverage | Done |
| 23 | Product Leverage is Egalitarian | Done |
| 24 | Pick a Business Model With Leverage | Done |
| 25 | Example: From Laborer to Entrepreneur | Done |
| 26 | Judgment Is the Decisive Skill | Done |
| 27 | Set an Aspirational Hourly Rate | Done |
| 28 | Work As Hard As You Can | Done |
| 29 | Be Too Busy to 'Do Coffee' | Done |
| 30 | Keep Redefining What You Do | Done |
| 31 | Escape Competition Through Authenticity | Done |
| 32 | Play Stupid Games, Win Stupid Prizes | Done |
| 33 | Eventually You Will Get What You Deserve | Done |
| 34 | Reject Most Advice | Done |
| 35 | A Calm Mind, a Fit Body, a House Full of Love | Done |
| 36 | There Are No Get Rich Quick Schemes | Done |
| 37 | Productize Yourself | Done |
| 38 | Accountability Means Letting People Criticize You | Done |
| 39 | We Should All Be Working for Ourselves | Done |
| 40 | Being Ethical Is Long-Term Greedy | Done |
| 41 | Envy Can Be Useful, or It Can Eat You Alive | Done |
| 42 | Principal-Agent Problem: Act Like an Owner | To Do |
| 43 | Kelly Criterion: Avoid Ruin | To Do |
| 44 | Schelling Point: Cooperating Without Communicating | To Do |
| 45 | Turn Short-Term Games Into Long-Term Games | To Do |
| 46 | Compounding Relationships Make Life Easier | To Do |
| 47 | Price Discrimination: Charge Some People More | To Do |
| 48 | Consumer Surplus: Getting More Than You Paid For | To Do |
| 49 | Net Present Value: What Future Income Is Worth Today | To Do |
| 50 | Externalities: Calculating the Hidden Costs of Products | To Do |
| 51 | Bonus: Finding Time to Invest in Yourself | To Do |
