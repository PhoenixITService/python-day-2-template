import glob
import io
import sys

def test_area_calc_output():
    py_files = glob.glob("*_area.py")
    assert py_files, "❌ No *_area.py file found."

    # Capture printed output
    sys.stdout = io.StringIO()
    try:
        exec(open(py_files[0]).read())
        output = sys.stdout.getvalue().strip()
    except Exception as e:
        output = ""
        assert False, f"❌ Error while executing the area calculator: {e}"
    finally:
        sys.stdout = sys.__stdout__

    assert "Area: 181" in output, f"❌ Output incorrect. Expected 'Area: 181'. Got:\n{output}"