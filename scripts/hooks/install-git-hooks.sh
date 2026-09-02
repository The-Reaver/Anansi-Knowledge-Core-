#!/usr/bin/env bash
# Install the Knowledge Core's git hooks into this clone.
#
# Hooks live in .git/hooks/, which git does NOT track, so every clone starts
# with none installed and no warning that a control is absent. That is exactly
# how this repository went from its first commit to 2026-09-01 with no secret
# scanning at all. Run this after cloning.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
hook="$repo_root/.git/hooks/pre-commit"

if [ ! -d "$repo_root/.git" ]; then
    echo "install-git-hooks: $repo_root is not a git checkout" >&2
    exit 1
fi

if [ -e "$hook" ] && ! grep -q "secret_check.py" "$hook"; then
    echo "install-git-hooks: a pre-commit hook already exists and is not ours." >&2
    echo "  Refusing to overwrite it. Merge the line below in by hand:" >&2
    echo '    python3 scripts/secret_check.py || exit 1' >&2
    exit 1
fi

cat > "$hook" <<'HOOK'
#!/usr/bin/env bash
# Anansi Knowledge Core pre-commit. Installed by scripts/hooks/install-git-hooks.sh.
set -euo pipefail
repo_root="$(git rev-parse --show-toplevel)"
python3 "$repo_root/scripts/secret_check.py" || exit 1
HOOK
chmod +x "$hook"
echo "install-git-hooks: installed $hook"
echo "  verify with: python3 scripts/secret_check.py --all"
