# Contributing to Prism Terminal

First off, thank you for considering contributing! It's people like you that make this project great. This document outlines our entire development process, from creating an issue to submitting a pull request.

## 🚀 The Core Workflow

Our project management is centered around **GitHub Issues** and a **GitHub Projects (Kanban) board**. Every piece of work, whether a new feature, a bug fix, or a refactor, is tracked as an issue.

The workflow on our Kanban board follows these stages:

- **📦 Backlog:** This is the "feature dump" or idea box. All new issues are created here. They are not yet ready to be worked on.
- **✅ To Do:** The senior development team has reviewed these issues, confirmed they are well-defined, have no outstanding dependencies, and are ready for development. **This is the column you should pick issues from.**
- **🧑‍💻 In Progress:** Once you pick an issue, assign it to yourself and move it to this column. This signals to everyone else that the task is being actively worked on.
- **🕵️ In Review:** After completing your work and opening a Pull Request, move the related issue to this column. Be sure to comment the PR number on the issue before moving it.
- **🎉 Done:** Once the PR is reviewed, approved, and merged, the issue will be moved here and automatically closed.

## 🌿 Branching and Pull Requests

We follow a strict branching and pull request model to keep the codebase stable and clean.

### Creating a Branch

**All pull requests must be made from a feature branch to the `dev` branch.** Pull requests made directly to the `main` branch will be rejected.

1.  **Find an Issue:** Pick an issue from the `To Do` column on our project board.
2.  **Create Your Branch:** Create a new branch **from the `dev` branch**. Please use the following naming convention:

    - **Features:** `feature/<short-description>` (e.g., `feature/user-profile-page`)
    - **Bug Fixes:** `fix/<issue-number>-<short-description>` (e.g., `fix/42-login-button-crash`)
    - **Refactoring:** `refactor/<area-of-code>` (e.g., `refactor/api-service-layer`)
    - **Documentation:** `docs/<topic>` (e.g., `docs/pr-template-guide`)
    - **Chores (build scripts, configs, etc.):** `chore/<task-name>` (e.g., `chore/update-eslint-config`)

    ```bash
    # Make sure you are on the dev branch and have the latest changes
    git checkout dev
    git pull origin dev

    # Create your new feature branch
    git checkout -b feature/your-new-feature
    ```

### Submitting a Pull Request

1.  Once your work is complete, commit your changes and push your branch to the repository.
2.  Open a Pull Request from your branch **to the `dev` branch**.
3.  Fill out the PR template completely. **Crucially, link the issue your PR resolves** using a keyword like `Closes #123`. This ensures the issue is automatically closed when the PR is merged.
4.  Assign a senior developer as a reviewer (refer to `CODEOWNERS` for details).
5.  Move the issue card on the project board to the **Under Review** column.

That's it! Thank you for your contribution.
