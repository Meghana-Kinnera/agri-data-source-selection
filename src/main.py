from .data_preprocessing import load_data, normalize_data
from .hesitant_fuzzy import apply_hesitant_fuzzy
from .rough_set import rough_set_approximation
from .madm_model import madm_ranking

if __name__ == "__main__":

    # 1️⃣ Load agricultural data
    data = load_data("data/sample_agricultural_data.csv")

    # 2️⃣ Normalize numeric data (Crop untouched)
    normalized_data = normalize_data(data)

    # 3️⃣ Apply hesitant fuzzy logic
    hf_data = apply_hesitant_fuzzy(normalized_data)

    # --------------------------------------------------
    # 🔴 INSERT YOUR 3 LINES RIGHT HERE 🔴
    # --------------------------------------------------

    print("Columns in hf_data:", hf_data.columns)

    hf_data['Score'] = hf_data.select_dtypes(include='number').mean(axis=1)

    ranked_sources = hf_data[['Crop', 'Score']].sort_values(
        by='Score', ascending=False
    ).reset_index(drop=True)

    ranked_sources.insert(0, 'Rank', ranked_sources.index + 1)

    # --------------------------------------------------

    # 4️⃣ Display output
    print("\nFinal Ranking of Agricultural Data Sources:\n")
    print(ranked_sources.to_string(index=False))

    # Save results to file
with open("results/ranking_output.txt", "w") as file:
    file.write("Final Ranking of Agricultural Data Sources\n\n")
    file.write(ranked_sources.to_string(index=False))

print("\nResults saved successfully in results/ranking_output.txt")

# python -m src.main
