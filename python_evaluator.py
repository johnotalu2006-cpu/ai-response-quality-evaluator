CRITERIA = [
    "Factual accuracy",
    "Instruction adherence",
    "Relevance",
    "Reasoning quality",
    "Clarity",
]


def collect_scores():
    scores = {}

    for criterion in CRITERIA:
        while True:
            try:
                score = int(input(f"{criterion} (1-5): "))

                if 1 <= score <= 5:
                    scores[criterion] = score
                    break

                print("Enter a score between 1 and 5.")

            except ValueError:
                print("Invalid input. Enter a whole number.")

    return scores


def calculate_average(scores):
    if not scores:
        raise ValueError("At least one score is required.")

    return sum(scores.values()) / len(scores)


def main():
    print("AI Response Quality Evaluation Tool")
    print("-" * 40)

    scores = collect_scores()
    average = calculate_average(scores)

    print("\nEvaluation Results")

    for criterion, score in scores.items():
        print(f"{criterion}: {score}/5")

    print(f"\nAverage score: {average:.2f}/5")
    print("Note: The average is not proof of factual correctness.")


if __name__ == "__main__":
    main()
