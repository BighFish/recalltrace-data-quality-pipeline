# STEP 6: Run all the basic pipeline steps together.
from extract import extract
from transform import transform
from validate import validate
from quality import quality
from save import save_csv

# Start with sample data. Change to False for real FDA records.
USE_SAMPLE = False


def main():
    extract(use_sample=USE_SAMPLE)
    transform()
    validate()
    quality()
    save_csv()
    print("Pipeline finished!")


if __name__ == "__main__":
    main()
