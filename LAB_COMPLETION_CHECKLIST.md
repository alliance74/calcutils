# 📋 Lab Completion Checklist

## Student Information
- **Name**: Bienvenue Alliance
- **Email**: bienvenuealliance@gmail.com
- **GitHub**: alliance74
- **Package Name**: calcutils

---

## ✅ COMPLETED ITEMS

### 1. ✅ Package Structure (Steps 1-3)
- [x] Python 3.8+ installed
- [x] `build` and `twine` tools installed
- [x] Standard package directory structure created
- [x] `src/calcutils/` layout implemented

### 2. ✅ Code Implementation (Step 4)
- [x] `operations.py` with three functions:
  - `add(a, b)` - Addition function
  - `multiply(a, b)` - Multiplication function
  - `average(numbers)` - Average calculation
- [x] Type hints added to all functions
- [x] Docstrings added to all functions
- [x] `__init__.py` properly configured

### 3. ✅ Project Configuration (Step 5)
- [x] `pyproject.toml` created with all metadata
- [x] Author information configured
- [x] License specified (MIT)
- [x] Python version requirements set
- [x] README.md written
- [x] LICENSE file added

### 4. ✅ Building (Step 6)
- [x] Package built successfully
- [x] Source distribution created: `calcutils-0.1.0.tar.gz`
- [x] Wheel distribution created: `calcutils-0.1.0-py3-none-any.whl`
- [x] Both files in `dist/` folder

### 5. ✅ Testing
- [x] Local test script created
- [x] All functions tested and working:
  - add(10, 25) = 35 ✅
  - multiply(5, 6) = 30 ✅
  - average([10, 20, 30, 40]) = 25.0 ✅
  - average([]) = 0.0 ✅

---

## 🔄 TODO: Steps 7-9 (To Complete)

### Step 7: ⏳ Publishing to TestPyPI
**Instructions**: See `PUBLISHING_GUIDE.md`

- [ ] Create TestPyPI account at https://test.pypi.org/account/register/
- [ ] Verify email address
- [ ] Generate API token from Account Settings
- [ ] Save token securely
- [ ] Run command: `python -m twine upload --repository testpypi dist/*`
- [ ] Enter `__token__` as username
- [ ] Paste API token as password
- [ ] Verify successful upload

**Expected Result**: Package visible at `https://test.pypi.org/project/calcutils/`

### Step 8: ⏳ Verification & Testing
- [ ] Create new virtual environment:
  ```bash
  python -m venv test_env
  test_env\Scripts\activate  # Windows
  ```
- [ ] Install from TestPyPI:
  ```bash
  pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ calcutils
  ```
- [ ] Test in Python shell:
  ```python
  from calcutils import add, multiply, average
  print(add(10, 25))
  print(multiply(5, 6))
  print(average([10, 20, 30, 40]))
  ```
- [ ] Take screenshots of successful installation and testing

### Step 9: ⏳ Lab Submission
Submit to your instructor:

1. **GitHub Repository Link**
   - [ ] Create repository at https://github.com/alliance74/calcutils
   - [ ] Push all project files (except dist/, build/, __pycache__)
   - [ ] Ensure README.md is visible
   - [ ] Submit link: `https://github.com/alliance74/calcutils`

2. **TestPyPI Package Link**
   - [ ] Verify package is live
   - [ ] Submit link: `https://test.pypi.org/project/calcutils/`

3. **Screenshots/Logs**
   - [ ] Screenshot of `twine upload` success
   - [ ] Screenshot of successful `pip install`
   - [ ] Terminal output showing function tests working
   - [ ] Save as: `lab_submission_screenshots.pdf` or similar

---

## 📝 Quick Commands for Steps 7-9

```bash
# Navigate to project directory
cd C:\Users\HP\Desktop\Pythonpackage\calcutils

# Step 7: Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Step 8: Test installation
python -m venv test_env
test_env\Scripts\activate
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ calcutils

# Test the package
python
>>> from calcutils import add, multiply, average
>>> print(add(10, 25))
>>> print(multiply(5, 6))
>>> print(average([10, 20, 30, 40]))
>>> exit()

# Deactivate virtual environment
deactivate
```

---

## 🎯 Submission Checklist

Before submitting, ensure you have:

- [ ] GitHub repository created and populated
- [ ] Package successfully uploaded to TestPyPI
- [ ] Package successfully installed and tested
- [ ] All screenshots captured
- [ ] All three submission items prepared:
  1. GitHub link
  2. TestPyPI link
  3. Screenshots/terminal logs

---

## 📞 Need Help?

If you encounter issues:
1. Check `PUBLISHING_GUIDE.md` for detailed instructions
2. Review `PROJECT_SUMMARY.md` for project overview
3. Verify Python and tools are installed: `python --version`
4. Ensure you're in the correct directory: `cd calcutils`

---

**Project Status**: ✅ Ready for Publishing  
**Next Action**: Follow Step 7 in PUBLISHING_GUIDE.md  
**Estimated Time**: 15-20 minutes for Steps 7-9
