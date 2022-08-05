# vscode-demo

A demo repository for VS Code used for talks.

Related presentation: <https://docs.google.com/presentation/d/1StvV-iIbExvw0ULIcbkTNqszGkY1_yo8sj5tyIZbVJ0/edit?usp=sharing>

## Prerequisites

- Install VS Code
- Install the Remote - SSH extension
  - <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>
- Install Miniconda on your SSH machine

## How to setup this repository

1. Open VS Code and sSH into your machine using this extension
2. Clone the repository in to your home directory
   `git clone https://github.com/tomvothecoder/vscode-demo.git`
3. Start from the root of the repository
   `cd vscode-demo`
4. Open the workspace file in VS Code with either:

   a. `code .vscode/vscode-demo.code-workspace` on the command line
   b. Or use _File > Open from Workspace File_ on the VS Code menu bar (Mac)

5. Install the conda environment using the repo's conda env yml file:

   `conda env create -n vscode-demo -f conda-env.yml`

6. Configure VS Code to use the `vscode-demo` conda env:

   a. _Python > Select Interpretor_ (VS Code command)

7. Ta-da all configured now
