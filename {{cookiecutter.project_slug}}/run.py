from {{ cookiecutter.project_slug }}.method import predict

if __name__ == "__main__":
    print("Generating outputs")
    predict()
    print("Done. Check data/outputs.json")
