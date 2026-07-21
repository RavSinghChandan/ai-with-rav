---
day: 2
video: 2
topic: Machine Learning
title: The 3 Families of Machine Learning
subtitle: Supervised, Unsupervised, Reinforcement
---

@callout|yellow|In One Line: A machine learns in 3 ways — with a teacher, by exploring on its own, or by reward & punishment. Just like a child.

@h2|Start here: how a child learns
Think about how a child learns three different things:
@bullets
**Maths** → a teacher shows the answer: "2 + 2 = 4." The child learns from **labelled examples.**
**Sorting toys** → nobody tells them the categories. They just notice "these are red, these are round" and **group by themselves.**
**Cycling** → no teacher can hand it over. They try, fall, adjust — **learn from reward (staying up) and punishment (falling).**
@end
Machines learn the exact same three ways. That's it — the whole map of ML.

@h2|The 3 families, side by side
@image|images/04-three-families.png|Supervised (teacher), Unsupervised (explore), Reinforcement (reward). Every ML algorithm belongs to one of these.

@h2|1. Supervised Learning — learn with a teacher
You give the machine data **with the answers already attached** (called *labels*). It learns the pattern from answer → input, so it can predict answers for new data.
@bullets
Email marked *spam / not-spam* → learns to filter your inbox
House features (size, location) + *actual price* → predicts price of a new house
X-ray image + *doctor's diagnosis* → flags disease in a new scan
@callout|green|Key sign: your data already has the right answers. You're teaching by example. Most business ML (fraud, churn, pricing) is supervised.

@h2|2. Unsupervised Learning — learn by exploring
Here the data has **NO answers**. The machine explores and finds hidden structure — groups, patterns — **by itself**, without anyone labelling anything.
@image|images/05-supervised-vs-unsupervised.png|Left: supervised — dots are pre-coloured (labelled). Right: unsupervised — all one color, the machine discovers the groups.
@bullets
A shop's customers → machine finds "budget buyers", "premium buyers", "festival-only buyers"
News articles → auto-groups into sports, politics, tech (nobody tagged them)
@callout|green|Key sign: no labels, you're asking "what natural groups or patterns are hiding in here?" Used for customer segments, recommendations, anomaly detection.

@h2|3. Reinforcement Learning — learn by reward
No teacher, no dataset. An **agent** tries actions, gets **reward** for good ones and **penalty** for bad ones, and slowly learns the best strategy — exactly like learning to cycle.
@bullets
Game AI → +1 for winning a point, learns to play better each round
Robot arm → reward for picking the object correctly
**ChatGPT** → RLHF: humans reward good answers, the model learns to prefer them
@callout|green|Key sign: an agent taking actions in an environment, learning from trial-and-error feedback. This is how the "personality" of ChatGPT was trained.

@h2|Quick comparison
@table
Family|Data has answers?|Learns from|Real example
Supervised|Yes (labels)|Examples with answers|Spam filter, price prediction
Unsupervised|No|Hidden structure|Customer groups, topic discovery
Reinforcement|No (gets reward)|Trial & error|Game AI, robots, ChatGPT (RLHF)
@end

@h2|Recap — the 20-second version
@bullets
Machines learn 3 ways — like a child: teacher, exploring, reward.
**Supervised** = data has answers → predict answers (most business ML).
**Unsupervised** = no answers → find hidden groups/patterns.
**Reinforcement** = agent learns from reward & punishment (game AI, ChatGPT).
Ask one question to classify any ML problem: *"Does my data already have the answers?"*
@end
@callout|teal|Next up — Video 3: The ML Workflow. How a real model is actually built, step by step — from raw data to a working prediction. See you Day 3.
