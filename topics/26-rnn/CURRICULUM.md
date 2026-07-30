# 🔁 RNN (Recurrent Neural Networks & Sequences) — 30-Day Curriculum (STATIC — never deviate)

> LOCKED agenda. Module 5 (after CNN). A FULL 30 days on sequences, time & memory.
> This module ENDS by motivating attention → sets up the Transformers module.
> Same rules: story-first, 5 diagrams/day, 6th-grade English, real formula simply.

## Part 1 — Why Sequences Are Different (Days 1-8)
| Day | Title | Covers | Story angle |
|---|---|---|---|
| 1 | Sequence Data | Order matters: text, time, audio | Words in a sentence, notes in a song |
| 2 | Why a Plain Net Fails on Sequences | No memory of the past | A reader who forgets each word |
| 3 | The RNN Idea | A loop that carries memory | Reading while remembering earlier words |
| 4 | The Hidden State | The running "memory" | A note you keep updating |
| 5 | Unrolling an RNN Through Time | One net, many time-steps | The same worker at each moment |
| 6 | Forward Pass in an RNN | Step-by-step through a sequence | Reading left to right |
| 7 | Backprop Through Time (BPTT) | Learning across time-steps | Feedback flowing back through history |
| 8 | Building a Tiny RNN | End-to-end minimal example | — |

## Part 2 — The Memory Problem & Fixes (Days 9-16)
| Day | Title | Covers | Story angle |
|---|---|---|---|
| 9 | The Vanishing Memory Problem | Why RNNs forget long-ago words | A whisper lost down a long line |
| 10 | Exploding Gradients & Clipping | The opposite failure & its fix | — |
| 11 | LSTM (part 1) — the gates | Forget / input / output gates | A notebook with a smart eraser |
| 12 | LSTM (part 2) — the cell state | The long-term memory highway | The conveyor belt of memory |
| 13 | GRU | A lighter LSTM | The simpler notebook |
| 14 | Bidirectional RNNs | Reading forwards AND backwards | Reading a sentence both ways |
| 15 | Stacked / Deep RNNs | Many recurrent layers | Layers of understanding over time |
| 16 | Training Sequence Models Well | Practical tips | — |

## Part 3 — Real Sequence Tasks (Days 17-24)
| Day | Title | Covers | Story angle |
|---|---|---|---|
| 17 | Text Classification with RNNs | Sentiment, spam over sequences | — |
| 18 | Time-Series with RNNs | Forecasting the future | Predicting tomorrow's demand |
| 19 | Word Embeddings | Words → meaningful vectors | Giving words a place on a map |
| 20 | Sequence-to-Sequence | Input seq → output seq | The translator |
| 21 | The Encoder-Decoder | Understand then generate | Listener + speaker |
| 22 | The Bottleneck Problem | One vector can't hold everything | Squeezing a book into a sentence |
| 23 | Attention (the fix!) | Letting the decoder look back | A reader highlighting key words |
| 24 | Seq2Seq + Attention (full) | The complete picture | — |

## Part 4 — Applications & The Leap (Days 25-30)
| Day | Title | Covers | Story angle |
|---|---|---|---|
| 25 | Text Generation | Producing text one token at a time | The storyteller |
| 26 | Speech & Audio Sequences | RNNs for sound | — |
| 27 | RNN Capstone (full app) | End-to-end sequence project | — |
| 28 | Limits of RNNs | Slow, sequential, forgetful | Why we needed something new |
| 29 | Why Attention Won | The idea that replaced recurrence | The invention that beat memory |
| 30 | Recap + Road to Transformers | From attention to the transformer | The graduation |

**Day 30 teaser → Module 6: Transformers.**
