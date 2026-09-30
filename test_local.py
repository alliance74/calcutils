"""
Local test script to verify calcutils functions work correctly
Run this before publishing to ensure everything is working.
"""

import sys
sys.path.insert(0, 'src')

from calcutils import add, multiply, average

def test_add():
    result = add(10, 25)
    expected = 35
    assert result == expected, f"add(10, 25) failed: expected {expected}, got {result}"
    print(f"✅ add(10, 25) = {result}")

def test_multiply():
    result = multiply(5, 6)
    expected = 30
    assert result == expected, f"multiply(5, 6) failed: expected {expected}, got {result}"
    print(f"✅ multiply(5, 6) = {result}")

def test_average():
    result = average([10, 20, 30, 40])
    expected = 25.0
    assert result == expected, f"average([10, 20, 30, 40]) failed: expected {expected}, got {result}"
    print(f"✅ average([10, 20, 30, 40]) = {result}")

def test_average_empty():
    result = average([])
    expected = 0.0
    assert result == expected, f"average([]) failed: expected {expected}, got {result}"
    print(f"✅ average([]) = {result}")

if __name__ == "__main__":
    print("Testing calcutils functions...\n")
    try:
        test_add()
        test_multiply()
        test_average()
        test_average_empty()
        print("\n🎉 All tests passed! Your package is ready to publish.")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
