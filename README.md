# MyNewProject

A Python project template with proper setup and structure.

## Description

This project demonstrates best practices for Python project organization, including:
- Virtual environment setup
- Git version control
- Proper directory structure
- Requirements management

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MyNewProject.git
   cd MyNewProject
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
MyNewProject/
├── src/                    # Source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── venv/                   # Virtual environment (not in git)
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── setup.py              # Package setup (optional)
```

## Usage

```python
# Example usage
from src.main import hello_world
hello_world()
```

## Development

- Install development dependencies: `pip install -r requirements-dev.txt`
- Run tests: `python -m pytest tests/`
- Format code: `black src/`
- Lint code: `flake8 src/`

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `python -m pytest`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.