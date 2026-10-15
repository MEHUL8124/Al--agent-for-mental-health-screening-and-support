# Model Card & NLP System Boundaries

## 1. Intended Use
- **Primary Domain**: Supportive conversational interaction, educational emotion reflection, and grounding guidance.
- **Intended Users**: Individuals seeking structured self-reflection, evidence-informed coping techniques, and mood habit tracking.
- **Out of Scope Use**:
  - Medical diagnosis or psychiatric evaluation.
  - Emergency suicide intervention or clinical crisis management.
  - Prescribing or reviewing psychiatric pharmacotherapy.

## 2. Model Pipeline Architecture
1. **Safety Heuristic Classifier**:
   - High-priority regex and lexicon matching for emergency indicators, suicidal ideation, and self-harm keywords.
   - When activated, safety overrides all other model responses and returns verified regional hotlines.
2. **Intent Classification Module**:
   - Classifies user messages into categories (e.g. Grounding, Anxiety, Low Mood, Sleep Trouble, Coping Strategies).
3. **Conversational Support Layer**:
   - **Primary**: Configurable OpenAI Chat Completion (`gpt-4o-mini` or compatible).
   - **Offline / Local Fallback**: Deterministic CBT/Grounding response engine providing evidence-based exercises (5-4-3-2-1 Sensory Grounding, 4x4 Box Breathing, Cognitive Reframing).

## 3. Limitations & Bias Mitigations
- **Non-Clinical Guarantee**: Text sentiment and emotion labels represent surface linguistic patterns and do not indicate psychiatric health.
- **Hallucination Protection**: Medical diagnoses and pharmaceutical recommendations are strictly forbidden in system instructions.
- **Offline Robustness**: The system functions completely without external network access or paid API keys.
