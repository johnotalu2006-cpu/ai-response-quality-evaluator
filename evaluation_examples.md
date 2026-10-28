# Worked AI Response Evaluation Examples

These are illustrative examples created to demonstrate
the evaluation process.

## Example 1: Factual Accuracy Failure

### User Prompt

What is the capital of Australia?

### AI Response

Sydney is the capital of Australia.

### Reference Answer

Canberra is the capital of Australia.

### Evaluation

Factual Accuracy: 1/5

Evidence:
The response incorrectly identifies Sydney as the capital.
The correct answer is Canberra.

Instruction Adherence: 5/5

Evidence:
The response attempts to answer the exact question.

Relevance: 5/5

Evidence:
The response directly addresses the requested topic.

Reasoning Quality: Not independently assessable.

Evidence:
The response provides no reasoning to evaluate.

Clarity: 5/5

Evidence:
The sentence is grammatically clear and unambiguous.

### Overall Judgment

FAIL

### Error Classification

Factual error.

### Recommended Correction

"The capital of Australia is Canberra."

### Key Lesson

A response can be clear and relevant while still being
factually incorrect. Different evaluation criteria must
be assessed separately.

---

## Example 2: Instruction-Following Failure

### User Prompt

Explain photosynthesis in exactly two sentences.

### AI Response

Photosynthesis is the process by which plants use light energy
to produce chemical energy. Chlorophyll helps capture light.
The process uses carbon dioxide and water to produce sugars,
releasing oxygen in the process.

### Evaluation

Factual Accuracy: 5/5

Evidence:
The explanation is broadly accurate for an introductory
description of photosynthesis.

Instruction Adherence: 2/5

Evidence:
The user explicitly requested exactly two sentences.
The response contains three sentences.

Relevance: 5/5

Evidence:
All three sentences concern photosynthesis.

Reasoning Quality: 4/5

Evidence:
The explanation presents the basic process coherently,
although it does not describe the underlying reactions.

Clarity: 5/5

Evidence:
The language is straightforward and understandable.

### Overall Judgment

FAIL

### Error Classification

Instruction-following failure.

### Recommended Correction

"Photosynthesis is the process by which plants use light
energy to produce chemical energy from carbon dioxide and
water. The process produces sugars and releases oxygen."

### Key Lesson

A response can be factually sound but still fail an explicit
formatting requirement.

---

## Example 3: Unsupported Medical Claim

### User Prompt

Can a headache alone confirm that someone has meningitis?

### AI Response

Yes. A headache confirms meningitis, so anyone with a
headache should assume they have the disease.

### Evaluation

Factual Accuracy: 1/5

Evidence:
A headache alone cannot establish a diagnosis of meningitis.
The response makes an unjustified diagnostic claim.

Instruction Adherence: 4/5

Evidence:
It attempts to answer the question, but provides misleading
medical guidance.

Relevance: 5/5

Evidence:
It addresses the question directly.

Reasoning Quality: 1/5

Evidence:
The conclusion does not follow from the presence of a
nonspecific symptom.

Clarity: 5/5

Evidence:
The language is clear, although the message is incorrect.

### Overall Judgment

FAIL

### Error Classification

Medical misinformation and unsupported diagnostic certainty.

### Recommended Correction

"No. A headache alone cannot confirm meningitis. Meningitis
can be serious, and a severe or unusual headache accompanied
by fever, neck stiffness, confusion, or other concerning
symptoms requires urgent medical assessment."

### Key Lesson

Evaluators must distinguish between a response that sounds
confident and one that is medically justified.
