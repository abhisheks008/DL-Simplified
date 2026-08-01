# Quick Start Guide for Contributors

This guide will help you set up your development environment and start contributing to DL-Simplified.

## Prerequisites

- Python 3.8 or higher
- Git
- Jupyter Notebook or JupyterLab

## Step 1: Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/DL-Simplified.git
cd DL-Simplified
```

## Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
# Install development dependencies
pip install -r requirements-dev.txt
```

## Step 4: Validate Project Structure

```bash
# Check all projects follow the structure guidelines
python validate_structure.py
```

## Step 5: Start Contributing

1. Create a new branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run linting: `make lint`
4. Format code: `make format`
5. Commit your changes
6. Push to your fork: `git push origin feature/your-feature`
7. Create a Pull Request

## Running Notebooks

```bash
# Start Jupyter
jupyter notebook

# Or JupyterLab
jupyter lab
```

## Getting Help

- Read [CONTRIBUTING.md](CONTRIBUTING.md)
- Check existing [Issues](https://github.com/abhisheks008/DL-Simplified/issues)
- Contact the maintainers
