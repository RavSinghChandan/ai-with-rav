# 🎓 AI with Rav — the complete learning universe

> **Learn AI the way you actually think.** Every topic, taught with Indian-context stories, clean diagrams, and zero jargon left unexplained — for the curious engineer *and* the smart non-techie.
>
> **▶ Watch:** [youtube.com/@aiwithrav](https://www.youtube.com/@aiwithrav) · **📖 Read:** you're here · every video is a downloadable branded PDF.

---

## 📚 The topics

Each folder = one YouTube playlist / learning track. Every video inside is a branded PDF built from the **same factory template** — identical premium look across all of them.

### 🧠 The AI / ML learning path
| # | Topic | What it covers |
|---|-------|----------------|
| 01 | [🧮 Mathematics](topics/01-mathematics/) | Vectors, calculus, probability — the root of everything |
| 02 | [🤖 Machine Learning](topics/02-machine-learning/) | Supervised, unsupervised, RL — **series started** |
| 03 | [🧠 Deep Learning](topics/03-deep-learning/) | Neural nets, backprop, CNNs, RNNs |
| 04 | [⚡ Transformers](topics/04-transformers/) | Attention, BERT, GPT |
| 05 | [💬 LLMs](topics/05-llms/) | Prompting, embeddings, fine-tuning |
| 06 | [🔎 RAG Systems](topics/06-rag-systems/) | Chunking, hybrid search, reranking |
| 07 | [🕹️ Agentic AI](topics/07-agentic-ai/) | Agents, LangGraph, multi-agent |
| 08 | [🔗 LangChain](topics/08-langchain/) | LangChain & LangGraph hands-on |
| 09 | [🚀 MLOps](topics/09-mlops/) | Deploy, monitor, version AI |
| 10 | [📊 AI Evaluation](topics/10-ai-evaluation/) | RAGAS, LLM-as-judge, metrics |

### 🛠️ Engineering & career
| # | Topic | What it covers |
|---|-------|----------------|
| 11 | [🏗️ System Design](topics/11-system-design/) | AI + general system design |
| 12 | [🛠️ Projects](topics/12-projects/) | Real end-to-end AI builds |
| 13 | [🌍 Open Source Contribution](topics/13-open-source/) | 3 merged PRs, how I did it |
| 14 | [☕ Java 8](topics/14-java/) | Java 8 features (Tech with Rav) |
| 15 | [🌱 Spring Boot](topics/15-spring-boot/) | Backend dev (Tech with Rav) |

---

## 🏭 How every video is made (the factory)

**Design is frozen. Content is per-video.** See [HOW_TO_MAKE_A_DAY.md](HOW_TO_MAKE_A_DAY.md).

```
build_master_pdf.py          ← the ONE frozen template (logo, photo, dark theme)
topics/<topic>/days/dayNN.md ← content only (title + story + diagrams)
   ↓  python3 build_master_pdf.py topics/<topic>/days/dayNN.md
AI-with-Rav_Day-NN_<title>.pdf  ← branded PDF, identical style
```

Same cover, same colors, same quality — **across every topic.** Change the content, the brand stays.

---

*Made to be understood, not to show off. — Rav*
