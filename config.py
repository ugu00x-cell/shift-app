import os
import secrets
import shutil
from pathlib import Path
from typing import Optional, Union

BASE_DIR = Path(__file__).resolve().parent


def _load_or_create_secret_key() -> str:
    """SECRET_KEYをファイルに永続化する。起動ごとに変わるとセッション・CSRFが無効化されるため。"""
    env_key = os.environ.get("SECRET_KEY")
    if env_key:
        return env_key

    key_file = BASE_DIR / ".secret_key"
    if key_file.exists():
        return key_file.read_text(encoding="utf-8").strip()

    new_key = secrets.token_hex(32)
    try:
        key_file.write_text(new_key, encoding="utf-8")
    except OSError:
        pass  # 書き込めなくても動作は継続する
    return new_key


def resolve_database_path(base_dir: Optional[Union[str, os.PathLike]] = None) -> str:
    """DBパスを解決する。環境変数 > アプリディレクトリ内 > 親ディレクトリの順で探索。"""
    explicit_path = os.environ.get("SHIFT_APP_DB_PATH")
    if explicit_path:
        db_path = Path(explicit_path).expanduser()
        db_path.parent.mkdir(parents=True, exist_ok=True)
        return str(db_path)

    resolved_base_dir = Path(base_dir).resolve() if base_dir is not None else BASE_DIR

    # まずアプリディレクトリ内を優先（書き込み権限が確実）
    local_path = resolved_base_dir / "shift.db"
    preferred_path = resolved_base_dir.parent / "shift.db"

    if local_path.exists():
        return str(local_path)

    if preferred_path.exists():
        return str(preferred_path)

    # 新規作成はアプリディレクトリ内に（親ディレクトリは書込み権限がない可能性）
    return str(local_path)


class Config:
    SECRET_KEY = _load_or_create_secret_key()
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{resolve_database_path()}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
