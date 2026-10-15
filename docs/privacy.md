# MindCare AI Privacy & Ethical Policies

## 1. Privacy-by-Design Principles
1. **Local Storage First**: All personal mood ratings, sleep logs, and screening histories are stored in a local SQLite database (`mindcare_wellness.db`) on the user's host machine.
2. **No Tracking or Advertising**: MindCare AI contains no third-party tracking scripts, advertising trackers, or fingerprinting code.
3. **No Mandatory User Accounts**: Users are not required to provide personal identity attributes such as legal name, email address, phone number, or government IDs.
4. **Data Ownership & Deletion**: Users have full control to inspect individual entries, delete specific records, or purge their entire history with one click in the application.

## 2. Third-Party Model Interactions
- When an `OPENAI_API_KEY` is provided, chat messages are transmitted to the LLM endpoint for empathetic response generation.
- No database logs or screening questionnaire responses are sent to the LLM API.
- If no API key is supplied, MindCare AI operates 100% locally and offline via the internal supportive rule engine.

## 3. Medical & Diagnostic Disclaimers
- MindCare AI is an educational wellness screening and reflection platform, **not a clinical diagnostic device**.
- It does not diagnose Major Depressive Disorder, Generalized Anxiety Disorder, or any mental illness.
- It does not provide medical treatment, psychotherapy, or prescription medication advice.
- Anyone experiencing acute emotional distress, self-harm thoughts, or psychiatric crises should immediately contact professional emergency resources (such as 112 in India, 988 in the US/Canada, or 999/116 123 in the UK).
