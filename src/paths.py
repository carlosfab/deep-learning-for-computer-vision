# --- Imports ---
from pathlib import Path

# --- Paths ---
PARENT_DIR = Path(__file__).parent.resolve().parent
DATA_DIR = PARENT_DIR / 'data'
MODEL_DIR = PARENT_DIR / 'models'


# def create_dirs(path: Path) -> None:
#     if not path.exists():
#         path.mkdir(parents=True, exist_ok=True)


# --- Main ---
MODEL_DIR.mkdir(parents=True, exist_ok=True)
# OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
