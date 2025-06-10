from src.pipeline import run_pipeline

def test_pipeline_runs():
    try:
        run_pipeline()
        assert True
    except Exception as e:
        assert False, f"Pipeline failed: {e}"
