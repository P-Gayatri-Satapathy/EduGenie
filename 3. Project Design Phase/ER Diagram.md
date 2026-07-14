# Entity Relationship (ER) Diagram

## Entities

### USER

Attributes
- user_id (PK)
- name
- email
- password
- created_at

---

### USER_QUERY

Attributes
- query_id (PK)
- user_id (FK)
- query_type
- query_text
- created_at

---

### AI_RESPONSE

Attributes
- response_id (PK)
- query_id (FK)
- response_text
- model_used
- created_at

---

### QUIZ

Attributes
- quiz_id (PK)
- query_id (FK)
- question_text
- option_a
- option_b
- option_c
- option_d
- correct_answer

---

### SUMMARY

Attributes
- summary_id (PK)
- query_id (FK)
- summarized_text

---

### LEARNING_PATH

Attributes
- path_id (PK)
- query_id (FK)
- topic
- difficulty_level
- recommended_resources

---

## Relationships

USER
│
├── 1 : Many ───── USER_QUERY
│
USER_QUERY
├── 1 : 1 ───── AI_RESPONSE
├── 1 : Many ── QUIZ
├── 1 : Many ── SUMMARY
└── 1 : Many ── LEARNING_PATH

---

## Purpose

The ER model organizes users, educational queries, AI responses, quizzes, summaries, and learning recommendations efficiently while minimizing redundancy and maintaining data integrity.