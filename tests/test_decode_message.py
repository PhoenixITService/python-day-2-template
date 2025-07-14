import glob
import io
import sys

def test_decode_message_output():
    py_files = glob.glob("*_decode.py")
    assert py_files, "❌ No *_decode.py file found."

    # Capture printed output
    sys.stdout = io.StringIO()
    try:
        exec(open(py_files[0]).read())
        output = sys.stdout.getvalue().strip().lower()
    except Exception as e:
        output = ""
        assert False, f"❌ Error while executing decode script: {e}"
    finally:
        sys.stdout = sys.__stdout__

    assert "name: luna" in output, "❌ Missing or incorrect line: Name: LUNA"
    assert "42 + 8 = 50" in output, "❌ Missing or incorrect line: 42 + 8 = 50"
    assert "3.14 * 2 = 6.28" in output, "❌ Missing or incorrect line: 3.14 * 2 = 6.28"
    assert "reversed title: thgink" in output, "❌ Missing or incorrect line: Reversed Title: thginK"
