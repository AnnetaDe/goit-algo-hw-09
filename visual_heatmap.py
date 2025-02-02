import matplotlib.pyplot as plt
import seaborn as sns


def visual_heatmap(dp_states, total):
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        dp_states,
        annot=True,
        fmt=".0f",
        cmap="coolwarm",
        linewidths=0.5,
        xticklabels=[str(i) for i in range(total + 1)],
        yticklabels=[f"Step {i+1}" for i in range(len(dp_states))],
    )

    plt.xlabel("Total ")
    plt.ylabel("Computation Step")
    plt.title("Steps in collecting coins")
    plt.show()
