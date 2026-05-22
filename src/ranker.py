def ranker(final_output):

    ranked_output = (
        final_output
        .sort_values("Scores", ascending=False)
        .reset_index(drop=True)
    )

    ranked_output.index = range(1, len(ranked_output) + 1)

    styled_output = ranked_output.style.background_gradient(
        subset=["Scores"],
        cmap="RdYlGn",
        vmin=ranked_output["Scores"].min(),
        vmax=ranked_output["Scores"].max()
    )

    return styled_output