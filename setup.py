import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Akshat"
SRC_REPO = "textSummarizer"  # Assuming this is the directory name where your code is
AUTHOR_EMAIL = "akshatsharma.sja@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(),
    install_requires=[
        "transformers",
        "transformers[sentencepiece]",
        "datasets",
        "sacrebleu",
        "rouge_score",
        "py7zr",
        "pandas",
        "nltk",
        "tqdm",
        "PyYAML",
        "matplotlib",
        "torch",
        "notebook",
        "boto3",
        "mypy-boto3-s3",
        "python-box==6.0.2",
        "ensure==1.0.2",
        "fastapi==0.78.0",
        "uvicorn==0.18.3",
        "Jinja2==3.1.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
