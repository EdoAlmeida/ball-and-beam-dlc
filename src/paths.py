from pathlib import Path

# ==========================================================
# CONFIGURAÇÃO BASE DO PROJETO
# ==========================================================
# Opção 1:
# Deixe como automático para uso normal no GitHub
ROOT_DIR = Path(__file__).resolve().parents[1]

# Opção 2:
# Se quiser forçar manualmente, comente a linha acima e use:
# ROOT_DIR = Path(r"D:\meu_projeto\DLC_projects4")
# ==========================================================

NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
SRC_DIR = ROOT_DIR / "src"
VIDEOS_DIR = ROOT_DIR / "videos"
RESULTS_DIR = ROOT_DIR / "results"

FIGURES_DIR = RESULTS_DIR / "figures"
TABLES_DIR = RESULTS_DIR / "tables"
COMPARISONS_DIR = RESULTS_DIR / "comparisons"
VALIDATION_GRIDS_DIR = RESULTS_DIR / "validation_grids"

# Nome da pasta do projeto DLC
PROJECT_FOLDER_NAME = "bab_bar_only-Edo-2026-03-08" # modificar conforme nome criado no Projeto
PROJECT_DIR = ROOT_DIR / PROJECT_FOLDER_NAME
CONFIG_PATH = PROJECT_DIR / "config.yaml"

# Vídeos padrão
VIDEO_SWEEP = VIDEOS_DIR / "swept_sine_ready.mp4"
VIDEO_RANDOM = VIDEOS_DIR / "random_steps_W.mp4"
VIDEO_RAMP = VIDEOS_DIR / "rampa_positiva.mp4"

def ensure_basic_dirs():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    COMPARISONS_DIR.mkdir(parents=True, exist_ok=True)
    VALIDATION_GRIDS_DIR.mkdir(parents=True, exist_ok=True)

def show_paths():
    print("ROOT_DIR:", ROOT_DIR)
    print("VIDEOS_DIR:", VIDEOS_DIR)
    print("RESULTS_DIR:", RESULTS_DIR)
    print("PROJECT_DIR:", PROJECT_DIR)
    print("CONFIG_PATH:", CONFIG_PATH)