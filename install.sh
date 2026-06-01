#!/usr/bin/env bash
# Install wechat-article-to-todo skill for Claude Code / OpenClaw
# Usage: ./install.sh [project_path]

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_NAME="wechat-article-to-todo"
TARGET="${1:-.}"

install_claude_code() {
  local target_dir="$1"
  local skill_dir="${target_dir}/.claude/skills/${SKILL_NAME}"

  echo "Installing for Claude Code..."
  mkdir -p "$(dirname "$skill_dir")"
  cp -r "${REPO_DIR}/skills/${SKILL_NAME}" "${skill_dir}"
  echo "  -> ${skill_dir}"
}

install_openclaw() {
  local target_dir="$1"
  local skill_dir="${target_dir}/.agents/skills/${SKILL_NAME}"

  echo "Installing for OpenClaw..."
  mkdir -p "$(dirname "$skill_dir")"
  cp -r "${REPO_DIR}/skills/${SKILL_NAME}" "${skill_dir}"
  echo "  -> ${skill_dir}"
}

copy_tools() {
  local target_dir="$1"
  local tools_dir="${target_dir}/tools"

  echo "Installing extraction tool..."
  mkdir -p "${tools_dir}"
  cp "${REPO_DIR}/tools/extract_from_imagenie.py" "${tools_dir}/"
  echo "  -> ${tools_dir}/extract_from_imagenie.py"
}

# Main
echo "=== wechat-article-to-todo installer ==="
echo ""

if [ ! -d "${TARGET}" ]; then
  echo "Creating project directory: ${TARGET}"
  mkdir -p "${TARGET}"
fi

TARGET="$(cd "${TARGET}" && pwd)"

install_claude_code "${TARGET}"
install_openclaw "${TARGET}"
copy_tools "${TARGET}"

echo ""
echo "Done! Installed to: ${TARGET}"
echo ""
echo "Usage:"
echo "  1. cd ${TARGET}"
echo "  2. Open Claude Code / OpenClaw"
echo "  3. Paste a WeChat article link to convert to todo list"
