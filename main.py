import os
from src.data_cleaning import load_and_clean_data
from src.eda import run_eda
from src.models import run_machine_learning

def main():
    print("🚀 Starting Uber Trip Analysis Pipeline...\n")
    
    # Set up paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, 'data', 'Uber-Jan-Feb-FOIL.csv')
    OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
    
    # --- PHASE 2: DATA CLEANING ---
    df_clean = load_and_clean_data(DATA_PATH)
    
    # --- PHASE 3: EXPLORATORY DATA ANALYSIS ---
    run_eda(df_clean, OUTPUT_DIR)
    
    # --- PHASE 4: MACHINE LEARNING ---
    model = run_machine_learning(df_clean, OUTPUT_DIR)
    
    print("\n🎉 PIPELINE FINISHED SUCCESSFULLY! 🎉")

if __name__ == "__main__":
    main()