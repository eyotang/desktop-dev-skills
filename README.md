# Desktop Dev Skills

面向 **macOS、Windows、Ubuntu** 的桌面应用开发 Agent Skills 合集。适用于 Codex 等支持 Agent Skills 的工具，持续沉淀真实项目中验证过的开发规则。

## Skills

| Skill | 用途 | 范围 |
| --- | --- | --- |
| [desktop-credential-storage](skills/desktop-credential-storage/SKILL.md) | 仅使用系统凭据存储，禁止普通文件保存，更新不回显旧凭据 | Tauri、Electron、原生桌面应用；不适用于 Web |

凭据持久化位置限定为 macOS Keychain、Windows Credential Manager 普通凭据、Ubuntu Secret Service（通常为 GNOME Keyring）。

## 安装

需要 Node.js/npm 和 Git。查看可用 skills：

```bash
npx skills add eyotang/desktop-dev-skills --list
```

安装单个 skill 到 Codex（全局）：

```bash
npx skills add eyotang/desktop-dev-skills --skill desktop-credential-storage -a codex -g
```

安装当前合集全部 skills 到 Codex：

```bash
npx skills add eyotang/desktop-dev-skills --skill '*' -a codex -g
```

在 Codex 中使用：

```text
使用 $desktop-credential-storage 检查当前桌面应用的凭据存储与更新流程。
```

如已手动安装同名 skill，先比较内容并保留需要的本地修改，再通过 CLI 统一管理，避免重复版本。

## 更新

```bash
npx skills update desktop-credential-storage -g
```

更新用于已安装的 skills；合集新增 skill 后，重新运行安装命令选择新条目。以本仓库为源文件维护，不直接修改安装副本。

## 扩展方向

未来按实际项目需要增加桌面 UI 设计、Tauri 开发、跨平台兼容、打包发布和原生测试。目前这些方向尚未提供独立 skill。

新增规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 本地校验

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
```

GitHub Actions 模板见 [templates/validate.yml](templates/validate.yml)。启用时将其移至 `.github/workflows/validate.yml`；通过 OAuth 推送工作流需要 `workflow` 权限。当前模板尚未启用。

校验涵盖 frontmatter、目录与名称一致性、重复名称、正文和 Codex UI 元数据；不替代实际行为验证，不检查远程链接可用性。

## skills.sh 收录

GitHub 是源文件仓库。根据 [skills.sh FAQ](https://www.skills.sh/docs/faq)，用户通过 `npx skills add` 安装后，平台依据匿名安装统计自动收录和排名；无需额外发布包，也不保证即时展示。

[Skills CLI 文档](https://github.com/vercel-labs/skills)

## License

[MIT](LICENSE)。引入第三方内容时须核对授权并保留来源声明。
