# Publishing Guide for calcutils

## ✅ Step 1-6: COMPLETED
Your package structure is ready and built!

## 📦 Step 7: Publishing to TestPyPI

### Step 7.1: Create an API Token

1. Go to https://test.pypi.org/account/register/ (or login if you already have an account)
2. Verify your email address
3. Navigate to Account Settings → API tokens
4. Click "Add API token"
5. Give it a name (e.g., "calcutils-upload")
6. Set scope to "Entire account" (or limit to this project if preferred)
7. Copy the generated token (starts with `pypi-`)

⚠️ **IMPORTANT**: Save this token somewhere safe - you won't be able to see it again!

### Step 7.2: Upload with Twine

Open your terminal in the `calcutils` directory and run:

```bash
python -m twine upload --repository testpypi dist/*
```

When prompted:
- **Username**: Enter `__token__` (exactly as written, with two underscores)
- **Password**: Paste your API token (including the `pypi-` prefix)

### Expected Output:
```
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: __token__
Enter your password: 
Uploading calcutils-0.1.0-py3-none-any.whl
Uploading calcutils-0.1.0.tar.gz
```

## 🧪 Step 8: Testing Your Package

### Create a test environment:

```bash
# Create a new virtual environment
python -m venv test_env

# Activate it
# On Windows:
test_env\Scripts\activate

# Install your package from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ calcutils
```

### Test the package:

```bash
python
```

Then in Python:
```python
from calcutils import add, multiply, average

print(add(10, 25))           # Should output: 35
print(multiply(5, 6))        # Should output: 30
print(average([10, 20, 30, 40]))  # Should output: 25.0
```

## 📋 Step 9: Lab Submission Checklist

Submit the following to your instructor:

1. ✅ **GitHub Repository Link**: Upload your `calcutils` folder to GitHub at https://github.com/alliance74/calcutils
   
2. ✅ **TestPyPI Package Link**: After uploading, your package will be at:
   `https://test.pypi.org/project/calcutils/`
   
3. ✅ **Terminal Screenshots**: Capture:
   - The successful upload output from `twine`
   - The installation and testing output showing your functions work

## 🚀 Publishing to Production PyPI (Optional)

Once you've successfully tested on TestPyPI, you can publish to the real PyPI:

1. Create an account at https://pypi.org/account/register/
2. Generate an API token at https://pypi.org/manage/account/
3. Upload using:
```bash
python -m twine upload dist/*
```

## 📝 Quick Command Reference

```bash
# Build the package
python -m build

# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Upload to PyPI (production)
python -m twine upload dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ calcutils

# Install from PyPI (production)
pip install calcutils
```

---

**Author**: Bienvenue Alliance  
**Email**: bienvenuealliance@gmail.com  
**GitHub**: [@alliance74](https://github.com/alliance74)
